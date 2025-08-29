import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import limpar_e_converter

st.set_page_config(
    page_title="LEPTO ",
    layout="wide",
    initial_sidebar_state="expanded")

st.markdown("""
    <style>
    /* Fundo do sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.4);
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
        background-color: rgba(59, 130, 246, 0.4);
        color: green;
    }
    </style>
""", unsafe_allow_html=True)

st.logo('image/nova10.png')
st.title('Resumo das OT-NR')
st.divider()

if 'df_carregado' in st.session_state:
    df = st.session_state['df_carregado']
    ot = df[df['Tipologia do Título'] =='OT-NR']
    

    ot['Variação (%)'] = limpar_e_converter(ot['Variação (%)'])
    ot['Quantidade'] = limpar_e_converter(ot['Quantidade'])
    ot['Montante'] = limpar_e_converter(ot['Montante'])
    ot['N° de Negócios'] = limpar_e_converter(ot['N° de Negócios'])
  
    col1,col2, =st.columns(2)
    with col1: 

        fig5=px.bar(ot,x="Montante",y="Valor Mobiliário",text="Montante",color="Valor Mobiliário",title=" Montante Movimentado por Titulo",orientation="h",color_discrete_sequence=['rgba(59, 130, 246, 0.4)','#3C3C3D','#007AFF','#E82127',"rgba(34, 197, 94, 0.4)"])
        st.plotly_chart(fig5) 
        maior_quantidade =ot["Quantidade"].max()
        nome_maior_quantidade=ot[ot["Quantidade"] >= maior_quantidade]
        ler_o_maior_quantidade = nome_maior_quantidade["Valor Mobiliário"].tolist() 
        ver =(','.join(ler_o_maior_quantidade))  
        
        mensangem =f"""
        <div style='
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 60px;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
            border: 1px solid rgba(59, 130, 246, 0.4);
            color: white;
            font-family: 'Noto Sans', sans-serif;
            margin-top:500px;'
        >
        <h3 style='margin-bottom:;color:rgba(59, 130, 246, 0.4);'>Quantidade Total Transacionada por Título</h3>

        <p> Este gráfico revela o volume de papéis movimentados por título, somando todas as compras e vendas realizadas no período.</p> 
        <p> Ele mostra quais ativos foram mais negociados em unidades, indicando o nível de atividade e interesse de mercado por cada um </p>
        <p> <strong>{ver}</strong> lidera em volume transacionado, sendo o título com maior movimentação em quantidade, o que pode refletir alta liquidez ou forte interesse dos investidores.</p>
        </div> 

        """
        st.markdown(mensangem, unsafe_allow_html=True) 

        fig = px.bar(ot,x='Valor Mobiliário',y='Variação (%)', title='Análise de Variação de Preço',color='Valor Mobiliário',color_discrete_sequence=['rgba(59, 130, 246, 0.4)','#3C3C3D','#007AFF','#E82127',"rgba(34, 197, 94, 0.4)"])
        st.plotly_chart(fig)

        maior_volume =ot["N° de Negócios"].max()
        nome_maior_volume =ot[ot["N° de Negócios"] == maior_volume]
        ler_o_maior_volume = nome_maior_volume["Valor Mobiliário"].tolist()
        ver1 = (','.join(ler_o_maior_volume))

        mensangem =f"""
        <div style='
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20%;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
            border: 1px solid rgba(59, 130, 246, 0.4);
            color: white;
            font-family: 'Noto Sans', sans-serif;'
        >
        <h3 style='margin-bottom:;color:rgba(59, 130, 246, 0.4);'> Volume de Negócios por Título </h3>

        <p>Este gráfico de barras apresenta o número total de negócios realizados para cada título. Cada barra representa quantas vezes aquele ativo foi negociado, independentemente do valor ou quantidade.</p> 
        <p> Títulos com barras mais altas foram mais frequentemente negociados, indicando maior atividade e liquidez diária.</p>
        <p> No período analisado, {ver1} liderou em volume de negócios, mostrando forte presença no mercado.
        </div> 

        """
        st.markdown(mensangem, unsafe_allow_html=True)
        st.divider()


       

    with col2:
        maior_montante =ot['Montante'].max()
        nome_maior_montante =ot[ot['Montante'] == maior_montante]
        ler_o_maior_montante = nome_maior_montante['Valor Mobiliário'].tolist()
        ver2 = (','.join(ler_o_maior_montante))

        mensangem =f"""
        <div style='
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
            border: 1px solid rgba(59, 130, 246, 0.4);
            color: white;
            font-family: 'Noto Sans', sans-serif;'
        >
        <h3 style='margin-bottom:;color:rgba(59, 130, 246, 0.4);'>Montante Movimentado por Título </h3>

        <p>Este gráfico mostra <strong> quanto foi movimentado em dinheiro por cada título, </strong> somando compras e vendas.  </p> 
        <p>Cada barra representa um título e o <strong> valor total que passou por ele.</strong>Assim ,é possivel ver <strong> quais ativos tiveram mais movimentação financeira </strong> no periodo analisado </p> 
        <p><strong>Maior Movimentação:<strong style='color:rgba(59, 130, 246, 0.4);'>{ver2} </strong> </strong> com <strong style='color:rgba(59, 130, 246, 0.4);'>{maior_montante} KZ.</strong> </p>
        <p>isso indica que a <strong style ="color:rgba(59, 130, 246, 0.4);">{ver2}</strong> foi o título com maior volume financeiro movimentado neste período </p>
        </div> 

        """
        st.markdown(mensangem, unsafe_allow_html=True)
        st.divider()

        cores=['rgba(59, 130, 246, 0.4)','#3C3C3D','#007AFF','#E82127',"rgba(34, 197, 94, 0.4)"]
        fig2 = px.pie(ot,names='Valor Mobiliário', values='Quantidade',hole=0.7,title='Quantidade Total Transacionada por Título',color_discrete_sequence=cores)  
        st.plotly_chart(fig2)

        variacao_max =ot[ot['Variação (%)'] == ot['Variação (%)'].max()]
        variacao_min =ot[ot['Variação (%)'] == ot['Variação (%)'].min()]
        varlista = variacao_max['Valor Mobiliário'].tolist()
        varlista1 = variacao_min['Valor Mobiliário'].tolist()
        ver3 = (','.join(varlista))
        ver6 = (','.join(varlista1))

        mensangem =f"""
        <div style='
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
            border: 1px solid rgba(59, 130, 246, 0.4);
            color: white;
            font-family: 'Noto Sans', sans-serif;'
        >
        <h3 style='margin-bottom:;color:rgba(59, 130, 246, 0.4);'>Análise de Variação de Preço </h3>

        <p>Este gráfico de barras mostra a variação de preço dos títulos no período analisado. Títulos com barras acima de 0 tiveram valorização, enquanto os que estão abaixo de 0 sofreram desvalorização.</p>
        <p> Mais valorizado:<strong>{ver3}</strong></p>
        <p> Menos Valorizado:<trong>{ver6}</strong></p>  
        <p> Esses destaques indicam, respectivamente, o título com melhor desempenho e o que teve pior performance no período.</p>
        </div> 

        """
        st.markdown(mensangem, unsafe_allow_html=True)

        fig5=px.bar(ot,x="N° de Negócios",y="Valor Mobiliário",text="N° de Negócios",color="Valor Mobiliário",title=" Volume de Negócios por Título",orientation="h",color_discrete_sequence=['rgba(59, 130, 246, 0.4)','#3C3C3D','#007AFF','#E82127',"rgba(34, 197, 94, 0.4)"])
        st.plotly_chart(fig5)
        st.divider()
 
 
    comprar =ot[  
        (ot["N° de Negócios"] >= ot["N° de Negócios"].max())& 
        (ot["Quantidade"] >=ot["Quantidade"].max())&
        (ot["Montante"] >=ot["Montante"].max())]    
    ler_comprar = comprar["Valor Mobiliário"].tolist()
    ver4 = (','.join(ler_comprar))
    mensangem =f"""
        
        <h2 style='margin-bottom:;color:rgba(59, 130, 246, 0.4);'>Destaque </h2>

        <p>Após analisar os dados de montante movimentado, quantidade transacionada e variação de preço, o ativo <strong>{ver4}</strong> se destacou em todos os indicadores </p> 
        <p><strong>{ver4}</strong>  demonstrou forte liquidez, alta demanda e desempenho positivo, sendo o título mais relevante no mercado analisado.  Esse conjunto de fatores pode indicar confiança dos investidores e boa performance no período.</p>
       

        """
    st.markdown(mensangem, unsafe_allow_html=True) 

    mensangem =f"""
        <div style='
            border-radius: 15px;
            padding: 10px;
            margin-left:50px;
            margin-right:50px;
            margin-bottom: 20%;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
            border: 1px solid rgba(59, 130, 246, 0.4);
            color: white;
            font-family: 'Noto Sans', sans-serif;'
        >
        <h3 style='margin-bottom:;color:rgba(59, 130, 246, 0.4);'> {ver4} </h3>

        <p><strong>Montande</strong>:<strong style="color:rgba(59, 130, 246, 0.4);">{maior_montante} kz</strong>    .O {ver4} tem a maior um montante movimentado supeior a media </p>
        <p><strong>Quantidade</strong>:</strong><strong  style="color:rgba(59, 130, 246, 0.4);">{maior_quantidade} </strong>     .O {ver4} tem a maior uma quantia transacionada  supeior a media</p>
        <p><strong>Numero de Negocios</strong>:</strong><strong  style="color:rgba(59, 130, 246, 0.4);">{maior_volume:,.0f} </strong>    .O {ver4} tem a maior o volume de Negocios supeior a media</p>
        </p> 
        </div> 

        """
    st.markdown(mensangem, unsafe_allow_html=True)

  