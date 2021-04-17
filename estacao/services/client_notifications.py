import pika
import uuid
import logging, logging.config
import json
from settings import RABBIT_SERVER, EXCHANGE_NOTIFICATIONS, ROUTING_KEY_NOTIFICATIONS, EXCHANGE_TYPE
from pika import BlockingConnection, ConnectionParameters, PlainCredentials, BasicProperties

credentials = PlainCredentials(RABBIT_SERVER['USER'], RABBIT_SERVER['PASS'])
parameters = ConnectionParameters(RABBIT_SERVER['HOST'],RABBIT_SERVER['PORT'],credentials=credentials)
connection = BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE_NOTIFICATIONS, exchange_type=EXCHANGE_TYPE)

result = channel.queue_declare(queue=ROUTING_KEY_NOTIFICATIONS, exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=EXCHANGE_NOTIFICATIONS, queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()