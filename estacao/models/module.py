from principal.db import db

class Module(db.Model):
    __tablename__ = 'Module'

    id_module = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.String)
    url_codigo_fonte = db.Column(db.String)

    def __init__(self, id_module: str, url_codigo_fonte: str, description=None):
        self.id_module = id_module
        self.description = description
        self.url_codigo_fonte = url_codigo_fonte

    def save_db(self):
        db.session.add(self)
        db.session.commit()

    def update_db(self):
        db.session.flush(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, id_module: str):
        return cls.query.filter_by(id_module=id_module).first()

    @classmethod
    def find_by_all(cls):
        return cls.query.all()

    def __repr__(self):
        return 'Module("%s","%s","%s")' % (self.id_module, self.description, self.url_codigo_fonte)