class MegaEvolucion:
    def __init__(self):
        self.__mega_evolucionado = False

    def get_mega_evolucionado(self):
        return self.__mega_evolucionado

    def set_mega_evolucionado(self, valor):
        self.__mega_evolucionado = valor

    def mega_evolucionar(self):
        if not self.get_mega_evolucionado():
            self.set_mega_evolucionado(True)
            return f"¡{self.get_nombre()} ha Mega Evolucionado!"
        return f"{self.get_nombre()} ya está en forma Mega"

    def estado_mega(self):
        return "Mega Evolucionado" if self.get_mega_evolucionado() else "Normal"