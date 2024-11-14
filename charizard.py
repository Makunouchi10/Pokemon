from fuego import PokemonFuego

class Charizard(PokemonFuego):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.__tipo_secundario = "Volador"

    def get_tipo_secundario(self):
        return self.__tipo_secundario

    def ataque_aereo(self):
        return f"{self.get_nombre()} usa Ala de Acero"

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo secundario: {self.get_tipo_secundario()}"