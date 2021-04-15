from modules.interfaces import IModule
from random import randint

class BMP280(IModule):
    def __init__(self):
        self.active = True
       
    def read(self, type_grandeza: str):
        if type_grandeza.upper() == "Temperatura":
            return randint(0,100)
        elif type_grandeza.upper() == "Pressure":
            return randint(300,3000)
        else:
            return randint(0,50)
    
    def start(self):
        print("Iniciando {}".format(self.__class__))