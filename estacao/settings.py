# False para Desenvolvimento
PRODUCTION=False

if PRODUCTION:
    DB_PATH='/estacao/estacao.db'
else:
    DB_PATH='estacao.db'

PREFIX_API_VERSION = '/api/v1'
API_PORT = 5000                         # Se alterar a Porta da API aqui, deve-se alterar no arquivo uwsgi.ini também.
API_DEBUG = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH

LOGGING_CONF = 'logging.ini'

# Ativação dos Serviços de Mensagens para requisições(MESSAGE) ou Notificações(NOTIFICATION)
SERVICE_MESSAGE = True
SERVICE_NOTIFICATION = True

# Altere para informações do Servidor de Fila de Mensagens (Broker)
# Projeto utiliza o broker do RabbitMQ
RABBIT_SERVER = {
    'HOST' : 'us127.serverdo.in',        # FQDN ou IP do servidor.
    'PORT' : 5672,                       # Porta para conexão, padrão do RabbitMQ é 5672.
    'USER' : 'admin',                    # Usuário do servidor de mensagens.
    'PASS' : 'pji29006'                  # Senha do Usuário informando.
}
EXCHANGE_NOTIFICATIONS='notifications'   # Exchange do Servidor RabbitMQ para envio das notificações (Publish/Subscribe).
EXCHANGE_TYPE='fanout'                   # Tipo de Exchange do servidor RabbitMQ (Publish/Subscribe).
ROUTING_KEY_NOTIFICATIONS=''             # Routing Key do servidor - Default ''
INTERVAL=15                              # Periodicidade para serviço de notificação ler sensores em segundos.


QUEUE_MESSAGES='rpc_queue'               # Nome da fila para requisições via RPC do RabbitMQ (RPC).
EXCHANGE_MESSAGES=''                     # Exchange do Servidor RabbitMQ para Serviço de Mensagens (RPC).








