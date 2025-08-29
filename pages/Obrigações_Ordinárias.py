import streamlit as st
import pandas as od
import plotly.express as px
import base64


st.set_page_config(
    page_title="LEPTO ",
    layout="wide",
    initial_sidebar_state="expanded"
)
def set_bg_from_local(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-color: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(30px);
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position:center;
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_from_local("image/leptoverde.png")   
st.markdown("""
    <style>
    /* Fundo do sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
        box-shadow: 0 4px 20px rgba(34, 197, 94, 0.4);
     
    }

    /* Texto dos links do menu */
    section[data-testid="stSidebar"] a {
        color: white;
        text-decoration: none;
        padding: 10px 15px;
        display: block;
        border-radius: 5px;
        transition: 0.3s ease;
    }

    /* Hover nos links */
    section[data-testid="stSidebar"] a:hover {
        background-color: rgba(34, 197, 94, 0.4);
        color: #f7931a;
    }
    </style>
""", unsafe_allow_html=True)

if 'df_carregado' in st.session_state:
    df = st.session_state['df_carregado']
    obrigacoes = df[df['Tipologia do Título'] == 'Obrigações Ordinárias']
    st.dataframe(obrigacoes)
