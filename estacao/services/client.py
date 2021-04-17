import pika
import uuid
import logging, logging.config
import json
from settings import RABBIT_SERVER, QUEUE_MESSAGES, EXCHANGE_MESSAGES
from pika import BlockingConnection, ConnectionParameters, PlainCredentials, BasicProperties

class Client(object):

    def __init__(self):
        credentials = PlainCredentials(RABBIT_SERVER['USER'], RABBIT_SERVER['PASS'])
        parameters = ConnectionParameters(RABBIT_SERVER['HOST'],RABBIT_SERVER['PORT'],credentials=credentials)
        self.connection = BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=QUEUE_MESSAGES)

        result = self.channel.queue_declare(queue=EXCHANGE_MESSAGES, exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = True
            self.response_body = body
            self.response_status = props.headers['Status']

    def call(self, request_path, request_method, request_body):
        self.response = False
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=EXCHANGE_MESSAGES,
            routing_key=QUEUE_MESSAGES,
            properties=BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
                content_type='application/json',
                headers={'Method': request_method, 'Path': request_path}
            ),
            body=json.dumps(request_body))
        while not self.response:
            self.connection.process_data_events()
        return self.response_body, self.response_status