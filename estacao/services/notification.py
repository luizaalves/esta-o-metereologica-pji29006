from threading import Thread
from principal.utils import Medida, Notification
from settings import LOGGING_CONF, RABBIT_SERVER, API_PORT, EXCHANGE_NOTIFICATIONS
from pika import BlockingConnection, ConnectionParameters, PlainCredentials, BasicProperties

import logging, logging.config, time, json

logging.config.fileConfig(fname=LOGGING_CONF)
logger = logging.getLogger(__name__)

class NotificationService(Thread):
    def __init__(self, read_interval, controller):
        Thread.__init__(self)
        self.read_interval = read_interval
        self.app_controller = controller
        logger.info("Thread Notification Service Create")

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
                    notification = Notification(id_sensor, medida)
                    self.create_connection()
                    self.notify(notification)
    
    def create_connection(self):
        credentials = PlainCredentials(RABBIT_SERVER['USER'], RABBIT_SERVER['PASS'])
        parameters = ConnectionParameters(RABBIT_SERVER['HOST'],RABBIT_SERVER['PORT'],credentials=credentials)
        self.connection = BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=EXCHANGE_NOTIFICATIONS, exchange_type='fanout')

    def notify(self, notification: Notification):
        logger.info("notify() - %s" % notification)

        self.channel.basic_publish(exchange=EXCHANGE_NOTIFICATIONS,
                     routing_key='',
                     properties=BasicProperties(content_type='application/json'),
                     body=str(notification))

        self.connection.close()