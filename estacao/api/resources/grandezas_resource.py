from flask_restful import fields, marshal_with, marshal, reqparse, Resource
from models.entities import Grandeza
from principal.dictionary import Unidade
from api.resources.errors import NotFoundError, BadRequestError, ConflictError, InternalServerError

post_parser = reqparse.RequestParser()

post_parser.add_argument('type_grandeza', dest='type_grandeza', location='json', required=True,
    help='Tipo da Grandeza é obrigatório - {error_msg}',
)
post_parser.add_argument('unit', dest='unit', location='json', required=True,
    help='Campo unit é obrigatório - {error_msg}',
)

grandeza_fields = {
    'type_grandeza': fields.String,
    'unit': fields.String(x.name for x in Unidade),
}
error_fields = {
    'code': fields.Integer,
    'message': fields.String,
    'description': fields.String
}
conflit_description = "Grandeza com mesmo tipo já cadastrada"
notfound_description = "tipo não encontrado ou inválido"
badrequest_description = "Unidade não cadastrada"

class GrandezasAPI(Resource):
    def __init__(self, **kwargs):

        self.estacao = kwargs['estacao']

    def get(self, type_grandeza=None):
        if type_grandeza is None:
            grandezas = list(self.estacao.grandezas.values())
            return  marshal(grandezas, grandeza_fields, 'grandezas'), 200
        
        # se receber o parâmetro type_grandeza na URL
        
        grandeza_list = list(self.estacao.grandezas.values())
        grandeza_filter = [grandeza for grandeza in grandeza_list if type_grandeza.lower() in grandeza.type_grandeza.lower()]
        
        if grandeza_filter is None:
            error = NotFoundError(notfound_description)
            return marshal(error, error_fields, 'error'), 404
        
        return marshal(grandeza_filter, grandeza_fields, 'grandezas'), 200           

    def post(self):
        args = post_parser.parse_args()
        unit_str = args.unit
        result_add = self.estacao.add_grandeza(args.type_grandeza, unit_str)
        if result_add == 3:
            error = BadRequestError(badrequest_description)
            return marshal(error, error_fields, 'error'), 400
        if result_add == 2:
            error = ConflictError(conflit_description)
            return marshal(error, error_fields, 'error'), 409
        new_grandeza = self.estacao.grandezas.get(unit_str)
        return  marshal(new_grandeza, grandeza_fields), 201