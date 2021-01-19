from flask_restful import fields, marshal_with, reqparse, Resource
from principal.dictionary import Unidade

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'id_sensor', dest='id_sensor',
    location='json', required=True,
    help='Identificador do Sensor - {error_msg}',
)
post_parser.add_argument(
    'type_grandeza', dest='type_grandeza',
    location='json', required=True,
    help='Grandeza Medida pelo Sensor - {error_msg}',
)
post_parser.add_argument(
    'id_module', dest='id_module',
    location='json', required=True,
    help='Identificador do Módulo utilizado - {error_msg}',
)
modules_fields = {
    'id_sensor': fields.String,
    'description': fields.String,
    'type_grandeza': Unidade,
    'id_module': fields.String
}

class SensorsAPI(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.estacao = kwargs['estacao']

    def get(self, id_sensor=None):
        interval = self.estacao.read_interval
        return interval

    @marshal_with(modules_fields, envelope='sensors')
    def post(self):
        args = post_parser.parse_args()
        sensor = args.id_sensor
        print(sensor)
        return  sensor,201



