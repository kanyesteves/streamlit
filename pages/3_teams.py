import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="FIFA23"
)

df = st.session_state["data"]

# Sidebar
clubes = df["Club"].unique()
club = st.sidebar.selectbox("Clubes", clubes)
df_players = df[df["Club"] == club].set_index("Name")

st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")

# Body
st.image(df_players.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined",
           "Height(cm.)", "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_players[columns], 
             column_config={
                "Overall": st.column_config.ProgressColumn(
                    "Overall", format="%d", min_value=0, max_value=100
                ),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country")
             })
