from principal.db import db
from models.grandeza import Grandeza
from principal.dictionary import Unidade

class Sensor(db.Model):
    __tablename__ = 'Sensor'

    id_sensor = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.String)
    type_grandeza = db.Column(db.String, db.ForeignKey('Grandeza.type_grandeza'), nullable=False)
    Grandeza = db.relationship("Grandeza", backref="Sensor")
    id_module = db.Column(db.String, db.ForeignKey('Module.id_module'), nullable=False)
    Module = db.relationship("Module", backref="Sensor")

    def __init__(self, id_sensor: str, type_grandeza: Grandeza, id_module: str):
        self.id_sensor = id_sensor
        self.type_grandeza = type_grandeza
        self.id_module = id_module