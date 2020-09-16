### Casos de uso 

*Em construção*

***Descrição do sistema raspberry***

| Nome do caso de uso | Leitura instantanea do sensor                                |
| ------------------- | ------------------------------------------------------------ |
| Ator principal      | Sistema servidor                                             |
| Atores Secundários  | Admin, sensor                                                |
| Resumo              | Esse caso de uso descreve as etapas percorridas para o <br/>sistema servidor obter a leitura instantanea do sensor. |
| Pré-condições       | Estar conectado a uma rede wi-fi                             |

**Fluxo principal**

| Ações do ator                              | Ações do sistema                                             |
| ------------------------------------------ | ------------------------------------------------------------ |
| 1. Efetuar o login com seu usuario e senha |                                                              |
|                                            | 2. Validar acesso                                            |
|                                            | 3. Enviar informações instantaneas da leitura do sensor      |
| 4. Visualizar informações na tela          |                                                              |
| **Restrições**                             | 1. O usuário precisa ter uma conta de acesso fornecida pelo admin. |

**Fluxo de exceção**

| Ações do ator                               | Ações do sistema                                     |
| ------------------------------------------- | ---------------------------------------------------- |
| 1. Digitar incorretamente o login e a senha |                                                      |
|                                             | 2. Comunicar o usuário que os dados estão incorretos |
|                                             | 3. Recusar pedido                                    |

