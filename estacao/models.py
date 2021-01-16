from api.apirest import db
from estacao.dictionary import Unidade

class Module(db.Model):
    __tablename__ = 'Module'

    id_module = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.String)
    url_codigo_fonte = db.Column(db.String)

    def __init__(self, id_module: str, url_codigo_fonte: str):
        self.id_module = id_module
        self.source_code_url = url_codigo_fonte

class Grandeza(db.Model):
    __tablename__ = 'Grandeza'

    type_grandeza = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    unit = db.Column(db.String,nullable=False)

    def __init__(self, type_grandeza: str, unit: Unidade):
        self.type_grandeza = type_grandeza
        self.unit = unit

class Sensor(db.Model):
    __tablename__ = 'Sensor'

    id_sensor = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.String)
    type_grandeza = db.Column(db.String, db.ForeignKey('Grandeza.type_grandeza'), nullable=False)
    Grandeza = db.relationship("Grandeza", backref="Sensor")
    id_module = db.Column(db.String, db.ForeignKey('Module.id_module'), nullable=False)
    Module = db.relationship("Module", backref="Sensor")

    def __init__(self, id_sensor: str, type_grandeza: str, id_module: str):
        self.id_sensor = id_sensor
        self.type_grandeza = type_grandeza
        self.id_module = id_module

class Limiar(db.Model):
    __tablename__ = 'Limiar'

    id_sensor = db.Column(db.String, db.ForeignKey('Sensor.id_sensor'), primary_key=True, nullable=False)
    Sensor = db.relationship("Sensor", backref="Limiar")
    value_min = db.Column(db.Float, nullable=False)
    value_max = db.Column(db.Float, nullable=False)

    def __init__(self, id_sensor: str, value_min: float, value_max: float):
        self.id_sensor = id_sensor
        self.value_min = value_min
        self.value_max = value_max

if __name__ == "__main__":
    db.drop_all()
    db.create_all()