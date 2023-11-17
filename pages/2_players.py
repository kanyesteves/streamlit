import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="FIFA23"
)

df = st.session_state["data"]

# Sidebar
clubes = df["Club"].unique()
club = st.sidebar.selectbox("Clubes", clubes)
df_players = df[df["Club"] == club]

players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador", players)
player_stats = df[df["Name"] == player].iloc[0]

st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")

# Body
st.image(player_stats["Photo"])
st.title(player_stats["Name"])
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3 = st.columns(3)

col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de recisão", value=f"£ {player_stats['Release Clause(£)']:,}")
