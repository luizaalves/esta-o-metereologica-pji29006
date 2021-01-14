# Modulo para classes uteis que são utilizadas pelo módulo controller

from estacao.dictionary import Unidade

# Classe reponsável por representar uma grandeza
class Grandeza:

    def __init__(self, nome: str, unidade: Unidade):
        """Construtor da classe

        Args:
            nome (str): [nome da grandeza - Ex.: Temperatura]
            unidade (Unidade): [unidade da grandeza - Ex.: Celsius]
        """
        self.nome = nome
        self.unidade = unidade

@property
def nome(self) -> str:
    return self._nome

@nome.setter
def nome(self, nome: str):
    self._nome = nome

@property
def unidade(self) -> Unidade:
    return self._unidade

@unidade.setter
def unidade(self, unidade: Unidade):
    if not isinstance(unidade, Unidade):
        raise TypeError("Deve ser um Unidade, não {}".format(type(unidade)))
    self._unidade = unidade


# Classe responsável por representar uma Medida
class Medida:
    def __init__(self, valor: float, grandeza: Grandeza):
        self.grandeza = grandeza
        self.valor = valor