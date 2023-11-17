import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    layout="wide",
    page_title="FIFA23"
)

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] >= 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

# Sidebar
st.sidebar.markdown("Desenvolvido por [Kanydian Esteves](https://www.linkedin.com/in/kanydian-esteves-07b0531a7/)")

# Body
st.title("FIFA23 OFICIAL DATASET")

st.markdown(
    """
    ## Contexto
    O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes de contratos e afiliações de clubes. Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados ​​em explorar vários aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento do jogador ao longo do tempo.
    """
)

st.markdown(
    """
    ## Colunas
    - **ID**: Um identificador exclusivo para cada jogador.
    - **Nome**: O nome do jogador.
    - **Idade**: A idade do jogador no momento da coleta de dados.
    - **Foto**: Um link ou referência à fotografia do jogador.
    - **Nacionalidade**: A nacionalidade do jogador.
    - **Bandeira**: A bandeira nacional associada à nacionalidade do jogador.
    - **Geral**: A classificação geral das habilidades e habilidades do jogador.
    - **Potencial**: A classificação potencial que representa o desenvolvimento futuro do jogador.
    - **Clube**: A afiliação atual do clube do jogador.
    - **Logotipo do clube**: Um link ou referência ao logotipo do clube do jogador.
    - **Valor (£)**: O valor de mercado estimado do jogador em libras (£).
    - **Salário (£)**: O salário semanal do jogador em libras (£).
    - **Especial**: Um valor numérico que representa as habilidades especiais do jogador.
    - **Pé Preferido**: O pé preferido do jogador para jogar.
    - **Reputação Internacional**: Uma classificação que indica a reputação internacional do jogador.
    - **Pé Fraco**: Uma classificação que representa as habilidades do pé mais fraco do jogador.
    - **Movimentos de Habilidade**: O número de movimentos de habilidade que o jogador possui.
    - **Taxa de trabalho**: A taxa de trabalho do jogador.
    - **Tipo de corpo**: A constituição física ou tipo de corpo do jogador.
    - **Rosto Real**: Indica se o jogador possui uma representação de rosto real.
    - **Posição**: A posição de jogo preferida do jogador.
    - **Ingressado**: A data em que o jogador ingressou no clube atual.
    - **Emprestado de**: O clube do qual o jogador está atualmente emprestado.
    - **Contrato válido até**: A data até a qual o contrato do jogador é válido.
    - **Altura (cm.)**: A altura do jogador em centímetros.
    - **Peso (lbs.)**: O peso do jogador em libras.
    - **Cláusula de rescisão (£)**: O valor da cláusula de rescisão do jogador em libras (£).
    - **Número do Kit**: O número do kit do jogador.
    - **Melhor Classificação Geral**: A classificação geral mais alta do jogador.
    - **Ano de ingresso**: O ano em que o jogador ingressou no clube atual.
    """
)

st.link_button("Acesso os dados no Keggle", "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")



