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

    st.markdown(title_style, unsafe_allow_html=True)
    # Contenuto principale
    st.markdown("<div class='title-container'>Centro di Comparazione</div>", unsafe_allow_html=True)
    st.divider()
    st.markdown(custom_style_subtitle, unsafe_allow_html=True)


    analitica = pd.read_csv("Analitica_mensile.csv")

    analitica["Data"] = pd.to_datetime(analitica["Data"])

    #st.dataframe(analitica)
    df = analitica

    st.markdown("<div class='subtitle-container'>Scegli lo scopo dell'analisi!</div>", unsafe_allow_html=True)
    st.write(" ")
    col1,col2 = st.columns(2)

    #CREO TUTTO IL SISTEMA DI SELEZIONE PER FILTRI
    articoli_unici = analitica["Articolo"].unique().tolist()
    articoli_unici.append("Tutti")
    scelta_prodotto = col1.multiselect("Seleziona uno o più **Prodotti**:", articoli_unici,default='Tutti')
    if "Tutti" in scelta_prodotto:
        df_scopo = df
    else:
        df_scopo = df[df["Articolo"].isin(scelta_prodotto)]

    canali_unici = df_scopo["Tipologia"].unique().tolist()
    canali_unici.append("Tutti")
    scelta_canale = col2.multiselect("Seleziona uno o più **Canali**:", canali_unici,default="Tutti")
    if "Tutti" in scelta_canale:
        df_scopo = df_scopo
    else:
        df_scopo = df_scopo[df_scopo["Tipologia"].isin(scelta_canale)]


    nazioni_unici = df_scopo["Nazione"].unique().tolist()
    nazioni_unici.append("Tutti")
    scelta_nazioni= col1.multiselect("Seleziona uno o più **Nazioni**:", nazioni_unici,default="Tutti")
    if "Tutti" in scelta_nazioni:
        df_scopo = df_scopo
    else:
        df_scopo = df_scopo[df_scopo["Nazione"].isin(scelta_nazioni)]

    famiglia_unici = df_scopo["Famiglia"].unique().tolist()
    famiglia_unici.append("Tutti")
    scelta_famiglia = col2.multiselect("Seleziona uno o più **Famiglie di Prodotto**:", famiglia_unici,default="Tutti")
    if "Tutti" in scelta_famiglia:
        df_scopo = df_scopo
    else:
        df_scopo = df_scopo[df_scopo["Famiglia"].isin(scelta_famiglia)]

    data_minima = min(analitica["Data"])
    data_massima = max(analitica["Data"])

    st.markdown(subtitle_style, unsafe_allow_html=True)
    st.write(" ")
    col1,col2 = st.columns(2)

    col1.markdown("<div class='subtitle-container'>Scegli il primo intervallo dell'Analisi</div>", unsafe_allow_html=True)
    col1.write(" ")
    input_data_inizio_uno = pd.to_datetime(col1.date_input("Seleziona la data di inizio",min_value=data_minima,value=pd.to_datetime("2022-01-01"),key="A"))
    input_data_fine_uno = pd.to_datetime(col1.date_input("Seleziona la data di fine",max_value=data_massima,value=pd.to_datetime("2023-01-01"),key="B"))


    col2.markdown("<div class='subtitle-container'>Scegli l' intervallo da comparare</div>", unsafe_allow_html=True)
    col2.write(" ")
    input_data_inizio_due = pd.to_datetime(col2.date_input("Seleziona la data di inizio",min_value=data_minima,value=pd.to_datetime("2023-01-01"),key="C"))
    input_data_fine_due = pd.to_datetime(col2.date_input("Seleziona la data di fine",max_value=data_massima,value=pd.to_datetime("2024-01-01"),key="D"))

    primo_df_scopo = df_scopo
    secondo_df_scopo = df_scopo

    primo_df_scopo = primo_df_scopo[primo_df_scopo["Data"]<=input_data_fine_uno]
    primo_df_scopo = primo_df_scopo[primo_df_scopo["Data"]>=input_data_inizio_uno]

    secondo_df_scopo = secondo_df_scopo[secondo_df_scopo["Data"]<=input_data_fine_due]
    secondo_df_scopo = secondo_df_scopo[secondo_df_scopo["Data"]>=input_data_inizio_due]




    Volumi = st.toggle("Visualizza in Volumi di vendita")
    annotazione = "Volume finanziaro"

    if Volumi:
        annotazione = "Volumi"
        primo_df_scopo["Quantità"] = primo_df_scopo["Somma di Q.tà"]
        secondo_df_scopo["Quantità"] = secondo_df_scopo["Somma di Q.tà"]
    else:
        primo_df_scopo["Quantità"] = primo_df_scopo["Somma di Importo"]
        secondo_df_scopo["Quantità"] = secondo_df_scopo["Somma di Importo"]


    st.divider()
    scelta_raggruppamento= st.selectbox("Voglio vedere la Differenza per:", ["Articolo","Nazione","Tipologia","Linea Prodotto","Famiglia"])


    primo_df_scopo = primo_df_scopo[[scelta_raggruppamento,"Quantità"]]
    primo_df_scopo = primo_df_scopo.groupby(scelta_raggruppamento).sum().reset_index()

    secondo_df_scopo = secondo_df_scopo[[scelta_raggruppamento,"Quantità"]]
    secondo_df_scopo = secondo_df_scopo.groupby(scelta_raggruppamento).sum().reset_index()

    df_merged = pd.merge(primo_df_scopo, secondo_df_scopo, on=scelta_raggruppamento, suffixes=('_periodo1', '_periodo2'),how="outer")
    df_merged = df_merged.fillna(0)

    df_merged['Differenza'] = df_merged['Quantità_periodo2'] - df_merged['Quantità_periodo1']
    df_merged['Differenza % '] = (df_merged['Quantità_periodo2'] - df_merged['Quantità_periodo1'])/df_merged['Quantità_periodo1']

    df_merged['Differenza % ']  = df_merged['Differenza % '].fillna(0)

    # Calculate absolute values for sorting
    df_merged['AbsDifferenza'] = df_merged['Differenza'].abs()
    # Sort by absolute difference and get the top 10
    top_nations = df_merged.nlargest(10, 'AbsDifferenza')

    # Check if there are more than 10 entries to aggregate
    if len(df_merged) > 10:
        other_sum = df_merged[~df_merged[scelta_raggruppamento].isin(top_nations[scelta_raggruppamento])]['Differenza'].sum()
        other_row = pd.DataFrame({scelta_raggruppamento: ['Other'], 'Differenza': [other_sum]})
        top_nations = pd.concat([top_nations, other_row], ignore_index=True)

    # Create a bar chart
    fig = px.bar(top_nations, x=scelta_raggruppamento, y='Differenza',
                 color='Differenza',
                 labels={'Differenza': 'Differenza'},
                 title='Top 10 Differenze per {} (Aggregato come "Other")'.format(scelta_raggruppamento))

    # Adjust the x-axis to show negative values to the left
    fig.update_traces(marker=dict(color=top_nations['Differenza'].apply(lambda x: 'red' if x < 0 else 'green')))
    fig.update_layout(
        title="",
        xaxis_title="Nazione",
        yaxis_title="Differenza",
        hovermode="x unified",
        width=1600, # Set the width of the plot,
        height = 500,
        plot_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del grafico
        paper_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del box
    )

    st.markdown("<div class='subtitle-container'>Top 10 differenze ({})</div>".format(annotazione), unsafe_allow_html=True)
    st.plotly_chart(fig)

    df_merged_df = df_merged[[scelta_raggruppamento,"Differenza"]]

    col1,col2,col3= st.columns(3)
    st.markdown("<div class='subtitle-container'>Dati Raw</div>", unsafe_allow_html=True)
    st.dataframe(df_merged_df,width=2500,height=500)
