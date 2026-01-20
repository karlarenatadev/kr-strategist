import streamlit as st
import pandas as pd
import json
import os
from openai import OpenAI
from pandas.errors import EmptyDataError

# --- 1. CONFIGURAÇÃO DA AGÊNCIA ---
st.set_page_config(page_title="KR-Strategist Pro", page_icon="👔", layout="wide")

st.title("👔 KR-Strategist: Cockpit do Gerente")
st.markdown("*Análise de Crédito, Vendas e Recomendações em Tempo Real.*")

# --- 2. CARREGAMENTO INTELIGENTE (COM FILTRO DE PRODUTOS) ---
@st.cache_data
def carregar_dados_agencia():
    contexto = {}
    saldo_atual = 0.0
    produtos_disponiveis = []
    
    # A. DADOS DO CLIENTE (Transações)
    try:
        df = pd.read_csv('data/transacoes.csv')
        entradas = df[df['tipo']=='entrada']['valor'].sum()
        saidas = df[df['tipo']=='saida']['valor'].sum()
        saldo_atual = entradas - saidas
        contexto['financeiro'] = f"Saldo em Conta: R$ {saldo_atual:,.2f} | Movimentações: {len(df)}"
    except:
        contexto['financeiro'] = "Extrato do cliente não carregado."
        saldo_atual = 0.0

    # B. CATÁLOGO DE PRODUTOS
    try:
        with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
            todos_produtos = json.load(f)
            # FILTRO: Seleciona apenas o que o cliente PODE pagar
            produtos_disponiveis = [p for p in todos_produtos if p.get('aporte_minimo', 0) <= saldo_atual]
            
            contexto['produtos_elegiveis'] = json.dumps(produtos_disponiveis, indent=2, ensure_ascii=False)
            contexto['qtd_produtos'] = len(produtos_disponiveis)
    except:
        contexto['produtos_elegiveis'] = "[]"
        contexto['qtd_produtos'] = 0

    # C. PLAYBOOK DE VENDAS
    try:
        with open('data/objecoes_e_respostas.json', 'r', encoding='utf-8') as f:
            contexto['scripts'] = json.load(f)
    except:
        contexto['scripts'] = []
        
    return contexto, saldo_atual, produtos_disponiveis

dados, saldo_cliente, produtos_oferta = carregar_dados_agencia()

# --- 3. SIDEBAR (RADAR DE OPORTUNIDADES) ---
with st.sidebar:
    st.header("⚡ Radar do Cliente")
    
    # Mostra o dinheiro na mesa
    st.metric("Disponível para Investir", f"R$ {saldo_cliente:,.2f}")
    
    st.divider()
    
    # RECOMENDAÇÃO AUTOMÁTICA (Lógica Rápida)
    if produtos_oferta:
        # Pega o produto com maior rentabilidade (simulação simples) ou o último da lista filtrada
        produto_top = produtos_oferta[-1] # Assume que o JSON está ordenado ou pega um destaque
        
        st.subheader("🌟 Oportunidade do Dia")
        st.info(f"**{produto_top['nome']}**")
        st.caption(f"Rentabilidade: {produto_top['rentabilidade']}")
        st.caption(f"Argumento: {produto_top['indicado_para']}")
        
        st.success(f"🎯 {dados['qtd_produtos']} produtos encaixam neste saldo.")
    else:
        st.warning("Saldo insuficiente para produtos de investimento.")

    st.divider()
    api_key = st.text_input("OpenAI API Key", type="password")
    if not api_key:
        st.warning("Conecte a IA para gerar o pitch.")
        st.stop()
        
    client = OpenAI(api_key=api_key)

# --- 4. PROMPT DE VENDAS (FOCO EM FECHAMENTO RÁPIDO) ---
system_instruction = f"""
VOCÊ É O KR-STRATEGIST, O COPILOTO DO GERENTE DE CONTAS.

--- CENÁRIO ATUAL ---
O Gerente está atendendo um cliente com saldo de **R$ {saldo_cliente:,.2f}**.
Produtos que cabem no bolso dele agora: 
{dados['produtos_elegiveis']}

--- SUA MISSÃO ---
Ajudar o gerente a **fechar a aplicação** de forma rápida.

1. **Se o Gerente pedir "Recomendação":**
   - Escolha O MELHOR produto da lista acima (foco em rentabilidade e segurança).
   - Escreva um PITCH DE VENDAS curto (máx 3 linhas) para ele falar pro cliente.
   - Use gatilhos mentais (Escassez, Autoridade, Segurança).

2. **Se o Gerente pedir "Ajuda com Objeção":**
   - Use o conhecimento de vendas para quebrar a resistência do cliente.

FORMATO DE RESPOSTA:
Direto, persuasivo e pronto para falar (Speech).
"""

# --- 5. CHATBOT ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": system_instruction}]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# Sugestões rápidas de perguntas (Botões)
col1, col2 = st.columns(2)
if col1.button("🚀 Gerar Pitch Rápido"):
    prompt = f"Crie um argumento de venda infalível para aplicar os R$ {saldo_cliente} do cliente no melhor produto hoje."
else:
    prompt = st.chat_input("Ex: Cliente disse que prefere deixar na Poupança. O que eu falo?")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            stream=True
        )
        response = st.write_stream(stream)
    
    st.session_state.messages.append({"role": "assistant", "content": response})