### Casos de uso - Alterar limiar do sensor 

*Em construção*

***Descrição do caso de uso do sistema servidor***

| Nome do caso de uso | Alterar limiar do sensor                                     |
| ------------------- | ------------------------------------------------------------ |
| Ator principal      | Usuário                                                      |
| Atores Secundários  | Sistema raspberry                                            |
| Resumo              | Esse caso de uso descreve as etapas percorridas para o <br/>usuário alterar o limiar do sensor. |
| Pré-condições       | Estar conectado a uma rede wi-fi ou rede móvel               |

**Fluxo principal**

| Ações do ator                                   | Ações do sistema                 |
| ----------------------------------------------- | -------------------------------- |
| 1. Efetuar o login com seu usuario e senha      |                                  |
|                                                 | 2. Validar acesso                |
|                                                 | 3. Exibe opções do sistema       |
| 4. Seleciona a opção 'Alterar limiar do sensor' |                                  |
|                                                 | 5. Exibe os sensores disponíveis |
| 6. Seleciona o sensor                           |                                  |
| 7. Edita o limiar do sensor                     |                                  |
|                                                 | 8. Valida a operação             |

**Fluxo de exceção**

| Ações do ator                               | Ações do sistema                                     |
| ------------------------------------------- | ---------------------------------------------------- |
| 1. Digitar incorretamente o login e a senha |                                                      |
|                                             | 2. Comunicar o usuário que os dados estão incorretos |
|                                             | 3. Recusar pedido                                    |

