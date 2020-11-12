###  Casos de uso - Leitura periódica 

***Descrição do caso de uso do sistema raspberry***

| Nome do caso de uso | Leitura periódica                                            |
| ------------------- | ------------------------------------------------------------ |
| Ator principal      | Sistema servidor                                             |
| Atores Secundários  | Sensor                                                       |
| Resumo              | Esse caso de uso descreve as etapas percorridas para o <br/>sistema servidor obter a leitura periódica do sensor. |
| Pré-condições       | Estar conectado a uma rede wi-fi ou rede móvel               |

**Fluxo principal**

| Ações do ator                   | Ações do sistema                                             |
| ------------------------------- | ------------------------------------------------------------ |
|                                 | 1. Sistema gera uma notificação com a leitura periódica do sensor programada |
| 2. Recebe a notificação e trata |                                                              |
| **Restrições**                  | 1. O sistema  obter um token do usuário para o envio da notificação inválido |
