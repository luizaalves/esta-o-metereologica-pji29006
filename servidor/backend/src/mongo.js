const mongoose = require('mongoose');
const Notifica = require('./model/Notifica');

    mongoose.set('useFindAndModify', false);
    mongoose.connect('mongodb+srv://omnistack:omnistack@omnistack.q0cn4.mongodb.net/pji-backend?retryWrites=true&w=majority',{
        useNewUrlParser:true,
        useUnifiedTopology:true,
    });

    var notificacoes = await Notifica.find({id_sensor:json.id_sensor});
    notificacoes.sort(function compare(a, b) {
        var dateA = new Date(a.date);
        var dateB = new Date(b.date);
        return dateA - dateB;
    });
    if(notificacoes.length<20){
        const horas = new Date();
        await Notifica.create({
            id_sensor: json.id_sensor,
            type_grandeza: json.type_grandeza,
            unit: json.unit,
            value: json.value,
            hora:horas
        });
    }else{
        const filter = { hora: notificacoes[0].hora };
        const newNotify = Notifica;
        newNotify.id_sensor= json.id_sensor;
        newNotify.type_grandeza= json.type_grandeza;
        newNotify.unit= json.unit;
        newNotify.value= json.value;
        newNotify.hora=horas;
        await Sensor.findOneAndUpdate(filter, newNotify);
    }
    
    