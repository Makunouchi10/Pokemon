from elemental import PokemonElemental

class PokemonAgua(PokemonElemental):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel, "Agua")

    def hidrobomba(self):
        return f"{self.get_nombre()} usa Hidrobomba"

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Elemento: {self.get_elemento()}"