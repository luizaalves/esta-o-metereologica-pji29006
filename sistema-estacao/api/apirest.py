from flask import request, Flask
from flask_restful import Api
from resources.modules import Modules

PREFIX_API_VERSION = '/api/v1'

app = Flask(__name__)
api = Api(app, prefix=PREFIX_API_VERSION)

api.add_resource(Modules, '/modules', '/modules/<string:id_module>')

if __name__ == '__main__':
    app.run(debug=True)