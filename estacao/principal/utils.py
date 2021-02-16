# Classes uteis que são utilizadas pelo módulo controller
from models.grandeza import Grandeza
from models.sensor import Sensor

# Classe responsável por representar uma Medida
class Medida:
    def __init__(self, valor: float, grandeza: Grandeza):
        self.grandeza = grandeza
        self.valor = valor        