from pprint import pprint
import requests
from dotenv import load_dotenv, find_dotenv
import os

# Procura e carrega o arquivo .env
if not load_dotenv(find_dotenv()):
    print("Aviso: Arquivo .env não encontrado. Verifique a localização e o nome do arquivo.")

# Usa os.getenv() para obter a chave da API de forma segura
token = os.getenv('CHAVE_API_OPEN_WEATHER')

# Verifica se a chave foi realmente carregada
if token is None:
    print("Erro Crítico: A variável de ambiente 'CHAVE_API_OPEN_WEATHER' não foi encontrada.")
    print("Por favor, verifique se o arquivo .env está correto e no lugar certo.")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    'appid': token,
    'q': 'Catalão',
    'units': 'metric'
}

resposta = requests.get(url, params=params)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None
else:
    resultado = resposta.json()

pprint(resultado)
