from pokemon import Pokemon

class PokemonElemental(Pokemon):
    def __init__(self, nombre, nivel, elemento):
        super().__init__(nombre, nivel)
        self.__elemento = elemento

    def get_elemento(self):
        return self.__elemento

    def ataque_elemental(self):
        return f"{self.get_nombre()} realiza un ataque de tipo {self.get_elemento()}"

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Elemento: {self.get_elemento()}"