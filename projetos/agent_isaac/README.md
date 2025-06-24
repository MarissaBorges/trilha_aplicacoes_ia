####

### 🤖🎙️ Assistente de Voz com Agente Duplo (Isaac)

🔗 **Link do Projeto**: Este é um projeto de desktop e não possui um link para a web.

#### 📌 Descrição

**Isaac** é um assistente pessoal ativado por voz, projetado para interagir com o usuário de forma conversacional e analítica. Utilizando um simples atalho de teclado (`<ctrl>+<shift>+a`), o usuário pode iniciar e parar a gravação de sua voz. O áudio é então transcrito para texto via **Whisper**, processado por um **Large Language Model (LLM)** da OpenAI através do LangChain, e a resposta é convertida de volta para áudio com a API de **Text-to-Speech (TTS)** da OpenAI.

O grande diferencial do projeto é seu **sistema de agente duplo**. Isaac opera em um modo de conversação geral, mas pode dinamicamente alternar para um **agente especializado em análise de dados com Pandas**. Ao detectar a intenção do usuário de analisar um arquivo, ele solicita o caminho de um CSV no terminal e ativa o modo analítico, permitindo que o usuário faça perguntas sobre os dados diretamente por voz.

---

#### 🚀 Funcionalidades

- **Interação por Voz:** Ativação da gravação de áudio através de um atalho de teclado global.
- **Transcrição e Síntese de Voz:** Ciclo completo de Speech-to-Text (Whisper) e Text-to-Speech (OpenAI).
- **Agente de Conversação:** Um assistente geral (Isaac) com memória para manter o contexto da conversa.
- **Agente de Análise de Dados:** Um segundo agente especializado que pode ser ativado para ler e analisar arquivos **CSV** usando Pandas.
- **Roteamento Dinâmico de Agentes:** O sistema identifica a intenção do usuário e alterna entre o agente geral e o de análise de dados automaticamente.
- **Execução Assíncrona:** Uso de `threading` para que a síntese de voz e o input de arquivos no terminal não bloqueiem a interface principal.

---

#### 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1A1A1A?style=for-the-badge&logo=langchain&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

#### 🚀 Como Executar Localmente

Siga os passos abaixo para configurar e executar o projeto na sua máquina.

**Pré-requisitos:**
* Python 3.9 ou superior.
* [Git](https://git-scm.com/) instalado.
* Uma chave de API da [OpenAI](https://platform.openai.com/api-keys).
* `ffmpeg` instalado (necessário para o Whisper). Você pode instalar via `sudo apt update && sudo apt install ffmpeg` (Linux) ou `choco install ffmpeg` (Windows com Chocolatey).

**1. Clone o Repositório**
```bash
# Clone o projeto para a sua máquina local
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)

# Entre no diretório do projeto
cd seu-repositorio
```

**2. Crie e Ative um Ambiente Virtual**
É uma boa prática isolar as dependências do projeto.
```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

**3. Instale as Dependências**
Com o ambiente virtual ativo!!
Use o arquivo `requirements.txt` para instalar as dependências usando *pip*.
```bash
# Instale todas as bibliotecas necessárias
pip install -r requirements.txt
```

**4. Configure sua Chave de API**
Crie um arquivo chamado .env na pasta do projeto e adicione sua chave da OpenAI.
A chave pode ser adquirida em [OpenAI Platform](https://platform.openai.com/api-keys)
```bash
OPENAI_API_KEY="sk-sua-chave-de-api-secreta-aqui"
```

**5. Execute o Assistente**
Com tudo configurado, inicie o programa.
```bash
python conversando_llm.py
```

**6. Como Interagir**
-   Pressione a combinação de teclas **`<ctrl>+<shift>+a`** para **iniciar ou parar** a gravação da sua voz.
-   Para **encerrar o programa**, certifique-se de que o foco está na janela do terminal e pressione a tecla **`ESC`**.

---

#### 🔒 Destaques Técnicos
-   🧠 **Sistema de Agente Duplo:** O núcleo do projeto. Um agente geral decide, com base na intenção do usuário, quando delegar a tarefa a um agente especializado em Pandas, usando flags (`[ACTIVATE_PANDAS_AGENT]`) para o roteamento.
-   🗣️ **Interface de Voz Completa (STT/TTS):** Implementação de um fluxo contínuo de voz: `pynput` e `sounddevice` para captura -> `Whisper` para transcrição -> `OpenAI TTS` para resposta audível.
-   💾 **Memória Conversacional:** Utilização da `ConversationBufferMemory` do LangChain para que ambos os agentes (geral e Pandas) tenham acesso ao histórico da conversa, permitindo interações contextuais.
-   🔄 **Processamento Não-Bloqueante:** O uso de `threading` para a fila de TTS e para o input do caminho do arquivo garante que a aplicação continue responsiva enquanto tarefas demoradas são executadas em segundo plano.
-   ⌨️ **Controle por Atalho Global:** A biblioteca `pynput` permite que o assistente seja ativado de qualquer janela do sistema operacional, tornando a interação mais fluida e natural.

---

#### 🖼️ Demonstrações (fluxo de uso)
A interação ocorre no terminal e por voz. Abaixo, uma representação textual do fluxo:

**1. Conversa Geral** O terminal exibe as instruções iniciais e o usuário interage por voz.
```bash
Pressione <ctrl>+<shift>+a para iniciar ou parar a gravação.
Pressione <esc> para fechar o programa.

Gravação iniciada
(Usuário fala: "Isaac, qual a capital da França?")
Gravação finalizada
Salvando e transcrevendo...
Usuário: Isaac, qual a capital da França?
(Isaac responde por áudio: "A capital da França é Paris.")
```

**2. Ativação do Agente de Análise** O usuário expressa a necessidade de analisar um arquivo.
```bash
Gravação iniciada
(Usuário fala: "Gostaria de analisar um arquivo de dados.")
Gravação finalizada
Salvando e transcrevendo...
Usuário: Gostaria de analisar um arquivo de dados.
(Isaac responde por áudio: "Entendido. Por favor, digite o caminho para o arquivo CSV no terminal.")

Por favor, insira o caminho para o arquivo CSV (ou 'cancelar')
Para colar um caminho deve apertar Ctrl+Shift+C: C:\Users\user\Documents\vendas.csv
```

**3. Interação com o Agente Pandas** Após carregar o arquivo, o usuário faz perguntas sobre os dados por voz.
```bash
(Isaac responde por áudio: "Modo de análise de arquivo ativado. Pode fazer suas perguntas sobre os dados.")
Gravação iniciada
(Usuário fala: "Qual foi o total de vendas do produto X?")
Gravação finalizada
Salvando e transcrevendo...
Usuário: Qual foi o total de vendas do produto X?

> Executing new cache chain...
(LangChain/Pandas processa a query)

(Isaac responde por áudio com o resultado da análise.)
```

---
