from modules.interfaces import IModule
from random import randint

class Example(IModule):
    def __init__(self):
        self.active = False
        # Adicionar propriedades necessárias para o Modulo

    def read(self, type_grandeza: str):
        grandeza = type_grandeza.lower()
        if grandeza == "temperatura":
            return float("{:.2f}".format(randint(0,100)))
        elif grandeza == "umidade":
            return float("{:.2f}".format(randint(0,100)))
        else:
            raise Exception("Grandeza %s não suportado pelo Modulo" % grandeza)

    def start(self):
        try:
            # Configurações relacionadas ao módulo físico
            # Portas GPIO, Intefaces (I2C, SPI)
            print("Módulo conectado a GPIO 7")
        except Exception as e:
            raise e
        else:
             # Configuração para iniciar/ativar módulo
             print("Ativação do Módulo Example")
             self.active = True