from flask import Flask, Request
from flask_restful import Resource, Api
from resources.modules_resource import ModulesAPI
from resources.sensors_resource import SensorsAPI
from settings import PREFIX_API_VERSION
from principal.controller import AppController

app = Flask(__name__)
app.config.from_pyfile('../settings.py')
api = Api(app, prefix=PREFIX_API_VERSION)

@app.before_first_request
def create_tables():
    db.create_all()

# Instância do AppController responsável pelas operações da estação (Rasp)
estacao = AppController()

api.add_resource(ModulesAPI, '/modules', '/modules/<string:id_module>',
                                resource_class_kwargs={'estacao': estacao})
                        
api.add_resource(SensorsAPI, '/sensors', '/sensors/<string:id_sensor>',
                                resource_class_kwargs={'estacao': estacao})

if __name__ == '__main__':
    from principal.db import db 
    db.init_app(app)
    with app.app_context():
        estacao.load_all()
    app.run(debug=True)