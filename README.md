# 🏦 KR-Strategist: O Gerente Geral com IA

> **"Protegendo seu caixa enquanto alavanca suas vendas."**

O **KR-Strategist** é um agente de Inteligência Artificial Híbrido projetado para resolver a maior dor do pequeno empreendedor: a necessidade de ser **Diretor Financeiro (CFO)** e **Diretor Comercial** ao mesmo tempo.

Diferente de chatbots comuns, ele possui uma **dupla personalidade profissional** que alterna automaticamente baseada na intenção do usuário e na saúde do caixa.

🌐 **[Acesse o projeto rodando ao vivo na nuvem aqui!](https://kr-strategist.streamlit.app/)**

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
    * Quebra de Objeções (ex: "Tá caro", "Vou pensar") consultando o Playbook (`objecoes_e_respostas.json`).
    * Auditoria de Conteúdo (Engajamento vs. Conversão).

---

## ⚡ Radar de Oportunidades (O Diferencial)

O KR-Strategist conecta os dois mundos. Ele analisa o saldo do cliente e sugere a melhor ação comercial:

> *“Se o cliente tem R$ 5.000 parados (Dados Financeiros), o agente sugere ofertar o LCI de Liquidez Diária usando o Gatilho da Segurança (Dados de Vendas).”*

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Interface e Deploy:** Streamlit Community Cloud
* **Manipulação de Dados:** Pandas
* **Inteligência Artificial:** Llama 3 (via Groq API)

---

## 📂 Estrutura do Projeto

```text
kr-strategist/
│
├── data/                          # O Cérebro do Agente
│   ├── transacoes.csv             # Extrato Bancário (Modelo)
│   ├── produtos_financeiros.json  # Catálogo de Investimentos
│   ├── objecoes_e_respostas.json  # Scripts de Vendas (O Playbook)
│   └── historico_posts.csv        # Analytics de Marketing
│
├── docs/                          # Documentação da Regra de Negócio
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── app.py                         # Aplicação Principal (Cockpit do Gerente)
├── requirements.txt               # Dependências do Projeto
└── README.md                      # Este arquivo
```

---

## 🚀 Como Rodar o Projeto Localmente

1.Clone o repositório:

```Bash
git clone [https://github.com/seu-usuario/kr-strategist.git](https://github.com/seu-usuario/kr-strategist.git)
cd kr-strategist
```

2.Instale as dependências:

```Bash
pip install -r requirements.txt
```

3.Configure a Chave da API (Groq):
Crie uma pasta oculta chamada `.streamlit` na raiz do projeto e dentro dela um arquivo `secrets.toml`:

```Ini, TOML
GROQ_API_KEY = "sua_chave_gratuita_aqui"
```

4.Execute a aplicação:

```Bash
streamlit run app.py
```

5.O painel abrirá automaticamente em `http://localhost:8501`.

---

## 📊 Métricas de Sucesso

O agente é avaliado por:

- **Rigor Financeiro**: Ele vetou compras quando o saldo era insuficiente?

- **Persuasão Comercial**: Ele usou o script de ancoragem correto quando o cliente pediu desconto?

- **Segurança e Anti-Alucinação**: Ele evitou ofertar produtos que não existem no catálogo ou que exigem aporte mínimo maior que o saldo?

---

## 📢 Pitch

"O KR-Strategist não apenas conta moedas; ele cria estratégias. Ele transforma 'eu-quipes' desorganizadas em empresas estruturadas, unindo a prudência de um banco com a agressividade de uma consultoria de vendas."

Desenvolvido por **Karla Renata**.