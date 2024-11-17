# pokemon_mejorado.py
from electrico import PokemonElectrico

class PokemonConHabilidad(PokemonElectrico):
    def __init__(self, nombre, nivel, voltaje, habilidad): #tipo
        super().__init__(nombre, nivel, voltaje, habilidad) #tipo

    def atacar(self):
        return f"{self.get_nombre()} usa un ataque eléctrico mejorado con la habilidad {self.get_habilidad()}!"

    def __str__(self):
        return f"{self.get_nombre()} (Electrico) - Nivel {self.get_nivel()} - Voltaje: {self.get_voltaje()}V - {self.get_habilidad()}"

