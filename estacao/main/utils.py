# Modulo para classes uteis que são utilizadas pelo módulo controller
from models import Grandeza

# Classe responsável por representar uma Medida
class Medida:
    def __init__(self, valor: float, grandeza: Grandeza):
        self.grandeza = grandeza
        self.valor = valor
