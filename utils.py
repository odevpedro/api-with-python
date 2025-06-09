from models import Character
# utils.py

def handle_api_error(error: Exception):
    """
    Exibe mensagens de erro padrão da API.
    """
    print(f"[API ERROR] {type(error).__name__}: {error}")


def format_character(character: dict) -> str:
    """
    Recebe um dicionário de personagem e retorna uma string formatada.
    """
    name = character.get("name", "Desconhecido")
    status = character.get("status", "???")
    species = character.get("species", "???")
    return f"{name} | {status} | {species}"


def character_from_dict(data: dict) -> Character:
    return Character(
        name=data.get("name", "???"),
        status=data.get("status", "???"),
        species=data.get("species", "???")
    )
