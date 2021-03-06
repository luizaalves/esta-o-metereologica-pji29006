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
        logger.info("Thread Notification Create")

    def run(self):
        logger.info("Iniciando Serviço de Notificação")
        while True:
            time.sleep(self.read_interval)
            medidas = self.app_controller.read_all()
            for id_sensor, medida in medidas.items():
                limiar = self.app_controller.limiares.get(id_sensor.lower())
                min_reached = medida.value < limiar.value_min
                max_reached = medida.value > limiar.value_max
                if min_reached or max_reached:
                    logger.info("Limite atingido. Enviando Notificação")
                    self.app_controller.notify(id_sensor, medida)