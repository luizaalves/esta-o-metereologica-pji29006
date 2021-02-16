from flask_restful import fields, marshal_with, marshal, reqparse, Resource
from models.sensor import Sensor
from principal.dictionary import Unidade
from api.resources.errors import NotFoundError, BadRequestError, ConflictError, InternalServerError
import logging, logging.config

logging.config.fileConfig(fname='logging.conf')
logger = logging.getLogger(__name__)

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'id_sensor', dest='id_sensor',
    location='json', required=True,
    help='campo id_sensor obrigatório - {error_msg}',
)
post_parser.add_argument(
    'type_grandeza', dest='type_grandeza',
    location='json', required=True,
    help='campo type_grandeza obrigatório- {error_msg}',
)
post_parser.add_argument(
    'unit', dest='unit',
    location='json', required=True,
    help='campo unit obrigatório- {error_msg}',
)
post_parser.add_argument(
    'id_module', dest='id_module',
    location='json', required=True,
    help='campo id_module obrigatório - {error_msg}',
)
post_parser.add_argument('description', dest='description', location='json',
    help='Descrição do módulo - {error_msg}',
)
sensors_fields = {
    'id_sensor': fields.String,
    'description': fields.String,
    'type_grandeza': fields.String,
    'unit': fields.String(x.name for x in Unidade),
    'id_module': fields.String
}
error_fields = {
    'code': fields.Integer,
    'message': fields.String,
    'description': fields.String
}

conflit_description = "Sensor com id_sensor=%s já cadastrado"
notfound_description = "id_sensor=%s não encontrado"

class SensorsAPI(Resource):
    def __init__(self, **kwargs):

        self.estacao = kwargs['estacao']

    def get(self, id_sensor=None):
        if id_sensor is None:
            sensors = list(self.estacao.sensores.values())
            return  marshal(sensors, sensors_fields, 'sensores'), 200
        
        # se receber o parâmetro id_sensor na URL
        sensor = self.estacao.sensores.get(id_sensor, None)
        if sensor is None:
            error = NotFoundError(notfound_description % (id_sensor))
            return marshal(error, error_fields, 'error'), 404
        return marshal(sensor, sensors_fields), 200      

    def post(self):
        args = post_parser.parse_args()
        id_sensor = args.id_sensor
        type_grandeza = args.type_grandeza
        unit = args.unit
        id_module = args.id_module
        description = args.description

        new_sensor =  Sensor(id_sensor, type_grandeza, unit, id_module, description)
        result_add = self.estacao.add_sensor(new_sensor)
        if result_add == 4: # Tipo de grandeza ou unidade inexistente
            error = BadRequestError('Grandeza (tipo ou unidade) não cadastrada')
            return marshal(error, error_fields, 'error'), 400
        if result_add == 3: # id_module inexistente
            error = BadRequestError('id_module inexistente')
            return marshal(error, error_fields, 'error'), 400
        if result_add == 2: # Sensor com mesmo id já cadastrado
            error = ConflictError(conflit_description % (id_sensor))
            return marshal(error, error_fields, 'error'), 409
        return  marshal(new_sensor, sensors_fields), 201

    def put(self):
        args = post_parser.parse_args()
        id_sensor = args.id_sensor
        type_grandeza = args.type_grandeza
        unit = args.unit
        id_module = args.id_module
        description = args.description

        change_sensor =  Sensor(id_sensor, type_grandeza, unit, id_module, description)
        result_change = self.estacao.change_sensor(change_sensor)
        if result_change == 4: # Tipo de grandeza ou unidade inexistente
            error = BadRequestError('Grandeza (tipo ou unidade) não cadastrada')
            return marshal(error, error_fields, 'error'), 400
        if result_change== 3: # id_module inexistente
            error = BadRequestError('id_module inexistente')
            return marshal(error, error_fields, 'error'), 400
        if result_change == 1: # Sensor com id inexistente
            error = NotFoundError(notfound_description % (id_sensor))
            return marshal(error, error_fields, 'error'), 404
        return  None, 204
