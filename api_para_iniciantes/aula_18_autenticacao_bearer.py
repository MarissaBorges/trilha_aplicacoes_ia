from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
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
    resultado = {}
else:
    resultado = resposta.json()

token = resultado['access_token']

id_artista = "78nr1pVnDR7qZH6QbVMYZf"

url = f"https://api.spotify.com/v1/artists/{id_artista}"
headers = {
    'Authorization': f'Bearer {token}'
}

resposta = requests.get(url=url, headers=headers)
pprint(resposta.json())