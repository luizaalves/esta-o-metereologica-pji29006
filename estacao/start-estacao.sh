#!/bin/bash

SYSTEM_DIR=/etc/systemd/system
SYSTEM_FILE=system-unit

if [[ $EUID -ne 0 ]]; then
	echo "Necessário executar como root (sudo)" 
       	exit 1
fi

echo "Criando estacao.service em ${SYSTEM_DIR}"
cp ${SYSTEM_FILE} ${SYSTEM_DIR}/estacao.service

echo "Configurando Serviço para iniciar com o SO"
systemctl enable estacao

echo "Iniciando serviço....."
systemctl start estacao
