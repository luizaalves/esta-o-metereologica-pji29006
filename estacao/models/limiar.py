from principal.db import db

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