from enum import Enum
import logging, logging.config

logging.config.fileConfig(fname='logging.conf')
logger = logging.getLogger(__name__)

class Unidade(Enum):
    metro = 'm'
    segundo = 's'
    celsius = '°C'
    porcent = '%'
    kelvin = 'K'
    pascal = 'Pa'

    @staticmethod
    def has_key(str_unidade: str):
        unit = str_unidade.lower()
        if unit in Unidade.__members__:
            return Unidade[unit]
        else:
            logger.error("{} não existe no Enum Unidade".format(str_unidade))
            return None
    
    def __repr__(self):
        return str(self.name)