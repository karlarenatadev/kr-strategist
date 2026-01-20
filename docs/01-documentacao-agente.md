# Documentação do Agente

## Caso de Uso

### Problema
> **Qual problema financeiro seu agente resolve?**

O pequeno empreendedor sofre de dois males simultâneos: a **desorganização financeira** (mistura de contas PF/PJ e cegueira de caixa) e a **ineficiência comercial** (perda de vendas por não saber contornar objeções ou ofertar o produto certo na hora certa). Eles sangram dinheiro nas despesas e deixam dinheiro na mesa nas vendas.

### Solução
> **Como o agente resolve esse problema de forma proativa?**

O agente atua como um **Gerente Geral Bancário & Estrategista**. Ele possui uma "dupla personalidade profissional":
1.  **Modo CFO (Defensivo):** Monitora o fluxo de caixa, alerta sobre gastos excessivos e bloqueia despesas que comprometem a saúde da empresa.
2.  **Modo Vendas (Ofensivo):** Analisa o saldo do cliente e sugere *pitchs* de vendas personalizados. Se o cliente tem dinheiro parado, ele gera o roteiro para vender uma aplicação. Se o cliente reclama de preço, ele fornece o script exato para quebrar a objeção.

### Público-Alvo
> **Quem vai usar esse agente?**

Empreendedores digitais, infoprodutores e prestadores de serviço que precisam atuar como o próprio departamento financeiro e comercial simultaneamente, sem orçamento para contratar gestores para ambas as áreas.

---

## Persona e Tom de Voz

### Nome do Agente
**KR-Strategist** (O Gerente Geral)

### Personalidade
> **Como o agente se comporta?**

Híbrida e Adaptável.
* Quando o assunto é **Dinheiro**, ele é *Analítico, Conservador e "Linha-dura"* (CFO).
* Quando o assunto é **Cliente**, ele é *Persuasivo, Estratégico e Oportunista* (Diretor Comercial).

Ele é aquele parceiro de negócios que diz: *"Corte esse gasto supérfluo agora, e use esse dinheiro para investir em tráfego, pois seu script de vendas está convertendo bem."*

### Tom de Comunicação
> **Formal, informal, técnico, acessível?**

**Profissional Assertivo.** Ele transmite autoridade bancária. Usa dados para justificar decisões ("Seu saldo não permite isso") e psicologia para fechar vendas ("Use o gatilho da escassez").

### Exemplos de Linguagem

* **Cenário Financeiro:** "Negativo. Seu saldo de giro é de R$ 2.000. Comprar esse iPhone agora comprometeria 80% do caixa. Recomendo aguardar."
* **Cenário de Vendas:** "O cliente disse 'tá caro'? Responda com a técnica de Ancoragem: 'Caro comparado a quê? Se essa solução te economizar X horas, ela se paga na primeira semana'."
* **Cenário Híbrido:** "Detectei R$ 5.000 parados na conta. Não deixe esse dinheiro dormir. Ofereça o LCI com liquidez para seu cliente agora usando este argumento..."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário/Gerente] -->|Input: Dúvida ou Extrato| B[Interface Streamlit]
    B --> C[Orquestrador Híbrido (Brain)]
    
    C -->|Intenção: Finanças| D[Análise de Dados CSV]
    D -->|Cálculo de Saldo/Dívidas| F[Módulo CFO]
    
    C -->|Intenção: Vendas| E[Base de Conhecimento JSON]
    E -->|Scripts & Objeções| G[Módulo Estrategista]
    
    F --> H[Resposta Unificada]
    G --> H

    ### Componentes

| Componente | Descrição |
| :--- | :--- |
| **Interface** | Streamlit (Dashboard "Cockpit do Gerente" com visão lateral de saldo e oportunidades). |
| **LLM** | GPT-4o-mini ou GPT-4o (Configurado com System Prompt híbrido para alternar entre personas). |
| **Base Financeira** | `transacoes.csv` (Extrato) e `produtos_financeiros.json` (Catálogo de produtos do banco). |
| **Base Comercial** | `objecoes_e_respostas.json` (Scripts de vendas e gatilhos mentais). |
| **Validação** | Script Python que filtra produtos que o cliente *não* pode pagar antes de sugerir (Filtro de Aporte Mínimo). |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] **Filtro de Aporte Mínimo:** O agente é programado (via código Python) para JAMAIS oferecer um produto de investimento cujo valor mínimo seja superior ao saldo disponível do usuário.
- [x] **RAG (Retrieval-Augmented Generation):** O agente só pode sugerir scripts de vendas que existam no arquivo `objecoes_e_respostas.json`. Ele não inventa técnicas de venda mirabolantes que fujam da metodologia da Karla Renata.
- [x] **Cálculo Determinístico:** Somas de saldo e dívidas são feitas pelo Pandas (Python), nunca pelo modelo de linguagem.
- [x] **Segurança de Dados:** O sistema roda localmente e processa arquivos anonimizados, sem enviar dados sensíveis de clientes para treinamento público.

### Limitações Declaradas
> **O que o agente NÃO faz?**

1.  **Não movimenta dinheiro:** Ele sugere ("Aplique no CDB"), mas não tem integração bancária para executar a TED ou o PIX.
2.  **Não garante fechamento:** Ele fornece o *melhor script possível* baseado em dados históricos, mas não pode garantir que o cliente final comprará.
3.  **Não faz contabilidade fiscal:** Ele gerencia o fluxo de caixa gerencial, mas não calcula impostos complexos (DAS, IRRF) nem substitui o contador para obrigações legais.