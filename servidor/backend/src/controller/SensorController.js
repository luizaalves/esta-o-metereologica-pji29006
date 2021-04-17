const Sensor = require('../model/Sensor');
const Rabbit = require('../rpc_function');
var sensores= new Array();
const Notifica = require('../model/Notifica');
var correlationId = Math.random().toString() +
                            Math.random().toString() +
                            Math.random().toString();

function listarSensores(req,res){
    Rabbit.sendToQueue('GET','sensors','',
    async function getSensores(msg){
        var str = msg.content.toString();
        var json = JSON.parse(str);
        for(var i=0;i<json.sensores.length;i++){
            const filter = { id_sensor: json.sensores[i].id_sensor };
            await Sensor.findOne(filter,async function(err, sensor){
                if(sensor==null){
                    await Sensor.create({
                        id_sensor: json.sensores[i].id_sensor,
                        description: json.sensores[i].description,
                        type_grandeza: json.sensores[i].type_grandeza,
                        unit: json.sensores[i].unit,
                        id_module: json.sensores[i].id_module,
                        value_max: 0,
                        value_min: 0,
                    });
                }
            });
        }
        return res.json(json.sensores);
        }
    );
}

async function listarNotificações(req,res){
    var notificacoes = await Notifica.find();
    return res.json(notificacoes);
}

function limiaresSensor(req,res){
    var {id_sensor} = req.headers;
    Rabbit.sendToQueue('GET',`sensors/${id_sensor}/limiares`,'',
    async function getLimiares(msg){
        var str = msg.content.toString();
        var json = JSON.parse(str);
        const filter = { id_sensor: id_sensor };
        const update = { value_max: Number(json.value_max),
            value_min: Number(json.value_min) };
        await Sensor.findOneAndUpdate(filter, update);
        return res.json(json);
    });
}
function update(req,res){
    var {id_sensor} = req.headers;
    Rabbit.sendToQueue('PUT',`sensors/${id_sensor}/limiares`,JSON.stringify(req.body),
    async function putLimiares(msg){
        const filter = { id_sensor: id_sensor };
        await Sensor.findOneAndUpdate(filter, req.body);
    });
}

module.exports = {
    listarSensores,
    limiaresSensor,
    update,
    listarNotificações
}