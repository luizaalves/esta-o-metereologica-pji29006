from unittest import main, TestCase

from principal.controller import AppController
from models.module import Module
from models.sensor import Sensor
from models.grandeza import Grandeza
from models.limiar import Limiar
from principal.dictionary import Unidade


appController = AppController(backup=False)

class TestAppControl(TestCase):

    # Testes Modulos
    def test_add_module_success(self):
        new_module = Module("BMP180","https","Teste module add")       
        self.assertTrue(appController.add_module(new_module))

    def test_add_module_duplicated(self):
        new_module = Module("mDHT2","https","Teste module add")
        appController.add_module(new_module)       
        self.assertFalse(appController.add_module(new_module))

    # Testes Grandeza
    def test_add_grandeza_success(self): 
        self.assertEqual(appController.add_grandeza("Temperatura", "Celsius"), 1, "Não foi possível criar a Grandeza")

    def test_add_grandeza_duplicated(self):
        appController.add_grandeza("tempo", "segundo")       
        self.assertEqual(appController.add_grandeza("tempo", "segundo"), 2, "Adicionou grandeza já cadastrada")

    def test_add_grandeza_unit_error(self):  
        self.assertEqual(appController.add_grandeza("Temperatura", "fahrenheit"), 3, "Adicionou grandeza com unidade não cadastrada")

    # Testes Sensores
    def test_add_sensor_success(self):
        new_sensor = Sensor("estufa", "temperatura", "celsius", "BMP180")
        self.assertEqual(appController.add_sensor(new_sensor), 1, "Não foi possível inserir sensor")

    def test_add_sensor_duplicated(self):
        new_sensor = Sensor("sala", "temperatura", "celsius", "BMP180")
        appController.add_sensor(new_sensor)      
        self.assertEqual(appController.add_sensor(new_sensor), 2, "Cadastrou sensor com id_sensor ja cadastrado")

    def test_add_sensor_module_error(self):
       new_sensor = Sensor("sala1", "temperatura", "celsius", "mDHT5")    
       self.assertEqual(appController.add_sensor(new_sensor), 3, "Cadastrou sensor com id_module inexistente")

    def test_add_sensor_grandeza_error(self):
        new_sensor = Sensor("sala2", "proximidade", "celsius", "BMP180")    
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