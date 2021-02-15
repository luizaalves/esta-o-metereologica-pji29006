from models.sensor import Sensor
from models.limiar import Limiar
from models.module import Module
from models.grandeza import Grandeza
from principal.db import db
from principal.utils import Medida
from principal.dictionary import Unidade
import logging

class AppController:
    def __init__(self, read_interval=1, backup=True):

        self.read_interval = read_interval
        self.backup = backup
        self.limiares = {}
        self.sensores = {}
        self.modules = {}
        self.grandezas = {}

    def add_module(self, new_module: Module) -> bool:
        id_new_module = new_module.id_module
        if id_new_module in self.modules:
            return False
        self.modules[id_new_module] = new_module
        #TODO - Inserir lógica para adicionar script python referente ao módulo
        
        if self.backup:
            logging.info('Salvando novo Módulo no banco')
            new_module.save_db()
        return True

    def change_module(self, change_module: Module) -> bool:
        id_change_module = change_module.id_module
        if not id_change_module in self.modules:
            logging.warn('id_module %s não existe' % id_change_module)
            return False
        self.modules[id_change_module] = change_module
        #TODO - Inserir lógica para alterar script python referente ao módulo
        if self.backup:
            logging.info('Salvando Alteração do Módulo no banco')
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
            logging.info('Salvando nova Grandeza no banco')
            new_grandeza.save_db()
        return 1

    def add_sensor(self, new_sensor: Sensor) -> int:
        return 0
    
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
        logging.info('Carregando em memória')
        self.__load_modules()
        self.__load_grandezas()
            
    def __load_modules(self):
        logging.info('Carregando Modulos')
        list_modules = Module.find_by_all()
        for module in list_modules:
            self.modules[module.id_module] = module
    
    def __load_grandezas(self):
        logging.info('Carregando Grandezas')
        list_grandezas = Grandeza.find_by_all()
        for grandeza in list_grandezas:
            self.grandezas[grandeza.unit] = grandeza