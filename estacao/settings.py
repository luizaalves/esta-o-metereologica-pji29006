PRODUCTION=True

if PRODUCTION:
    DB_PATH='/estacao/estacao.db'
else:
    DB_PATH='estacao.db'

PREFIX_API_VERSION = '/api/v1'
API_PORT = 5000
API_DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH

RABBIT_SERVER = {
    'HOST' : 'us127.serverdo.in',
    'PORT' : 5672,
    'USER' : 'admin',
    'PASS' : 'pji29006'
}
EXCHANGE_NOTIFICATIONS='notifications'

SERVICE_NOTIFICATION = True
SERVICE_MESSAGE = True
LOGGING_CONF = 'logging.ini'


