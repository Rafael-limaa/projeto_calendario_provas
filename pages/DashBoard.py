import pandas as pd
import streamlit as st
import plotly.express as px


file_path = ("Calendario.xlsx")
df = pd.read_excel(file_path)


st.set_page_config(page_title="Student Habits", layout="wide")

st.markdown("A ideia seria aqui ter os indicadores relevantes e pop-up com os ofensoires e avisos de atrasos e possíveis atrasos")


st.dataframe(df.head())

qtd_provas = df.groupby('CURSO')['CÓDIGO'].count().reset_index()
fig_product = px.bar(qtd_provas, x='CURSO', y='CÓDIGO', title="Quantidade de Provas",
                         labels={'CURSO': 'CURSO', 'CÓDIGO': 'Quantidade'})
st.plotly_chart(fig_product, use_container_width=True)