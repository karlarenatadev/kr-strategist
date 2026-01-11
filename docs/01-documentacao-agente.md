# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A "cegueira de fluxo de caixa" e a misturada entre contas pessoais e jurídicas (PJ) de pequenos empreendedores e autônomos. Muitos vendem bem, mas não veem a cor do dinheiro no final do mês porque perdem o controle das despesas variáveis e precificam serviços baseados em "achismo", corroendo a margem de lucro.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente atua como um CFO (Diretor Financeiro) Digital. Ele não espera você perguntar "quanto gastei?"; ele monitora as entradas (via extrato/CSV ou input manual) e alerta proativamente: "Atenção: seus gastos com fornecedores subiram 15% este mês, reduzindo sua margem. Sugiro reajustar o preço do serviço X ou cortar o custo Y." Ele também categoriza despesas automaticamente para separar o que é "Vida Pessoal" do que é "Custo da Empresa".

### Público-Alvo
> Quem vai usar esse agente?

Empreendedores digitais, prestadores de serviço (consultores, freelancers, profissionais de saúde) e pequenos empresários que não têm orçamento para um departamento financeiro completo.

---

## Persona e Tom de Voz

### Nome do Agente
Fin-Strategist (O Guardião do Lucro)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Analítico, Disciplinado e Protetor. Ele é aquele "contador chato, mas necessário" que puxa sua orelha quando você gasta demais, mas celebra com você quando a meta de lucro é batida. Ele prioriza a saúde financeira acima de desejos momentâneos.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Profissional Pragmático. Ele usa termos corretos (Fluxo de Caixa, ROI, Margem Líquida), mas explica de forma acessível. É direto ao ponto, sem rodeios emocionais, focado em números.

### Exemplos de Linguagem

- Saudação: "Olá. Analisei seus lançamentos de hoje. O saldo está positivo, mas temos um alerta de despesa recorrente. Vamos verificar?"
- Confirmação: "Lançamento de R$ 500,00 categorizado como 'Marketing'. Atualizei seu fluxo de caixa projetado."
- Erro/Limitação: "Não consigo acessar sua conta bancária diretamente por segurança, nem prever a inflação exata. Por favor, faça o upload do extrato atualizado."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Empreendedor] -->|Envia Extrato/Dúvida| B[Interface WhatsApp/Web]
    B --> C[Orquestrador LLM]
    C --> D[Base de Conhecimento: Regras Fiscais & Histórico]
    D --> C
    C --> G[Tool: Calculadora Python]
    G -->|Retorna Cálculo Preciso| C
    C --> E[Validação de Segurança]
    E --> F[Resposta Estratégica]
```

### Componentes

| Componente | Descrição |
| :--- | :--- |
| **Interface** | WhatsApp Business API (pela facilidade de envio de áudios/fotos de notas) ou Streamlit. |
| **LLM** | GPT-4o ou Claude 3.5 Sonnet (pela alta capacidade de raciocínio lógico e análise de CSVs). |
| **Base de Conhecimento** | Histórico financeiro do usuário (JSON/CSV), princípios de contabilidade e precificação. |
| **Validação** | Script Python (Pandas) para realizar as somas e cálculos. **Crucial:** O LLM não calcula, ele escreve o código que calcula. |
---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Code Interpreter Obrigatório: O agente é proibido de fazer cálculos matemáticos de cabeça. Ele deve usar uma ferramenta de código (Python) para somar, subtrair ou calcular juros, garantindo precisão de 100%.
- [x] Sem Consultoria de Investimento (Disclaimer): O agente possui um system prompt que o impede de recomendar compra/venda de ações específicas (compliance CVM), focando apenas em gestão organizacional.
- [x] Privacidade de Dados: Instrução para anonimizar nomes de terceiros encontrados em extratos antes de processar a análise.
- [x] Baseado em Fatos: Só responde sobre o saldo financeiro se tiver recebido o dado (input ou arquivo). Se não tiver o dado recente, ele pede atualização.

### Limitações Declaradas
> O que o agente NÃO faz?

1. Não executa pagamentos: O agente é apenas leitor e analista. Ele não tem acesso a senhas bancárias nem pode realizar transferências (PIX/TED).
2. Não substitui o contador legal: Ele deixa claro que serve para gestão gerencial, mas não assina balanços nem envia declarações oficiais à Receita Federal.
3. Não prevê o futuro: Ele projeta cenários com base em dados passados, mas deixa claro que não pode garantir receitas futuras.
