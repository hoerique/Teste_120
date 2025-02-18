import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard de Tráfego Pago", layout="wide")

st.title("📊 Dashboard de Tráfego Pago - Meta Ads")

# URL do arquivo CSV no formato raw do GitHub
url = "https://raw.githubusercontent.com/hoerique/Teste_120/main/campanhas_Meta_ads.csv"

# Carregar os dados com pandas
df = pd.read_csv(url)

# Calcular totais
totais = {
    "Total impressões": df["impressões"].sum(),
    "Total cliques": df["cliques"].sum(),
    "Total CTR": df["CTR"].mean(),
    "Total investimento": df["investimento"].sum(),
    "Total CPC": df["CPC"].mean(),
    "Total CPM": df["CPM"].mean()
}

# Exibir os KPIs dentro de um contêiner
with st.container():
    st.subheader("🔹 Total Calculados")

col1, col2, col3, col4, col5, col6 = st.columns(6)

# Criar uma função para formatar os números com CSS reduzindo o tamanho da fonte
def format_metric(label, value):
    return f"""
    <div style="text-align: center;">
        <p style="font-size:12px; font-weight:bold; margin-bottom: 2px;">{label}</p>
        <p style="font-size:18px; font-weight:bold; color:#333;">{value}</p>
    </div>
    """

col1.markdown(format_metric("📢 Impressões", f"{totais['Total impressões']:,}"), unsafe_allow_html=True)
col2.markdown(format_metric("📊 Cliques", f"{totais['Total cliques']:,}"), unsafe_allow_html=True)
col3.markdown(format_metric("📈 CTR Médio", f"{totais['Total CTR']:.2f}%"), unsafe_allow_html=True)
col4.markdown(format_metric("💰 Investimento", f"R$ {totais['Total investimento']:,.2f}"), unsafe_allow_html=True)
col5.markdown(format_metric("⚡ CPC Médio", f"R$ {totais['Total CPC']:.2f}"), unsafe_allow_html=True)
col6.markdown(format_metric("📉 CPM Médio", f"R$ {totais['Total CPM']:.2f}"), unsafe_allow_html=True)

##Criativos com Maior Investimento e Impressões
# Ordenar pelo maior investimento e selecionar o top 5
top5 = df.nlargest(5, "investimento")

# Criar o gráfico de barras empilhadas
fig = go.Figure()

# Adicionar barras para Investimento
fig.add_trace(go.Bar(
    y=top5["nome_campanha"],
    x=top5["investimento"],
    name="Investimento",
    marker_color="blue",
    text=top5["investimento"],
    textposition="inside",
    orientation="h"
))

# Adicionar barras para Impressões
fig.add_trace(go.Bar(
    y=top5["nome_campanha"],
    x=top5["impressões"],
    name="Impressões",
    marker_color="orange",
    text=top5["impressões"],
    textposition="inside",
    orientation="h"
))

# Ajustar layout
fig.update_layout(
    title="Criativos com Maior Investimento e Impressões",
    xaxis_title="Valores",
    yaxis_title="Criativos",
    barmode="group",  # As barras ficam uma abaixo da outra
    height=450,
    legend_title="Métricas"
)

# Exibir no Streamlit
st.plotly_chart(fig, use_container_width=True)


