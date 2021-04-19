//importar uma dependencia externa;
const express = require('express');
const cors = require('cors');
const routes = require('./src/router');
const mongoose = require('mongoose');
const app = express();

mongoose.set('useFindAndModify', false);
mongoose.connect('mongodb+srv://omnistack:omnistack@omnistack.q0cn4.mongodb.net/pji-backend?retryWrites=true&w=majority',{
    useNewUrlParser:true,
    useUnifiedTopology:true,
});

//Alterei o CORS pra testar
//app.use(cors({}))    estava assim antes
app.use(cors()); //qualquer aplicação acesse a api ou origin:'http://localhost:3333'
//dizendo pro express que utiliza o formato json
app.use(express.json());
app.use(routes);
require('child_process').fork('./src/notifica.js');
//ouvindo no localhost na porta 3333
app.listen(3333);