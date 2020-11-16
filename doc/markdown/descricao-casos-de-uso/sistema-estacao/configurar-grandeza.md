**Caso de uso**: Configurar Grandeza

**Identificador**: CSU06

**Requisito**: RF.04

**Sumário**: Admin utiliza o Sistema para efetuar a configuração da grandeza que será medida pelo Sensor.

**Ator Primário**: Admin

**Ator Secundário**: Sensor

**Precondições**: Pelo menos uma grandeza cadastrada no Sistema.

**Fluxo Principal**:

1. Herdar o caso de uso: CSU04.

2. O Admin envia uma requisição ao Sistema com as informações do Sensor que deseja configurar e a grandeza que será medida.

3. O Sistema realiza a configuração da grandeza no Sensor.

4. O Sistema exibe resultado ao Admin.

**Fluxo de Exceção (3)**: Houve erro ao configurar grandeza.

**a**. Se a configuração da grandeza no Sensor falhar, o Sistema reporta o erro e o caso de uso termina.

**Pós-condições**: A grandeza de medida do Sensor foi configurada. 
