from flask_restful import fields, marshal_with, marshal, reqparse, Resource
from models.entities import Limiar
from api.resources.errors import NotFoundError, BadRequestError, ConflictError, InternalServerError

put_parser = reqparse.RequestParser()

put_parser.add_argument('value_min', type=float, dest='value_min', location='json', required=True,
    help='Campo value_min é obrigatório - {error_msg}',
)
put_parser.add_argument('value_max', type=float, dest='value_max', location='json', required=True,
    help='Campo value_max é obrigatório - {error_msg}'
)

limiar_fields = {
    'value_min': fields.Float,
    'value_max': fields.Float
}
error_fields = {
    'code': fields.Integer,
    'message': fields.String,
    'description': fields.String
}

notfound_description = "id_sensor não encontrado"

class LimiaresAPI(Resource):
    def __init__(self, **kwargs):

        self.estacao = kwargs['estacao']

    def get(self, id_sensor):
        sensor_id = id_sensor.lower() 
        sensor = self.estacao.sensores.get(sensor_id)       
        if sensor is None:
            error = NotFoundError(notfound_description)
            return marshal(error, error_fields, 'error'), 404
        limiar = self.estacao.limiares.get(sensor_id)
        return marshal(limiar, limiar_fields), 200

    def put(self, id_sensor):
        args = put_parser.parse_args()
        change_limiar =  Limiar(id_sensor, args.value_min, args.value_max)
        result_change = self.estacao.config_limiar(change_limiar)
        if result_change == 2:
            error = NotFoundError(notfound_description)
            return marshal(error, error_fields, 'error'), 404
        return  None , 204           