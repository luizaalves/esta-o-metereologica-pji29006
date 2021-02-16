from principal.db import db
from models.grandeza import Grandeza
from models.module import Module
from principal.dictionary import Unidade
from modulos.interfaces import IModule

class Sensor(db.Model):
    __tablename__ = 'Sensor'

    id_sensor = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.String)
    type_grandeza = db.Column(db.String, nullable=False)
    unit = db.Column(db.String,nullable=False)
    id_module = db.Column(db.String,nullable=False)

    def __init__(self, id_sensor: str, type_grandeza: str, unit: str, id_module: str, description = None):
        self.id_sensor = id_sensor
        self.type_grandeza = type_grandeza
        self.unit = unit
        self.id_module = id_module
        self.description = description
        self.module = IModule()
    
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    def update_db(self):
        db.session.flush(self)
        db.session.commit()
    
    @classmethod
    def find_by_all(cls):
        return cls.query.all()

    def __repr__(self):
        return 'Sensor("%s","%s","%s","%s","%s")' % (self.id_sensor, self.type_grandeza,
                                                 self.unit, self.description, self.id_module)