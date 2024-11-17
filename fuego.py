# pokemon_fuego.py
from nivel import PokemonNivel

class PokemonFuego(PokemonNivel):
    def __init__(self, nombre, nivel, temperatura): #tipo="fuego", se le pone eso si lo quieres cambiar, que le estas poniendo uno por defecto para despues cambiarlo
        super().__init__(nombre, "Fuego", nivel) #El tipo de pokemon se esta poniendo asi para decir que es de valor fijo
        self._temperatura = temperatura

    def get_temperatura(self):
        return self._temperatura

    def set_temperatura(self, temperatura):
        self._temperatura = temperatura

    def atacar(self):
        return f"{self.get_nombre()} usa un ataque de fuego a {self.get_temperatura()}°C!"

    def __str__(self):
        return f"{self.get_nombre()} (Fuego) - Nivel {self.get_nivel()} - Temperatura: {self.get_temperatura()}°C" #Y aqui le quitas fuego y lo mandas a llamar, {self.get_tipo()}
