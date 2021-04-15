from threading import Thread
from requests import get, put
from settings import LOGGING_CONF, API_PORT, PREFIX_API_VERSION
from settings import RABBIT_SERVER, QUEUE_MESSAGES, EXCHANGE_MESSAGES
from pika import BlockingConnection, ConnectionParameters, PlainCredentials, BasicProperties
from pika.exceptions import AMQPConnectionError, AMQPChannelError

import re
import logging, logging.config, json

logging.config.fileConfig(fname=LOGGING_CONF)
logger = logging.getLogger(__name__)

class MessageService(Thread):
    """Classe do Serviço de Mensagens para Requisições externas.
       O código representa o Servidor e
       foi construido utilizando a implementação de RPC do rabbitMQ.

    Args:
        Thread : Extende a classe Thread para o serviço ficar rodando como outro processo.
    """
    def __init__(self):
        Thread.__init__(self, daemon=True)

        # Informações do Broker 
        USER = RABBIT_SERVER['USER']
        PASS = RABBIT_SERVER['PASS']
        HOST = RABBIT_SERVER['HOST']
        PORT = RABBIT_SERVER['PORT']

        credentials = PlainCredentials(USER, PASS)
        self.parameters = ConnectionParameters(HOST, PORT, credentials=credentials)

        self.__create_connection()
        logger.info("Serviço criado!")
        
    def run(self):
        logger.info("Iniciando Serviço de Mensagens")
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=QUEUE_MESSAGES, on_message_callback=self.request_callback)

        logger.info("Aguardando Requisições")
        self.channel.start_consuming()

    def request_callback(self, ch, method, props, body):
                
        logger.debug("propriedades request %s" % props)
        request_method = props.headers['Method']
        request_path = props.headers['Path']
        
        logger.info("Method request = %s" % request_method)
        logger.info("Path request = %s" % request_path)
        logger.info("Body request = %s" % body)

        response_body, response_status = self.__do_request(request_method, request_path, body)

        logger.debug("Response status = %s" % response_status)
        logger.debug("Response body = %s" % response_body)

        
        headers={'Status':response_status}
        content='application/json'

        basic_properties = BasicProperties(correlation_id = props.correlation_id, 
                                           headers=headers, 
                                           content_type=content)

        ch.basic_publish(exchange=EXCHANGE_MESSAGES,
                     routing_key=props.reply_to,
                     properties=basic_properties,
                     body=json.dumps(response_body))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def __create_connection(self):
        logger.info("Conectando ao broker...")
        try:
            connection = BlockingConnection(self.parameters)
        except AMQPConnectionError:
            logger.error("Não foi possível estabelecer conexão com Broker. Verifique parâmetros em settings.py")
            raise
        except Exception as e:
            logger.error(e)
            raise
        else:
            self.channel = connection.channel()
            self.channel.queue_declare(queue=QUEUE_MESSAGES)

    def __do_request(self, method, path, body):

        # Metodos e Paths da API disponiveis para Requisições externas
        METHODS = ['GET', 'PUT']
        SENSORS = PREFIX_API_VERSION + '/sensors'
        PATTERN_PATH_GET = re.compile(r'(' + SENSORS + '$)|(' + 
                                         SENSORS + '/[\w]+$)|(' + 
                                         SENSORS + '/[\w]+/limiares$)')
        
        PATTERN_PATH_PUT = re.compile(r'(' + SENSORS + '/[\w]+/limiares$)')

        url = 'http://localhost:' + str(API_PORT) + path

        if method not in METHODS:
            msg = ('Method %s invalido' % method)
            response_body = {'Error': msg}
            return response_body, 400
        elif method == 'GET':
            match = bool(re.match(PATTERN_PATH_GET, path))    
            logger.debug("Match %s" % match)
            if not match:
                msg = ('Path %s invalida' % path)
                response_body = {'Error': msg}
                return response_body, 400
            
            response = get(url)
            response_body = response.json()
        elif method == 'PUT':
            match = bool(re.match(PATTERN_PATH_PUT, path))    
            logger.debug("Match %s" % match)
            if not match:
                msg = ('Path %s invalida' % path)
                response_body = {'Error': msg}
                return response_body, 400

            request_body_json = json.loads(body)
            logger.debug("body_json = %s" % request_body_json)
            response = put(url,json=request_body_json)
            if response.status_code == 204:
                response_body = ''
            else:
                response_body = response.json()
        
        logger.debug("Response = %s" % response)
        
        return response_body, response.status_code