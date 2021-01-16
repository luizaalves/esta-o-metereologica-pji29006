from flask import Flask, Request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from resources.modules import ModulesAPI
from resources.sensores import SensorsAPI
from estacao.controller import AppController
from settings import PREFIX_API_VERSION

app = Flask(__name__)
app.config.from_pyfile('../settings.py')
db = SQLAlchemy(app)
api = Api(app, prefix=PREFIX_API_VERSION)

# Instância do AppController responsável pelas operações da estação (Rasp)
estacao = AppController()

api.add_resource(ModulesAPI, '/modules', '/modules/<string:id_module>', 
                        resource_class_kwargs={'estacao': estacao})
api.add_resource(SensorsAPI, '/sensors', '/sensors/<string:id_sensor>', 
                        resource_class_kwargs={'estacao': estacao})

if __name__ == '__main__':
    app.run(debug=True)