import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import plotly.graph_objects as go

st.set_page_config(layout="wide")

title_style = """
<style>
.title-container {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
    font-size: 2.5rem;
    font-weight: bold;
    color: #000000; /* Colore blu di Apple */
    text-align: center;
    padding: 1rem;
    border-radius: 0.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    background-color: #CEADDE; /* Colore di sfondo grigio chiaro */
}
</style>
"""


subtitle_style = """
<style>
.subtitle-container {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
    font-size: 1.3rem;
    font-weight: bold;
    color: #000000; /* Colore blu di Apple */
    text-align: center;
    padding: 1rem;
    border-radius: 0.5rem;
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.1);
    background-color: #CEADDE; /* Colore di sfondo grigio chiaro */
}
</style>
"""

# Define the card_style with smaller dimensions
card_style = """
<style>
.card-container {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
    font-size: 0.8rem; /* Smaller font size */
    font-weight: bold;
    color: #000000; /* Black color */
    padding: 0.5rem; /* Smaller padding */
    border-radius: 0.3rem; /* Smaller border radius */
    box-shadow: 0 1px 1.5px rgba(0, 0, 0, 0.1);
    background-color: #D7CDDC; /* Light gray background color */
    display: flex; /* Use flexbox layout */
    flex-direction: column; /* Arrange items vertically */
    align-items: center; /* Center align items horizontally */
    justify-content: center; /* Center align items vertically */
    height: 80px; /* Set a smaller fixed height for the card */
    width: 130px; /* Set a smaller fixed width for the card */
    margin-bottom: 10px; /* Add smaller bottom margin for spacing */
}
</style>
"""

card_css = """
<style>
    .metric-card {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin: 10px;
    }
    .metric-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #333;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #ceadde;
    }
</style>
"""

def create_metric_card(title, value,col):
    card_html = f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
    </div>
    """
    col.markdown(card_html, unsafe_allow_html=True)

custom_style = """
<style>
.bold-text {
    font-weight: bold; /* Make text bold */
    font-size: 18px; /* Increase font size */
    color: #black; /* Change text color to blue */
}
</style>
"""


custom_style_subtitle = """
<style>
.bold-text-subtitle {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
    font-weight: bold; /* Make text bold */
    font-size: 28px; /* Increase font size */
    color: #black; /* Change text color to blue */
    text-align:center;
    margin-bottom:30px;
    margin-top:-60px;
}
</style>
"""

st.markdown("""
    <style>
    body {
        zoom: 1; /* Regola il valore per impostare lo zoom, 1.0 è il 100%, 1.2 è il 120% */
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Selettore per l'elemento con classi specifiche */
    .st-ag.st-dc.st-dd.st-de.st-df.st-ay {
        background-color: #ceadde; /* Imposta il colore di sfondo */
    }
    </style>
    """, unsafe_allow_html=True)


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "PredictAI";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 35px;
                position: relative;
                top: -10px;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()

st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #CEADDE;
        }
    </style>
    """, unsafe_allow_html=True)


if 'Light' not in st.session_state:
    st.session_state['Light'] = 'red'

if st.session_state['Light'] == 'red':
    st.write("Prego fare accesso dalla pagina Login.")
