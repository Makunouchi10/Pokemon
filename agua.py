from elemental import PokemonElemental

class PokemonAgua(PokemonElemental):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel, "Agua")

    def hidrobomba(self):
        return f"{self.get_nombre()} usa Hidrobomba"