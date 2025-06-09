import requests
from config import BASE_URL, TIMEOUT
from utils import handle_api_error

class RickAndMortyClient:
    def fetch(self, endpoint: str, params: dict = None) -> dict | None:
        url = f"{BASE_URL}{endpoint}"
        try:
            response = requests.get(url, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError) as error:
            handle_api_error(error)
            return None
