#!/bin/bash

ESTACAO_HOMEDIR="/estacao"
ESTACAO_VENV="${ESTACAO_HOMEDIR}/venv"

if [[ $EUID -ne 0 ]]; then
	echo "Necessário executar como root (sudo)" 
       	exit 1
fi

export PYTHONPATH="${PYTHONPATH}:${ESTACAO_HOMEDIR}"

echo "Instalando requisitos dos módulos"
echo "Atenção! Esta etapa pode demorar alguns minutos....."
${ESTACAO_VENV}/bin/pip3 install -r ${ESTACAO_HOMEDIR}/modules/requirements.txt

echo "Reiniciando serviço....."
systemctl restart estacao