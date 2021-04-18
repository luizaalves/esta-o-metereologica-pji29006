const mongoose = require('mongoose');

const SensorSchema = new mongoose.Schema({
    id_sensor: String,
    description: String,
    type_grandeza: String,
    unit: String,
    id_module: String,
    value_max: Number,
    value_min: Number
});
 
// exportar o modulo daqui de dentro
module.exports = mongoose.model('Sensor', SensorSchema);