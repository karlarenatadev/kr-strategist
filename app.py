import streamlit as st
import pandas as pd
import json
from openai import OpenAI

# --- 1. CONFIGURAÇÃO DA AGÊNCIA ---
st.set_page_config(page_title="KR-Strategist Pro", page_icon="👔", layout="wide")

st.title("👔 KR-Strategist: Cockpit do Gerente")
st.markdown("*Análise de Crédito, Vendas e Recomendações em Tempo Real.*")

# --- 2. CARREGAMENTO DOS DADOS ESTÁTICOS (JSON) ---
@st.cache_data
def carregar_playbook():
    try:
        with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
            todos_produtos = json.load(f)
    except:
        todos_produtos = []
        
    try:
        with open('data/objecoes_e_respostas.json', 'r', encoding='utf-8') as f:
            scripts = json.load(f)
    except:
        scripts = []
        
    return todos_produtos, scripts

todos_produtos, scripts = carregar_playbook()

# --- 3. PROCESSAMENTO DO EXTRATO DINÂMICO (CSV) ---
def processar_transacoes(ficheiro_csv, produtos):
    contexto = {}
    saldo_atual = 0.0
    produtos_disponiveis = []
    
    if ficheiro_csv is not None:
        try:
            df = pd.read_csv(ficheiro_csv)
            entradas = df[df['tipo']=='entrada']['valor'].sum()
            saidas = df[df['tipo']=='saida']['valor'].sum()
            saldo_atual = entradas - saidas
            contexto['financeiro'] = f"Saldo em Conta: R$ {saldo_atual:,.2f} | Movimentações: {len(df)}"
            
            # FILTRO: Seleciona apenas o que o cliente PODE pagar
            produtos_disponiveis = [p for p in produtos if p.get('aporte_minimo', 0) <= saldo_atual]
            contexto['produtos_elegiveis'] = json.dumps(produtos_disponiveis, indent=2, ensure_ascii=False)
            contexto['qtd_produtos'] = len(produtos_disponiveis)
        except Exception as e:
            st.error(f"Erro ao ler o CSV: {e}")
            contexto['financeiro'] = "Erro ao processar extrato."
    else:
        contexto['financeiro'] = "Aguardando carregamento do extrato..."
        contexto['produtos_elegiveis'] = "[]"
        contexto['qtd_produtos'] = 0
        
    return contexto, saldo_atual, produtos_disponiveis

# --- 4. PAINEL LATERAL (SIDEBAR) ---
with st.sidebar:
    st.header("⚙️ Configurações e Dados")
    
    # 🔴 NOVO: Carregamento dinâmico do ficheiro CSV
    ficheiro_transacoes = st.file_uploader("Carregue o Extrato (CSV)", type=["csv"])
    
    st.divider()
    st.header("⚡ Radar do Cliente")
    
    # Processa os dados com base no ficheiro carregado
    dados, saldo_cliente, produtos_oferta = processar_transacoes(ficheiro_transacoes, todos_produtos)
    
    st.metric("Disponível para Investir", f"R$ {saldo_cliente:,.2f}")
    
    st.divider()
    
    if produtos_oferta:
        produto_top = produtos_oferta[-1] 
        st.subheader("🌟 Oportunidade do Dia")
        st.info(f"**{produto_top['nome']}**")
        st.caption(f"Rentabilidade: {produto_top['rentabilidade']}")
        st.caption(f"Argumento: {produto_top['indicado_para']}")
        st.success(f"🎯 {dados['qtd_produtos']} produtos encaixam neste saldo.")
    else:
        st.warning("Saldo insuficiente ou extrato não carregado.")

    st.divider()

# --- 5. TRAVAS DE SEGURANÇA (Para UX na Nuvem) ---
try:
    # O Streamlit puxa a chave de forma invisível e segura
    api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=api_key)
except KeyError:
    st.error("Chave de API não encontrada nas configurações de segurança do Streamlit.")
    st.stop()

# --- 6. PROMPT E CHATBOT (Mantém-se igual ao original) ---
system_instruction = f"""
VOCÊ É O KR-STRATEGIST, O COPILOTO DO GERENTE DE CONTAS.

--- CENÁRIO ATUAL ---
O Gerente está a atender um cliente com saldo de **R$ {saldo_cliente:,.2f}**.
Produtos que cabem no bolso dele agora: 
{dados['produtos_elegiveis']}

--- A SUA MISSÃO ---
Ajudar o gerente a **fechar a aplicação** de forma rápida.

1. **Se o Gerente pedir "Recomendação":**
   - Escolha O MELHOR produto da lista acima.
   - Escreva um PITCH DE VENDAS curto (máx 3 linhas).
   - Use gatilhos mentais (Escassez, Autoridade, Segurança).

FORMATO DE RESPOSTA: Direto, persuasivo e pronto para falar (Speech).
"""

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": system_instruction}]

# Atualizar o contexto do sistema se o saldo/produtos mudarem
st.session_state.messages[0] = {"role": "system", "content": system_instruction}

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

col1, col2 = st.columns(2)
if col1.button("🚀 Gerar Pitch Rápido"):
    prompt = f"Crie um argumento de venda infalível para aplicar os R$ {saldo_cliente} do cliente no melhor produto hoje."
else:
    prompt = st.chat_input("Ex: O cliente disse que prefere deixar na Poupança. O que eu digo?")

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