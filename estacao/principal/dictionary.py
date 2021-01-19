from enum import Enum
import logging

class Unidade(Enum):
    metro = 1
    segundo = 2
    celsius = 3

    @classmethod
    def has_key(cls, str_unidade: str):
        if str_unidade in cls.__members__:
            return str_unidade
        else:
            logging.error("{} não existe no Enum Unidade".format(str_unidade))
            raise ValueError('{} não é uma unidade válida'.format(str_unidade))