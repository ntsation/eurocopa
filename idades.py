import streamlit as st
import plotly.express as px
import main


st.title('Distribuição de Idade')

# Calculando a distribuição de idade
idade_distribuicao = main.df['Age'].value_counts().sort_index().reset_index()
idade_distribuicao.columns = ['Idade', 'Número de Jogadores']


fig = px.bar(idade_distribuicao, x='Idade', y='Número de Jogadores', title='Distribuição de Idade')
st.plotly_chart(fig)
