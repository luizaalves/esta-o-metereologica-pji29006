### Casos de uso - Leitura instantanea do sensor 

***Descrição do caso de uso do sistema raspberry***

| Nome do caso de uso | Leitura instantanea do sensor                                |
| ------------------- | ------------------------------------------------------------ |
| Ator principal      | Admin                                                        |
| Atores Secundários  | Sensor,                                                      |
| Resumo              | Esse caso de uso descreve as etapas percorridas para o <br/>admin obter a leitura instantanea do sensor. |
| Pré-condições       | Estar conectado a uma rede ethernet                          |

**Fluxo principal**

| Ações do ator                          | Ações do sistema                                        |
| -------------------------------------- | ------------------------------------------------------- |
| 1. Acessar a área de configurar sensor |                                                         |
|                                        | 2. Exibe a lista de usuários disponíveis                |
| 3. Seleciona o usuário                 |                                                         |
|                                        | 4. Valida a operação                                    |
|                                        | 5. Exibe as opções                                      |
| 6. Seleciona a opção 'Leitura sensor'  |                                                         |
|                                        | 7. Exibe os sensores disponíveis                        |
| 8. Seleciona o sensor                  |                                                         |
|                                        | 9. Enviar informações instantaneas da leitura do sensor |
| 10. Visualizar informações na tela     |                                                         |

**Fluxo de exceção**

| Ações do ator             | Ações do sistema                                   |
| ------------------------- | -------------------------------------------------- |
| 1. Digitar a opção errada |                                                    |
|                           | 2. Comunicar o admin que os dados estão incorretos |
|                           | 3. Recusar pedido                                  |

