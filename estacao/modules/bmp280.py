from modules.interfaces import IModule
import board
import busio
import adafruit_bmp280
from settings import I2C_ADDRESS, SEA_LEVEL_PRESSURE

class BMP280(IModule):
    def __init__(self):
        self.active = False
        self.address = I2C_ADDRESS
        self.sea_level_pressure = SEA_LEVEL_PRESSURE

    def read(self, type_grandeza: str):
        grandeza = type_grandeza.lower()
        if grandeza == "temperatura":
            return float("{:.2f}".format(self.bmp_i2c.temperature))
        elif grandeza == "pressure":
            return float("{:.2f}".format(self.bmp_i2c.pressure))
        elif grandeza == "altitude":
            return float("{:.2f}".format(self.bmp_i2c.altitude))
        else:
            return None

    def start(self):
        try:
            # Create library object using our Bus I2C port
            i2c = busio.I2C(board.SCL, board.SDA)
            self.bmp_i2c = adafruit_bmp280.Adafruit_BMP280_I2C(i2c,address=self.address)
        except Exception as e:
            raise e
        else:
            # change this to match the location's pressure (hPa) at sea level
            self.bmp_i2c.sea_level_pressure = self.sea_level_pressure
            self.active = True
