from unittest import main, TestCase

from principal.controller import AppController
from models.module import Module
from models.sensor import Sensor


appController = AppController(backup=False)

class TestAppControl(TestCase):

    def test_add_module_success(self):
        new_module = Module("mDHT","https","Teste module add")       
        self.assertTrue(appController.add_module(new_module))

    def test_add_module_duplicated(self):
        new_module = Module("mDHT2","https","Teste module add")
        appController.add_module(new_module)       
        self.assertFalse(appController.add_module(new_module))


if __name__ == '__main__':
    main()