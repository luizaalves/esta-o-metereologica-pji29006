**Caso de uso**: Cadastrar Grandeza

**Identificador**: CSU02

**Requisito**: RF.03

**Sumário**: Admin cadastra no Sistema uma grandeza a ser medida.

**Ator Primário**: Admin

**Fluxo Principal**:

1. O Admin envia uma requisição ao Sistema informando uma grandeza e unidade de medida para cadastro.

2. O Sistema verifica informações e exibe resultado para o Admin.

**Fluxo de Exceção (2)**: Grandeza já existe.

**a**. Se a grandeza desejada já estiver sido cadastrada anteriormente, o Sistema reporta o fato e o caso de uso retorna ao passo 1.

**Pós-condições**: A grandeza foi cadastrada e fica disponível para configuração do Sensor. 
