from unittest import main, TestCase
from modules.bmp280 import BMP280


bmp = BMP280()
bmp.start()
class TestModuleBMP280(TestCase):

    def test_read_temperatura(self):
        medida_temperatura = bmp.read('Temperatura')
        assert (medida_temperatura >= 0) or (medida_temperatura <= 100)

    def test_read_pressure(self):
        medida_pressure = bmp.read('Pressure')
        assert (medida_pressure >= 300) or (medida_pressure <= 3000)

    def test_read_invalid_grandeza(self):
        medida_umidade = bmp.read('Umidade')
        self.assertFalse(medida_umidade, 'Leitura realizada mesmo sem suporte')
