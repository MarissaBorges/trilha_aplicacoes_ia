from pprint import pprint
import requests

nome = "laura"

url = f"https://servicodados.ibge.gov.br/api/v2/censos/xxxxxx/{nome}"

resposta = requests.get(url)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None
else:
    resultado = resposta.json()

# print com identação para listas e formulários
pprint(resultado)