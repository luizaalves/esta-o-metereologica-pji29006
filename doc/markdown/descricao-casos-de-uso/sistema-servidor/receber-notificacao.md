**Caso de uso**: Receber Notificação

**Identificador**: CSU03

**Requisito**: RF.06

**Sumário**: Sistema Servidor recebe notificação do Sistema EM

**Ator Primário**: Sistema EM

**Precondições**: Limiar de algum Sensor atingido.

**Fluxo Principal**:

1. Sistema EM executa leitura de todos os sensores instalados e configurados.

2. Se o limiar de medida de algum Sensor for atingido, Sistema EM gera a notificação para o Sistema Servidor

3. Sistema Servidor acrescenta notificação em sua lista de notificações.

**Pós-condições**: Notificações disponíveis para Usuário.

**Regras de Negócio**: RN.04. 
