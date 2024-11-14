class Pokemon:
    def __init__(self, nombre, nivel):
        self.__nombre = nombre
        self.__nivel = nivel

    def get_nombre(self):
        return self.__nombre

    def get_nivel(self):
        return self.__nivel

    def set_nivel(self, nivel):
        if nivel >= 0:
            self.__nivel = nivel

    def mostrar_info(self):
        return f"Nombre: {self.get_nombre()}, Nivel: {self.get_nivel()}"