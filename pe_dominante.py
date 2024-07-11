import streamlit as st
import plotly.express as px
import main


st.title('Pé Dominante dos Jogadores')

pe_dominante = main.df['Foot'].value_counts().reset_index()
fig = px.pie(pe_dominante, values='count', names='Foot', title='Pé Dominante dos Jogadores (Direito ou Esquerdo)')
st.plotly_chart(fig)
