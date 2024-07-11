import streamlit as st
import plotly.express as px
import main

st.title('Altura Média dos Jogadores')

fig = px.box(main.df, x="Position", y="Height", title='Altura Média por Posição')

st.plotly_chart(fig)
