#!/usr/bin/env node

var amqp = require('amqplib/callback_api');
const RABBITMQ = 'amqp://admin:pji29006@us127.serverdo.in:5672';
const Notifica = require('./model/Notifica');
const mongoose = require('mongoose');

mongoose.set('useFindAndModify', false);
mongoose.connect('mongodb+srv://omnistack:omnistack@omnistack.q0cn4.mongodb.net/pji-backend?retryWrites=true&w=majority',{
    useNewUrlParser:true,
    useUnifiedTopology:true,
});

    amqp.connect(RABBITMQ,  function(err, conn){ conn.createChannel( function(err, channel){
        var exchange = 'notifications';

        channel.assertQueue('', {exclusive: true}, 
            function(error2, q) {
                console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", q.queue);
                    channel.bindQueue(q.queue, exchange, '');
                    channel.consume(q.queue,async function(msg) {
                        if(msg.content) {
                            console.log(" [x] %s", msg.content.toString());
                            var str = msg.content.toString();
                            var json = JSON.parse(str);
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
                                    hora:horas.toString()
                                });
                            }else{
                                const newHora = new Date();
                                const filter = {horas: notificacoes[0].hora};
                                var newNotify = Notifica;
                                newNotify.id_sensor= json.id_sensor;
                                newNotify.type_grandeza= json.type_grandeza;
                                newNotify.unit= json.unit;
                                newNotify.value= json.value;
                                newNotify.hora=newHora.toString();
                                await Notifica.findOneAndReplace(filter,newNotify);
                            }
                        }
                    }, {
                        noAck: true
                    });
                
            });
        })
    });


    
