from flask_restful import fields, marshal_with, reqparse, Resource

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'id_module', dest='id_module',
    location='json', required=True,
    help='Identificador do módulo de um tipo de sensor.',
)
post_parser.add_argument(
    'url_codigo_fonte', dest='url_source',
    location='json', required=True,
    help='Descrição do Módulo',
)
modules_fields = {
    'id_module': fields.String,
    'url_source': fields.String,
    'description': fields.String
}

class ModulesAPI(Resource):
    def __init__(self, **kwargs):
        # smart_engine is a black box dependency
        self.estacao = kwargs['estacao']
        
    def get(self, id_module):
        return {
        "modules": [
            {
            "id_module": "mDHT",
            "description": "Módulo para sensor DHT11",
            "url_codigo_fonte": "http://example.com/DHT.py"
            }
        ]
        }
    @marshal_with(modules_fields, envelope='modules')
    def post(self):
        args = post_parser.parse_args()
        module =  1
        print(module)
        return  module,201
