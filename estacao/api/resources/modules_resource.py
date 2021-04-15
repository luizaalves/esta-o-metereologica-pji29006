from flask_restful import fields, marshal_with, marshal, reqparse, Resource
from models.entities import Module
from api.resources.errors import NotFoundError, BadRequestError, ConflictError, InternalServerError
import logging, logging.config
from settings import LOGGING_CONF

logging.config.fileConfig(fname=LOGGING_CONF)
logger = logging.getLogger(__name__)

post_parser = reqparse.RequestParser()

post_parser.add_argument('id_module', dest='id_module', location='json', required=True,
    help='Identificador do módulo é obrigatório - {error_msg}',
)
post_parser.add_argument('grandezas_medidas', dest='grandezas_medidas', location='json',
    help='Grandezas medidas pelo módulo - {error_msg}',
)
post_parser.add_argument('description', dest='description', location='json',
    help='Descrição do módulo - {error_msg}',
)


modules_fields = {
    'id_module': fields.String,
    'grandezas_medidas': fields.String,
    'description': fields.String
}
error_fields = {
    'code': fields.Integer,
    'message': fields.String,
    'description': fields.String
}
conflit_description = "Módulo com mesmo id_module já cadastrado"
notfound_description = "id_module não encontrado ou inválido"
internalserver_description = "Erro ao validar módulo. Consulte Logs do Sistema"

class ModulesAPI(Resource):
    def __init__(self, **kwargs):

        self.estacao = kwargs['estacao']

    def get(self, id_module=None):
        if id_module is None:
            modules = list(self.estacao.modules.values())
            return  marshal(modules, modules_fields, 'modules'), 200
        
        # se receber o parâmetro id_module na URL
        module = self.estacao.modules.get(id_module.lower(), None)
        if module is None:
            error = NotFoundError(notfound_description)
            return marshal(error, error_fields, 'error'), 404
        
        return marshal(module, modules_fields), 200           

    def post(self):
        args = post_parser.parse_args()

        new_module =  Module(args.id_module, args.url_codigo_fonte, args.description)
        result = self.estacao.add_module(new_module)
        if result == 2:
            logger.warn("Erro ao inserir Modulo, id_module %s já existe" % new_module.id_module)
            error = ConflictError(conflit_description)
            return marshal(error, error_fields, 'error'), 409
        elif result == 3:
            logger.error("Erro ao instanciar Módulo")
            error = InternalServerError(internalserver_description)
            return marshal(error, error_fields, 'error'), 500
        return  marshal(new_module, modules_fields), 201

    def put(self):
        args = post_parser.parse_args()

        change_module =  Module(args.id_module, args.url_codigo_fonte, args.description)
        if not self.estacao.change_module(change_module):
            error = NotFoundError(notfound_description)
            return marshal(error, error_fields, 'error'), 404
        return  None , 204