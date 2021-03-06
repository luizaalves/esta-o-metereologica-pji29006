import pika
import uuid
import logging, logging.config
from settings import RABBIT_SERVER
from pika import BlockingConnection, ConnectionParameters, PlainCredentials, BasicProperties

class Client(object):

    def __init__(self):
        credentials = PlainCredentials(RABBIT_SERVER['USER'], RABBIT_SERVER['PASS'])
        parameters = ConnectionParameters(RABBIT_SERVER['HOST'],RABBIT_SERVER['PORT'],credentials=credentials)
        self.connection = BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='rpc_queue')

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)