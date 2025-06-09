from dataclasses import dataclass

@dataclass
class Character:
    name: str
    status: str
    species: str

    def __str__(self):
        return f"{self.name} | {self.status} | {self.species}"
