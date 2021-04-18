//importar uma dependencia externa;
const express = require('express');


var id_sensor=0;
var sensores=[];
const SensorModel = require('./model/Sensor');
const SensorController = require('./controller/SensorController');
const routes = express.Router();

routes.get('/sensores',SensorController.listarSensores);
routes.get(`/notificacoes`,SensorController.listarNotificações);
routes.put(`/limiares`,SensorController.update);
routes.get('/sensor',SensorController.limiaresSensor)

//exportando as rotas daqui de dentro
module.exports = routes;
 