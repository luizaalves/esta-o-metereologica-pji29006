from threading import Thread
from principal.utils import Medida, Notification
from settings import LOGGING_CONF, API_PORT, PREFIX_API_VERSION
from settings import RABBIT_SERVER, EXCHANGE_NOTIFICATIONS, EXCHANGE_TYPE, ROUTING_KEY_NOTIFICATIONS
from pika import BlockingConnection, ConnectionParameters, PlainCredentials, BasicProperties
from pika.exceptions import AMQPConnectionError, AMQPChannelError

import logging, logging.config, time, json

logging.config.fileConfig(fname=LOGGING_CONF)
logger = logging.getLogger(__name__)

class NotificationService(Thread):
    """Classe do Serviço de Notificações.
       O código representa o Produtor e
       foi construido utilizando a implementação de Publish/Subscribe do RabbitMQ.

    Args:
        Thread : Extende a classe Thread para o serviço ficar rodando como outro processo.
    """
    def __init__(self, read_interval, controller):
        Thread.__init__(self, daemon=True)
        self.read_interval = read_interval
        self.app_controller = controller

        # Informações do Broker 
        USER = RABBIT_SERVER['USER']
        PASS = RABBIT_SERVER['PASS']
        HOST = RABBIT_SERVER['HOST']
        PORT = RABBIT_SERVER['PORT']

        credentials = PlainCredentials(USER, PASS)
        self.parameters = ConnectionParameters(HOST, PORT, credentials=credentials)

        logger.info("Serviço de Notificação criado!")

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
                    logger.info("Limite atingido")
                    notification = Notification(id_sensor, medida)
                    self.__create_connection()
                    self.__notify(notification)
    
    def __create_connection(self):
        logger.info("Conectando ao broker...")
        try:
            self.connection = BlockingConnection(self.parameters)
        except AMQPConnectionError:
            logger.error("Não foi possível estabelecer conexão com Broker. Verifique parâmetros em settings.py")
            raise 
        else:
            self.channel = self.connection.channel()
            self.channel.exchange_declare(exchange=EXCHANGE_NOTIFICATIONS, exchange_type=EXCHANGE_TYPE)

    def __notify(self, notification: Notification):
        logger.info("Enviando Notificação - %s" % notification)

        content='application/json'
        basic_properties = BasicProperties(content_type=content)

        self.channel.basic_publish(exchange=EXCHANGE_NOTIFICATIONS,
                            routing_key=ROUTING_KEY_NOTIFICATIONS,
                            properties=basic_properties,
                            body=str(notification))

        self.connection.close()