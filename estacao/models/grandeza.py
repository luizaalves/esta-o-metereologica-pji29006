from principal.db import db
from principal.dictionary import Unidade

class Grandeza(db.Model):
    __tablename__ = 'Grandeza'

    type_grandeza = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    unit = db.Column(db.String,nullable=False)

    def __init__(self, type_grandeza: str, unit: Unidade):
        self.type_grandeza = type_grandeza
        self.unit = unit