from flask import Flask, Request
from flask_restful import Resource, Api
from resources.modules_resource import ModulesAPI
from resources.sensors_resource import SensorsAPI
from resources.grandezas_resource import GrandezasAPI
from resources.limiares_resource import LimiaresAPI
from resources.medidas_resource import MedidasAPI
from settings import PREFIX_API_VERSION, API_DEBUG
from principal.controller import AppController

app = Flask(__name__)
app.config.from_pyfile('../settings.py')
api = Api(app, prefix=PREFIX_API_VERSION)

# Instância do AppController responsável pelas operações da estação (Rasp)
estacao = AppController()

api.add_resource(ModulesAPI, '/modules', '/modules/<string:id_module>',
                                resource_class_kwargs={'estacao': estacao})

api.add_resource(GrandezasAPI, '/grandezas', '/grandezas/<string:type_grandeza>',
                                resource_class_kwargs={'estacao': estacao})
                        
api.add_resource(SensorsAPI, '/sensors', '/sensors/<string:id_sensor>',
                                resource_class_kwargs={'estacao': estacao})

api.add_resource(LimiaresAPI, '/sensors/<string:id_sensor>/limiares',
                                resource_class_kwargs={'estacao': estacao})

api.add_resource(MedidasAPI, '/sensors/<string:id_sensor>/medidas',
                                resource_class_kwargs={'estacao': estacao})

if __name__ == '__main__':
    with app.app_context():
        estacao.load_all()
    app.run(debug=API_DEBUG)