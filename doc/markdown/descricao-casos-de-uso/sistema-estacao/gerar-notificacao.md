**Caso de uso**: Gerar Notificação

**Identificador**: CSU09

**Requisito**: RF.06

**Sumário**: Sistema gera notificação para Sistema Servidor caso um limiar seja atingido.

**Ator Primário**: Sistema Servidor

**Precondições**: Pelo menos um Sensor instalado e configurado.

**Fluxo Principal**:

1. Sistema verifica a lista com Sensores instalados e configurados.

2. Incluir o caso de uso CSU07 e realizar leitura para cada Sensor da lista.

3. O Sistema verifica leitura de cada Sensor e compara com seus limiares configurados.

4. Se algum limiar for atingido, o Sistema envia notificação para o Sistema Servidor.

**Fluxo de Exceção (2)**: Erro ao obter leitura do Sensor.

**a**. Se a leitura da grandeza medida por um Sensor falhar, o Sistema exibe o erro e o caso de uso continua com a leitura do próximo Sensor.

**Pós-condições**: As leituras de cada Sensor foram realizadas e notificações necessárias enviadas.

**Regras de Negócio**: RN.04. 
