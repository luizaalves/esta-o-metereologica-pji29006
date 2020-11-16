**Caso de uso**: Configurar Sensor

**Identificador**: CSU01

**Sumário**: Usuário realiza configurações do Sensor no Sistema

**Ator Primário**: Usuário

**Ator Secundário**: Sistema EM

**Precondições**: Pelo menos um Sensor instalado no Sistema EM.

**Fluxo Principal**:

1. O Usuário acessa Sistema Servidor para configurar o Sensor.

2. Sistema Servidor solicita lista de Sensores instalados para o Sistema EM.

3. O Sistema EM retorna a lista para o Sistema Servidor que exibe ao Usuário.

4. O Usuário escolhe o Sensor a ser configurado.

5. Sistema Servidor solicita opções de configurações do Sensor escolhido para o Sistema EM.

6. Sistema EM envia as configurações possíveis para o Sistema Servidor.

7. Sistema Servidor apresenta as configurações possíveis para o Usuário.

8. Usuário seleciona a configuração desejada e informa valores.

9. Sistema Servidor envia as configurações para o Sistema EM.

10. Sistema EM executa a validação das configurações e envia resultado para o Sistema Servidor.

11. Sistema Servidor exibe resultado para o Usuário.

**Fluxo de Exceção (10)**: Configuração não suportada.

**a**. Se a validação das configurações não for positiva, o Sistema Servidor exibe o erro e o caso de uso retorna ao passo 3.

**Pós-condições**: As configurações do Sensor foram executadas. 
