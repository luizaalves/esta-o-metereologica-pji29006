## Levantamento de requisitos: ##
### Requisitos Funcionais (RF): ###

**RF.01 -** Permitir que sejam inseridos módulos/drivers para novos sensores;

**RF.02 -** Possibilitar a instalação de sensor(es);

**RF.03 -** Permitir cadastrar grandezas a serem medidas;

**RF.04 -** Permitir a configuração do sensor e da grandeza a ser medida;

**RF.05 -** Possibilitar a configuração de limiar (inferior e superior) da grandeza medida pelo sensor;

**RF.06 -** Gerar notificações de medidas;

**RF.07 -** Permitir a leitura da grandeza medida pelo sensor; 

**RF.08 -** Permitir multiplicidade de sensores;

### Requisitos não funcionais (RNF): ###

**RNF.01 -** As funcionalidades do sistema devem ser acessadas localmente através de uma API REST;

**RNF.02 -** O sistema deve possuir módulos/drivers para os sensores:
    - BMP280
    - HDC1080
    - DHT11
    - Presença PIR 

**RNF.03 -** O Sistema deve ser implementado em uma RaspBerry PI; 

### Regras de negócio (RN): ###

**RN.01 -** Somente sensor com módulo/driver previamente instalado e inserido poderá ser adicionado;

**RN.02 -** Uma mesma grandeza poderá ser medida por mais de um sensor;

**RN.03 -** Poderá ser instalado mais de um sensor do mesmo tipo;

**RN.04 -** As notificações só serão geradas para medidas que atingirem os limiares configurados; 

