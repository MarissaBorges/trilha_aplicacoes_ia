from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv, find_dotenv
import os
import streamlit as st

load_dotenv(find_dotenv())

def autenticar():
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    auth = HTTPBasicAuth(username=client_id, password=client_secret) # type: ignore

    url = "https://accounts.spotify.com/api/token"
    body = {
        'grant_type': 'client_credentials'
    }
    resposta = requests.post(url, data=body, auth=auth)

    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        token = None
    else:
        token = resposta.json()['access_token']
        print("Token obtido com sucesso!")
    return token

def busca_artista(nome, headers):
    url = "https://api.spotify.com/v1/search"
    params = {
        'q': nome,
        'type': 'artist'
    }
    resposta = requests.get(url, params=params, headers=headers)
    try:
        primeiro_resultado = resposta.json()['artists']['items'][0]
    except IndexError:
        primeiro_resultado = None
    return primeiro_resultado

def busca_top_musicas(id_artista, headers):
    url = f"https://api.spotify.com/v1/artists/{id_artista}/top-tracks"
    resposta = requests.get(url=url, headers=headers)
    return resposta.json()['tracks']

def main():
    st.set_page_config(
        page_icon="🎵",
        page_title="Web App Spotify",
        layout='wide'
    )
    col1, col2 = st.columns([0.6, 0.4])
    with col1:
        st.title("Músicas mais tocadas do Spotify")
        st.markdown("Link da API [API Spotify](https://developer.spotify.com/documentation/web-api)")
    with col2:
        with st.form(key="search_form", border=False):
            st.write("")
            st.write("")
            col1, col2 = st.columns([4, 1])
            with col1:
                nome_artista = st.text_input(
                    "Busque por um artista", 
                    placeholder="Digite o nome de um artista...", 
                    label_visibility="collapsed")
            with col2:
                botao = st.form_submit_button("Buscar")

    if botao and nome_artista:
        token = autenticar()
        if not token:
            st.stop()

        headers = {
            'Authorization': f'Bearer {token}'
        }

        artista = busca_artista(nome=nome_artista, headers=headers)
        if not artista:
            st.warning(f"Artista '{nome_artista}' não foi encontrado!")
            st.stop()
        
        token = autenticar()
        headers = {
            'Authorization': f'Bearer {token}'
        }

        artista = busca_artista(nome=nome_artista, headers=headers)
        if not artista:
            st.warning(f"Artista {nome_artista} não foi encontrado!")
            st.stop()
        id_artista = artista['id']
        nome_artista = artista['name']
        link_artista = artista['external_urls']['spotify']
        popularidade_artista = artista['popularity']
        foto_artista = artista['images'][0]['url']
        seguidores = int(artista['followers']['total'])
        generos = str(artista['genres'])
        generos = "".join([caracter for caracter in generos if caracter not in "[]'"])

        col1, col2, col3 = st.columns([0.2,0.6, 0.2])
        with col1:
            st.image(foto_artista, use_container_width=False)
        with col2:
            col1, col2 = st.columns([0.4, 0.6])
            with col1:
                st.markdown(f"## {nome_artista}")
                st.markdown(f"[Link para o Spotify]({link_artista})")
                st.metric(value=popularidade_artista, label="Popularidade do Artista")
                st.metric(value=f"{seguidores:,.0f}", label="Seguidores", )
            with col2:
                st.markdown(f"## **Gêneros**")
                st.markdown(f"### - {generos}")
        melhores_musicas = busca_top_musicas(id_artista, headers)
        st.write("")
        st.subheader("Albuns e Tracks")

        for musica in melhores_musicas:
            album_foto = musica['album']['images'][0]['url']
            nome_musica = musica['name']
            popularidade = musica['popularity']
            link_musica = musica['external_urls']['spotify']
            col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
            with col1:
                st.image(album_foto, width=120)
            with col2:
                st.subheader(f"{nome_musica}")
                st.markdown(f"[Ouvir no Spotify]({link_musica})")
            with col3:
                st.metric(value=popularidade, label="Popularidade da Música")



if __name__ == "__main__":
    main()