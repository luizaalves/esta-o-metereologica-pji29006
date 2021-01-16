from unittest import main, TestCase

from estacao.utils import Medida, Grandeza
from estacao.dictionary import Unidade
from estacao.controller import AppController
from estacao.sensor import Sensor
from modules.interfaces import IModule

appController = AppController(None, None, None)
bmp180 = IModule()
celsius = Unidade.celsius
temperatura = Grandeza("Temperatura", celsius )
id_sensor = "sensor_temp"
sensor_temp = Sensor(id_sensor, "Sensor de temperatura", temperatura, bmp180)

class TestAppControl(TestCase):

    def test_add_sensor_success(self):       
        self.assertTrue(appController.add_sensor(sensor_temp))
    
    def test_compare_sensor_add(self):
        sensor_get = appController.get_sensor(id_sensor)       
        self.assertEqual(sensor_temp.id_sensor, sensor_get.id_sensor)

if __name__ == '__main__':
    main()