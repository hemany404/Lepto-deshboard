import streamlit as st
import pandas as pd
import plotly.express as px
import base64

st.set_page_config(
    page_title="LEPTO ",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon = ""
)


st.logo('image/nova10.png')

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

carregar_ficheiro = st.file_uploader('Coloca o arquivo excell do Resumo de Mercado da BODIVA',type=['xlsx'])
if carregar_ficheiro:
    df =pd.read_excel(carregar_ficheiro)
    st.session_state['df_carregado'] =df

st.markdown("""
    <style>
    /* Fundo do sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
        box-shadow: 0 4px 20px rgba(249, 147, 26, 0.3);
    }

    /* Texto dos links do menu */
    section[data-testid="stSidebar"] a{
        color: white;
        text-decoration: none;
        padding: 10px 15px;
        display: block;
        border-radius: 5px;
        transition: 0.3s ease;
    }

    /* Hover nos links */
    section[data-testid="stSidebar"] a:hover {
        background-color: rgba(249, 147, 26, 0.3);
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)


set_bg_from_local("image/leptoouro.png")