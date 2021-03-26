#!/bin/bash

ESTACAO_HOMEDIR="/estacao"
ESTACAO_VENV="${ESTACAO_HOMEDIR}/venv"

if [[ $EUID -ne 0 ]]; then
	echo "Necessário executar como root (sudo)" 
       	exit 1
fi

if [ -d "${ESTACAO_HOMEDIR}" ]
then
	echo "Diretório ${ESTACAO_HOMEDIR} encontrado"
else
	echo "Criando diretório de implantação....."
	mkdir ${ESTACAO_HOMEDIR}
	echo "Copiando arquivos para diretório de implantação....."
	cp -r ./estacao/* ${ESTACAO_HOMEDIR}
fi

if [ -d "${ESTACAO_VENV}" ]
then
	echo "Ambiente virtual encontrado em ${ESTACAO_VENV}"
else
	echo "Criando ambiente virtual em ${ESTACAO_VENV}"
	echo "Atenção! Esta etapa pode demorar alguns minutos....."
	virtualenv -p python3 ${ESTACAO_VENV}
fi

echo "Instalando requisitos da aplicação"
echo "Atenção! Esta etapa pode demorar alguns minutos....."
${ESTACAO_VENV}/bin/pip3 install -r ${ESTACAO_HOMEDIR}/requirements.txt

export PYTHONPATH="${PYTHONPATH}:${ESTACAO_HOMEDIR}"

echo "Criando banco de dados para backup das informações..."
${ESTACAO_VENV}/bin/python ${ESTACAO_HOMEDIR}/models/entities.py