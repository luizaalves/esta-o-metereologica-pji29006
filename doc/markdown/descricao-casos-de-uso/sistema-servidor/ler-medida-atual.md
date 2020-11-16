**Caso de uso**: Ler Medida Atual

**Identificador**: CSU02

**Requisito**: RF.07

**Sumário**: Usuário utiliza Sistema Servidor para realizar leitura atual da grandeza medida por um Sensor.

**Ator Primário**: Usuário

**Ator Primário**: Sistema EM

**Precondições**: Sensor desejado instalado e configurado.

**Fluxo Principal**:

1. O Usuário acessa Sistema Servidor para realizar leitura de medida atual de um Sensor.

2. O Sistema Servidor solicita ao Sistema EM a lista de Sensores instalados e configurados.

3. Sistema EM retorna a lista para o Sistema Servidor que exibe ao Usuário.

4. Usuário seleciona Sensor que deseja obter leitura.

5. O Sistema Servidor envia solicitação de leitura atual ao Sistema EM.

6. O Sistema EM executa a leitura da grandeza medida pelo Sensor e retorna para o Sistema Servidor.

7. O Sistema Servidor apresenta leitura ao Usuário.

**Fluxo de Exceção (6)**: Erro ao obter leitura do Sensor.

**a**. Se a leitura da grandeza medida pelo Sensor falhar, o Sistema Servidor exibe o erro e o caso de uso retorna ao passo 2.

**Pós-condições**: A leitura da medida atual foi apresentada para o Usuário. 
