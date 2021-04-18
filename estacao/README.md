## Sistema Estação Meteorológica

Este diretório contém o código-fonte do sistema estação meteorológica e alguns tutoriais para Instalação, Administração e Manutenção do Sistema numa Raspberry.

### Organização dos tutoriais

- [Implantação do Sistema](#implantação)
  - [Requisitos](#requisitos)
  - [Instalação](#instalação) 
  - [Atualização](#atualização)
  - [Teste](#teste)
  - [Logs e comandos](#logs-e-comandos)
- [Instalação de novos Módulos/Drivers para Sensores](#instalaçao-de-novos-módulos-para-sensores)
  - [Módulo de Exemplo - Stub](#módulo-stub)
- [Exemplos de Requisições](#exemplos-de-requisições)
  - [Adicionar Módulo na Estação](#adicionar-módulo-na-estação)
  - [Adicionar Grandeza na Estação](#adicionar-grandeza-na-estação)
  - [Adicionar Sensor na Estação](#adicionar-sensor-na-estação)
  - [Alterar Limiares de Sensor](#alterar-limiares-de-sensor)
- [Exemplos de Clients para Fila de Mensagens (RabbitMQ)](#exemplos-de-clients-rabbitmq)
  - [Client para Notificações(Consumer)](#client-para-notificações) 
  - [Client para Requesições (RPC)](#client-para-requisições) 
---
## Implantação
### Requisitos

* Placa Raspberry PI e acesso root.
* Git.
* Python 3.7.3 ou superior.
* virtualenv 15.1.0 ou superior.

### Instalação

1. Faça o download do repositório do projeto na versão mais atual e acesse o diretório.

   ```bash
   $ git clone -b estacao-v3.0.0 --single-branch https://github.com/PJI29006-classroom/2020-01-estacao-metereologica-estacao-alexandre-andre-e-luiza.git estacao-v3.0.0 
   
   $ cd ./estacao-v3.0.0
   ```


2. Execute o script para instalação do Sistema Estação.

	```bash
	$ sudo ./install-estacao.sh
	```

3. Acesse o diretório de implantação (`/estacao`).

	```bash
	$ cd /estacao
	```

4. Edite o arquivo `settings.py` alterando as informações referentes ao servidor de mensagens.

	```python
	## Ativação dos Serviços 
	# Mensagens para requisições(MESSAGE) ou Notificações(NOTIFICATION).
	# False se não deseja utilizar um dos (ou os dois) Serviços.
	SERVICE_MESSAGE = True
	SERVICE_NOTIFICATION = True

	## Configurar informações de conexão com o broker.
	RABBIT_SERVER = {
		'HOST' : 'IP ou FQDN do broker',
		'PORT' : Porta_do_broker,
		'USER' : 'User',
		'PASS' : 'Password'
	}

	## Configurar informações da Fila de Notificações
	# Exchange RabbitMQ para envio das notificações (Pub/Subs).
	EXCHANGE_NOTIFICATIONS='notifications'
	# Tipo de Exchange do servidor RabbitMQ (Publish/Subscribe).
	EXCHANGE_TYPE='fanout'
	# Routing Key do servidor - Default ''
	ROUTING_KEY_NOTIFICATIONS=''
	# Periodicidade (segundos) para serviço de notificação ler sensores.
	INTERVAL=5                               
	
	## Configurar informações da Fila de requisições
	# Nome da fila para requisições via RPC do RabbitMQ (RPC).
	QUEUE_MESSAGES='rpc_queue'
	# Exchange RabbitMQ para envio das requsições (RPC).
	EXCHANGE_MESSAGES=''
	```

	**Obs.:** Este projeto foi desenvolvido utilizando o broker de mensagens do [RabbitMQ](https://www.rabbitmq.com/), especificamente com as implementações de [RPC](https://www.rabbitmq.com/tutorials/tutorial-six-python.html) e [Publish/Subscribe](https://www.rabbitmq.com/tutorials/tutorial-three-python.html). Para outras implementações é necessário testar a compatibilidade e se preciso alterar o código.

5. Ainda no arquivo `settings.py`, configure o modulo/driver BMP280 (implementado por padrão). Caso não deseje utilizar, altere `USE_BMP280` para `False`.

	```python
	## Configurações do Modulo/driver BMP280 padrão

	# Verificar endereço da interface na Rasp - sudo i2cdetect -y 1
	# Se o comando acima não retornar nada é possível que a interface 
	# I2C na rasp não esteja habilitada.
	# Para habilitar execute - sudo raspi-config - 
	# e escolha as opções 5 e P5.
	# Algumas placas o endereço é 0x77
	I2C_ADDRESS = 0x76
	# Pressao nivel do mar em Florianopolis
	SEA_LEVEL_PRESSURE = 1020.00 
	# True para utilizar o módulo BMP280 implementado por padrão.
	USE_BMP280=True              
	```
6. Execute o script para iniciar o Sistema Estação

	```bash
	$ sudo ./start-estacao.sh
	```
### Atualização

Caso você já tenha executado a instalação de alguma versão anterior do sistema, execute os seguintes passos para atualização.

1. Faça o download do repositório do projeto na versão mais atual e acesse o diretório.

	```bash
	$ git clone -b estacao-v3.0.0 --single-branch https://github.com/PJI29006-classroom/2020-01-estacao-metereologica-estacao-alexandre-andre-e-luiza.git estacao-v3.0.0
	
	$ cd ./estacao-v3.0.0
	```

2. Execute o script para atualização do Sistema Estação.

	```bash
	$ sudo ./update-estacao.sh
	```

**Obs.:** O script de atualização cria um arquivo compactado com backup do diretório de implantação com o seguinte nome - `/estacao/backup-AAAA-MM-DD.tar.gz`.

### Teste

O Sistema Estação é administrado por meio de API REST conforme descrito na [documentação](https://estacao.docs.apiary.io/) e as requsições estarão disponíveis somente na rede local da Rasp. Segue um exemplo de requisição para verificar se a instalação foi bem sucedida.

**Obs.:** Substitua `localhost` pelo IP da Rasp se estiver executando em outro computador da rede local.

```bash
$ curl http://localhost:5000/api/v1/grandezas -H "Accept: application/json"
```

### Logs e comandos

O Sistema Estação instalado seguindo as instruções deste documento é executado como um serviço do Systemd. Seguem alguns comandos que podem ser úteis para administração do serviço.

1. Verificar logs do serviço:

	```bash
	$ sudo journalctl -f -u estacao
	```

2. Parar, reiniciar ou iniciar o serviço.

	```bash
	$ sudo systemctl [stop|restart|start] estacao
	```
---

## Instalaçao de novos Módulos para Sensores

Para instalar um novo Módulo/Driver no Sistema é preciso desenvolver uma classe que implemente a interface `IModule` disponível em `/estacao/modules/interface.py`. A classe deve ser escrita num arquivo python e adicionada no diretório `/estacao/modules`. Depois é preciso editar o arquivo `/estacao/modules/drivers.py` para incluir linha de importação do novo Módulo. A seguir é descrito um exemplo de instalação de um Módulo.

### Módulo Stub

Execute os seguintes passos para instalação do Módulo chamado `Stub`.

1. Pare o serviço estação executanto o comando:

	```bash
	$ sudo systemctl stop estacao
	```

2. Efetue a instalação física do Módulo/Sensor na Raspberry.

3. Acesse o diretório de módulos do sistema estação e copie o arquivo de Exemplo de módulo, renomeando para o nome do novo módulo.

	```bash
	$ cd /estacao/modules
	$ sudo cp example.py stub.py
	```
	
4. Edite o arquivo efetuando a alteração do nome da classe e implementando os dois métodos (`read()` e `start()`) necessários para funcionamento.
    - O Método `read()` recebe como argumento uma string com o nome da grandeza que será lida. Essa grandeza é configurada via API na hora de adicionar o Sensor na estação. Alguns módulos podem efetuar a leitura de mais de uma grandeza (e.g., BMP280) e para isso é necessário que o método `read()` esteja preparado para retornar isso de acordo com o informado via argumento.
    - O Método `start()` é executado logo após o Módulo ser adicionado, via API, na estação. Nesse método deve ser adicionado qualquer configuração necessária para funcionamento do Módulo Físico instalado na Raspberry, como porta GPIO utilizada ou configurações de Interface I2C, SPI, etc.

    **Obs.:** Edite o arquivo `/estacao/modules/bmp280.py` e verifique como foi implementado o módulo BMP280 usando a biblioteca `adafruit-circuitpython-bmp280`.

	Segue um exemplo de uma classe de módulo Stub.
	```python
	from modules.interfaces import IModule
	from random import randint
	
	class Stub(IModule):
	    def __init__(self):
	        self.active = False
	        # Adicionar propriedades necessárias para o Modulo

	    def read(self, type_grandeza: str):
	        grandeza = type_grandeza.lower()
	        if grandeza == "temperatura":
	            return float("{:.2f}".format(randint(0,100)))
	        elif grandeza == "umidade":
	            return float("{:.2f}".format(randint(0,100)))
	        else:
	            raise Exception("Grandeza %s não suportado pelo Modulo" % grandeza)

	    def start(self):
	        try:
	            # Configurações relacionadas ao módulo físico
	            # Portas GPIO, Intefaces (I2C, SPI)
	            print("Módulo conectado a GPIO 7")
	        except Exception as e:
	            raise e
	        else:
	             # Configuração para iniciar/ativar módulo
	             print("Ativação do Módulo")
	             self.active = True
	```

5. Edite o arquivo `/estacao/modules/requirements.txt`, adicionando as bibliotecas externas utilizadas na implementação do novo Módulo.

6. Edite o arquivo `/estacao/modules/drivers.py`, adicionando as linhas referentes à importação do novo Módulo conforme exemplo.

	```python
	def get_instance(id_module: str):
	    module = id_module.upper()
	    if module == "BMP280":
	        from modules.bmp280 import BMP280
	        return BMP280()
	    # Adicione aqui a importação de um novo módulo.
	    elif module == "STUB":
	        from modules.stub import Stub
	        return Stub()
	```
	**Obs.:** A string de comparação (e.g., `"STUB"`) deve ser escrita em letras maísculas. Quando o módulo for adicionado na estação via API é necessário colocar como `id_module` o mesmo valor que essa string de comparação (sem obrigatoriedade de ser em letras maíscula nesse caso).

7. Execute o script `update-modules.sh` para instalação dos requisitos do módulo e atualização do sistema estação.

	```bash
	$ cd /estacao
	$ sudo ./update-modules.sh
	```

8. Acompanhe os Logs do serviço estação e caso não apresente nenhum erro siga as etapas do tutorial [Exemplos de Requisições](#exemplos-de-requisições) para adicionar o novo módulo na estação e configurar um Sensor.
---
## Exemplos de requisições

A requsições estarão disponíveis somente na rede local da Raspberry. Abaixo seguem 3 requsições executas após instalar o módulo seguindo o tutorial [Instalação de novos Módulos/Drivers para Sensores](#instalaçao-de-novos-módulos-para-sensores). Para mais informações de como administrar o sistema estação consulte a [documentação](https://estacao.docs.apiary.io/) da API REST.

**Obs.:** Substitua, nas requsições a seguir, o `localhost` pelo IP da Raspberry se estiver executando em outro computador da rede local.

### Adicionar Módulo na Estação

```bash
$ curl http://127.0.0.1:5000/api/v1/modules -H "Content-Type: application/json" -d '{"id_module":"stub","description":"Módulo stub","grandezas_medidas":"temperatura,umidade"}'
```

### Adicionar Grandeza na Estação

Antes de adicionar o Sensor na Estação, é necessário incluir um tipo de grandeza e unidade a ser medida. Por padrão o sistem já possui as seguintes Grandeas cadastradas.
* type_grandeza = temperatura, unit = celsius.
* type_grandeza = pressure, unit = hectopascal.
* type_grandeza = altitude, unit = metro.

É possível verificar a lista de grandezas com a seguinte requisição.

```bash
$ curl http://127.0.0.1:5000/api/v1/grandezas -H "Accept: application/json"
```

Se a grandeza medida pelo Módulo ainda não estiver disponível, é necessário adicioná-la com a seguinte requisição.

```bash
$ curl http://127.0.0.1:5000/api/v1/grandezas -H "Content-Type: application/json" -d '{"type_grandeza":"Umidade","unit":"porcent"}'
```

**Obs.:** Estão disponíveis as seguintes unidades de medidas.
* metro, segundo, celsius, kelvin, porcent, pascal, hectopascal. 

A adição de novas unidades é feita diretamente no código editando o arquivo `/estacao/principal/dictionary.py`.

### Adicionar Sensor na Estação

```bash
$ curl http://127.0.0.1:5000/api/v1/sensors -H "Content-Type: application/json" -d '{"id_sensor":"stub-temperatura","type_grandeza":"temperatura","unit":"celsius","id_module":"stub","description":"sensor de temperatura do modulo Stub"}'
```

### Alterar Limiares de Sensor

```bash
$ curl -X PUT http://127.0.0.1:5000/api/v1/sensors/stub-temperatura/limiares -H "Content-Type: application/json" -d '{"value_min":30.0,"value_max":45.0}'
```
**Obs.:** Mais exemplos de requisições com `curl` podem ser encontrados no arquivo `/estacao/api/requests_examples.txt`.

---

## Exemplos de Clients RabbitMQ

Para facilitar os testes com os serviços de mensagens (requisições ou notificações) foram desenvolvidos dois clients pythons para simular requsições do sistema Web na própria Raspberry.

**Obs.:** Os clients utilizam as mesmas configurações que o sistema estação. Antes de executá-los verifique se as informações de conexão com a fila de mensagem estão corretas em `settings.py`.

### Client para Notificações

Execute os seguintes passos para executar o client que irá consumir as notificações geradas pelo sistema estação. 

1. Acesse o diretório de implantação e ative o ambiente virtual python.

```bash
$ cd /estacao
$ source venv/bin/activate
```

2. Execute o script python `client_notifications.py` para iniciar o consumer de notificações.

```bash
$ python services/client_notifications.py
```

3. Em outro terminal, altere o limiar de um dos sensores para verificar o recebimento de notificações.

### Client para Requisições

Execute os seguintes passos para executar o client que irá efetuar requisições ao sistema estação. 

1. Acesse o diretório de implantação e ative o ambiente virtual python.

```bash
$ cd /estacao
$ source venv/bin/activate
```

2. Execute o script python `client_requests.py` com os seguintes argumentos apresentados nos exemplos para efetuar uma requisição.

    - Exemplo GET
		```bash
		$ python services/client_requests.py "GET" "/api/v1/sensors/stub-temperatura/medidas"
		```
    - Exemplo PUT
		```bash
		$ python services/client_requests.py "PUT" "/api/v1/sensors/stub-temperatura/limiares" '{"value_min":0.0,"value_max":100.0}'
		```

**OBS.:** As operações disponíveis via Client Requests são: 
  - Alterações de Limiares de um Sensor (PUT).
  - Leitura da grandeza medida por um Sensor (GET).
  - Listar Sensores disponíveis na Estação (GET)
  - Lista Informações de um Sensor (GET)  



