# Em construção
## Sistema Estação Meteorológica

Este diretório contém o código-fonte do sistema estação meteorológica. A seguir estão descritos as informações para Instalar e configurar o sistema numa placa Raspberry PI. 

## Requisitos

* Placa Raspberry PI e acesso root.
* Git.
* Python 3.7.3 ou superior.
* virtualenv 15.1.0 ou superior.

## Instalação

1. Faça o download do reporsitório do projeto e acesse este diretório.

	```bash
	$ git clone https://github.com/PJI29006-classroom/2020-01-estacao-metereologica-estacao-alexandre-andre-e-luiza.git
	$ cd ./2020-01-estacao-metereologica-estacao-alexandre-andre-e-luiza/estacao
	```

2. Edite o arquivo `settyngs.py` alterando as informações referentes ao servidor de mensagens.

	```python
	RABBIT_SERVER = {
		'HOST' : 'IP ou FQDN do broker',
		'PORT' : Porta_do_broker,
		'USER' : 'User',
		'PASS' : 'Password'
	}
	```
	**Obs.:** Este projeto foi desenvolvido utilizando o broker de mensagens do [RabbitMQ](https://www.rabbitmq.com/), especificamente com as implementações de [RPC](https://www.rabbitmq.com/tutorials/tutorial-six-python.html) e [Publish/Subscribe](https://www.rabbitmq.com/tutorials/tutorial-three-python.html). Para outras implementações será preciso alterações no código.

3. Crie um ambiente virtual e ative-o para instalação dos pacotes necessários.

    ```bash
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    ```

4. Instale os requisitos do sistema instação usando pip. 

	```bash
	(venv)$ pip3 install -r requirements.txt
	```
