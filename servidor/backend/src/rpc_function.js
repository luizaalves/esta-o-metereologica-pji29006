var amqp = require('amqplib/callback_api');
const RABBITMQ = 'amqp://admin:pji29006@us127.serverdo.in:5672';
var correlationId = Math.random().toString() +
                    Math.random().toString() +
                    Math.random().toString();

async function sendToQueue(method,pasta,data,callback){
  return amqp.connect(RABBITMQ,  function(err, conn){ conn.createChannel( function(err, channel){
    channel.assertQueue('', {exclusive: true}, 
      function(error2, q) {
        channel.sendToQueue('rpc_queue',
          Buffer.from(data),{
          headers: {Path:'/api/v1/'+pasta,Method:method},
          contentType: 'application/json',
          correlationId: correlationId,
          replyTo: q.queue }
        );
        channel.consume(q.queue,function(msg) {
          if (msg.properties.correlationId == correlationId) {
            var statusResponse = msg.properties.headers.Status
            console.log(statusResponse);
            if(statusResponse.toString()=='200'||statusResponse.toString()=='204'){
              callback(msg);
              conn.close();
            }
          }
          setTimeout(function() {
            conn.close();
          }, 500);
        }, { noAck: true });
      });
    })});
  }

  module.exports = {
    sendToQueue,
  }