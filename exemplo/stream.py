import streamlit as st
import xlrd
import plotly.express as px
import pandas as pd


st.set_page_config(page_title="Cuidados", layout='wide', page_icon="🏠")

@st.cache_data
def carregar_dados(caminho_arquivo):
    xls = pd.ExcelFile(caminho_arquivo)

    abas_anos = [sheet for sheet in xls.sheet_names if "(CV)" not in sheet]

    dados_totais = []

    for ano in abas_anos:
        df_raw = pd.read_excel(xls, sheet_name=ano)

        start_idx = df_raw[df_raw.iloc[:, 0] == "Brasil"].index[0]

        df_ano = df_raw.iloc[start_idx:, [0,1,2,3]].copy()
        df_ano.columns = ["Localidade", 'Total', 'Homem', 'Mulher']

        df_ano = df_ano.dropna(subset=['Localidade'])
        df_ano - df_ano[df_ano['Localidade'].astype(str).str.strip() != '']

        for col in ['Total', 'Homem', 'Mulher']:
            df_ano[col] = pd.to_numeric(df_ano[col], errors='coerce')

        df_ano["Ano"] = str(ano)
        dados_totais.append(df_ano)

    df_completo = pd.concat(dados_totais, ignore_index=True)
    return df_completo

caminho_arquivo = r'H:\Python\exemplo\Tabela 1.1.2.xls'

try:
    df = carregar_dados(caminho_arquivo)

    st.sidebar.header("🔍 Filtros")

    anos_disponiveis = sorted(df["Ano"].unique(), reverse=True)
    ano_selecionado = st.sidebar.selectbox("Selecione o Ano:", anos_disponiveis)

    #Seleção de Localidades
    localidades_disponiveis = df['Localidade'].unique().tolist()
    localidades_selecionadas = st.sidebar.multiselect(
        'Selecione as Regiões/UFs',
        options=localidades_disponiveis,
        default=["Brasil", "Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]
    )

    #Corpo da aplicação
    st.title("📊 Horas Dedicadas a Cuidados e Afazeres Domésticos")
    st.markdown("Análise de média de horas semanais dedicadas por pessoas ocupadas de 14 anos ou mais, por sexo")

    #Filtrar Dataframe com base nas seleções
    df_filtrado = df[(df["Ano"] == ano_selecionado) & (df["Localidade"].isin(localidades_selecionadas))]

    if not df_filtrado.empty:
        
except:

