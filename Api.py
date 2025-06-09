
import requests

'montando a chamada na url'
def fetch_data(endpoint):
    base_url = "https://rickandmortyapi.com/api/"
    response = requests.get(base_url + endpoint)
    return response.json()

'chamando o método definido'
data = fetch_data("character")

'pego os resultados de data e transformo em collection'
characters = data["results"]

'intero em cima da coleção que foi gerada'
for character in characters[:9]:
    name = character["name"]
    species = character["species"]
    status = character["status"]
    print(f"{name}: {status}")
