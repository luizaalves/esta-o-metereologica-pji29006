**Caso de uso**: Ler Medida Atual

**Identificador**: CSU08

**Requisito**: RF.07

**Sumário**: Admin utiliza Sistema para realizar leitura atual da grandeza medida pelo Sensor.

**Ator Primário**: Admin

**Precondições**: Sensor desejado instalado e configurado.

**Fluxo Principal**:

1. O Admin solicita ao Sistema uma lista com sensores instalado.

2. O Sistema apresenta a lista

3. Admin envia requisição ao Sistema informando qual Sensor deseja obter leitura.

4. Incluir caso de uso: CSU07.

5. O Sistema exibe ao Admin o valor da grandeza medida.

**Fluxo de Exceção (4)**: Erro ao obter leitura do Sensor.

**a**. Se a leitura da grandeza medida pelo Sensor falhar, o Sistema exibe o erro e o caso de uso retorna ao passo 2.

**Pós-condições**: A leitura da medida atual foi apresentada para o Admin. 
