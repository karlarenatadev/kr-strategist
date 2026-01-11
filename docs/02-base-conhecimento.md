# Base de Conhecimento

## Dados Utilizados

Neste projeto, utilizamos um conjunto de dados expandido para simular a realidade de um empreendedor que mistura finanças pessoais e empresariais.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `transacoes.csv` | CSV | Analisar fluxo de caixa misto (PF/PJ) e categorizar despesas por centro de custo. |
| `dividas_e_parcelamentos.csv` | CSV | **(Novo)** Projetar o comprometimento de renda futura e calcular o "Sobrevivência Runway". |
| `perfil_investidor.json` | JSON | Identificar perfil de risco e dados do negócio (regime tributário, meta de giro). |
| `produtos_financeiros.json` | JSON | Sugerir alocação de caixa (LCI/CDB) ou investimentos de longo prazo. |
| `historico_atendimento.csv` | CSV | Dar contexto de "memória" para evitar perguntas repetitivas. |

---

## Adaptações nos Dados

Para tornar o agente um verdadeiro "CFO Digital", os dados originais foram significativamente enriquecidos:

1.  **Expansão de Volume:** As bases foram aumentadas para conter entre 10 a 20 registros cada, permitindo testes de padrões mais complexos.
2.  **Novas Colunas em `transacoes.csv`:**
    * `origem_recurso`: Identifica se o dinheiro saiu da conta Pessoa Física (PF) ou Jurídica (PJ).
    * `centro_custo`: Categoriza o gasto (ex: Marketing, Vida Pessoal, Ferramentas).
    * `dedutivel`: Flag para identificar despesas que podem abater impostos.
3.  **Criação de `dividas_e_parcelamentos.csv`:** Um dataset novo para mapear parcelas futuras (cartão, empréstimos), essencial para o cálculo de fluxo de caixa projetado.
4.  **Dados de Negócio no JSON:** Inclusão de campos como `regime_tributario` e `reserva_giro_necessaria` no perfil do investidor.

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos CSV e JSON são carregados utilizando a biblioteca **Pandas** no Python assim que a aplicação inicia. Eles são convertidos em *DataFrames* para facilitar filtragens (ex: "Filtrar apenas gastos da categoria Marketing do último mês").

### Como os dados são usados no prompt?
Não enviamos o banco de dados inteiro para o LLM a cada mensagem para economizar tokens. A estratégia é **RAG (Retrieval-Augmented Generation) Simplificado**:

1.  O usuário faz uma pergunta (ex: "Como está meu fluxo de caixa?").
2.  O script Python pré-processa os dados (calcula totais, separa PF de PJ).
3.  Um **resumo estruturado** é injetado no *System Prompt* dinamicamente.

---

## Exemplo de Contexto Montado

Abaixo, um exemplo de como as informações são apresentadas ao Agente (LLM) "por trás dos panos":

```text
CONTEXTO FINANCEIRO ATUAL (Atualizado em: 2025-10-31):

1. PERFIL DO CLIENTE:
   - Nome: João Silva (PJ: Simples Nacional)
   - Meta de Giro: R$ 15.000 | Atual: R$ 3.000 (ALERTA: Baixo)

2. RESUMO DO MÊS (Outubro/2025):
   - Receita PJ: R$ 8.500,00
   - Gastos PJ: R$ 2.189,90 (Principais: Marketing, Ferramentas)
   - Gastos PF Pagos com Conta PJ (ERRO): R$ 0,00 (Parabéns! Nenhuma mistura detectada hoje)
   - Gastos Pessoais Totais: R$ 4.200,00

3. DÍVIDAS E COMPROMETIMENTOS FUTUROS:
   - Total em Parcelas para Nov/2025: R$ 1.650,00
   - Destaque: Parcela 8/8 Notebook Trabalho (R$ 450,00) - Finaliza em breve.

INSTRUÇÃO: Com base nisso, responda à pergunta do usuário focando na recomposição do Capital de Giro.
