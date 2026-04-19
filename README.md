# 🏦 KR-Strategist: O Gerente Geral com IA

> **"Protegendo seu caixa enquanto alavanca suas vendas."**

O **KR-Strategist** é um agente de Inteligência Artificial Híbrido projetado para resolver a maior dor do pequeno empreendedor: a necessidade de ser **Diretor Financeiro (CFO)** e **Diretor Comercial** ao mesmo tempo.

Diferente de chatbots comuns, ele possui uma **dupla personalidade profissional** que alterna automaticamente baseada na intenção do usuário e na saúde do caixa.

---

## 🧠 Como Funciona (A Dupla Personalidade)

O sistema opera com dois módulos integrados:

### 1. 🛡️ Modo CFO (Defensivo)

* **Objetivo:** Proteger o fluxo de caixa e garantir a sobrevivência do negócio.
* **Funcionalidades:**
    * Análise de Extrato Bancário (`transacoes.csv`).
    * Detecção de Mistura Patrimonial (Gastos PF na conta PJ).
    * Bloqueio de compras supérfluas se houver dívidas futuras (`dividas_e_parcelamentos.csv`).

### 2. 🚀 Modo Estrategista (Ofensivo)
* **Objetivo:** Gerar receita nova e fechar vendas.
* **Funcionalidades:**
    * Geração de Scripts de Vendas baseados em metodologia SPIN Selling.
    * Quebra de Objeções (ex: "Tá caro", "Vou pensar") consultando o Playbook (`objecoes.json`).
    * Auditoria de Conteúdo (Engajamento vs. Conversão).

---

## ⚡ Radar de Oportunidades (O Diferencial)

O KR-Strategist conecta os dois mundos. Ele analisa o saldo do cliente e sugere a melhor ação comercial:

> *“Se o cliente tem R$ 5.000 parados (Dados Financeiros), o agente sugere ofertar o LCI de Liquidez Diária usando o Gatilho da Segurança (Dados de Vendas).”*

---

## 📂 Estrutura do Projeto

```text
kr-strategist/
│
├── data/                          # O Cérebro do Agente
│   ├── transacoes.csv             # Extrato Bancário (O Cofre)
│   ├── produtos_financeiros.json  # Catálogo de Investimentos
│   ├── objecoes_e_respostas.json  # Scripts de Vendas (O Playbook)
│   └── historico_posts.csv        # Analytics de Marketing
│
├── docs/                          # Documentação do Desafio
│   ├── 01-documentacao-agente.md  # Visão Geral e Arquitetura
│   ├── 02-base-conhecimento.md    # Estrutura dos Dados
│   ├── 03-prompts.md              # Engenharia de Prompt (System Prompt)
│   ├── 04-metricas.md             # Testes e Validação
│   └── 05-pitch.md                # Roteiro de Apresentação
│
├── src/                           # Código Fonte
│   └── app.py                     # Aplicação Streamlit (Cockpit do Gerente)
│
└── README.md                      # Este arquivo

## 🛠️ Como Rodar o Projeto

**Pré-requisitos:** Python 3.10+ e uma chave da OpenAI.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/kr-strategist.git](https://github.com/seu-usuario/kr-strategist.git)
   cd kr-strategist

   ### Instale as dependências:

    ```bash
    pip install streamlit pandas openai

    ###Execute a aplicação: 

    ```bash
    streamlit run src/app.py

### Acesse no navegador:

O painel abrirá automaticamente em `http://localhost:8501`. Insira sua API Key na barra lateral para ativar a inteligência.

---

## 📊 Métricas de Sucesso

O agente é avaliado por:

* **Rigor Financeiro:** Ele vetou compras quando o saldo era insuficiente?
* **Persuasão Comercial:** Ele usou o script de ancoragem correto quando o cliente pediu desconto?
* **Segurança:** Ele evitou alucinar produtos que não existem no catálogo?

---

## 📢 Pitch

> "O KR-Strategist não apenas conta moedas; ele cria estratégias. Ele transforma 'eu-quipes' desorganizadas em empresas estruturadas, unindo a prudência de um banco com a agressividade de uma consultoria de vendas."

---

Desenvolvido por **Karla Renata** para o Desafio de IA Generativa.