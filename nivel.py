# pokemon_nivel.py
from pokemon import Pokemon

class PokemonNivel(Pokemon):
    def __init__(self, nombre, tipo, nivel):
        super().__init__(nombre, tipo)
        self._nivel = nivel

    def get_nivel(self):
        return self._nivel

    def set_nivel(self, nivel):
        self._nivel = nivel

    def __str__(self):
        return f"{self.get_nombre()} (Nivel {self.get_nivel()}) - Tipo: {self.get_tipo()}"
