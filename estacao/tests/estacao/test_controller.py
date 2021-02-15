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
        self.assertEqual(appController.add_grandeza("tempo", "segundo"), 2, "Grandeza já existe")

    def test_add_grandeza_unit_error(self):  
        self.assertEqual(appController.add_grandeza("Temperatura", "fahrenheit"), 3, "Unidade não cadastrada")

if __name__ == '__main__':
    main()