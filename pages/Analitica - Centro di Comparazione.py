import streamlit as st
import pandas as pd
import plotly.express as px
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
    analitica["Somma di Q.tà"] = analitica["Somma di Q.tà"].round(0)
    analitica["Somma di Importo"] = analitica["Somma di Importo"].round(0)

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

    linea_unici = df_scopo["Linea Prodotto"].unique().tolist()
    linea_unici.append("Tutti")
    scelta_linea = col2.multiselect("Seleziona uno o più **Linea di Prodotto**:", linea_unici,default="Tutti")
    if "Tutti" in scelta_linea:
        df_scopo = df_scopo
    else:
        df_scopo = df_scopo[df_scopo["Linea Prodotto"].isin(scelta_linea)]

    codici_unici = df_scopo["Codice"].unique().tolist()
    codici_unici.append("Tutti")
    scelta_codici = st.multiselect("Seleziona uno o più **Codici**:", codici_unici,default="Tutti")
    if "Tutti" in scelta_codici:
        df_scopo = df_scopo
    else:
        df_scopo = df_scopo[df_scopo["Codice"].isin(scelta_codici)]

    data_minima = min(analitica["Data"])
    data_massima = max(analitica["Data"])
    default_value_min_1 = pd.to_datetime("2023/09/01")
    default_value_max_1 = pd.to_datetime("2023/10/01")

    default_value_min_2= pd.to_datetime("2024/09/01")
    default_value_max_2 = pd.to_datetime("2024/10/01")

    st.markdown(subtitle_style, unsafe_allow_html=True)
    st.write(" ")
    col1,col2 = st.columns(2)

    col1.markdown("<div class='subtitle-container'>Scegli il primo intervallo dell'Analisi</div>", unsafe_allow_html=True)
    col1.write(" ")
    input_data_inizio_uno = pd.to_datetime(col1.date_input("Seleziona la data di inizio",min_value=data_minima,value=default_value_min_1,key="A"))
    input_data_fine_uno = pd.to_datetime(col1.date_input("Seleziona la data di fine",max_value=data_massima,value=default_value_max_1,key="B"))


    col2.markdown("<div class='subtitle-container'>Scegli l'intervallo da comparare</div>", unsafe_allow_html=True)
    col2.write(" ")
    input_data_inizio_due = pd.to_datetime(col2.date_input("Seleziona la data di inizio",min_value=data_minima,value=default_value_min_2,key="C"))
    input_data_fine_due = pd.to_datetime(col2.date_input("Seleziona la data di fine",max_value=data_massima,value=default_value_max_2,key="D"))

    df_scopo = df_scopo.rename(columns={'Tipologia': 'Canale'})

    primo_df_scopo = df_scopo
    secondo_df_scopo = df_scopo

    primo_df_scopo = primo_df_scopo[primo_df_scopo["Data"]<=input_data_fine_uno]
    primo_df_scopo = primo_df_scopo[primo_df_scopo["Data"]>=input_data_inizio_uno]

    secondo_df_scopo = secondo_df_scopo[secondo_df_scopo["Data"]<=input_data_fine_due]
    secondo_df_scopo = secondo_df_scopo[secondo_df_scopo["Data"]>=input_data_inizio_due]






    Volumi = st.toggle("Visualizza in Volume Finanzario")
    Percentuali = st.toggle("Visualizza differenza in Percentuale")

    annotazione = "Quantità"

    if Volumi:
        annotazione = "Volume Finanziario"
        primo_df_scopo["Quantità"] = primo_df_scopo["Somma di Importo"]
        secondo_df_scopo["Quantità"] = secondo_df_scopo["Somma di Importo"]
    else:
        primo_df_scopo["Quantità"] = primo_df_scopo["Somma di Q.tà"]
        secondo_df_scopo["Quantità"] = secondo_df_scopo["Somma di Q.tà"]

    if Percentuali:
        colonna_to_plot = "Differenza % "
    else:
        colonna_to_plot = "Differenza"

    if len(primo_df_scopo)>0 and len(secondo_df_scopo)>0:
        if str(min(primo_df_scopo["Data"])) != str(input_data_inizio_uno) and len(scelta_prodotto)==1:
            st.warning(
                "Attenzione! Il prodotto selezionato è stato venduto a partire da una data maggiore alla data di inizio del primo periodo selezionato! La prima data di vendita è " +str(min(primo_df_scopo["Data"]))[:10] )

        else:
            pass
    else:
        st.warning("Non sono stati trovati dati per questa analisi in questo periodo.")

    st.divider()



    scelta_raggruppamento= st.selectbox("Voglio vedere la Differenza per:", ["Articolo","Nazione","Canale","Linea Prodotto","Famiglia"])

    primo_df_scopo = primo_df_scopo[[scelta_raggruppamento,"Quantità"]]
    primo_df_scopo = primo_df_scopo.groupby(scelta_raggruppamento).sum().reset_index()

    secondo_df_scopo = secondo_df_scopo[[scelta_raggruppamento,"Quantità"]]
    secondo_df_scopo = secondo_df_scopo.groupby(scelta_raggruppamento).sum().reset_index()

    df_merged = pd.merge(primo_df_scopo, secondo_df_scopo, on=scelta_raggruppamento, suffixes=('_periodo1', '_periodo2'),how="outer")
    df_merged = df_merged.fillna(0)

    df_merged['Differenza'] = df_merged['Quantità_periodo2'] - df_merged['Quantità_periodo1']
    df_merged['Differenza % '] = df_merged.apply(
        lambda row: (row['Quantità_periodo2'] - row['Quantità_periodo1']) / row['Quantità_periodo1'] * 100 if row['Quantità_periodo1'] != 0 else 0,axis=1)

    # Fill NaN values for percentage
    df_merged['Differenza % '] = df_merged['Differenza % '].fillna(0)
    df_merged['Differenza % '] = df_merged['Differenza % '].round(2)

    # Calcolare valori assoluti per ordinamento
    df_merged['AbsDifferenza'] = df_merged['Differenza'].abs()

    # Selezionare le 10 nazioni/articoli/etc. principali in base alla differenza assoluta
    top_nations = df_merged.nlargest(10, 'AbsDifferenza')

    # Gestire il caso in cui ci siano più di 10 elementi
    if len(df_merged) > 10:
        # Sommare le quantità e differenze per le altre nazioni
        other_sum = df_merged[~df_merged[scelta_raggruppamento].isin(top_nations[scelta_raggruppamento])][
            ["Quantità_periodo1", "Quantità_periodo2", "Differenza"]].sum()

        # Calcolare la media ponderata delle percentuali, evitando divisioni per zero
        total_quantity_periodo1 = df_merged[~df_merged[scelta_raggruppamento].isin(top_nations[scelta_raggruppamento])][
            "Quantità_periodo1"].sum()

        if total_quantity_periodo1 != 0:
            other_weighted_percentage = (
                    df_merged[~df_merged[scelta_raggruppamento].isin(top_nations[scelta_raggruppamento])]
                    .apply(lambda row: row["Differenza % "] * row["Quantità_periodo1"], axis=1).sum()
                    / total_quantity_periodo1
            )
        else:
            other_weighted_percentage = 0  # Se non c'è quantità nel periodo 1, la percentuale diventa 0

        # Creazione della riga 'Other'
        other_row = pd.DataFrame({
            scelta_raggruppamento: ['Other'],
            "Quantità_periodo1": [other_sum["Quantità_periodo1"]],
            "Quantità_periodo2": [other_sum["Quantità_periodo2"]],
            "Differenza": [other_sum["Differenza"]],
            "Differenza % ": [other_weighted_percentage],
            "AbsDifferenza" : abs(other_sum["Differenza"])
        })

        # Concatenare 'Other' a 'top_nations'
        top_nations = pd.concat([top_nations, other_row], ignore_index=True)


    # Create a bar chart
    fig = px.bar(top_nations, x=scelta_raggruppamento, y=colonna_to_plot,
                 color=colonna_to_plot,
                 labels={colonna_to_plot: colonna_to_plot},
                 title='Top 10 Differenze per {} (Aggregato come "Other")'.format(scelta_raggruppamento),
                 custom_data=['Differenza % '])  # Passa i valori di "Differenza % " come dati aggiuntivi

    # Modifica il colore delle barre in base al valore
    fig.update_traces(
        marker=dict(color=top_nations[colonna_to_plot].apply(lambda x: 'red' if x < 0 else 'green')),
        hovertemplate='<b>%{x}</b><br>' +
                      colonna_to_plot + ': %{y}<br>' +
                      'Differenza %: %{customdata[0]:.2f}%'  # Aggiungi "Differenza %" all'hover
    )
    fig.update_layout(
        title="",
        xaxis_title=scelta_raggruppamento,
        yaxis_title=colonna_to_plot,
        hovermode="x unified",
        width=1600, # Set the width of the plot,
        height = 500,
        plot_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del grafico
        paper_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del box
    )

    st.markdown("<div class='subtitle-container'>Top differenze ({})</div>".format(annotazione), unsafe_allow_html=True)
    st.plotly_chart(fig)

    df_merged_df = df_merged[[scelta_raggruppamento,"Quantità_periodo1","Quantità_periodo2", "Differenza","Differenza % "]]

    df_merged_df["Differenza % "] = (df_merged_df["Differenza % "]).astype(str) + " %"


    col1,col2,col3= st.columns(3)
    st.markdown("<div class='subtitle-container'>Dati Raw</div>", unsafe_allow_html=True)
    st.dataframe(df_merged_df,width=2500,height=500)