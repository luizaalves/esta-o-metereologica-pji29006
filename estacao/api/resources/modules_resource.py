from flask_restful import fields, marshal_with, marshal, reqparse, Resource
from models.module import Module
from api.resources.errors import NotFoundError, BadRequestError, ConflictError, InternalServerError

post_parser = reqparse.RequestParser()
        
post_parser.add_argument('id_module', dest='id_module', location='json', required=True,
    help='Identificador do módulo é obrigatório - {error_msg}',
)
post_parser.add_argument('url_codigo_fonte', dest='url_codigo_fonte', location='json', required=True,
    help='Campo url_codigo_fonte obrigatório - {error_msg}',
)
post_parser.add_argument('description', dest='description', location='json',
    help='Descrição do módulo - {error_msg}',
)

modules_fields = {
    'id_module': fields.String,
    'url_codigo_fonte': fields.String,
    'description': fields.String
}
error_fields = {
    'code': fields.Integer,
    'message': fields.String,
    'description': fields.String
}
conflit_description = "Módulo com mesmo id_module já cadastrado"
notfound_description = "id_module não encontrado ou inválido"

class ModulesAPI(Resource):
    def __init__(self, **kwargs):

        self.estacao = kwargs['estacao']

    def get(self, id_module=None):
        if id_module is None:
            modules = list(self.estacao.modules.values())
            return  marshal(modules, modules_fields, 'modules'), 200
        
        # se receber o parâmetro id_module na URL
        module = self.estacao.modules.get(id_module, None)
        if module is None:
            error = NotFoundError(notfound_description)
            return marshal(error, error_fields, 'error'), 404
        
        return marshal(module, modules_fields), 200           

    def post(self):
        args = post_parser.parse_args()
        id_module = args.id_module

        if id_module in self.estacao.modules:
            error = ConflictError(conflit_description)
            return marshal(error, error_fields, 'error'), 409
        
        new_module =  Module(args.id_module, args.url_codigo_fonte)
        self.estacao.modules[id_module] = new_module
        #module.save_db()
        return  marshal(new_module, modules_fields), 201