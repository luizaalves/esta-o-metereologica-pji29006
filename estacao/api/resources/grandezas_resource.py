from flask_restful import fields, marshal_with, marshal, reqparse, Resource
from models.grandeza import Grandeza
from principal.dictionary import Unidade
from api.resources.errors import NotFoundError, BadRequestError, ConflictError, InternalServerError

post_parser = reqparse.RequestParser()

post_parser.add_argument('type_grandeza', dest='type_grandeza', location='json', required=True,
    help='Tipo da Grandeza é obrigatório - {error_msg}',
)
post_parser.add_argument('unit', dest='unit', location='json', required=True,
    help='Campo unit é obrigatório - {error_msg}',
)

modules_fields = {
    'type_grandeza': fields.String,
    'unit': Unidade,
}
error_fields = {
    'code': fields.Integer,
    'message': fields.String,
    'description': fields.String
}
conflit_description = "Grandeza com mesmo tipo já cadastrada"
notfound_description = "tipo não encontrado ou inválido"

class GrandezasAPI(Resource):
    def __init__(self, **kwargs):

        self.estacao = kwargs['estacao']