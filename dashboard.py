import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dashboard Hotel", layout="wide")

st.title("Dashboard - Hotel RAITeis")

if not os.path.exists("clientes.csv"):
    st.error("Arquivo clientes.csv não encontrado!")
    st.stop()

if not os.path.exists("reservas.csv"):
    st.error("Arquivo reservas.csv não encontrado!")
    st.stop()

clientes = pd.read_csv("clientes.csv")
reservas = pd.read_csv("reservas.csv")

clientes["cpf"] = clientes["cpf"].astype(str).str.replace(r"\D", "", regex=True)
reservas["cpfcliente"] = reservas["cpfcliente"].astype(str).str.replace(r"\D", "", regex=True)

df = reservas.merge(clientes, left_on="cpfcliente", right_on="cpf")

df = df.rename(columns={
    "status_x": "status_reserva",
    "status_y": "status_cliente"
})

col1, col2, col3 = st.columns(3)

col1.metric("Total de Clientes", len(clientes))
col2.metric("Total de Reservas", len(reservas))
col3.metric("Faturamento Total", f"R$ {df['valor_pagar'].sum():.2f}")

st.sidebar.title("Filtros")

cidade = st.sidebar.selectbox(
    "Filtrar por cidade",
    ["Todas"] + sorted(df["cidade"].dropna().unique())
)

if cidade != "Todas":
    df = df[df["cidade"] == cidade]

st.subheader("Reservas por Cidade")
st.bar_chart(df["cidade"].value_counts())

st.subheader("Faturamento por Cliente")
top_clientes = df.groupby("nome")["valor_pagar"].sum().sort_values(ascending=False)
st.bar_chart(top_clientes)

st.subheader("Status das Reservas")
st.bar_chart(df["status_reserva"].value_counts())

st.subheader(" Top 20 Clientes")

tabela = df.groupby("nome").agg({
    "valor_pagar": "sum",
    "diarias": "sum"
}).sort_values(by="valor_pagar", ascending=False).head(20)

st.dataframe(tabela)


#PARA RODAR O DASHBOARD, ABRA "raiteis-grupo-3" no vs code, 
# crie um novo terminal (ctrl + shift +´)
# e digite "python -m streamlit run dashboard.py"
