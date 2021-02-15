from models.sensor import Sensor
from models.limiar import Limiar
from models.module import Module
from models.grandeza import Grandeza
from principal.db import db
from principal.utils import Medida
from flask import current_app as app

class AppController:
    def __init__(self, read_interval=1, backup=True):

        self.read_interval = read_interval
        self.backup = backup
        self.limiares = {}
        self.sensores = {}
        self.modules = {}
        self.gradezas = {}

    def add_module(self, new_module: Module) -> bool:
        id_new_module = new_module.id_module
        if id_new_module in self.modules:
            return False
        self.modules[id_new_module] = new_module
        #TODO - Inserir lógica para adicionar script python referente ao módulo
        
        if self.backup:
            app.logger.info('Salvando novo Módulo no banco')
            new_module.save_db()
        return True

    def change_module(self, change_module: Module) -> bool:
        id_change_module = change_module.id_module
        if not id_change_module in self.modules:
            app.logger.warn('id_module %s não existe' % id_change_module)
            return False
        self.modules[id_change_module] = change_module
        #TODO - Inserir lógica para alterar script python referente ao módulo
        if self.backup:
            app.logger.info('Salvando Alteração do Módulo no banco')
            change_module.update_db()
        return True

    def add_sensor(self, sensor: Sensor) -> bool:
        return False
    
    def config_limiar(self, limiares: str, id_sensor: str) -> bool:
        return False

    def read_one(self, id_sensor: str) -> str:
        return None

    def read_all(self) -> list:
        return None

    def notify(self, id_sensor: str):
        pass

    def _read_db(self):
        pass

    def _write_db(self):
        pass

    def get_sensor(self, id_sensor) -> str:
        return None
    
    def load_all(self):
        app.logger.info('Carregando em memória')
        self.__load_modules()
            
    def __load_modules(self):
        app.logger.info('Carregando Modulos')
        list_modules = Module.find_by_all()
        for module in list_modules:
            self.modules[module.id_module] = module