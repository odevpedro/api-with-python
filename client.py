import requests
from utils import handle_api_error

class RickAndMortyClient:
    BASE_URL = "https://rickandmortyapi.com/api/"

    def fetch(self, endpoint: str) -> dict | None:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError) as error:
            handle_api_error(error)
            return None
