## Levantamento de requisitos: ##
### Requisitos Funcionais (RF): ###

**RF.01 -** Permitir Registro e Autenticação do cliente;

**RF.02 -** Visualizar e Alterar dados dos sensores;

**RF.03 -** Possibilitar a leitura de dados dos sensores;

**RF.04 -** Permitir a configuração dos sensores;

**RF.05 -** Permitir a configuração dos limiares superiores e inferiores dos sensores;

**RF.06 -** Avisar o cliente quando os limiares de algum sensor for alcançado;

**RF.07 -** Possibilitar a realização de outras configurações;

**RF.08 -** Permitir multiplicidade de sensores;


### Requisitos não funcionais (RNF): ###

**RNF.01 -** O cliente precisa estar conectado a internet;

**RNF.02 -** Requerido uma Raspberry PI versão xxx;

**RNF.03 -** Deve ser possível utilizar os seguintes sensores:
    - BMP180
    - HDC1080
    - DHT11
    - Presença PIR 


### Regras de negócio (RN): ###

**RN.01 -** Somente cliente com autenticação no sistema e conectado na internet poderá configurar os sensores e os limiares;

**RN.02 -** A estação Raspberry PI tem que estar conectado no(s) sensor(es);

**RN.03 -** A estação Raspberry PI tem que estar conectado na internet localhost.
