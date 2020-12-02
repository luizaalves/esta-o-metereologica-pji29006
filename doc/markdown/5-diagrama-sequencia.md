### Diagrama de sequência

***Sistema Estação Meteorológica:***

***Atores***

**Admin**: Indivíduo responsável pela administração do Sistema.

**Sensor**: Hardware responsável por fornecer informações de grandezas medidas para o Sistema.

**Sistema Servidor**: Sistema responsável pela interface WEB. 

8. [Ler Medida Atual (CSU08)](./images/diagrama-de-sequencia/sistema-estacao/ler-medida-atual.png)
7. [Gerar Notificação (CSU09)](./images/diagrama-de-sequencia/sistema-estacao/gerar-notificacao.png)


***Sistema servidor:***

***Atores***

**Usuário**: Indivíduo com possibilidade de realizar algumas operações no Sistema

**Sistema E.M.**: Sistema Estação Meteorológica. 

1. [Configurar Sensor (CSU01)](./images/diagrama-de-sequencia/sistema-servidor/configurar-sensor.png)
2. [Ler Medida Atual (CSU02)](./images/diagrama-de-sequencia/sistema-servidor/ler-medida-atual.png)
