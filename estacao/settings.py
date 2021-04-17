# False para Desenvolvimento
PRODUCTION=True

if PRODUCTION:
    DB_PATH='/estacao/estacao.db'
    LOGGING_CONF = '/estacao/logging.ini'
else:
    DB_PATH='estacao.db'
    LOGGING_CONF = 'logging.ini'

PREFIX_API_VERSION = '/api/v1'
# Se alterar a Porta da API aqui, deve-se alterar no arquivo uwsgi.ini também.
API_PORT = 5000                         
API_DEBUG = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH

## Ativação dos Serviços 
# Mensagens para requisições(MESSAGE) ou Notificações(NOTIFICATION).
# Altere para False se não deseja utilizar um dos (ou os dois) Serviços.
SERVICE_MESSAGE = True
SERVICE_NOTIFICATION = True

## Configurar informações de conexão com o broker.
RABBIT_SERVER = {
	'HOST' : 'IP ou FQDN do broker',
	'PORT' : Porta_do_broker,
	'USER' : 'User',
	'PASS' : 'Password'
}

## Configurar informações da Fila de Notificações

# Exchange RabbitMQ para envio das notificações (Pub/Subs).
EXCHANGE_NOTIFICATIONS='notifications'
# Tipo de Exchange do servidor RabbitMQ (Publish/Subscribe).
EXCHANGE_TYPE='fanout'
# Routing Key do servidor - Default ''
ROUTING_KEY_NOTIFICATIONS=''
# Periodicidade (segundos) para serviço de notificação ler sensores.
INTERVAL=5                               

## Configurar informações da Fila de requisições

# Nome da fila para requisições via RPC do RabbitMQ (RPC).
QUEUE_MESSAGES='rpc_queue'
# Exchange RabbitMQ para envio das requsições (RPC).
EXCHANGE_MESSAGES='' 

## Configurações do Modulo/driver BMP280 padrão

# Verificar endereço da interface na Rasp - sudo i2cdetect -y 1
# Se o comando acima não retornar nada é possível que a interface 
# I2C na rasp não esteja habilitada.
# Para habilitar execute - sudo raspi-config - 
# e escolha as opções 5 e P5.

# Algumas placas o endereço é 0x77
I2C_ADDRESS = 0x76
# Pressao nivel do mar em Florianopolis
SEA_LEVEL_PRESSURE = 1020.00 
# True para utilizar o módulo BMP280 implementado por padrão.
USE_BMP280=True 




