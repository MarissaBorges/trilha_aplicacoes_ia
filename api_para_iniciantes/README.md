<!-- BADGES -->

<h1 align="center" style="font-weight: bold;">API para Iniciantes – Curso e Exemplos 🌐</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge">
  <img src="https://img.shields.io/badge/Requests-20232a?style=for-the-badge" alt="Requests">
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

Este diretório reúne códigos introdutórios para consumir APIs com Python: primeiros requests, tratamento de erros, autenticação (básica e bearer), e pequenos web apps com Streamlit integrando serviços como IBGE, OpenWeather e Spotify.

Este diretório faz parte de um repositório maior onde organizo os cursos que desenvolvo na **Asimov Academy**.

---

## 📚 Conteúdos e Exemplos

- `aula_03_primeiro_request.py`, `aula_05_gerando_requests.py`, `aula_06_codigos_de_status.py`: fundamentos de requisições HTTP.
- `aula_10_primeira_api.py`: primeiro exemplo de requisição a uma API pública (IBGE).
- `aula_11_schemas_parametros.py`, `aula_12_combinando_requests.py`: parâmetros, schemas e composição de chamadas.
- `aula_13_web_app_ibge.py`: web app com Streamlit consumindo a API do IBGE.
- Autenticação: `aula_14_autenticacao_basica.py`, `aula_15_autenticacao_bearer.py`, `aula_18_autenticacao_bearer.py`.
- Apps integrados: `aula_16_web_app_open_weather.py`, `aula_20_web_app_spotify.py`.

> Ajuste suas chaves de API no `.env` quando necessário (por exemplo, `CHAVE_API_OPEN_WEATHER`, `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`).

---

## 📦 Requisitos

- Python ≥ 3.11
- Dependências sugeridas:
  - `requests`, `python-dotenv`, `streamlit`, `pandas` (para alguns apps)

Instalação rápida:

```bash
pip install -U requests python-dotenv streamlit pandas
```

Com `uv`:

```bash
uv add requests python-dotenv streamlit pandas
```

---

## ▶️ Como Executar

- Scripts simples (terminal):

```bash
python api_para_iniciantes/aula_10_primeira_api.py
```

- Streamlit (IBGE, OpenWeather, Spotify):

```bash
streamlit run api_para_iniciantes/aula_13_web_app_ibge.py
streamlit run api_para_iniciantes/aula_16_web_app_open_weather.py
streamlit run api_para_iniciantes/aula_20_web_app_spotify.py
```

> Garanta que o `.env` contenha as variáveis necessárias antes de executar apps que exigem autenticação.

---

## 📂 Estrutura

```
api_para_iniciantes/
├── aula_03_primeiro_request.py
├── aula_05_gerando_requests.py
├── aula_06_codigos_de_status.py
├── aula_10_primeira_api.py
├── aula_11_schemas_parametros.py
├── aula_12_combinando_requests.py
├── aula_13_web_app_ibge.py
├── aula_14_autenticacao_basica.py
├── aula_15_autenticacao_bearer.py
├── aula_16_web_app_open_weather.py
├── aula_18_autenticacao_bearer.py
├── aula_20_web_app_spotify.py
└── pagina_google.html
```

---

Caso queira adaptar os exemplos para outros serviços, reutilize o padrão de função `fazer_request`, variáveis do `.env` e estrutura dos web apps.
