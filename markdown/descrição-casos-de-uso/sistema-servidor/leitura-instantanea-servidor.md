###  Casos de uso - Leitura instantanea do sensor 

*Em construção*

***Descrição do caso de uso do sistema raspberry***

| Nome do caso de uso | Leitura instantanea do sensor                                |
| ------------------- | ------------------------------------------------------------ |
| Ator principal      | Usuário                                                      |
| Atores Secundários  | Sistema raspberry                                            |
| Resumo              | Esse caso de uso descreve as etapas percorridas para o <br/>usuário obter a leitura instantanea do sensor. |
| Pré-condições       | Estar conectado a uma rede wi-fi ou rede móvel               |

**Fluxo principal**

| Ações do ator                              | Ações do sistema                                             |
| ------------------------------------------ | ------------------------------------------------------------ |
| 1. Efetuar o login com seu usuario e senha |                                                              |
|                                            | 2. Validar acesso                                            |
|                                            | 3. Exibe opções do sistema                                   |
| 4. Seleciona a opção 'Leitura do sensor'   |                                                              |
|                                            | 5. Enviar informações instantaneas da leitura do sensor      |
| 6. Visualizar informações na tela          |                                                              |
| **Restrições**                             | 1. O usuário precisa ter uma conta de acesso fornecida pelo admin. |

**Fluxo de exceção**

| Ações do ator                               | Ações do sistema                                     |
| ------------------------------------------- | ---------------------------------------------------- |
| 1. Digitar incorretamente o login e a senha |                                                      |
|                                             | 2. Comunicar o usuário que os dados estão incorretos |
|                                             | 3. Recusar pedido                                    |

