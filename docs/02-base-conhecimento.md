# Base de Conhecimento

## Visão Geral dos Dados

O KR-Strategist utiliza uma arquitetura de dados híbrida, dividida em dois "hemisférios": o **Cofre** (Dados Financeiros) e o **Playbook** (Dados Comerciais). Isso permite que o agente atue simultaneamente como CFO e Diretor Comercial.

### 1. O Cofre (Módulo Financeiro)

| Arquivo | Formato | Função no Agente |
|---------|---------|------------------|
| `transacoes.csv` | CSV | **Fonte da Verdade Financeira.** Contém o extrato bancário unificado. Usado para calcular saldo, separar PF/PJ e gerar alertas de fluxo de caixa. |
| `produtos_financeiros.json` | JSON | **Catálogo de Investimentos.** Lista os produtos disponíveis no banco (CDB, LCI, Fundos) com regras de aporte mínimo e rentabilidade. |
| `dividas_e_parcelamentos.csv` | CSV | **Radar de Compromissos.** Mapeia parcelas futuras para impedir que o usuário gaste dinheiro que já está comprometido. |

### 2. O Playbook (Módulo Comercial)

| Arquivo | Formato | Função no Agente |
|---------|---------|------------------|
| `objecoes_e_respostas.json` | JSON | **Cérebro de Vendas.** Contém scripts, gatilhos mentais e técnicas de contorno de objeções (ex: "Tá caro", "Vou pensar"). |
| `historico_posts_analytics.csv` | CSV | **Inteligência de Marketing.** Histórico de posts com dados de engajamento vs. conversão, usado para sugerir melhorias na estratégia de conteúdo. |

---

## Estrutura e Enriquecimento dos Dados

Para suportar as decisões complexas do "Gerente Geral", os dados foram estruturados com campos específicos:

### A. Dados Financeiros (Foco em Compliance)
O arquivo `transacoes.csv` possui colunas estratégicas para detectar a saúde do negócio:
* `origem_recurso`: Identifica se o pagamento saiu da conta **PF** ou **PJ**.
* `centro_custo`: Categoriza o gasto (ex: "Marketing", "Vida Pessoal").
* `dedutivel`: Flag para planejamento fiscal simples.

### B. Dados Comerciais (Foco em Conversão)
O arquivo `objecoes_e_respostas.json` não é apenas texto, ele possui lógica de aplicação:
* `gatilho`: A palavra-chave que o cliente diz (ex: "desconto").
* `fase`: Em qual etapa do funil isso ocorre (ex: "Negociação").
* `regra`: A instrução de ouro por trás do script (ex: "Nunca dar desconto sem pedir algo em troca").

---

## Estratégia de Integração (RAG Seletivo)

Para economizar tokens e manter o agente focado, utilizamos uma estratégia de **Injeção de Contexto Dinâmica**:

1.  **Carregamento Inicial:** Ao iniciar, o Python carrega todos os CSVs e JSONs para a memória RAM (DataFrames e Dictionaries).
2.  **Pré-Processamento:**
    * *Financeiro:* O script calcula saldo atual, total de entradas/saídas e filtra produtos que o cliente pode pagar (Filtro de Aporte Mínimo).
    * *Vendas:* O script indexa os gatilhos para busca rápida.
3.  **Montagem do Prompt:** O System Prompt recebe apenas o resumo processado, não os arquivos brutos inteiros.

---

## Exemplo de Contexto Injetado

Abaixo, um exemplo de como o "Cérebro" do agente enxerga os dados em tempo real:

```text
--- CONTEXTO ATUAL DA AGÊNCIA ---

[MÓDULO CFO - STATUS: ATIVO]
- Saldo Disponível: R$ 5.200,00 (ATENÇÃO: R$ 1.500 já comprometidos com dívidas futuras)
- Mistura PF/PJ Detectada: 2 ocorrências este mês.
- Oportunidade de Investimento: Cliente tem saldo para "LCI 90 Dias" (Mínimo R$ 5k).

[MÓDULO ESTRATEGISTA - STATUS: ATIVO]
- Scripts Carregados: 15 técnicas (Ancoragem, Escassez, Prova Social).
- Top Post da Semana: "Erros de Gestão" (Alta Conversão).
- Recomendação do Dia: Usar o saldo parado para tráfego pago no post "Erros de Gestão".

INSTRUÇÃO: Atue com base nesses dois pilares para orientar o usuário.