from principal.db import db
from principal.dictionary import Unidade

class Grandeza(db.Model):
    __tablename__ = 'Grandeza'

    type_grandeza = db.Column(db.String, primary_key=True, nullable=False)
    unit = db.Column(db.String,primary_key=True, unique=True, nullable=False)

    def __init__(self, type_grandeza: str, unit: str):

        self.type_grandeza = type_grandeza
        self.unit = unit

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
        return 'Grandeza("%s","%s")' % (self.type_grandeza, self.unit)