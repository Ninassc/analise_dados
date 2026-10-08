import streamlit as st
import pandas as pd

st.set_page_config(page_title="Super", page_icon="🛒", layout="wide")

nome = st.text_input("Digite seu nome:")
st.markdown("_____________________________________________________________")

st.title(f"BEM-VINDO AO SUPERMERCADO **SUPER**, {nome}", icon="🛒", text_alignment="center")

if nome != "":
    st.balloons()
    
st.divider()

def carregar_dados():

    dados = {
        "id_produto": [101, 102, 103, 104, 105, 106],
        "nome_produto": [
            "Arroz 5kg",
            "Feijão Preto 1kg",
            "Leite Integral 1L",
            "Maçã Fuji (kg)",
            "Detergente 500ml",
            "Café Torrado 500g",
        ],
        "categoria": [
            "Mercearia",
            "Mercearia",
            "Laticínios",
            "Hortifrúti",
            "Limpeza",
            "Mercearia",
        ],
        "preco_unitario": [24.90, 7.50, 4.80, 8.99, 2.30, 16.50],
        "quantidade_estoque": [50, 80, 120, 45, 150, 60],
        "validade": [
            "2027-05-10",
            "2027-03-15",
            "2026-12-01",
            "2026-10-20",
            "2028-01-01",
            "2027-08-30",
        ],
    }

    df_supermercado = pd.DataFrame(dados)

    df_supermercado["valor_total_estoque"] = (
        df_supermercado["preco_unitario"] * df_supermercado["quantidade_estoque"]
    )
    
    return df_supermercado

df = carregar_dados()
st.dataframe(df)

st.divider()

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro Número", min_value=0.0, value=0.0, step=0.5)

with col2:
    num2 = st.number_input("Segundo Número", min_value=0.0, value=0.0, step=1.0)
    
operacao = st.selectbox(
    "Escolha a operação",
    ["Adição (+)", "Subtração (-)", "Multiplicação (x)", "Divisão (/)"]
)

if st.button("Calcular", type="primary"):
    resultado = None
    
    if operacao == "Adição (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (x)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        if num2 != 0:
            resultado = num1 / num2
        else:
            st.error(f"Erro: Divisão por zero não é permitida.")
    
    if resultado is not None:
        st.success(f"**Resultado:** {resultado}")
        
precos_itens = {
    "Arroz 5kg": 24.90,
    "Feijão Preto 1kg": 7.50,
    "Leite Integral 1L": 4.80,
    "Maçã Fuji (kg)": 8.99,
    "Detergente 500ml": 2.30,
    "Café Torrado 500g": 16.50,
}

def calcular_preco_total(itens_selecionados):
    total = sum(precos_itens[item] for item in itens_selecionados)
    return total

itens_selecionados = st.multiselect(
    label="Selecione os itens do supermercado",
    options=list(precos_itens.keys())
)

if itens_selecionados:
    st.subheader("Itens Selecionados:")
    for item in itens_selecionados:
        st.write(f"{item}")