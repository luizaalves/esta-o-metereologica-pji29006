from models.entities import Sensor, Limiar, Module, Grandeza
from principal.db import session
from principal.utils import Medida
from modules.drivers import ModulesAvailable
from principal.dictionary import Unidade
from services.notification import NotificationService
from services.messages import MessageService
import logging, logging.config
from settings import SERVICE_NOTIFICATION as NOTIFICATION_START
from settings import SERVICE_MESSAGE as MESSAGE_START
from settings import INTERVAL
from pika.exceptions import AMQPConnectionError, AMQPChannelError

logging.config.fileConfig(fname='logging.ini')
logger = logging.getLogger(__name__)

class AppController:
    def __init__(self, read_interval=INTERVAL, backup=True):

        self.read_interval = read_interval
        self.backup = backup
        self.limiares = {}
        self.sensores = {}
        self.modules = {}
        self.grandezas = {}

        self.load_all() 
        self.notification_service = None
        self.__start_services()
              
    def add_module(self, new_module: Module) -> int:
        id_new_module = new_module.id_module.lower()
        if id_new_module in self.modules:
            return 2
        new_module.id_module = id_new_module
        try:
            new_module.driver = ModulesAvailable.get_instance(id_new_module)
        except Exception as e:
            logger.error(e)
            logger.error('O Módulo %s não está implementado ou nome da classe está incorreto' % id_new_module)
            return 3

        self.modules[id_new_module] = new_module
        #TODO - Inserir lógica para fazer download do script python referente ao módulo
        if self.backup:
            logger.info('Salvando novo Módulo (id_module=%s) no banco' % id_new_module)
            new_module.save_db()
        logger.info('Adicionando novo Módulo (id_module=%s) na Estação' % id_new_module)
        return 1

    def change_module(self, change_module: Module) -> bool:
        id_change_module = change_module.id_module.lower()
        if not id_change_module in self.modules:
            logger.debug('id_module %s não existe' % id_change_module)
            return False
        change_module.id_module = id_change_module
        self.modules[id_change_module] = change_module
        #TODO - Inserir lógica para alterar script python referente ao módulo
        if self.backup:
            logger.info('Salvando Alteração do Módulo (id_module=%s) no banco' % id_change_module)
            module = Module.find_by_id(id_change_module)
            module.update_db(change_module)
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
            #new_sensor.module = ModulesAvailable.get_instance(new_sensor.id_module)
            id_module = new_sensor.id_module.lower()
            module_driver = self.modules.get(id_module).driver
            logger.debug('Link module %s ao sensor' % (module_driver))
            new_sensor.module_driver = module_driver
            limiar = Limiar(id_sensor)
            new_sensor.id_sensor = id_sensor
            self.sensores[id_sensor] = new_sensor
            self.limiares[id_sensor] = limiar
            if self.backup:
                logger.debug('Gravando novo Sensor (id_sensor=%s) no banco' % (id_sensor))
                new_sensor.save_db()
                limiar.save_db()
            logger.info('Gravando novo Sensor (id_sensor=%s) na Estação' % (id_sensor))
            if (len(self.sensores) == 1) and self.notification_service:
                self.notification.start()
            return result_verify
        return result_verify
    
    def change_sensor(self, change_sensor: Sensor) -> int:
        result_verify = self.__verify_sensor(change_sensor)
        if result_verify != 2:
            return result_verify
        id_change_sensor = change_sensor.id_sensor.lower()
        change_sensor.module_driver = self.modules.get(change_sensor.id_module).driver
        change_sensor.id_sensor = id_change_sensor
        self.sensores[id_change_sensor] = change_sensor
        if self.backup:
            logger.info('Salvando Alteração do Sensor (id_sensor=%s) no banco' % id_change_sensor)
            sensor = Sensor.find_by_id(id_change_sensor)
            sensor.update_db(change_sensor)
        return result_verify

    def config_limiar(self, limiar_change: Limiar) -> int:
        id_sensor = limiar_change.id_sensor.lower()
        if not id_sensor in self.sensores:
            return 2
        limiar_change.id_sensor = id_sensor
        self.limiares[id_sensor] = limiar_change
        if self.backup:
            limiar = Limiar.find_by_id(id_sensor)
            if limiar:
                logger.info('Salvando Alteração de Limiar do Sensor (id_sensor=%s) no banco' % id_sensor)
                limiar.update_db(limiar_change)
        return 1

    def read_one(self, id_sensor: str) -> Medida:
        sensor = self.sensores.get(id_sensor.lower())
        logger.debug('Lendo Sensor %s' % id_sensor)
        value_read = sensor.module_driver.read()
        logger.debug('Valor %d lido para sensor %s' % (value_read,id_sensor))
        grandeza = self.grandezas.get(sensor.unit.lower())
        logger.debug('grandeza do sensor %s' % (grandeza))
        medida = Medida(value_read, grandeza)
        logger.debug('Medida do sensor %s' % (medida))
        return medida

    def read_all(self) -> dict:
        medidas = {}
        for sensor in self.sensores.values():
            sensor_id = sensor.id_sensor.lower()
            medidas[sensor_id] = self.read_one(sensor_id)
        return medidas
    
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
            module.driver = ModulesAvailable.get_instance(module.id_module)
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
            sensor.module_driver = self.modules.get(sensor.id_module).driver
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
    
    def __start_services(self):
        if MESSAGE_START:
            try:
                logger.info("Criando Serviço de Mensagens")
                self.message_service = MessageService()
            except AMQPConnectionError:
                logger.error("Não foi possível criar o Serviço de Mensagens para requisições! Verifique configurações e reinicie o Serviço!")
            else:
                self.message_service.start()

        if NOTIFICATION_START:
            try:
                self.notification_service = NotificationService(self.read_interval, self)
            except AMQPConnectionError:
                logger.error("Erro ao iniciar Broker Channel. Verifique configurações e reinicie o serviço!")
            else:
                if self.sensores and NOTIFICATION_START:
                    self.notification_service.start()