import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from Utils import add_logo

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

button_style = """
<style>
.stButton {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
    font-size: 2rem; /* Imposta la dimensione del testo del bottone */
    font-weight: bold;
    color: #000000;
    text-align: center;
    padding: 1.5rem 2rem; /* Imposta il padding interno del bottone per aumentarne le dimensioni */
    border-radius: 1rem; /* Aumenta il border-radius per arrotondare gli angoli del bottone */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    background-color: #eeeeee;
    border: none; /* Rimuovi il bordo del bottone */
}
</style>
"""

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
    st.markdown("<div class='title-container'>Genera Previsione</div>", unsafe_allow_html=True)

    previsioni_1 = pd.read_csv("File_forecaster_1.csv")
    previsioni_2 = pd.read_csv("File_forecaster_2.csv")
    previsioni_3 = pd.read_csv("File_forecaster_3.csv")
    previsioni_4 = pd.read_csv("File_forecaster_4.csv")
    previsioni_5 = pd.read_csv("File_forecaster_5.csv")
    previsioni_6 = pd.read_csv("File_forecaster_6.csv")
    previsioni_7 = pd.read_csv("File_forecaster_7.csv")


    previsioni = pd.concat([previsioni_1, previsioni_2, previsioni_3, previsioni_4, previsioni_5,previsioni_6,previsioni_7])


    previsioni["Key"] = previsioni["Articolo"].astype(str) + "__" + previsioni["Canale"].astype(str) + "__" +previsioni["Nazione"].astype(str)
    previsioni = previsioni.drop(["Key"],axis=1)

    previsioni["Quantità"] = previsioni["Quantità"].round(0)

    data_minima = pd.to_datetime("11/04/2024")
    data_massima = max(pd.to_datetime(previsioni["ds"]))
    st.markdown(subtitle_style, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    input_data_inizio = pd.to_datetime(col1.date_input("Seleziona la data di inizio",min_value=data_minima,value=data_minima))
    input_data_fine = pd.to_datetime(col2.date_input("Seleziona la data di fine",max_value=data_massima,value=data_massima))
    st.write(" ")



    #CREO TUTTO IL SISTEMA DI SELEZIONE PER FILTRI
    articoli_unici = previsioni["Articolo"].unique().tolist()
    articoli_unici.append("Tutti")
    scelta_prodotto = col1.multiselect("Seleziona uno o più **Prodotti**:", articoli_unici,default='Tutti')
    if "Tutti" in scelta_prodotto:
        previsioni_scopo = previsioni
    else:
        previsioni_scopo = previsioni[previsioni["Articolo"].isin(scelta_prodotto)]

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

    linea_unici = previsioni_scopo["Linea Prodotto"].unique().tolist()
    linea_unici.append("Tutti")
    scelta_linea = col2.multiselect("Seleziona uno o più **Linea di Prodotto**:", linea_unici,default="Tutti")
    if "Tutti" in scelta_linea:
        previsioni_scopo = previsioni_scopo
    else:
        previsioni_scopo = previsioni_scopo[previsioni_scopo["Linea Prodotto"].isin(scelta_linea)]


    codici_unici = previsioni_scopo["Codice"].unique().tolist()
    codici_unici.append("Tutti")
    scelta_codici = st.multiselect("Seleziona uno o più **Codici**:", codici_unici,default="Tutti")
    if "Tutti" in scelta_codici:
        previsioni_scopo = previsioni_scopo
    else:
        previsioni_scopo = previsioni_scopo[previsioni_scopo["Codice"].isin(scelta_codici)]



    ordine = previsioni_scopo.copy()
    #ordine = previsioni[["ds","Articolo","Quantità"]]
    ordine["ds"] = pd.to_datetime(ordine["ds"])

    ordine = ordine[ordine["ds"]>=input_data_inizio]
    ordine = ordine[ordine["ds"]<=input_data_fine]


    ordine = ordine[["Articolo","Quantità"]]

    ordine = ordine.groupby("Articolo").sum().reset_index()
    #input_data_inizio = input_data_inizio.dt.strftime('%d-%m-%Y')

    input_data_inizio = pd.to_datetime(input_data_inizio)
    input_data_inizio = input_data_inizio.strftime('%d-%m-%Y')

    input_data_fine = pd.to_datetime(input_data_fine)
    input_data_fine = input_data_fine.strftime('%d-%m-%Y')

    ordine["Periodo"] = str(input_data_inizio) + " - " + str(input_data_fine)

    st.markdown(button_style, unsafe_allow_html=True)
    genera = st.button("Genera!")
    if genera:
        st.dataframe(ordine,width=1000)
