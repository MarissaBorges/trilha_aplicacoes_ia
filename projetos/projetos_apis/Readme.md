# 🚀 Portfólio de Aplicações Web com Python e Streamlit

Este repositório contém uma coleção de aplicações web interativas desenvolvidas com Python e a biblioteca Streamlit. Cada projeto demonstra a integração com diferentes APIs e a visualização de dados de forma prática e elegante.

---

### 📚 Índice de Projetos

1.  [**📊 Análise de Nomes IBGE**](#-análise-de-nomes-no-brasil-com-python-e-streamlit)
2.  [**☀️ App de Previsão do Tempo**](#️-app-de-previsão-do-tempo-com-python-e-streamlit)
3.  [**🎵 Busca de Artistas no Spotify**](#-busca-de-artistas-no-spotify-com-python-e-streamlit)

---

### 🏃 Como Executar os Projetos

As instruções abaixo são gerais. Cada projeto pode exigir uma configuração adicional (como chaves de API), detalhada em sua respectiva seção.

1.  **Clone o Repositório:**

    ```bash
    git clone https://github.com/MarissaBorges/apps_web_apis.git

    cd apps_web_apis
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**

    ```bash
    # Windows
    python -m venv venv
    .\\venv\\Scripts\\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    - Use o arquivo [`requirements.txt`](requirements.txt) presente no repositório e instale as bibliotecas com o comando:
    ```bash
    pip install -r requirements.txt
    ```

---

---

## 📊 Análise de Nomes no Brasil com Python e Streamlit

#### 📌 Descrição

O **Analisador de Nomes IBGE** é uma aplicação web interativa desenvolvida para visualizar a popularidade de nomes no Brasil ao longo das décadas. A ferramenta consome a API pública de Nomes do **IBGE** e apresenta a frequência de um determinado nome em uma tabela e em um gráfico de linha.

#### 🚀 Funcionalidades

- **Consulta Dinâmica:** Busque qualquer nome e veja sua frequência histórica.
- **Tabela de Frequência:** Exibe os dados de frequência para cada década.
- **Gráfico de Evolução:** Plota um gráfico de linhas que ilustra a popularidade do nome no tempo.

#### 🖼️ [Demonstrações (captura de tela)](#-screenshots-web-app-ibge)

#### 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

#### ▶️ Como Executar este Projeto

- Após seguir os passos gerais de instalação, execute o comando:
  ```bash
  streamlit run web_app_api_ibge.py
  ```

---

---

## ☀️ App de Previsão do Tempo com Python e Streamlit

#### 📌 Descrição

O **App de Previsão do Tempo** permite aos usuários consultar as condições climáticas atuais de qualquer cidade do mundo. A ferramenta utiliza a API da **OpenWeather** para buscar dados em tempo real, como temperatura, sensação térmica, umidade e cobertura de nuvens.

#### 🚀 Funcionalidades

- **Busca por Cidade:** Consulte o tempo inserindo o nome de qualquer cidade.
- **Dados em Tempo Real:** Exibe informações climáticas atualizadas.
- **Métricas Detalhadas:** Apresenta temperatura, sensação térmica, umidade e nuvens.

#### 🖼️ [Demonstrações (captura de tela)](#️-screenshots-web-app-openweather)

#### 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![API](https://img.shields.io/badge/OpenWeather%20API-EB6E4B?style=for-the-badge&logo=openweathermap&logoColor=white)

#### ▶️ Como Executar este Projeto

1.  **Configure a Chave da API:**
    - Entre no site da [OpenWeather](https://openweathermap.org/api) e crie sua chave de API gratuitamente
    - Crie um arquivo chamado `.env` na raiz do projeto.
    - Dentro dele, adicione sua chave da API da OpenWeather:
      ```
      CHAVE_API_OPEN_WEATHER="sua_chave_aqui"
      ```
2.  **Execute a Aplicação:**
    - Após seguir os passos gerais de instalação, execute o comando:
      ```bash
      streamlit run web_app_open_weather.py
      ```

---

---

## 🎵 Busca de Artistas no Spotify com Python e Streamlit

#### 📌 Descrição

O **Busca de Artistas Spotify** permite pesquisar por um artista e visualizar suas informações detalhadas, incluindo popularidade, seguidores, gêneros e as suas 10 músicas mais populares, utilizando a **[API oficial do Spotify](https://developer.spotify.com/documentation/web-api)**.

#### 🚀 Funcionalidades

- **Busca de Artistas:** Encontre qualquer artista cadastrado no Spotify.
- **Dashboard do Artista:** Exibe foto, link, popularidade, seguidores e gêneros.
- **Top 10 Músicas:** Lista as 10 faixas mais populares com capa e link.
- **Autenticação Segura:** Utiliza OAuth 2.0 para acessar a API.

#### 🖼️ [Demonstrações (captura de tela)](#-screenshots-web-app-spotify)

#### 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify%20API-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

#### ▶️ Como Executar este Projeto

1.  **Configure as Credenciais da API:**
    - Obtenha seu `Client ID` e `Client Secret` no [Dashboard de Desenvolvedor do Spotify](https://developer.spotify.com/dashboard/).
    - Crie ou edite o arquivo `.env` na raiz do projeto e adicione suas credenciais:
      ```
      SPOTIFY_CLIENT_ID="seu_client_id_aqui"
      SPOTIFY_CLIENT_SECRET="seu_client_secret_aqui"
      ```
2.  **Execute a Aplicação:**
    - Após seguir os passos gerais de instalação, execute o comando:
      ```bash
      streamlit run web_app_spotify.py
      ```

---

## 🖼️ Demonstrações (capturas de tela)

### 📊 Screenshots Web App IBGE

![Tela Inicial](https://i.postimg.cc/VLWnLqvt/image.png)

![Tela de Pesquisa](https://i.postimg.cc/KYHwyH4f/image.png)

---

---

### ☀️ Screenshots Web App OpenWeather

![Tela Inicial](https://i.postimg.cc/1XCNWwv8/image.png)

![Tela de Pesquisa](https://i.postimg.cc/9fJnCFFy/image.png)

---

---

### 🎵 Screenshots Web App Spotify

![Tela Inicial](https://i.postimg.cc/t4ybgJyc/image.png)

![Tela de Pesquisa Artista](https://i.postimg.cc/76cDPNY1/image.png)

![Tela de Pesquisa Albuns](https://i.postimg.cc/N0XjnM8f/image.png)
