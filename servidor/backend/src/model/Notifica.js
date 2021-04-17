const mongoose = require('mongoose');

const NotificaSchema = new mongoose.Schema({
    id_sensor: String,
    type_grandeza: String,
    unit: String,
    value: Number,
    hora:String
});
 
// exportar o modulo daqui de dentro
module.exports = mongoose.model('Notifica', NotificaSchema);