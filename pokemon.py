# pokemon.py
class Pokemon:
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return f"{self.get_nombre()} es un Pokémon de tipo {self.get_tipo()}"
