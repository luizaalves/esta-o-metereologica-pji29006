# Classes uteis que são utilizadas pelo módulo controller
from models.entities import Grandeza

# Classe responsável por representar uma Medida
class Medida:
    def __init__(self, valor: float, grandeza: Grandeza):
        self.value = valor 
        self.unit = grandeza.unit
        self.type_grandeza = grandeza.type_grandeza
               

    def __repr__(self):
        return 'Medida("%s","%s","%s")' % (self.type_grandeza, self.value, self.unit)