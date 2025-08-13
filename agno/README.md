<!-- BADGES -->

<h1 align="center" style="font-weight: bold;">Agno – Exemplos e Agentes de IA 🤖</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge">
  <img src="https://custom-icon-badges.demolab.com/badge/-Agno-fc4415?style=for-the-badge&logo=agno&logoColor=white" alt="Agno">
  <img src="https://img.shields.io/badge/AI%20Agents-4682B4?style=for-the-badge" alt="AI Agents Badge">
  <img src="https://img.shields.io/badge/RAG-6A5ACD?style=for-the-badge" alt="RAG Badge">
  <img src="https://img.shields.io/badge/Playground-000000?style=for-the-badge" alt="Playground Badge">
</p>

<p align="center">
  <a href="#-descrição">Descrição</a> •
  <a href="#-exemplos-inclusos">Exemplos Inclusos</a> •
  <a href="#-requisitos">Requisitos</a> •
  <a href="#-como-executar">Como Executar</a> •
  <a href="#-estrutura">Estrutura</a>
</p>

---

## 📌 Descrição

Este diretório reúne exemplos práticos usando a biblioteca `agno` para construir agentes de IA, integrar bases de conhecimento (RAG), persistir histórico e executar um playground web para testes interativos. Os scripts aqui servem como base para montar agentes conversacionais com ferramentas e memória.

Este diretório faz parte de um repositório maior onde organizo os cursos que desenvolvo na Asimov Academy.

---

## 🧪 Exemplos Inclusos

- `0.llm_call.py`: chamada simples a LLM (ex.: Groq/OpenAI) com carregamento de variáveis de ambiente via `dotenv`.
- `1.1.researcher.py` e `1.2.analista.py`: agentes temáticos para tarefas de pesquisa/análise.
- `1.3.own_tools.py`: exemplo de agente utilizando ferramentas próprias.
- `21_storage.py`: armazenamento com `SqliteStorage` para histórico e estado de execução.
- `22_rag_agent.py`: agente RAG com PDF usando `PDFKnowledgeBase`, `ChromaDb` e `Playground` para interface.
- `31_memory.py`: padrões de memória e histórico de conversas.

> Observação: Ajuste as chaves de API no `.env` (ex.: `OPENAI_API_KEY`, `GROQ_API_KEY`) e os caminhos de arquivos (ex.: PDF) antes de executar.

---

## 📦 Requisitos

- Python ≥ 3.11
- Dependências sugeridas (instale conforme os exemplos que for executar):
  - `agno`, `python-dotenv`, `chromadb`
  - Provedores de LLM (instale e configure conforme necessidade): `openai`, `groq`

Instalação rápida (com `pip`):

```bash
pip install -U agno python-dotenv chromadb openai groq
```

Ou com `uv`:

```bash
uv add agno python-dotenv chromadb openai groq
```

Variáveis de ambiente (arquivo `.env` na raiz do workspace):

```bash
OPENAI_API_KEY=...
GROQ_API_KEY=...
```

> Dica: Se você tiver um projeto Python chamado `agno` no `pyproject.toml`, evite instalar a dependência `agno` como obrigatória para não criar auto‑dependência. Renomeie o projeto (ex.: `agno-app`) ou instale como `--dev`/`--optional`.

---

## ▶️ Como Executar

Execute a partir da raiz do repositório (o `launch.json` já está configurado para usar o diretório do arquivo):

```bash
python agno/0.llm_call.py
```

Agente RAG com Playground (garanta que o PDF exista):

```bash
python agno/22_rag_agent.py
```

No VS Code, basta abrir o arquivo desejado e pressionar `F5` para depurar/executar usando a configuração "Python: Arquivo Atual".

---

## 📂 Estrutura

```
agno/
├── 0.llm_call.py          # Chamada simples a LLM
├── 1.1.researcher.py      # Agente pesquisador
├── 1.2.analista.py        # Agente analista
├── 1.3.own_tools.py       # Ferramentas próprias para agentes
├── 21_storage.py          # Persistência com SqliteStorage
├── 22_rag_agent.py        # Agente RAG com PDF + Playground
├── 31_memory.py           # Padrões de memória
├── GlobalEVOutlook2025.pdf# Exemplo de fonte PDF
└── README.md              # Este arquivo
```

---

Se tiver dúvidas ou quiser estender algum exemplo (ou integrar novas fontes de dados e ferramentas), ajuste os scripts correspondentes e rode novamente com `F5` ou `python caminho/do/arquivo.py`.
