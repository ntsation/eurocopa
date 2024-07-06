import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('euro2024_players.csv')

# Calculando a distribuição de idade
idade_distribuicao = df['Age'].value_counts().sort_index().reset_index()
idade_distribuicao.columns = ['Idade', 'Número de Jogadores']

st.title('Distribuição de Idade')

tipo_grafico = st.selectbox('Selecione o tipo de gráfico', ['Barra', 'Linha'])

if tipo_grafico == 'Barra':
    fig = px.bar(idade_distribuicao, x='Idade', y='Número de Jogadores', title='Distribuição de Idade')
else:
    fig = px.line(idade_distribuicao, x='Idade', y='Número de Jogadores', title='Distribuição de Idade')

st.plotly_chart(fig)
