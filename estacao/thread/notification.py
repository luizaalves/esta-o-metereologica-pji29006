from threading import Thread
from principal.utils import Medida
import time
import logging, logging.config

logging.config.fileConfig(fname='logging.conf')
logger = logging.getLogger(__name__)

class Notification(Thread):
    def __init__(self, read_interval, controller):
        Thread.__init__(self)
        self.read_interval = read_interval
        self.app_controller = controller

    def run(self):
        while True:
            time.sleep(self.read_interval)
            medidas = self.app_controller.read_all()
            if medidas:
                for id_sensor, medida in medidas.items():
                    limiar = self.app_controller.limiares.get(id_sensor)
                    lim_max = medida.value > limiar.value_max
                    lim_min = medida.value < limiar.value_min
                    if lim_max or lim_min:
                        logger.debug('Limiar atingindo. Sensor = %s, medida = %s' % (id_sensor, medida))
                        self.app_controller.notify(id_sensor, medida)
            else:
                logger.debug('Nenhuma medida retornada')
                break