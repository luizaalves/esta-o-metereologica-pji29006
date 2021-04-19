## Configuração de hospedagem do Servidor WEB da E.M.

#### Arquitetura
O projeto é dividido em 2 blocos, *backend* e *frontend*. O *frontend* deve possuir conexão com o *backend* para que o sistema desenvolva o comportamento esperado. O **IP/URL:porta** em que o *backend* estará executando deverá ser informado no código do *frontend*, na arquivo ``` frontend/src/services/api.js ```. No caso de executar na porta 3333 da mesma máquina: http://localhost:3333.

A visualização gráfica do sistema ***(frontend)*** é montada e ilustrada pelo **React**, que por sua vez se comunica com o  ***(backend)*** que é estruturado pelo **Node**.

#### Backend

Assim que clonado o repositório para a máquina onde o projeto será executado, é necessário atualizar as referências do gerenciador de pacotes utilizado para desenvolver este projeto ``` yarn ```.

Para isso, é necessário acessar o diretório do *backend*, e executar o comando:

> ``` yarn ```

Para executar o *Backend*, devemos executar o arquivo "``` backend/server.js ```" utilizando o seguinte comando:

> ``` node backend/server.js ```


#### Frontend

Assim que como relizado com o diretório do *backend*, é necessário atualizar as referências do gerenciador de pacotes utilizado para desenvolver este projeto ``` yarn ```.

Para isso, é necessário acessar o diretório do *frontend*, e executar novamente o comando:

> ``` yarn ```

Para executar o *frontend* utilizamos o comando:

> ``` yarn start ```

Ele executa a aplicação na porta 3000 do localhost, que é possivel ter acessibilidade através de um navegador por ``` http://localhost:3000 ``` por exemplo.

Porém a forma mais correta de configurar para uma aplicação WEB real seria utilizar o comando:

> ``` yarn build ```

Esta ferramenta agrupa corretamente o React no modo de produção e otimiza a construção para melhorar o desempenho da exibição pois a compilação do arquivo é reduzida e os nomes dos arquivos incluem hashes.

Então, através do servidor WEB, configura-se a visualização dos arquivos estáticos. 

> **Para rodar o projeto em nuvem podemos utilizar um servidor WEB como Apache ou Nginx para controlar os acesso e estruturar os arquivos estáticos.**

Este projeto em sua originalidade esta configurado no diretório ``` /var/www/nomeDoProjeto ```, desta forma, para exibir o **arquivo estático** (``` index.html ```) que inicia a navegação pela interface WEB do projeto estará localizado em ``` /var/www/nomeDoProjeto/frontend/build ``` .


#### Message Broker

Estamos utilizando como Message Broker o RabbitMQ cujo protocolo de comunicação utilizado é o AMQP.

Esa estrutura permite fazer a comunicação de forma ASSÍNCRONA da aplicação em Nodejs com outras aplicações, no caso a Estação Metereológica.

A aplicação em Node encaminha as mensagens para a fila de mensagens do RabbitMQ, que pode ser consumida pela aplicação na outra ponta.

O RabbitMQ recebe e entrega mensagens, e armazena todas elas em fila, para garantir que haja entrega e que a mesma seja assíncrona entre as partes da aplicação.

Estados do RabbitMQ:

> **Produtor**: Quando está enviando mensagens é chamado de produtor.

As mensagens são armazenadas em uma fila dentro do RabbitMQ, o limite deste armazenamento é o disco do Host. Muitos produtores podem enviar mensagens que vão para uma fila e muitos consumidores podem tentar receber dados de uma fila.

> **Consumidor**: é um programa que fica esperando receber mensagens

***Consumidor e Produtor não precisam estar no mesmo Host**

É possivel se comunicar com o servidor RabbitMQ atarvés da porta 5672.

Para estabelecer conexão através de rede externa:

> ``` amqp://user:password@dominio/IP:5672 ```

Há um plugin instalado rodando na porta 15672, que permite visualização em tempo real da fila de mensagens em um navegador:

>  http://dominio/IP:15672

Para instalar o Mensage broker basta digitar os comandos:

> sudo apt-get install rabbitmq-server

Para criar usuário e senha:

> sudo rabbitmqctl add_user **```user```** **```password```**

Tornar usuário como administrador:

> sudo rabbitmqctl set_user_tags user administrator









