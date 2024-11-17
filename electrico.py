# pokemon_electrico.py
from nivel import PokemonNivel
from habilidad import Habilidad

class PokemonElectrico(PokemonNivel, Habilidad):
    def __init__(self, nombre, nivel, voltaje, habilidad):
        PokemonNivel.__init__(self, nombre,"Electrico", nivel)
        Habilidad.__init__(self, habilidad)
        self._voltaje = voltaje

    def get_voltaje(self):
        return self._voltaje

    def set_voltaje(self, voltaje):
        self._voltaje = voltaje

    def atacar(self):
        return f"{self.get_nombre()} usa un ataque eléctrico con {self.get_voltaje()} voltios!"

    def __str__(self):
        return f"{self.get_nombre()} (Electrico) - Nivel {self.get_nivel()} - Voltaje: {self.get_voltaje()}V - {self.get_habilidad()}"

