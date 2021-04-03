from modules.interfaces import IModule
import logging, logging.config

logging.config.fileConfig(fname='logging.ini')
logger = logging.getLogger(__name__)



class ModulesAvailable:
    # Nome da Classe e id_module devem ser os mesmos
    @staticmethod
    def get_instance(id_module: str):
        module = id_module.upper()
        if(module == "BMP180"):
            from modules.bmp180 import BMP180
            return BMP180()
        elif(module == "DHT11"):
            from modules.dht11 import DHT11
            return DHT11()
        elif(module == "HDC1080"):
            from modules.hdc1080 import HDC1080
            return HDC1080()
        elif(module == "PIR"):
            from modules.pir import PIR
            return PIR()
        elif(module == "BMP280"):
            from modules.bmp280 import BMP280
            return BMP280()
        else:
            logger.error('Não foi possível instanciar driver para módulo %s' % module)
            raise Exception("NotImplementedException - Driver não implementado")
            return None