"""Dashboard de população por estado (IBGE) com Streamlit + Plotly."""
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Brasil em Dados", page_icon="🇧🇷", layout="wide")


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv("data/populacao_uf.csv")


df = load_data()

st.title("🇧🇷 Brasil em Dados – População por Estado")
st.caption("Fonte: IBGE, Censo Demográfico 2022")

regioes = st.sidebar.multiselect("Região", sorted(df["regiao"].unique()), default=sorted(df["regiao"].unique()))
filtrado = df[df["regiao"].isin(regioes)].sort_values("populacao", ascending=False)

if filtrado.empty:
    st.warning("Selecione ao menos uma região.")
    st.stop()

c1, c2, c3 = st.columns(3)
c1.metric("População total", f"{filtrado['populacao'].sum():,.0f}".replace(",", "."))
c2.metric("Estado mais populoso", filtrado.iloc[0]["estado"])
c3.metric("Estados", len(filtrado))

col_a, col_b = st.columns([2, 1])
with col_a:
    fig = px.bar(filtrado, x="populacao", y="estado", color="regiao", orientation="h",
                 title="Ranking de população por estado")
    fig.update_layout(yaxis={"categoryorder": "total ascending"}, height=650)
    st.plotly_chart(fig, use_container_width=True)
with col_b:
    por_regiao = filtrado.groupby("regiao", as_index=False)["populacao"].sum()
    st.plotly_chart(px.pie(por_regiao, names="regiao", values="populacao", title="Participação por região"),
                    use_container_width=True)

st.subheader("Tabela")
st.dataframe(filtrado, use_container_width=True, hide_index=True)
st.download_button("⬇️ Baixar CSV", filtrado.to_csv(index=False), "populacao_filtrada.csv")
