import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

with st.sidebar:
    st.title('Análise de lucro')
    uploaded_file = st.file_uploader('Adicione seu arquivo aqui:')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    with st.sidebar:
        regiao_especifica = df['Region'].unique().tolist()

        regiao_selecionada = st.selectbox('Região específica:', regiao_especifica)
        vendedor_selecionado = st.radio('Vendedor', ['H', 'C', 'M', 'L'], index=None)

        if regiao_selecionada:
            df = df[df['Region'] == regiao_selecionada]

        if vendedor_selecionado:
            df = df[df['Order Priority'] == vendedor_selecionado]


    st.write('Lucro por tipo de item:')