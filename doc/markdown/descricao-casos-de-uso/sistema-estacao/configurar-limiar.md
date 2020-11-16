**Caso de uso**: Configurar Limiar

**Identificador**: CSU05

**Requisito**: RF.05

**Sumário**: Admin utiliza o Sistema para efetuar a configuração de limiar (inferior e superior).

**Ator Primário**: Admin

**Fluxo Principal**:

1. Herdar o caso de uso: CSU04.

2. O Admin envia uma requisição ao Sistema com as informações do Sensor que deseja configurar e os valores para limiar inferior e superior.

3. O Sistema executa a validação dos valores e apresenta resultado ao Admin.

**Fluxo de Exceção (3)**: Sensor não suporta valor informado.

**a**. Se a validação dos valores de limiar não for positiva, o Sistema exibe o erro e o caso de uso retorna ao passo 2.

**Pós-condições**: Os limiares para envio de Notificação foram configurados. 
