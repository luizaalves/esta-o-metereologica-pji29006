#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "Necessário executar como root (sudo)" 
       	exit 1
fi

ESTACAO_HOMEDIR="/estacao"
ESTACAO_VENV="${ESTACAO_HOMEDIR}/venv"

DATE=`date +'%Y-%m-%d'`
BACKUP_FILE="/estacao/backup-${DATE}.tar.gz"

echo "Parando serviço estacao..."
systemctl stop estacao

if [ -d "${ESTACAO_HOMEDIR}" ]
then
	echo "Diretório ${ESTACAO_HOMEDIR} encontrado"
    echo "Criando backup "
    tar cfz ${BACKUP_FILE} ${ESTACAO_HOMEDIR}
else
	echo "Diretório de implantação (${ESTACAO_HOMEDIR}) não encontrado"
    echo "Se não possuir nenhum instalação so sistema, execute o script de instalação."
    exit 1
fi

if [ -d "${ESTACAO_VENV}" ]
then
	echo "Ambiente virtual encontrado em ${ESTACAO_VENV}"
else
	echo "Criando ambiente virtual em ${ESTACAO_VENV}"
	echo "Atenção! Esta etapa pode demorar alguns minutos....."
	virtualenv -p python3 ${ESTACAO_VENV}
fi

echo "Fazendo backup dos arquivos de configuração"
cp ${ESTACAO_HOMEDIR}/settings.py ${ESTACAO_HOMEDIR}/bkp-settings.py
cp ${ESTACAO_HOMEDIR}/logging.ini ${ESTACAO_HOMEDIR}/bkp-logging.ini
cp ${ESTACAO_HOMEDIR}/estacao.db ${ESTACAO_HOMEDIR}/bkp-estacao.db
cp ${ESTACAO_HOMEDIR}/uwsgi.ini ${ESTACAO_HOMEDIR}/bkp-uwsgi.ini

echo "Instalando requisitos da aplicação"
echo "Atenção! Esta etapa pode demorar alguns minutos....."
${ESTACAO_VENV}/bin/pip3 install -r ${ESTACAO_HOMEDIR}/requirements.txt

export PYTHONPATH="${PYTHONPATH}:${ESTACAO_HOMEDIR}"

echo "Revertendo arquivos de configuração"
mv ${ESTACAO_HOMEDIR}/bkp-settings.py ${ESTACAO_HOMEDIR}/settings.py
mv ${ESTACAO_HOMEDIR}/bkp-logging.ini ${ESTACAO_HOMEDIR}/logging.ini
mv ${ESTACAO_HOMEDIR}/bkp-estacao.db ${ESTACAO_HOMEDIR}/estacao.db
vm ${ESTACAO_HOMEDIR}/bkp-uwsgi.ini ${ESTACAO_HOMEDIR}/uwsgi.ini

echo "Reiniciando serviço do Sistema Estação..."
systemctl start estacao