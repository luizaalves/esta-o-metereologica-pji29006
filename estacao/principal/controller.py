from models.sensor import Sensor
from models.limiar import Limiar
from models.module import Module
from models.grandeza import Grandeza
from principal.db import db
from principal.utils import Medida
from principal.dictionary import Unidade
import logging, logging.config

logging.config.fileConfig(fname='logging.conf')
logger = logging.getLogger(__name__)

class AppController:
    def __init__(self, read_interval=1, backup=True):

        self.read_interval = read_interval
        self.backup = backup
        self.limiares = {}
        self.sensores = {}
        self.modules = {}
        self.grandezas = {}

    def add_module(self, new_module: Module) -> bool:
        id_new_module = new_module.id_module.lower()
        if id_new_module in self.modules:
            return False
        self.modules[id_new_module] = new_module
        #TODO - Inserir lógica para adicionar script python referente ao módulo
        
        if self.backup:
            logger.info('Salvando novo Módulo (id_module=%s) no banco' % id_new_module)
            new_module.save_db()
        return True

    def change_module(self, change_module: Module) -> bool:
        id_change_module = change_module.id_module.lower()
        if not id_change_module in self.modules:
            logger.warn('id_module %s não existe' % id_change_module)
            return False
        self.modules[id_change_module] = change_module
        #TODO - Inserir lógica para alterar script python referente ao módulo
        if self.backup:
            logger.info('Salvando Alteração do Módulo (id_module=%s) no banco' % id_change_module)
            change_module.update_db()
        return True

    def add_grandeza(self, new_type: str, new_unit: str) -> int:
        unit_new_grandeza = Unidade.has_key(new_unit)
        if unit_new_grandeza is None:
            return 3
        if unit_new_grandeza.name in self.grandezas:
            return 2
        new_grandeza = Grandeza(new_type, str(unit_new_grandeza.name))
        self.grandezas[unit_new_grandeza.name] = new_grandeza
        if self.backup:
            logger.info('Gravando nova Grandeza no banco')
            new_grandeza.save_db()
        return 1

    def add_sensor(self, new_sensor: Sensor) -> int:
        new_unit_str = new_sensor.unit.lower()
        new_type_grandeza = new_sensor.type_grandeza.lower()
        unit = self.grandezas.get(new_unit_str)
        if (unit is None) or (new_type_grandeza != unit.type_grandeza.lower()):
            return 4
        new_module = new_sensor.id_module.lower()
        if not new_module in self.modules:
            return 3
        new_id_sensor = new_sensor.id_sensor.lower()
        if new_id_sensor in self.sensores:
            return 2
        self.sensores[new_id_sensor] = new_sensor
        if self.backup:
            logger.info('Gravando novo Sensor no banco')
            #new_sensor.save_db()
        return 1
    
    def change_sensor(self, new_sensor: Sensor) -> int:
        return 0

    def config_limiar(self, limiares: str, id_sensor: str) -> bool:
        return False

    def read_one(self, id_sensor: str) -> str:
        return None

    def read_all(self) -> list:
        return None

    def notify(self, id_sensor: str):
        pass

    def get_sensor(self, id_sensor) -> str:
        return None
    
    def load_all(self):
        logger.info('Carregando informações em memória')
        self.__load_modules()
        self.__load_grandezas()
            
    def __load_modules(self):
        logger.info('Carregando Modulos cadastrados')
        list_modules = Module.find_by_all()
        for module in list_modules:
            self.modules[module.id_module.lower()] = module
    
    def __load_grandezas(self):
        logger.info('Carregando Grandezas cadastradas')
        list_grandezas = Grandeza.find_by_all()
        for grandeza in list_grandezas:
            self.grandezas[grandeza.unit.lower()] = grandeza