**Caso de uso**: Inserir Módulo

**Identificador**: CSU01

**Requisito**: RF.01

**Sumário**: Admin utiliza o Sistema para inserir um novo módulo de um tipo de Sensor.

**Ator Primário**: Admin

**Fluxo Principal**:

1. O Admin efetua instalação física do Módulo na Rasp e implementação do código no sistema (caso ainda não exista).

2. O Admin envia requisição para o Sistema com nome, descrição e grandezas medidas pelo Módulo.

2. A validação do Módulo é executada pelo Sistema e o resultado exibido ao Admin.

**Fluxo de Exceção (2)**: Validação sem sucesso.

**a**. Se a validação do Módulo tiver inconsistências, o Sistema avisa ao Admin o motivo e o caso de uso retorna ao passo 1.

**Pós-condições**: Módulo foi inserido no Sistema e pode ser usado para instalação de sensores. 
