**Caso de uso**: Instalar Sensor

**Identificador**: CSU03

**Requisito**: RF.02

**Sumário**: Admin utiliza o Sistema para instalar o Sensor desejado.

**Ator Primário**: Admin

**Ator Secundário**: Sensor

**Precondições**: O Módulo referente ao Sensor a ser instalado deve estar inserido no Sistema.

**Fluxo Principal**:

1. O Admin envia requisição para o Sistema solicitando informações dos Módulos instalados.

2. O Sistema apresenta os Módulos instalados.

3. O Admin solicita ao Sistema a instalação do Sensor informando um Nome e o Módulo que a instância do Sensor irá utilizar.

4. O Sistema executa uma verificação da instalação física do Sensor e realiza uma leitura inicial.

5. Sistema exibe as informações do Sensor adicionado para o Admin.

**Fluxo de Exceção (5)**: Módulo do Sensor não reconhecido ou erro durante leitura inicial

**a**. Se a verificação da instalação física do Sensor não for positiva, o Sistema exibe o erro e o caso de uso retorna ao passo 2.

**b**. Se a leitura inicial do Sensor falhar , o Sistema apresenta o motivo e o caso de uso termina.

**Pós-condições**: O Sensor foi instalado e está disponível para configurações.

**Regras de Negócio**: RN.01. 