else:

    # Inseriamo lo stile del titolo nel frontend usando st.markdown()
    st.markdown(title_style, unsafe_allow_html=True)
    # Contenuto principale
    st.markdown("<div class='title-container'>Previsioni di Domanda</div>", unsafe_allow_html=True)
    st.divider()
    st.write(" ")
    st.write(" ")
    st.write(" ")


    st.markdown(custom_style_subtitle, unsafe_allow_html=True)
    st.markdown("<div class='bold-text-subtitle'>Analizza la previsione nel tempo!</div>", unsafe_allow_html=True)

    previsioni_1 = pd.read_csv("File_forecaster_1.csv")
    previsioni_2 = pd.read_csv("File_forecaster_2.csv")
    previsioni_3 = pd.read_csv("File_forecaster_3.csv")
    previsioni_4 = pd.read_csv("File_forecaster_4.csv")
    previsioni_5 = pd.read_csv("File_forecaster_5.csv")

    previsioni = pd.concat([previsioni_1,previsioni_2,previsioni_3,previsioni_4,previsioni_5])



    st.write(" ")
    st.markdown("<div class='subtitle-container'>Definisci lo scopo dell'analisi!</div>", unsafe_allow_html=True)
    st.write(" ")


    col1, col2 = st.columns(2)
    st.markdown(card_css, unsafe_allow_html=True)

    previsioni_scopo = previsioni


    #CREO TUTTO IL SISTEMA DI SELEZIONE PER FILTRI
    articoli_unici = previsioni_scopo["Articolo"].unique().tolist()
    articoli_unici.append("Tutti")
    scelta_prodotto = col1.multiselect("Seleziona uno o più **Prodotti**:", articoli_unici,default='Acido ialuronico - multiplo peso molecolare (30 ml)')
    if "Tutti" in scelta_prodotto:
        previsioni_scopo = previsioni_scopo
    else:
        previsioni_scopo = previsioni_scopo[previsioni_scopo["Articolo"].isin(scelta_prodotto)]

    canali_unici = previsioni_scopo["Canale"].unique().tolist()
    canali_unici.append("Tutti")
    scelta_canale = col2.multiselect("Seleziona uno o più **Canali**:", canali_unici,default="Tutti")
    if "Tutti" in scelta_canale:
        previsioni_scopo = previsioni_scopo
    else:
        previsioni_scopo = previsioni_scopo[previsioni_scopo["Canale"].isin(scelta_canale)]

    nazioni_unici = previsioni_scopo["Nazione"].unique().tolist()
    nazioni_unici.append("Tutti")
    scelta_nazioni= col1.multiselect("Seleziona uno o più **Nazioni**:", nazioni_unici,default="Tutti")
    if "Tutti" in scelta_nazioni:
        previsioni_scopo = previsioni_scopo
    else:
        previsioni_scopo = previsioni_scopo[previsioni_scopo["Nazione"].isin(scelta_nazioni)]

    famiglia_unici = previsioni_scopo["Famiglia"].unique().tolist()
    famiglia_unici.append("Tutti")
    scelta_famiglia = col2.multiselect("Seleziona uno o più **Famiglie di Prodotto**:", famiglia_unici,default="Tutti")
    if "Tutti" in scelta_famiglia:
        previsioni_scopo = previsioni_scopo
    else:
        previsioni_scopo = previsioni_scopo[previsioni_scopo["Famiglia"].isin(scelta_famiglia)]

    #CREO IL DF per il grafico
    previsioni_scopo_grafico = previsioni_scopo[["ds","Quantità","Volume finanziario","Volume finanziario Basso"]]

    previsioni_scopo_grafico = previsioni_scopo_grafico.groupby("ds").sum().reset_index()

    previsioni_scopo_grafico["ds"] = pd.to_datetime(previsioni_scopo_grafico["ds"])
    full_range = pd.date_range(start=previsioni_scopo_grafico['ds'].min(), end=previsioni_scopo_grafico['ds'].max(), freq='W-MON')
    full_df = pd.DataFrame({'ds': full_range})
    previsioni_scopo_grafico = pd.merge(full_df, previsioni_scopo_grafico, on='ds', how='left').fillna(0)


    st.markdown("""
        <hr style="border: 1px solid #ccc; margin: 20px 0;" />
    """, unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write(" ")
    col1, col2,col3 = st.columns(3)


    col1, col2 = st.columns([1, 2])  # 1:3 ratio to give more space to col2
    data_minima = min(pd.to_datetime(previsioni["ds"]))
    data_massima = max(pd.to_datetime(previsioni["ds"]))
    col1.markdown(subtitle_style, unsafe_allow_html=True)
    col1.markdown("<div class='subtitle-container'>Scegli le impostazioni del grafico</div>", unsafe_allow_html=True)
    col1.write(" ")
    input_data_inizio = pd.to_datetime(col1.date_input("Seleziona la data di inizio",min_value=data_minima,value=data_minima))
    input_data_fine = pd.to_datetime(col1.date_input("Seleziona la data di fine",max_value=data_massima,value=data_massima))
    col1.write(" ")

    Economico = col1.toggle("Visualizza in Euro")

    if Economico:
        previsioni_scopo_grafico["Quantità"] = previsioni_scopo_grafico["Volume finanziario"]




    previsioni_scopo_grafico = previsioni_scopo_grafico[previsioni_scopo_grafico["ds"]>input_data_inizio]
    previsioni_scopo_grafico = previsioni_scopo_grafico[previsioni_scopo_grafico["ds"]<input_data_fine]



    #CREO GRAFICO
    today = datetime.today()
    # Split the data into actuals and forecasts
    df_actual = previsioni_scopo_grafico[previsioni_scopo_grafico['ds'] <= today]
    df_forecast = previsioni_scopo_grafico[previsioni_scopo_grafico['ds'] > today]

    fig = go.Figure()

    # Add actual data (before today)
    fig.add_trace(go.Scatter(
        x=df_actual['ds'],
        y=df_actual['Quantità'],
        mode='lines',
        name='Vendite',
        line=dict(color='blue')
    ))

    # Add forecast data (after today)
    fig.add_trace(go.Scatter(
        x=df_forecast['ds'],
        y=df_forecast['Quantità'],
        mode='lines',
        name='Previsione',
        line=dict(color='#ceadde')  # Change to the specified color
    ))

    # Add interval shading (forecast area)

    # Add title and axis labels
    fig.update_layout(
        title="",
        xaxis_title="Data",
        yaxis_title="Quantità",
        hovermode="x unified",
        width=1000, # Set the width of the plot,
        height = 500,
        plot_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del grafico
        paper_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del box
    )
    col2.write(" ")
    col2.markdown("<div class='subtitle-container'>Vendite e Previsioni</div>", unsafe_allow_html=True)
    col2.plotly_chart(fig)

    col1.write(" ")

    oggi = datetime.now()
    previsioni_scopo_grafico_previsioni = previsioni_scopo_grafico[previsioni_scopo_grafico["ds"]>oggi]

    create_metric_card("Quantità previste", str(sum(previsioni_scopo_grafico_previsioni["Quantità"])).split(".")[0],col1)


    st.markdown("<div class='subtitle-container'>Dati Raw</div>", unsafe_allow_html=True)
    st.dataframe(previsioni_scopo_grafico.reset_index(drop=True)[["ds","Quantità"]],width=1500)


    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.markdown("<div class='subtitle-container'>Vendite e Previsioni per Gruppo Selezionato</div>", unsafe_allow_html=True)
    st.write(" ")
    parametro_raggrupamento = st.selectbox("Seleziona una Caratteristica:", ["Nazione","Articolo","Canale"])
    previsioni_scopo_secondo_grafico = previsioni_scopo[["ds","Quantità","Volume finanziario","Volume finanziario Basso",parametro_raggrupamento]]

    if Economico:
        previsioni_scopo_secondo_grafico["Quantità"] = previsioni_scopo_secondo_grafico["Volume finanziario"]
        previsioni_scopo_secondo_grafico["Intervallo Basso"] = previsioni_scopo_secondo_grafico["Volume finanziario Basso"]

    previsioni_scopo_secondo_grafico["ds"] = pd.to_datetime(previsioni_scopo_secondo_grafico["ds"])
    previsioni_scopo_secondo_grafico = previsioni_scopo_secondo_grafico.groupby(["ds",parametro_raggrupamento]).sum().reset_index()
    previsioni_scopo_secondo_grafico = previsioni_scopo_secondo_grafico.sort_values(by='Quantità', ascending=False)
    previsioni_scopo_secondo_grafico = previsioni_scopo_secondo_grafico[previsioni_scopo_secondo_grafico["ds"]>input_data_inizio]
    previsioni_scopo_secondo_grafico= previsioni_scopo_secondo_grafico[previsioni_scopo_secondo_grafico["ds"]<input_data_fine]
    # Supponiamo che il tuo DataFrame sia chiamato 'df'
    # df ha le colonne 'ds', 'Nazione', e 'Quantità'


    # Ordina le nazioni in base alle quantità totali, in ordine decrescente

    # Crea un dizionario per mappare le nazioni ai loro colori
    color_map = {parametro_raggrupamento: f'rgba({i * 20}, {100 + i * 10}, {150 + i * 10}, 0.8)' for i, parametro_raggrupamento in enumerate(previsioni_scopo_secondo_grafico[parametro_raggrupamento])}


    # Crea il grafico a barre
    fig2 = go.Figure()
    # Aggiungi barre per ogni nazione
    for gruppo in previsioni_scopo_secondo_grafico[parametro_raggrupamento].unique():
        gruppo_data = previsioni_scopo_secondo_grafico[previsioni_scopo_secondo_grafico[parametro_raggrupamento] == gruppo]
        fig2.add_trace(go.Bar(
            x=gruppo_data['ds'],
            y=gruppo_data['Quantità'],
            name=gruppo,
            hoverinfo='y+name',
            legendgroup=gruppo
        ))

    # Aggiungi una linea per la data di oggi
    fig2.add_shape(type="rect",
        x0=previsioni_scopo_secondo_grafico['ds'].min(), y0=0,
        x1=today, y1=previsioni_scopo_secondo_grafico['Quantità'].max()*1.8,  # Imposta l'altezza del rettangolo
        fillcolor="lightgray",
        line=dict(color="lightgray"),
        layer="below",
        opacity=0.3
    )

    # Aggiungi rettangolo viola chiaro dopo oggi
    fig2.add_shape(type="rect",
        x0=today, y0=0,
        x1=previsioni_scopo_secondo_grafico['ds'].max(), y1=previsioni_scopo_secondo_grafico['Quantità'].max()*1.8,  # Imposta l'altezza del rettangolo
        fillcolor="#ceadde",
        line=dict(color="#ceadde"),
        layer="below",
        opacity=0.3
    )
    # Aggiorna il layout
    fig2.update_layout(
        title='Quantità Settimanale per Nazione',
        xaxis_title='Settimana',
        yaxis_title='Quantità Totale',
        barmode='stack',
        legend_title=parametro_raggrupamento,
        xaxis_tickangle=-45
    )


    # Mostra il grafico
    st.plotly_chart(fig2)

    st.dataframe(previsioni_scopo_secondo_grafico.reset_index(drop=True)[["ds",parametro_raggrupamento,"Quantità"]],width=1200)

