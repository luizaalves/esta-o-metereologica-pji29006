from enum import Enum
import logging

class Unidade(Enum):
    metro = 'm'
    segundo = 's'
    celsius = '°C'
    porcent = '%'
    kelvin = 'K'

    @staticmethod
    def has_key(str_unidade: str):
        unit = str_unidade.lower()
        if unit in Unidade.__members__:
            return Unidade[unit]
        else:
            logging.error("{} não existe no Enum Unidade".format(str_unidade))
            return None
    
    def __repr__(self):
        return str(self.name)