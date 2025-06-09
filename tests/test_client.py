from utils import character_from_dict
from models import Character

def test_character_from_dict_creates_character_instance():
    data = {
        "name": "Rick Sanchez",
        "status": "Alive",
        "species": "Human"
    }

    character = character_from_dict(data)

    assert isinstance(character, Character)
    assert character.name == "Rick Sanchez"
    assert character.status == "Alive"
    assert character.species == "Human"


def test_character_from_dict_handles_missing_fields():
    data = {}  # dados incompletos

    character = character_from_dict(data)

    assert character.name == "???"
    assert character.status == "???"
    assert character.species == "???"

