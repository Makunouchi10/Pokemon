from elemental import PokemonElemental
from mega import MegaEvolucion

class PokemonFuego(PokemonElemental, MegaEvolucion):
    def __init__(self, nombre, nivel,):
        PokemonElemental.__init__(self, nombre, nivel, "Fuego")
        MegaEvolucion.__init__(self)

    def lanzallamas(self):
        return f"{self.get_nombre()} usa Lanzallamas"

    def ataque_mega(self):
        if self.get_mega_evolucionado():
            return f"{self.get_nombre()} usa un poderoso ataque Mega de fuego"
        return f"{self.get_nombre()} no puede usar ataques Mega sin Mega Evolucionar"

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Estado: {self.estado_mega()}"