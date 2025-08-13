<!-- BADGES -->

<h1 align="center" style="font-weight: bold;">Streamlit – Curso e Projetos 🖥️</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Badge">
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

Este diretório reúne exemplos e um projeto completos usando **Streamlit** para construir web apps interativos com Python.

Este diretório faz parte de um repositório maior onde organizo os cursos que desenvolvo na **Asimov Academy**.

---

## 📚 Conteúdos e Exemplos

- Pasta "Códigos de aula": exemplos simples incluindo `spotify.py` com páginas em `pages/` e dataset `01 Spotify.csv`.
- Pasta "Projeto Streamlit FIFA": app com múltiplas páginas (`1_🏠_home.py`, `pages/2_🏃🏼_players.py`, `pages/3_⚽️_teams.py`) e datasets na subpasta `datasets/`.
- Apostila: `Criando Aplicativos Web com Streamlit - Apostila Asimov Academy.pdf`.

---

## 📦 Requisitos

- Python ≥ 3.11
- Dependências sugeridas: `streamlit`, `pandas` (e quaisquer libs usadas em cada exemplo)

Instalação rápida:

```bash
pip install -U streamlit pandas
```

Com `uv`:

```bash
uv add streamlit pandas
```

---

## ▶️ Como Executar

Execute a partir da raiz do repositório ou da própria pasta, apontando para o arquivo `.py` do app:

```bash
streamlit run "streamlit/Códigos de aula/spotify.py"
```

Projeto FIFA:

```bash
streamlit run "streamlit/Projeto Streamlit FIFA/1_🏠_home.py"
```

> Em Windows, se houver problemas com o caminho por conter espaços/caracteres especiais, envolva o caminho entre aspas.

---

## 📂 Estrutura

```
streamlit/
├── Códigos de aula/
│   ├── 01 Spotify.csv
│   ├── spotify.py
│   └── pages/
│       └── page2.py
├── Projeto Streamlit FIFA/
│   ├── 1_🏠_home.py
│   ├── datasets/
│   │   ├── CLEAN_FIFA17_official_data.csv
│   │   ├── CLEAN_FIFA18_official_data.csv
│   │   ├── CLEAN_FIFA19_official_data.csv
│   │   ├── CLEAN_FIFA20_official_data.csv
│   │   ├── CLEAN_FIFA21_official_data.csv
│   │   ├── CLEAN_FIFA22_official_data.csv
│   │   └── CLEAN_FIFA23_official_data.csv
│   └── pages/
│       ├── 2_🏃🏼_players.py
│       └── 3_⚽️_teams.py
├── Criando Aplicativos Web com Streamlit - Apostila Asimov Academy.pdf
└── README.md
```

---

Adapte e expanda os exemplos conforme necessário, adicionando novas páginas e datasets. Para deploy, consulte a documentação oficial do Streamlit.
