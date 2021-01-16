from models import Sensor
from estacao.utils import Medida, Limiar

class AppController:
    def __init__(self, read_interval=1):

        self.read_interval = read_interval
        self.limiares = {}
        self.sensores = []
        self.modules = []
        self.gradezas = []

    def add_sensor(self, sensor: Sensor) -> bool:
        return False
    
    def config_limiar(self, limiares: Limiar, id_sensor: str) -> bool:
        return False

    def read_one(self, id_sensor: str) -> Medida:
        return None

    def read_all(self) -> list:
        return None

    def notify(self, id_sensor: str):
        pass

    def _read_db(self):
        pass

    def _write_db(self):
        pass

    def get_sensor(self, id_sensor) -> Sensor:
        return Sensor(None, None, None, None)