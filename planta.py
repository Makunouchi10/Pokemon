from elemental import PokemonElemental

class PokemonPlanta(PokemonElemental):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel, "Planta")

    def rayo_solar(self):
        return f"{self.get_nombre()} usa Rayo Solar"