import requests

def fetch_data(endpoint):
    base_url = "https://rickandmortyapi.com/api/"
    response = requests.get(base_url + endpoint)
    return response.json()

character = fetch_data("character")
print(character)

