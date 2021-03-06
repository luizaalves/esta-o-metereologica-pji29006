from modules.interfaces import IModule

class ModulesAvailable:
    # Nome da Classe e id_module devem ser os mesmos
    @staticmethod
    def get_instance(id_module: str):
        module = id_module.upper()
        if(module == "BMP180"):
            from modules.bmp180 import BMP180
            return BMP180()
        if(module == "DHT11"):
            from modules.dht11 import DHT11
            return DHT11()
        if(module == "HDC1080"):
            from modules.hdc1080 import HDC1080
            return HDC1080()
        if(module == "PIR"):
            from modules.pir import PIR
            return PIR()