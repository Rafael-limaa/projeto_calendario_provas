import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl as xl

st.set_page_config(page_title="Student Habits", layout="wide")

st.markdown("## Calendário de Prova 2025.1")

st.write("aqui a ideia é deixa o maior semelhante possível com uma tabela de excel, poderia até ter uma tela com curso")

st.write("é possível adicinar linhas, excluir, exportar, editar, filtrar, ocultar colunas etc.")

file_path = ("Calendário.xlsx")
sheet = 'Planilha1'



if 'data' not in st.session_state:
    df = pd.read_excel(file_path, sheet_name=sheet)
    st.session_state.data = df.copy()

#df['DATAS DASAVALIAÇÕES'] = pd.to_datetime(df['DATAS DASAVALIAÇÕES'], errors='coerce').dt.strftime('%d/%m/%Y')
#df['RECEBIDA EM'] = pd.to_datetime(df['RECEBIDA EM'], errors='coerce').dt.strftime('%d/%m/%Y')


df_editado = st.data_editor(st.session_state.data, 
                            num_rows="dynamic",
                            use_container_width=True,
                            height=600)

if df_editado is not None:
    st.session_state.data = df_editado

if st.button("SALVAR"):
    st.session_state.data.to_excel(file_path, sheet_name=sheet, index=False)
    st.success("Alterações Salvas")
    



