from client import RickAndMortyClient
from utils import format_character

def main():
    client = RickAndMortyClient()
    data = client.fetch("character")

    if data and "results" in data:
        characters = data["results"]
        for character in characters[:9]:
            print(format_character(character))
    else:
        print("Não foi possível obter dados da API.")

if __name__ == "__main__":
    main()
