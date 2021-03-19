from flask_restful import fields, marshal_with, marshal, reqparse, Resource
from principal.utils import Medida
from principal.dictionary import Unidade
from api.resources.errors import NotFoundError, BadRequestError, ConflictError, InternalServerError
import logging, logging.config
from settings import LOGGING_CONF

logging.config.fileConfig(fname=LOGGING_CONF)
logger = logging.getLogger(__name__)


medida_fields = {
    'type_grandeza': fields.String,
    'value': fields.Float,
    'unit': fields.String(x.name for x in Unidade),
}
error_fields = {
    'code': fields.Integer,
    'message': fields.String,
    'description': fields.String
}
notfound_description = "id_sensor não encontrado ou inválido"
internalserver_description = "Erro efetuar leitura do Sensor. Consulte Logs do Sistema"

class MedidasAPI(Resource):
    def __init__(self, **kwargs):

        self.estacao = kwargs['estacao']

    def get(self, id_sensor):
        sensor_id = id_sensor.lower() 
        sensor = self.estacao.sensores.get(sensor_id)
        logger.debug(sensor)       
        if sensor is None:
            error = NotFoundError(notfound_description)
            return marshal(error, error_fields, 'error'), 404
        medida = self.estacao.read_one(sensor_id)
        logger.debug(medida) 
        return marshal(medida, medida_fields), 200