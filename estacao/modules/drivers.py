from modules.interfaces import IModule
import logging, logging.config
from settings import LOGGING_CONF as CONF

logging.config.fileConfig(fname=CONF)
logger = logging.getLogger(__name__)



class ModulesAvailable:
    # Nome da Classe e id_module devem ser os mesmos
    @staticmethod
    def get_instance(id_module: str):
        module = id_module.upper()
        if module == "BMP280":
            from modules.bmp280 import BMP280
            return BMP280()
        #elif module == "EXAMPLE":
        #    from modules.example import EXAMPLE
        #    return EXAMPLE()
        else:
            logger.error('Não foi possível instanciar driver para módulo %s' % module)
            raise Exception("NotImplementedException - Driver não implementado")
            return None
