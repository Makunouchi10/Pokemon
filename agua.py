# pokemon_agua.py
from nivel import PokemonNivel

class PokemonAgua(PokemonNivel):
    def __init__(self, nombre, nivel, profundidad):
        super().__init__(nombre, "Agua", nivel)
        self._profundidad = profundidad

    def get_profundidad(self):
        return self._profundidad

    def set_profundidad(self, profundidad):
        self._profundidad = profundidad

    def atacar(self):
        return f"{self.get_nombre()} usa un ataque acuático a {self.get_profundidad()} metros de profundidad!"

    def __str__(self):
        return f"{self.get_nombre()} (Agua) - Nivel {self.get_nivel()} - Profundidad: {self.get_profundidad()}m"
