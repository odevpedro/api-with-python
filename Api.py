import requests

# Trata erros da API de forma genérica
def handle_api_error(error):
    print(f"[API ERROR] {type(error).__name__}: {error}")

# Montando a chamada na URL
def fetch_data(endpoint):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, ValueError) as error:
        handle_api_error(error)
        return None

# Chamando o méthodo definido
data = fetch_data("character")

# Pego os resultados de data e transformo em collection
if data:
    characters = data["results"]

    # Itero em cima da coleção que foi gerada
    for character in characters[:9]:
        name = character["name"]
        species = character["species"]
        status = character["status"]
        print(f"{name}: {status}")
else:
    print("Não foi possível obter os dados da API.")
