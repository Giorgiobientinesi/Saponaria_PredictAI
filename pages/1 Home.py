import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import openpyxl
from streamlit import components
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


# Definisci lo stile CSS per la card
card_css = """
<style>
    .metric-card {
        background-color: #f0f0f0;
        padding: 20px;
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
        font-size: 36px;
        font-weight: bold;
        color: #ceadde;
    }
</style>
"""

# Inserisci il CSS nella pagina
st.markdown(card_css, unsafe_allow_html=True)

# Funzione per creare la card con titolo e valore personalizzati
def create_metric_card(title, value,col):
    card_html = f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
    </div>
    """
    col.markdown(card_html, unsafe_allow_html=True)

if 'Light' not in st.session_state:
    st.session_state['Light'] = 'red'

if st.session_state['Light'] == 'red':
    st.write("Prego fare accesso dalla pagina Login.")
else:

    previsioni = pd.read_csv("File_Forecaster.csv")
    giacenze = pd.read_csv("Giacenze attuali.csv")

    # Inseriamo lo stile del titolo nel frontend usando st.markdown()
    st.markdown(title_style, unsafe_allow_html=True)
    # Contenuto principale
    st.markdown("<div class='title-container'>Home</div>", unsafe_allow_html=True)
    st.divider()
    st.write(" ")
    st.write(" ")
    st.write(" ")


    previsioni['ds'] = pd.to_datetime(previsioni['ds'])

    oggi = datetime.now()
    un_mese_fa = oggi - timedelta(days=30)

    df_ultimo_mese = previsioni[previsioni['ds'] >= un_mese_fa]
    df_ultimo_mese = df_ultimo_mese[df_ultimo_mese['ds'] < oggi]

    inizio_prossimo_mese = oggi + timedelta(days=1)
    fine_prossimo_mese = oggi + timedelta(days=31)
    df_prossimo_mese = previsioni[(previsioni['ds'] >= inizio_prossimo_mese) & (previsioni['ds'] <= fine_prossimo_mese)]


    value_1 = "{:,.0f}".format(df_ultimo_mese["Quantità"].sum().round(3))
    value_2 = "{:,.0f}".format(df_prossimo_mese["Quantità"].sum().round(3))
    value_3 = "{:,.0f}".format(df_ultimo_mese["Volume finanziario"].sum().round(3))
    value_4 = "{:,.0f}".format(df_prossimo_mese["Volume finanziario"].sum().round(3))

    # Use a metric value from your app
    col1, col2,col3,col4 = st.columns(4)

    # Esempio di utilizzo della funzione
    create_metric_card("Quantità registrate Ultimo Mese(K)", value_1,col1)
    create_metric_card("Quantità previste Prossimo Mese(K)",value_2,col2)
    create_metric_card("Fatturato registrato Ultimo mese(K)", "€" +value_3,col3)
    create_metric_card("Fatturato Prossimo mese(K)","€" +value_4,col4)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.divider()

    col1,col2 = st.columns(2)

    giacenze = giacenze.rename(columns={
        'Descrizione': 'Articolo',
        'QtaGiac': 'Quantità_giacenza'
    })

    df_prossimo_mese_giacenze = df_prossimo_mese[["Articolo","Quantità"]].groupby("Articolo").sum().reset_index()
    df_prossimo_mese_giacenze = pd.merge(df_prossimo_mese_giacenze, giacenze[["Articolo","Quantità_giacenza"]], on='Articolo', how='left')
    df_prossimo_mese_giacenze = df_prossimo_mese_giacenze.dropna(subset="Quantità_giacenza")
    df_prossimo_mese_giacenze["Differenza"] = df_prossimo_mese_giacenze["Quantità"] - df_prossimo_mese_giacenze["Quantità_giacenza"]
    df_prossimo_mese_giacenze = df_prossimo_mese_giacenze.sort_values(by="Differenza",ascending=False)
    df_prossimo_mese_giacenze_tail = df_prossimo_mese_giacenze.tail(5)
    df_prossimo_mese_giacenze_head = df_prossimo_mese_giacenze.head(5)

    fig = go.Figure()
    # Aggiunta delle barre per Quantità
    fig.add_trace(go.Bar(
        x=df_prossimo_mese_giacenze_tail['Articolo'],
        y=df_prossimo_mese_giacenze_tail['Quantità'],
        name='Quantità Previste',
        marker_color='#ceadde',

    ))
    # Aggiornamento del layout
    fig.update_layout(
        title='Quantità e Giacenza per Articolo',
        xaxis_title='Articolo',
        yaxis_title='Quantità',
        barmode='group'
    )
    # Aggiunta delle barre per Quantità_giacenza
    fig.add_trace(go.Bar(
        x=df_prossimo_mese_giacenze_tail['Articolo'],
        y=df_prossimo_mese_giacenze_tail['Quantità_giacenza'],
        name='Quantità in giacenza',
        marker_color='green'
    ))

    fig.update_layout(
        width=1000, # Set the width of the plot,
        height = 500,
        plot_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del grafico
        paper_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del box
    )

    col1.markdown(subtitle_style, unsafe_allow_html=True)
    col1.markdown("<div class='subtitle-container'>Top 5 Prodotti Safe</div>", unsafe_allow_html=True)
    col1.plotly_chart(fig)


    fig2 = go.Figure()
    # Aggiunta delle barre per Quantità
    fig2.add_trace(go.Bar(
        x=df_prossimo_mese_giacenze_head['Articolo'],
        y=df_prossimo_mese_giacenze_head['Quantità'],
        name='Quantità Previste',
        marker_color='red'
    ))
    # Aggiornamento del layout
    fig2.update_layout(
        title='Quantità e Giacenza per Articolo',
        xaxis_title='Articolo',
        yaxis_title='Quantità',
        barmode='group'
    )
    # Aggiunta delle barre per Quantità_giacenza
    fig2.add_trace(go.Bar(
        x=df_prossimo_mese_giacenze_head['Articolo'],
        y=df_prossimo_mese_giacenze_head['Quantità_giacenza'],
        name='Quantità in giacenza',
        marker_color='#ceadde'
    ))

    fig2.update_layout(
        width=1000, # Set the width of the plot,
        height = 500,
        plot_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del grafico
        paper_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del box
    )


    col2.markdown(subtitle_style, unsafe_allow_html=True)
    col2.markdown("<div class='subtitle-container'>Top 5 Prodotti in Alert</div>", unsafe_allow_html=True)
    col2.plotly_chart(fig2)

    col1.divider()
    col2.divider()

    col1.markdown("<div class='subtitle-container'>Top 5 Prodotti ultimo mese!</div>", unsafe_allow_html=True)
    col2.markdown("<div class='subtitle-container'>Top 5 Prodotti prossimo mese!</div>", unsafe_allow_html=True)

    col1.table(df_ultimo_mese[["Articolo","Quantità"]].groupby("Articolo").sum().reset_index().sort_values(by="Quantità",ascending=False).head(5).reset_index(drop=True))
    col2.table(df_prossimo_mese[["Articolo","Quantità"]].groupby("Articolo").sum().reset_index().sort_values(by="Quantità",ascending=False).head(5).reset_index(drop=True))

    col1.markdown("<div class='subtitle-container'>Top 5 Nazioni ultimo mese!</div>", unsafe_allow_html=True)
    col2.markdown("<div class='subtitle-container'>Top 5 Nazioni prossimo mese!</div>", unsafe_allow_html=True)

    col1.table(df_ultimo_mese[["Nazione","Quantità"]].groupby("Nazione").sum().reset_index().sort_values(by="Quantità",ascending=False).head(5).reset_index(drop=True))
    col2.table(df_prossimo_mese[["Nazione","Quantità"]].groupby("Nazione").sum().reset_index().sort_values(by="Quantità",ascending=False).head(5).reset_index(drop=True))

    col1.markdown("<div class='subtitle-container'>Top 5 Canali ultimo mese!</div>", unsafe_allow_html=True)
    col2.markdown("<div class='subtitle-container'>Top 5 Canali prossimo mese!</div>", unsafe_allow_html=True)

    col1.table(df_ultimo_mese[["Canale","Quantità"]].groupby("Canale").sum().reset_index().sort_values(by="Quantità",ascending=False).head(5).reset_index(drop=True))
    col2.table(df_prossimo_mese[["Canale","Quantità"]].groupby("Canale").sum().reset_index().sort_values(by="Quantità",ascending=False).head(5).reset_index(drop=True))


