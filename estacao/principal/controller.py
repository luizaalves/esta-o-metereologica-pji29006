from models.sensor import Sensor
from models.limiar import Limiar
from models.module import Module
from models.grandeza import Grandeza
from principal.db import db
from principal.utils import Medida
from modulos.drivers import ModulesAvailable
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
        #TODO - Inserir lógica para fazer download do script python referente ao módulo
        if self.backup:
            logger.info('Salvando novo Módulo (id_module=%s) no banco' % id_new_module)
            new_module.save_db()
        logger.info('Adicionando novo Módulo (id_module=%s) na Estação' % id_new_module)
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
        logger.info('Adicionando nova Grandeza na Estação')
        if self.backup:
            logger.info('Gravando nova Grandeza no banco')
            new_grandeza.save_db()
        return 1

    def add_sensor(self, new_sensor: Sensor) -> int:
        result_verify = self.__verify_sensor(new_sensor)
        if result_verify == 1:
            id_sensor = new_sensor.id_sensor.lower()
            new_sensor.module = ModulesAvailable.get_instance(new_sensor.id_module)
            limiar = Limiar(id_sensor)
            self.config_limiar(limiar)
            if self.backup:
                logger.debug('Salvando Limiar padrão do Sensor (id_sensor=%s) no banco' % id_sensor)
                limiar.save_db()
            self.sensores[id_sensor] = new_sensor
            if self.backup:
                logger.info('Gravando novo Sensor (id_sensor=%s) no banco' % (id_sensor))
                new_sensor.save_db()
            logger.info('Gravando novo Sensor (id_sensor=%s) na Estação' % (id_sensor))
            return result_verify
        return result_verify
    
    def change_sensor(self, change_sensor: Sensor) -> int:
        result_verify = self.__verify_sensor(change_sensor)
        if result_verify != 2:
            return result_verify
        id_change_sensor = change_sensor.id_sensor.lower()
        change_sensor.module = ModulesAvailable.get_instance(change_sensor.id_module)
        self.sensores[id_change_sensor] = change_sensor
        if self.backup:
            logger.info('Salvando Alteração do Sensor (id_sensor=%s) no banco' % id_change_sensor)
            change_sensor.update_db()
        return result_verify

    def config_limiar(self, limiar: Limiar) -> int:
        id_sensor = limiar.id_sensor.lower()
        if not id_sensor in self.sensores:
            return 2
        self.limiares[id_sensor] = limiar
        if self.backup:
            logger.info('Salvando Alteração de Limiar do Sensor (id_sensor=%s) no banco' % id_sensor)
            limiar.update_db()
        return 1

    def read_one(self, id_sensor: str) -> Medida:
        sensor = self.sensores.get(id_sensor.lower())
        value_read = sensor.module.read()
        logger.debug('Valor %d lido para sensor %s' % (value_read,id_sensor))
        grandeza = self.grandezas.get(sensor.unit.lower())
        logger.debug('grandeza do sensor %s' % (grandeza))
        medida = Medida(value_read, grandeza)
        logger.debug('Medida do sensor %s' % (medida))
        return medida

    def read_all(self) -> list:
        return None

    def notify(self, id_sensor: str):
        pass
    
    def load_all(self):
        logger.info('Carregando informações em memória')
        self.__load_modules()
        self.__load_grandezas()
        self.__load_sensors()
        self.__load_limiares()
            
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
        
    def __load_sensors(self):
        logger.info('Carregando Sensores cadastradas')
        list_sensors = Sensor.find_by_all()
        for sensor in list_sensors:
            sensor.module = ModulesAvailable.get_instance(sensor.id_module)
            self.sensores[sensor.id_sensor] = sensor

    def __load_limiares(self):
        logger.info('Carregando Limiares configurados')
        list_limiares = Limiar.find_by_all()
        for limiar in list_limiares:
            self.limiares[limiar.id_sensor] = limiar
        
    def __verify_sensor(self, sensor: Sensor) -> int:
        logger.debug('Verificando informações do Sensor')
        unit_str = sensor.unit.lower()
        type_grandeza = sensor.type_grandeza.lower()
        unit = self.grandezas.get(unit_str)
        if (unit is None) or (type_grandeza != unit.type_grandeza.lower()):
            logger.debug('Não foi encontrado nenhuma unidade=%s ou tipo=%s' % (unit_str,type_grandeza))
            return 4
        id_module = sensor.id_module.lower()
        if not id_module in self.modules:
            logger.debug('Não foi encontrado modulo com id_module=%s' % (id_module))
            return 3
        id_sensor = sensor.id_sensor.lower()
        if id_sensor in self.sensores:
            logger.debug('Sensor com id_sensor=%s já está cadastrado' % (id_sensor))
            return 2
        return 1