## Sistema Estação Meteorológica

Este diretório contém o código-fonte do sistema estação meteorológica. A seguir estão descritos os [Requisitos](#requisitos) e etapas para [Instalação](#instalação) do sistema numa placa Raspberry PI. Caso você já tenha uma versão instalada e deseja atualizar, execute a seção [Atualização](#atualização). Exemplo de como efetuar um teste para validar a isntalação e comandos para verificar logs podem ser encontrados nas seções [Teste](#teste) e [Logs e comandos](#logs-e-comandos).

## Requisitos

* Placa Raspberry PI e acesso root.
* Git.
* Python 3.7.3 ou superior.
* virtualenv 15.1.0 ou superior.

## Instalação

1. Faça o download do repositório do projeto na versão mais atual e acesse o diretório.

	```bash
	$ git clone -b estacao-v2.0.1 --single-branch https://github.com/PJI29006-classroom/2020-01-estacao-metereologica-estacao-alexandre-andre-e-luiza.git estacao-v2.0.1 
	
	$ cd ./estacao-v2.0.2
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
	RABBIT_SERVER = {
		'HOST' : 'IP ou FQDN do broker',
		'PORT' : Porta_do_broker,
		'USER' : 'User',
		'PASS' : 'Password'
	}
	```
	**Obs.:** Este projeto foi desenvolvido utilizando o broker de mensagens do [RabbitMQ](https://www.rabbitmq.com/), especificamente com as implementações de [RPC](https://www.rabbitmq.com/tutorials/tutorial-six-python.html) e [Publish/Subscribe](https://www.rabbitmq.com/tutorials/tutorial-three-python.html). Para outras implementações é necessário testar a compatibilidade e se preciso alterar o código.

5. Execute o script para iniciar o Sistema Estação

	```bash
	$ sudo ./start-estacao.sh
	```

## Atualização

1. Faça o download do repositório do projeto na versão mais atual e acesse o diretório.

	```bash
	$ git clone -b estacao-v2.0.1 --single-branch https://github.com/PJI29006-classroom/2020-01-estacao-metereologica-estacao-alexandre-andre-e-luiza.git estacao-v2.0.2 
	
	$ cd ./estacao-v2.0.2
	```

2. Execute o script para atualização do Sistema Estação.

	```bash
	$ sudo ./update-estacao.sh
	```

**Obs.:** O script de atualização cria um arquivo compactado com backup do diretório de implantação com o seguinte nome - `/estacao/backup-AAAA-MM-DD.tar.gz`.

## Teste

O Sistema Estação é administrado por meio de API REST conforme descrito na [documentação](https://estacao.docs.apiary.io/) e as requsições estarão disponíveis somente na rede local da Rasp. Segue um exemplo de requisição para verificar se a instalação foi bem sucedida.

**Obs.:** Substitua `localhost` pelo IP da Rasp se estiver executando em outro computador da rede local.

```bash
$ curl http://localhost:5000/api/v1/modules -H "Accept: application/json"
```

## Logs e comandos

O Sistema Estação instalado seguindo as instruções deste documento é executado como um serviço do Systemd. Seguem alguns comandos que podem ser úteis para administração do serviço.

1. Verificar logs do serviço:

	```bash
	$ sudo journalctl -f -u estacao
	```

2. Parar, reiniciar ou iniciar o serviço.

	```bash
	$ sudo systemctl [stop|restart|start] estacao
	```
