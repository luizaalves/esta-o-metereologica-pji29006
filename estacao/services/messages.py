from threading import Thread
import logging, logging.config
from settings import RABBIT_SERVER
from pika import BlockingConnection, ConnectionParameters, PlainCredentials, BasicProperties

logging.config.fileConfig(fname='logging.conf')
logger = logging.getLogger(__name__)

class MessageService(Thread):
    def __init__(self):
        Thread.__init__(self)
        logger.info("Thread Message Service Create")

        credentials = PlainCredentials(RABBIT_SERVER['USER'], RABBIT_SERVER['PASS'])
        parameters = ConnectionParameters(RABBIT_SERVER['HOST'],RABBIT_SERVER['PORT'],credentials=credentials)
        self.connection = BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='rpc_queue')

    def run(self):
        logger.info("Iniciando Serviço de Mensagens")
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='rpc_queue', on_message_callback=self.request_callback)

        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()

    def request_callback(self, ch, method, props, body):
        n = int(body)

        print(" [.] received(%s)" % n)
        response = n + 1

        ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=BasicProperties(correlation_id = props.correlation_id),
                     body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)

        