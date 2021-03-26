from models.entities import Grandeza
from principal.dictionary import Unidade
from flask_restful import fields, marshal_with, marshal
import json

# Classe responsável por representar uma Medida
class Medida:
    def __init__(self, valor: float, grandeza: Grandeza):
        self.value = valor 
        self.unit = grandeza.unit
        self.type_grandeza = grandeza.type_grandeza
               

    def __repr__(self):
        return 'Medida("%s","%s","%s")' % (self.type_grandeza, self.value, self.unit)

# Classe responsável por representar uma Notificação
class Notification:
    notification_fields = {
        'id_sensor': fields.String,
        'type_grandeza': fields.String,
        'value': fields.Float,
        'unit': fields.String(x.name for x in Unidade)
    }

    def __init__(self, id_sensor: str, medida: Medida):
        self.id_sensor = id_sensor
        self.value = medida.value 
        self.unit = medida.unit
        self.type_grandeza = medida.type_grandeza
               

    def __repr__(self):
        return json.dumps(marshal(self, self.notification_fields))