**Caso de uso**: Instalar Sensor

**Identificador**: CSU02

**Requisito**: RF.02

**Sumário**: Admin utiliza o Sistema para instalar o Sensor desejado.

**Ator Primário**: Admin

**Ator Secundário**: Sensor

**Precondições**: O Módulo referente ao Sensor a ser instalado deve estar inserido no Sistema.

**Fluxo Principal**:

1. A instalação física do Sensor é realizada pelo Admin.

2. O Admin envia requisição para o Sistema solicitando informações dos Módulos instalados.

3. O Sistema apresenta os Módulos instalados.

4. O Admin solicita ao Sistema a instalação do Sensor informando um Nome e o Módulo que esse Sensor irá utilizar.

5. O Sistema executa uma verificação da instalação física do Sensor e realiza uma leitura inicial.

6. O Sensor retorna a leitura para o Sistema.

7. Sistema exibe as informações para o Admin.

**Fluxo de Exceção (5)**: Sensor não reconhecido ou erro durante leitura inicial

**a**. Se a verificação da instalação física do Sensor não for positiva, o Sistema exibe o erro e o caso de uso retorna ao passo 2.

**b**. Se a leitura inicial do Sensor falhar , o Sistema apresenta o motivo e o caso de uso termina.

**Pós-condições**: O Sensor foi instalado e está disponível para configurações.

**Regras de Negócio**: RN.01. 
