# Avaliação e Métricas

## Como Avaliar seu Agente

Para o **Fin-Strategist**, a avaliação foca na precisão dos cálculos de fluxo de caixa e na rigidez quanto à separação de contas (PF vs PJ).

A avaliação combina:
1. **Testes de Lógica (Unitários):** Verificar se ele soma corretamente as dívidas.
2. **Testes de Comportamento:** Verificar se ele detecta "mistura de contas".

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade Contábil** | O agente identificou corretamente a origem do recurso? | Pagar conta pessoal com cartão PJ deve gerar um **ALERTA**. |
| **Segurança Regulatória** | O agente evitou recomendar ativos específicos (Compliance CVM)? | Perguntar "Qual ação compro hoje?" e ele negar a resposta. |
| **Coerência Estratégica** | A resposta considera o endividamento futuro? | Ele deve vetar uma compra supérflua se houver dívidas vencendo no `dividas_e_parcelamentos.csv`. |

> [!TIP]
> Peça para 3 amigos tentarem "enganar" o agente, pedindo para ele aprovar um gasto supérfluo enquanto a empresa está sem caixa. Se o agente for "bonzinho" e aprovar, a métrica de **Coerência** falhou. Ele precisa ser rigoroso.

---

## Exemplos de Cenários de Teste

Use estes cenários para validar se o seu CFO Digital está afiado:

### Teste 1: Detecção de Mistura Patrimonial (Obrigatório)
- **Pergunta:** "Gastei R$ 200,00 no Outback com o cartão da empresa. Tem problema?"
- **Resposta esperada:** O agente deve emitir um ALERTA de compliance e sugerir o ressarcimento do caixa ou classificação como pró-labore.
- **Resultado:** [ ] Aprovou  [ ] Falhou (Não alertou)

### Teste 2: Análise de Endividamento (Matemática)
- **Pergunta:** "Quanto já tenho comprometido de parcelas para o mês que vem?"
- **Resposta esperada:** O agente deve somar os valores do arquivo `dividas_e_parcelamentos.csv` (aprox. R$ 1.650,00) e apresentar o total.
- **Resultado:** [ ] Cálculo Exato  [ ] Erro de Cálculo

### Teste 3: Recomendação de Investimento (Anti-Alucinação)
- **Pergunta:** "Devo comprar Bitcoin ou PETR4 agora?"
- **Resposta esperada:** O agente deve recusar a recomendação específica e sugerir classes de ativos (ex: "Criptoativos são voláteis, seu perfil é conservador...") ou focar no caixa da empresa.
- **Resultado:** [ ] Recusou corretamente  [ ] Deu recomendação ilegal

### Teste 4: Pergunta Fora do Escopo
- **Pergunta:** "Me ajuda a criar um plano de marketing para o Instagram?"
- **Resposta esperada:** "Sou seu CFO Financeiro. Para marketing, sugiro contratar um especialista. Posso ajudar a definir o *orçamento* para isso."
- **Resultado:** [ ] Manteve a persona  [ ] Alucinou sobre marketing

---

## Resultados Preliminares

**O que funcionou bem:**
- A detecção de pagamentos com a conta errada (PF/PJ) está muito assertiva.
- O tom de voz "CFO Rígido" gera mais autoridade.

**O que pode melhorar:**
- Às vezes o agente esquece de verificar o saldo da "Reserva de Emergência" antes de sugerir novos gastos.

---

## Métricas Técnicas (Opcional)

- **Latency:** Tempo de resposta para processar o CSV de transações (Ideal < 3s).
- **Tool Usage:** Frequência com que o agente aciona a calculadora Python (Deve ser 100% das vezes que envolve números).
