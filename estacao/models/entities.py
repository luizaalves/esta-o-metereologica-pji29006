from modules.interfaces import IModule
from modules.drivers import ModulesAvailable
from principal.db import session
from sqlalchemy import Column, Integer, String, Float, event
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Module(Base):
    __tablename__ = 'Module'

    id_module = Column(String, primary_key=True, unique=True, nullable=False)
    description = Column(String)
    grandezas_medidas = Column(String)

    def __init__(self, id_module: str, grandezas_medidas: str, description=None):
        self.id_module = id_module
        self.description = description
        self.grandezas_medidas = grandezas_medidas
        self.driver = IModule()                     # Instância do driver para o Módulo
    
    def save_db(self):
        session.add(self)
        session.commit()

    def update_db(self, change_module):
        session.merge(change_module)
        session.commit()
    
    @classmethod
    def find_by_id(cls, id_module):
        return session.query(cls).filter_by(id_module=id_module).first()
    
    @classmethod
    def find_by_all(cls):
        return session.query(cls).all()

    def __repr__(self):
        return 'Module("%s","%s","%s")' % (self.id_module, self.description, self.url_codigo_fonte)

class Grandeza(Base):
    __tablename__ = 'Grandeza'

    type_grandeza = Column(String, primary_key=True, nullable=False)
    unit = Column(String,primary_key=True, unique=True, nullable=False)

    def __init__(self, type_grandeza: str, unit: str):

        self.type_grandeza = type_grandeza
        self.unit = unit

    def save_db(self):
        session.add(self)
        session.commit()

    def update_db(self):
        session.flush(self)
        session.commit()

    @classmethod
    def find_by_all(cls):
        return session.query(cls).all()

    def __repr__(self):
        return 'Grandeza("%s","%s")' % (self.type_grandeza, self.unit)

class Sensor(Base):
    __tablename__ = 'Sensor'

    id_sensor = Column(String, primary_key=True, unique=True, nullable=False)
    description = Column(String)
    type_grandeza = Column(String, nullable=False)
    unit = Column(String,nullable=False)
    id_module = Column(String,nullable=False)

    def __init__(self, id_sensor: str, type_grandeza: str, unit: str, id_module: str, description = None):
        self.id_sensor = id_sensor
        self.type_grandeza = type_grandeza
        self.unit = unit
        self.id_module = id_module
        self.description = description
        self.module_driver = IModule()
    
    def save_db(self):
        session.add(self)
        session.commit()


    def update_db(self, change_sensor):
        session.merge(change_sensor)
        session.commit()
    
    @classmethod
    def find_by_id(cls, id_sensor):
        return session.query(cls).filter_by(id_sensor=id_sensor).first()

    @classmethod
    def find_by_all(cls):
        return session.query(cls).all()

    def __repr__(self):
        return 'Sensor("%s","%s","%s","%s","%s")' % (self.id_sensor, self.type_grandeza,
                                                 self.unit, self.description, self.id_module)

class Limiar(Base):
    __tablename__ = 'Limiar'

    id_sensor = Column(String, primary_key=True, nullable=False)
    value_min = Column(Float, nullable=False)
    value_max = Column(Float, nullable=False)

    def __init__(self, id_sensor: str, value_min=0.0, value_max=100.0):
        self.id_sensor = id_sensor
        self.value_min = value_min
        self.value_max = value_max

    def save_db(self):
        session.add(self)
        session.commit()

    def update_db(self, change_limiar):
        session.merge(change_limiar)
        session.commit()
        session.close()
    
    @classmethod
    def find_by_id(cls, id_sensor):
        return session.query(cls).filter_by(id_sensor=id_sensor).first()

    @classmethod
    def find_by_all(cls):
        return session.query(cls).all()

    def __repr__(self):
        return 'Limiar("%s","%s","%s")' % (self.id_sensor,self.value_min, self.value_max)

def add_availables_modules():
    bmp280 = Module(id_module='BMP280', grandezas_medidas='temperatura, pressure, altitude', description='Módulo para BMP280')
    bmp280.driver = ModulesAvailable.get_instance('BMP280')
    session.add(bmp280)
    session.commit()

def add_availables_grandezas():
    temperatura_celsius = Grandeza('temperatura', 'celsius')
    pressure_hpa = Grandeza('pressure', 'hpa')
    altitude_metro = Grandeza('altitude', 'metro')
    session.add(temperatura_celsius)
    session.add(pressure_hpa)
    session.add(altitude_metro)
    session.commit()

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import SQLALCHEMY_DATABASE_URI as DB_URI
    engine = create_engine(DB_URI,connect_args={'check_same_thread':False})
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    add_availables_modules()
    add_availables_grandezas()

