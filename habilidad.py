# habilidad.py
class Habilidad:
    def __init__(self, habilidad):
        self._habilidad = habilidad

    def get_habilidad(self):
        return self._habilidad

    def set_habilidad(self, habilidad):
        self._habilidad = habilidad

    def __str__(self):
        return f"Habilidad especial: {self.get_habilidad()}"
