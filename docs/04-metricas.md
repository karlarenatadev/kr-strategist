# Avaliação e Métricas

## Como Avaliar seu Agente

Para o **KR-Strategist**, a avaliação é dupla: precisamos medir a **rigidez financeira** (CFO) e a **persuasão comercial** (Estrategista).

A avaliação combina:
1.  **Testes de Lógica (Unitários):** Verificar se ele soma as dívidas corretamente e filtra produtos pelo aporte mínimo.
2.  **Testes de Comportamento (Roleplay):** Verificar se ele detecta mistura de contas e se aplica técnicas de vendas (SPIN/Ancoragem) antes de dar preços.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de Sucesso |
| :--- | :--- | :--- |
| **Assertividade Contábil** | O agente protegeu o caixa da empresa? | Ao ver gasto pessoal na conta PJ, ele emite um **ALERTA DE COMPLIANCE**. |
| **Aderência ao Playbook** | O agente usou o script de vendas correto? | Se o cliente diz "tá caro", o agente usa a técnica de "Ancoragem" (do JSON), não uma desculpa genérica. |
| **Disciplina de Preço** | O agente evitou entregar o preço de bandeja? | Se perguntarem "quanto custa", ele devolve com uma pergunta (SPIN) em vez do valor. |
| **Coerência Híbrida** | A recomendação de venda respeita o saldo atual? | Ele veta uma campanha de tráfego pago se o saldo no `transacoes.csv` for insuficiente. |

> [!TIP]
> **O Teste do "Advogado do Diabo":** Peça para um amigo tentar arrancar o preço do agente logo na primeira mensagem. Se o agente der o preço sem qualificar, a métrica de **Disciplina de Preço** falhou.

---

## Exemplos de Cenários de Teste

Use estes cenários para validar as duas personalidades do seu agente:

### Teste 1: O CFO Rígido (Compliance)
- **Pergunta:** "Paguei meu almoço de domingo com o cartão da empresa. Tem problema?"
- **Resposta esperada:** O agente deve agir friamente, apontar o erro de misturar PF/PJ e sugerir descontar do pró-labore.
- **Resultado:** [ ] Reprovou a atitude  [ ] Aceitou passivamente (Falha)

### Teste 2: O Estrategista de Vendas (Objeção)
- **Pergunta:** "O cliente disse que vai falar com a esposa e depois retorna. O que eu digo?"
- **Resposta esperada:** O agente deve buscar no `objecoes_e_respostas.json` o script para "Vou pensar" ou "Terceiro Decisor" e sugerir uma resposta que isole a objeção.
- **Resultado:** [ ] Trouxe o script certo  [ ] Alucinou uma resposta genérica

### Teste 3: O Teste Híbrido (Onde investir?)
- **Contexto:** Saldo no CSV é de R$ 500,00. Produto mínimo no JSON custa R$ 1.000,00.
- **Pergunta:** "Tenho dinheiro parado. Qual a melhor aplicação do banco pra mim hoje?"
- **Resposta esperada:** O agente deve dizer que **nenhum** produto está disponível para esse saldo e sugerir acumular mais caixa antes de investir. (Não pode sugerir o produto de R$ 1k).
- **Resultado:** [ ] Respeitou o aporte mínimo  [ ] Ofereceu produto indisponível (Alucinação)

### Teste 4: A Regra de Ouro (Preço)
- **Pergunta:** "Quanto custa a sua mentoria?"
- **Resposta esperada:** Uma pergunta de qualificação (ex: "Antes de falar de valores, qual seu maior gargalo hoje?").
- **Resultado:** [ ] Fez SPIN Selling  [ ] Deu o preço direto (Falha Crítica)

---

## Resultados Preliminares

**O que funcionou bem:**
- A detecção de mistura PF/PJ continua muito assertiva.
- A busca por scripts de vendas ("tá caro") está funcionando via RAG.

**O que precisa de ajuste:**
- Às vezes, quando pergunto de investimento, ele esquece de checar se o saldo cobre o aporte mínimo. (Ajustar lógica no `app.py`).

---

## Métricas Técnicas

- **Retrieval Precision (RAG):** O agente encontrou o script de venda correto no JSON? (Meta: 100% de acerto para gatilhos exatos).
- **Latency:** O tempo para carregar os dois contextos (Financeiro + Vendas) deve ser imperceptível (< 3s).