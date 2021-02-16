from unittest import main, TestCase

from principal.controller import AppController
from models.module import Module
from models.sensor import Sensor
from models.grandeza import Grandeza
from principal.dictionary import Unidade


appController = AppController(backup=False)

class TestAppControl(TestCase):

    def test_add_module_success(self):
        new_module = Module("mDHT","https","Teste module add")       
        self.assertTrue(appController.add_module(new_module))

    def test_add_module_duplicated(self):
        new_module = Module("mDHT2","https","Teste module add")
        appController.add_module(new_module)       
        self.assertFalse(appController.add_module(new_module))

    def test_add_grandeza_success(self): 
        self.assertEqual(appController.add_grandeza("Temperatura", "Celsius"), 1, "Não foi possível criar a Grandeza")

    def test_add_grandeza_duplicated(self):
        appController.add_grandeza("tempo", "segundo")       
        self.assertEqual(appController.add_grandeza("tempo", "segundo"), 2, "Adicionou grandeza já cadastrada")

    def test_add_grandeza_unit_error(self):  
        self.assertEqual(appController.add_grandeza("Temperatura", "fahrenheit"), 3, "Adicionou grandeza com unidade não cadastrada")

    def test_add_sensor_success(self):
        new_sensor = Sensor("estufa", "temperatura", "celsius", "mDHT")
        self.assertEqual(appController.add_sensor(new_sensor), 1, "Não foi possível inserir sensor")

    def test_add_sensor_duplicated(self):
        new_sensor = Sensor("sala", "temperatura", "celsius", "mDHT")
        appController.add_sensor(new_sensor)      
        self.assertEqual(appController.add_sensor(new_sensor), 2, "Cadastrou sensor com id_sensor ja cadastrado")

    def test_add_sensor_module_error(self):
       new_sensor = Sensor("sala1", "temperatura", "celsius", "mDHT5")    
       self.assertEqual(appController.add_sensor(new_sensor), 3, "Cadastrou sensor com id_module inexistente")

    def test_add_sensor_grandeza_error(self):
        new_sensor = Sensor("sala2", "proximidade", "celsius", "mDHT")    
        self.assertEqual(appController.add_sensor(new_sensor), 4, "Cadastrou sensor com grandeza inexistente")

if __name__ == '__main__':
    main()