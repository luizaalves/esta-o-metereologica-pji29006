from principal.db import db

class Limiar(db.Model):
    __tablename__ = 'Limiar'

    id_sensor = db.Column(db.String, primary_key=True, nullable=False)
    value_min = db.Column(db.Float, nullable=False)
    value_max = db.Column(db.Float, nullable=False)

    def __init__(self, id_sensor: str, value_min=0.0, value_max=100.0):
        self.id_sensor = id_sensor
        self.value_min = value_min
        self.value_max = value_max

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
        return 'Limiar("%s","%s","%s")' % (self.id_sensor,self.value_min, self.value_max)