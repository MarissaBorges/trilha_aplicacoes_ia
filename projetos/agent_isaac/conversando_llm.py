# 1. Usar um atalho para gravar minha voz
# 2. Transcrever o audio para texto (em português) -> Whisper
# 3. De posse deste texto, quero jogar em uma LLM -> Agente
# 4. De posse da resposta da LLM, quero utilizar um modelo de TTS (API da OpenAI)

import openai
from dotenv import load_dotenv, find_dotenv
from pynput import keyboard
import sounddevice as sd
import wave
import numpy as np
import whisper
from langchain_openai import ChatOpenAI, OpenAI
from queue import Queue
import io
import soundfile as sf
import threading
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
import time
import sys

load_dotenv(find_dotenv())

client = openai.Client()

ACTIVATE_PANDAS_FLAG = "[ACTIVATE_PANDAS_AGENT]"
DEACTIVATE_PANDAS_FLAG = "[DEACTIVATE_PANDAS_AGENT]"

class ConversandoLLM():
    def __init__(self, model='gpt-4o-mini', whisper_size="small"):
        """Função __init__ define configurações importantes como modelo, atalho e nome do arquivo temporário."""
        self.is_recording = False
        self.audio_data = []
        self.samplerate = 44100
        self.channels = 1
        self.dtype = 'int16'
        self.filename = "temp.wav"
        self.hotkey = '<ctrl>+<shift>+z'

        self.whisper = whisper.load_model(whisper_size)
        self.llm = ChatOpenAI(model=model, temperature=0)
        self.llm_queue = Queue()
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", 
            return_messages=True
        )
        self.accepting_terminal_input = False

        self.agent_mode = 'geral' # Modos possíveis: 'geral', 'pandas'
        self.general_agent = self.criar_agent_geral()
        self.pandas_agent = None

    def criar_agent_geral(self):
        """Cria o agente de conversação geral com memória."""
        system_prompt = f"""Você é um assistente pessoal prestativo chamado Isaac. Seu objetivo é conversar com o usuário, lembrando-se de interações passadas na conversa atual. Responda prioritáriamente em Português Brasil.
        Caso o usuário diga dê a intenção de quer finalizar o programa ou disser algo como 'muito obrigado, até mais' ou 'tchau' você deve o lembrar que para finalizar o programa ele deve pressionar ESC no terminal
        
        REGRA MAIS IMPORTANTE: Se o usuário expressar qualquer desejo de analisar, ler, verificar ou trabalhar com um arquivo, planilha ou dados (como um arquivo CSV), você DEVE responder ÚNICA E EXCLUSIVAMENTE com a seguinte flag:
        {ACTIVATE_PANDAS_FLAG}
        
        Não adicione nenhuma outra palavra. Apenas a flag. Para todas as outras conversas, responda normalmente."""

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ])
        
        chain = (
            RunnablePassthrough.assign(
                chat_history=lambda x: self.memory.load_memory_variables(x)["chat_history"]
            )
            | prompt
            | self.llm
        )
        return chain
    
    def criar_agent_pandas(self, df: pd.DataFrame):
        """Cria e ativa o agente especializado em análise de dados com pandas."""
        system_prompt = f"""Você é Isaac, agora operando em modo de análise de dados. Você tem acesso a um DataFrame pandas.
        Responda às perguntas do usuário sobre estes dados.
        Use o histórico da conversa para entender o contexto.
        Responda prioritáriamente em Português Brasil
        
        REGRA IMPORTANTE: Se o usuário indicar que terminou a análise lembre a ele que para finalizar o programa ele deve pressionaar ESC, caso ele diga que não quer mais analisar o arquivo, ou disser algo como "obrigado, pode fechar" ou "vamos voltar ao normal", você DEVE responder ÚNICA E EXCLUSIVAMENTE com a seguinte flag:
        {DEACTIVATE_PANDAS_FLAG}
        
        Não adicione nenhuma outra palavra. Apenas a flag."""
        
        try:
            self.pandas_agent = create_pandas_dataframe_agent(
                self.llm,
                df, 
                prefix=system_prompt,
                verbose=True,
                agent_type=AgentType.OPENAI_FUNCTIONS,
                agent_executor_kwargs={'memory': self.memory}
            )
            self.agent_mode = 'pandas'
            self.llm_queue.put("Modo de análise de arquivo ativado. Pode fazer suas perguntas sobre os dados.")
        except Exception as e:
            print(f"Erro ao criar o agente pandas: {e}")
            self.llm_queue.put("Desculpe, houve um erro ao carregar o arquivo. Por favor, verifique o terminal e tente novamente.")
            self.agent_mode = 'geral'
    
    def _handle_file_loading_thread(self):
        """Função que roda em uma thread separada para não bloquear o programa principal."""
        self.llm_queue.put("Entendido. Por favor, digite o caminho para o arquivo CSV no terminal.")
        
        if sys.platform == 'win32':
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getch()
        else:
            import termios
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
        
        while True:
            self.accepting_terminal_input = True
            print("\nPor favor, insira o caminho para o arquivo CSV (ou 'cancelar')")
            caminho_arquivo_bruto = input("Caminho: ")
            self.accepting_terminal_input = False
            
            caminho_arquivo = caminho_arquivo_bruto.strip('\'"')
            
            if caminho_arquivo.lower() == 'cancelar':
                self.llm_queue.put("Análise cancelada. Voltando ao modo normal.")
                break
            try:
                df = pd.read_csv(caminho_arquivo)
                self.criar_agent_pandas(df)
                break 
            except Exception as e:
                print(f"[ERRO] Não foi possível carregar o arquivo: {e}")
                self.llm_queue.put("Não consegui carregar este arquivo. Por favor, verifique o caminho e o formato, e tente novamente.")

    def salvar_e_transcrever(self):
        """Função principal que transcreve o áudio e ROTEIA a entrada para o agente correto."""
        print("Salvando e transcrevendo...")
        with wave.open(self.filename, 'wb') as wav_file:
            wav_file.setnchannels(self.channels)
            wav_file.setsampwidth(2)
            wav_file.setframerate(self.samplerate)
            wav_file.writeframes(np.array(self.audio_data, dtype=self.dtype).tobytes())

        resultado = self.whisper.transcribe(self.filename, fp16=False)
        texto_usuario = resultado['text']
        if not texto_usuario: return
        
        print()
        print(f"Usuário: {texto_usuario}")

        if self.agent_mode == 'pandas' and self.pandas_agent is not None:
            resposta = self.pandas_agent.invoke({'input': texto_usuario})
            output = resposta["output"]
            
            if output.strip() == DEACTIVATE_PANDAS_FLAG:
                self.agent_mode = 'geral'
                self.pandas_agent = None
                self.memory.clear()
                self.llm_queue.put("Entendido. Saindo do modo de análise.")
            else:
                self.llm_queue.put(output)
        else:
            resposta = self.general_agent.invoke({'input': texto_usuario})
            output = str(resposta.content)
            
            self.memory.save_context(inputs={"input": texto_usuario}, outputs={"output": output})
            
            if output == ACTIVATE_PANDAS_FLAG:
                threading.Thread(target=self._handle_file_loading_thread).start()
            else:
                self.llm_queue.put(output)

    def start_ou_stop_gravacao(self):
        """Função que inicia ou para a gravação"""
        if self.is_recording:
            self.is_recording = False
            self.salvar_e_transcrever()
            self.audio_data = []
        else:
            print("Gravação iniciada")
            self.audio_data = []
            self.is_recording = True

    def converter_texto_para_audio(self):
        """Função que converte o texto para audio usando o modelo da OpenAI"""
        tts_text = ''
        while True:
            tts_text += self.llm_queue.get()

            if '.' in tts_text or '?' in tts_text or '!' in tts_text:
                print(tts_text)

                spoken_resposta = client.audio.speech.create(model='tts-1',
                    voice='echo',
                    response_format='opus',
                    input=tts_text
                    )
                
                buffer = io.BytesIO()
                for chunk in spoken_resposta.iter_bytes(chunk_size=4096):
                    buffer.write(chunk)
                buffer.seek(0)

                with sf.SoundFile(buffer, 'r') as sound_file:
                    data = sound_file.read(dtype='int16')
                    sd.play(data, sound_file.samplerate)
                    sd.wait()
                tts_text = ''

    def _callback(self, indata, frames, time, status):
        """Este é o método chamado para cada bloco de áudio do microfone."""
        if status:
            print(status)
        if self.is_recording:
            self.audio_data.extend(indata.copy())

    def run(self):
        """Função inicial que roda o código usando threading e define a lógica do atalho para gravação"""
        t1 = threading.Thread(target=self.converter_texto_para_audio, daemon=True)
        t1.start()

        print(f"Pressione {self.hotkey} para iniciar ou parar a gravação.")
        print("Pressione <esc> para fechar o programa.")

        with sd.InputStream(samplerate=self.samplerate, channels=self.channels, dtype=self.dtype, callback=self._callback):
            def on_activate():
                self.start_ou_stop_gravacao()
            
            hotkey = keyboard.HotKey(
                keyboard.HotKey.parse(self.hotkey),
                on_activate)

            def on_press(key):
                if self.accepting_terminal_input:
                    return
                if key == keyboard.Key.esc:
                    return False
                hotkey.press(listener.canonical(key))

            def on_release(key):
                if self.accepting_terminal_input:
                    return
                hotkey.release(listener.canonical(key))
            
            with keyboard.Listener(
                    on_press=on_press,  # type: ignore
                    on_release=on_release) as listener:
                listener.join()

if __name__ == "__main__":
    conversar_llm = ConversandoLLM()
    conversar_llm.run()