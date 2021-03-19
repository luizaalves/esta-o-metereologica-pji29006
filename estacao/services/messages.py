from threading import Thread
import logging, logging.config
import json
from requests import get, put
from settings import RABBIT_SERVER, API_PORT
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

        logger.info("Aguardando Requisições")
        self.channel.start_consuming()

    def request_callback(self, ch, method, props, body):
        
        logger.debug("propriedades request %s" % props)
        request_method = props.headers['Method']
        request_path = props.headers['Path']
        
        logger.info("Method request = %s" % request_method)
        logger.info("Path request = %s" % request_path)
        logger.info("Body request = %s" % body)

        url = 'http://localhost:' + str(API_PORT) + request_path

        if request_method == 'GET':
            response = get(url)
            response_body = response.json()

        elif request_method == 'PUT':
            request_body_json = json.loads(body)
            logger.debug("body_json = %s" % request_body_json)
            response = put(url,json=request_body_json)
            if response.status_code == 204:
                response_body = ''
            else:
                response_body = response.json()
        
        logger.debug("Response = %s" % response)
        
        response_status = response.status_code
        
        logger.debug("Response status = %s" % response_status)
        logger.debug("Response body = %s" % response_body)


        ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=BasicProperties(correlation_id = props.correlation_id, headers={'Status':response_status}, content_type='application/json'),
                     body=json.dumps(response_body))
        ch.basic_ack(delivery_tag=method.delivery_tag)

        