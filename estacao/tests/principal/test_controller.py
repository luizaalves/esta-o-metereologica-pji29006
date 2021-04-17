from unittest import main, TestCase

from principal.controller import AppController
from models.entities import Module, Sensor, Limiar
from principal.utils import Grandeza
from principal.dictionary import Unidade
from settings import INTERVAL


appController = AppController(read_interval=INTERVAL, backup=False)

class TestAppControl(TestCase):

    # Testes Modulos
    def test_add_module_1_success(self):
        new_module = Module("BMP280","temperatura, pressure, altitude","Test module add")
        result = appController.add_module(new_module)     
        self.assertEqual(result, 1, "Não foi possível adicionar módulo")

    def test_add_module_2_duplicated(self):
        new_module = Module("BMP280","temperatura, pressure, altitude","Test module duplicated")
        result = appController.add_module(new_module)        
        self.assertEqual(result, 2, "Adicionou modulo já cadastrado")
    
    def test_add_module_not_implemented(self):
        new_module = Module("BMP180","temperatura, pressure","Test module not implemented")
        result = appController.add_module(new_module)        
        self.assertEqual(result, 3, "Adicionou modulo sem driver implementado")

    # Testes Grandeza
    def test_add_grandeza_1_success(self):
        result =  appController.add_grandeza("Temperatura", "Celsius")
        self.assertEqual(result, 1, "Não foi possível criar a Grandeza")

    def test_add_grandeza_2_duplicated(self):
        appController.add_grandeza("tempo", "segundo")       
        self.assertEqual(appController.add_grandeza("tempo", "segundo"), 2, "Adicionou grandeza já cadastrada")

    def test_add_grandeza_unit_error(self):  
        self.assertEqual(appController.add_grandeza("Temperatura", "fahrenheit"), 3, "Adicionou grandeza com unidade não cadastrada")

    # Testes Sensores
    def test_add_sensor_1_success(self):
        new_sensor = Sensor("estufa", "temperatura", "celsius", "BMP280")
        self.assertEqual(appController.add_sensor(new_sensor), 1, "Não foi possível inserir sensor")

    def test_add_sensor_2_duplicated(self):
        new_sensor = Sensor("sala", "temperatura", "celsius", "BMP280")
        appController.add_sensor(new_sensor)      
        self.assertEqual(appController.add_sensor(new_sensor), 2, "Cadastrou sensor com id_sensor ja cadastrado")

    def test_add_sensor_module_error(self):
       new_sensor = Sensor("sala1", "temperatura", "celsius", "DHT5")    
       self.assertEqual(appController.add_sensor(new_sensor), 3, "Cadastrou sensor com id_module inexistente")

    def test_add_sensor_grandeza_error(self):
        new_sensor = Sensor("sala2", "proximidade", "celsius", "BMP280")    
        self.assertEqual(appController.add_sensor(new_sensor), 4, "Cadastrou sensor com grandeza inexistente")

    # Testes configuração de Limiar
    def test_config_limiar_success(self):
        new_limiar = Limiar("estufa", 30.0 ,37.0)
        self.assertEqual(appController.config_limiar(new_limiar), 1, "Não foi possível inserir sensor")
    
    def test_config_limiar_sensor_error(self):
        new_limiar = Limiar("estufa5", 30.0 ,37.0)
        self.assertEqual(appController.config_limiar(new_limiar), 2, "Cadastrou limiar com id_sensor inexistente")

if __name__ == '__main__':
    main()