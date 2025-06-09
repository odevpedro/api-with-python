from client import RickAndMortyClient
from utils import format_character, character_from_dict


def main():
    client = RickAndMortyClient()

    filters = {
        "name": "rick",
        "status": "alive"
    }

    data = client.fetch("character", params=filters)

    if data and "results" in data:
        characters_raw = data["results"]
        characters = [character_from_dict(c) for c in characters_raw[:9]]
        for character in characters:
            print(character)
    else:
        print("Não foi possível obter dados da API.")

if __name__ == "__main__":
    main()
