<!-- BADGES -->

<h1 align="center" style="font-weight: bold;">Agents – Curso e Notebooks 🤖</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge">
  <img src="https://img.shields.io/badge/LangChain-1A1A1A?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain Badge">
  <img src="https://img.shields.io/badge/AI%20Agents-4682B4?style=for-the-badge" alt="AI Agents Badge">
</p>

<p align="center">
  <a href="#-descrição">Descrição</a> •
  <a href="#-conteúdos-e-exemplos">Conteúdos e Exemplos</a> •
  <a href="#-requisitos">Requisitos</a> •
  <a href="#-como-executar">Como Executar</a> •
  <a href="#-estrutura">Estrutura</a>
</p>

---

## 📌 Descrição

Este diretório contém os notebooks do curso de **Agents**. Aqui você encontra exemplos práticos cobrindo LCEL, function calling, ferramentas, extração/rotulagem, tipos de agentes, memória, toolkits e execução de agentes.

Este diretório faz parte de um repositório maior onde organizo os cursos que desenvolvo na **Asimov Academy**.

---

## 📚 Conteúdos e Exemplos

- **LCEL e Base**: `02_lcel.ipynb`
- **Function Calling (OpenAI/LangChain)**: `03_adicao_de_funcoes_openai.ipynb`, `04_adicao_de_funcoes_langchain.ipynb`
- **Desafios**: `04_desafio.ipynb`, `06_desafio.ipynb`, `09_desafio.ipynb`
- **Tagging e Extraction**: `05_tagging.ipynb`, `06_extraction.ipynb`
- **Ferramentas**: `07_tools.ipynb`, `08_criando_uma_tool.ipynb`, `09_chatmodels_com_tools.ipynb`, `10_tools_padroes_do_langchain.ipynb`
- **Agents e Execução**: `11_agents.ipynb`, `12_agent_executor_e_memory.ipynb`, `13_agent_types.ipynb`, `14_agent_toolkits.ipynb`
- **Arquivos de apoio**: `arquivos/Chinook.db`, `arquivos/notas.txt`

> Ajuste suas chaves de API no ambiente (ex.: `OPENAI_API_KEY`) antes de rodar exemplos que usam provedores.

---

## 📦 Requisitos

- **Python**: 3.11+ recomendado
- **Dependências**: use o arquivo `agents/requirements.txt`

Instalação rápida:

```bash
pip install -r agents/requirements.txt
```

Com `uv`:

```bash
uv pip install -r agents/requirements.txt
```

Variáveis de ambiente (opcional, conforme os exemplos):

```bash
OPENAI_API_KEY=...
GROQ_API_KEY=...
```

---

## ▶️ Como Executar

- No VS Code: abra o notebook `.ipynb` e execute as células (Ctrl+Enter). Se preferir depurar, use o atalho F5 no arquivo Python quando aplicável.
- No Jupyter Lab:

```bash
pip install jupyterlab  # se necessário
jupyter lab
```

Abra os notebooks em `agents/` e execute célula a célula.

---

## 📂 Estrutura

```
agents/
├── 02_lcel.ipynb
├── 03_adicao_de_funcoes_openai.ipynb
├── 04_adicao_de_funcoes_langchain.ipynb
├── 04_desafio.ipynb
├── 05_tagging.ipynb
├── 06_desafio.ipynb
├── 06_extraction.ipynb
├── 07_tools.ipynb
├── 08_criando_uma_tool.ipynb
├── 09_chatmodels_com_tools.ipynb
├── 09_desafio.ipynb
├── 10_tools_padroes_do_langchain.ipynb
├── 11_agents.ipynb
├── 12_agent_executor_e_memory.ipynb
├── 13_agent_types.ipynb
├── 14_agent_toolkits.ipynb
├── arquivos/
│   ├── Chinook.db
│   └── notas.txt
└── requirements.txt
```

---

Em caso de dúvidas, abra o notebook correspondente e siga as instruções nas células. Ajuste variáveis de ambiente e dependências conforme o exemplo exigir.
