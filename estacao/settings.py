PREFIX_API_VERSION = '/api/v1'
API_PORT = 5000
API_DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///estacao.db'

RABBIT_SERVER = {
    'HOST' : 'us127.serverdo.in',
    'PORT' : 5672,
    'USER' : 'admin',
    'PASS' : 'pji29006'
}

SERVICE_NOTIFICATION = False
SERVICE_MESSAGE = True
LOGGING_CONF = 'logging.ini'


