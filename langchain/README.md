<!-- BADGES -->

<h1 align="center" style="font-weight: bold;">LangChain – Curso e Notebooks 🧠</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge">
  <img src="https://img.shields.io/badge/LangChain-1A1A1A?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain Badge">
  <img src="https://img.shields.io/badge/RAG-6A5ACD?style=for-the-badge" alt="RAG Badge">
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

Este diretório contém os notebooks do curso de **LangChain**, cobrindo desde conceitos essenciais até pipelines RAG, memória, vetorização e integração com LangSmith.

Este diretório faz parte de um repositório maior onde organizo os cursos que desenvolvo na **Asimov Academy**.

---

## 📚 Conteúdos e Exemplos

- Fundamentos de Modelos e LCEL: `02_models.ipynb`, `03_models_avancado.ipynb`, `06_chains_com_lcel.ipynb`
- Prompts e Parsers: `04_prompt_templates.ipynb`, `05_output_parsers.ipynb`, `08_runnables.ipynb`
- Roteamento e Memória: `09_roteamento.ipynb`, `10_memory.ipynb`
- Dados e RAG: `12_document_loaders.ipynb`, `13_text_splitting.ipynb`, `14_embeddings.ipynb`, `15_vector_stores.ipynb`, `16_retrieval.ipynb`, `17_pipeline_rag.ipynb`, `17_conversando_com_dados.ipynb`
- Outros: `07_chains_e_langsmith.ipynb`
- Recursos: pasta `arquivos/` e `docs/youtube/`

> Ajuste suas chaves de API e variáveis no ambiente, quando necessário (ex.: `OPENAI_API_KEY`).

---

## 📦 Requisitos

- Python ≥ 3.11
- Dependências: use `langchain/requirements.txt`

Instalação:

```bash
pip install -r langchain/requirements.txt
```

Com `uv`:

```bash
uv pip install -r langchain/requirements.txt
```

---

## ▶️ Como Executar

- No VS Code: abra o notebook `.ipynb` e execute células (Ctrl+Enter)
- No Jupyter Lab:

```bash
pip install jupyterlab  # se necessário
jupyter lab
```

Abra os notebooks em `langchain/` e execute célula a célula.

---

## 📂 Estrutura

```
langchain/
├── 02_models.ipynb
├── 03_models_avancado.ipynb
├── 04_prompt_templates.ipynb
├── 05_output_parsers.ipynb
├── 06_chains_com_lcel.ipynb
├── 07_chains_e_langsmith.ipynb
├── 08_runnables.ipynb
├── 09_roteamento.ipynb
├── 10_memory.ipynb
├── 12_document_loaders.ipynb
├── 13_text_splitting.ipynb
├── 14_embeddings.ipynb
├── 15_vector_stores.ipynb
├── 16_retrieval.ipynb
├── 17_conversando_com_dados.ipynb
├── 17_pipeline_rag.ipynb
├── arquivos/
│   ├── chroma_vectorstore/
│   ├── chroma_retrieval_bd/
│   ├── chat_retrieval_bd/
│   ├── faiss_bd/
│   ├── Top 1000 IMDB movies.csv
│   └── outros arquivos de apoio
└── docs/
    └── youtube/
        ├── Como usar o GPT com seus próprios dados？.m4a
        └── Como usar o GPT com seus próprios dados？.mp4
```

---

Caso precise adaptar os exemplos, ajuste dependências (requirements) e variáveis de ambiente conforme indicado em cada notebook.
