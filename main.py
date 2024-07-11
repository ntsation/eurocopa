import streamlit as st
import pandas as pd

df = pd.read_csv('src/euro2024_players.csv')


def pages():
    st.title("Paginas")


pg = st.navigation([
    st.Page("idades.py", title="Distribuição de idade"),
    st.Page("altura.py", title="Altura media dos jogadores"),
    st.Page("pe_dominante.py", title="Pe dominante dos jogadores"),
])
pg.run()
