import streamlit as st
import pandas as pd
import plotly.express as px

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
    st.markdown("<div class='title-container'>Analitica Generale</div>", unsafe_allow_html=True)
    st.divider()
    st.markdown(custom_style_subtitle, unsafe_allow_html=True)


    analitica = pd.read_csv("Analitica_mensile.csv")
    analitica["Data"] = pd.to_datetime(analitica["Data"])

    analitica["Somma di Q.tà"] = analitica["Somma di Q.tà"].round(0)
    analitica["Somma di Importo"] = analitica["Somma di Importo"].round(0)





    data_minima = min(analitica["Data"])
    data_massima = max(analitica["Data"])

    st.markdown(subtitle_style, unsafe_allow_html=True)
    st.markdown("<div class='subtitle-container'>Scegli il Periodo dell'Analisi</div>", unsafe_allow_html=True)
    st.write(" ")
    col1,col2 = st.columns(2)
    input_data_inizio = pd.to_datetime(col1.date_input("Seleziona la data di inizio",min_value=data_minima,value=data_minima))
    input_data_fine = pd.to_datetime(col2.date_input("Seleziona la data di fine",max_value=data_massima,value=data_massima))

    #CREO TUTTO IL SISTEMA DI SELEZIONE PER FILTRI
    articoli_unici = analitica["Articolo"].unique().tolist()
    articoli_unici.append("Tutti")
    scelta_prodotto = col1.multiselect("Seleziona uno o più **Prodotti**:", articoli_unici,default='Tutti')
    if "Tutti" in scelta_prodotto:
        analitica_scopo = analitica
    else:
        analitica_scopo = analitica[analitica["Articolo"].isin(scelta_prodotto)]

    canali_unici = analitica["Tipologia"].unique().tolist()
    canali_unici.append("Tutti")
    scelta_canale = col2.multiselect("Seleziona uno o più **Canali**:", canali_unici,default="Tutti")
    if "Tutti" in scelta_canale:
        analitica_scopo = analitica_scopo
    else:
        analitica_scopo = analitica_scopo[analitica_scopo["Tipologia"].isin(scelta_canale)]


    nazioni_unici = analitica_scopo["Nazione"].unique().tolist()
    nazioni_unici.append("Tutti")
    scelta_nazioni= col1.multiselect("Seleziona uno o più **Nazioni**:", nazioni_unici,default="Tutti")
    if "Tutti" in scelta_nazioni:
        analitica_scopo = analitica_scopo
    else:
        analitica_scopo = analitica_scopo[analitica_scopo["Nazione"].isin(scelta_nazioni)]

    linea_unici = analitica_scopo["Linea Prodotto"].unique().tolist()
    linea_unici.append("Tutti")
    scelta_linea = col2.multiselect("Seleziona uno o più **Linea di Prodotto**:", linea_unici,default="Tutti")
    if "Tutti" in scelta_linea:
        analitica_scopo = analitica_scopo
    else:
        analitica_scopo = analitica_scopo[analitica_scopo["Linea Prodotto"].isin(scelta_linea)]


    codici_unici = analitica_scopo["Codice"].unique().tolist()
    codici_unici.append("Tutti")
    scelta_codici = st.multiselect("Seleziona uno o più **Codici**:", codici_unici,default="Tutti")
    if "Tutti" in scelta_codici:
        analitica_scopo = analitica_scopo
    else:
        analitica_scopo = analitica_scopo[analitica_scopo["Codice"].isin(scelta_codici)]


    Volumi = st.toggle("Visualizza in Volume finanziario")

    st.divider()
    st.write(" ")
    st.write(" ")
    st.write(" ")

    analitica_scopo = analitica_scopo[analitica_scopo["Data"]>=input_data_inizio]
    analitica_scopo = analitica_scopo[analitica_scopo["Data"]<=input_data_fine]
    analitica_scopo["Quantità"] = analitica_scopo["Somma di Q.tà"]
    annotazione = "Quantità"
    if Volumi:
        annotazione = "Volume finanziaro"
        analitica_scopo["Quantità"] = analitica_scopo["Somma di Importo"]


    primo_grafico  = analitica_scopo[["Data","Quantità"]]
    primo_grafico = primo_grafico.groupby("Data").sum().reset_index()
    fig = px.line(primo_grafico, x='Data', y="Quantità", title='Somma di Importo nel Tempo')
    fig.update_layout(xaxis_title='Data', yaxis_title=annotazione)
    fig.update_layout(
        title="",
        xaxis_title="Data",
        yaxis_title=annotazione,
        hovermode="x unified",
        width=1400, # Set the width of the plot,
        height = 500,
        plot_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del grafico
        paper_bgcolor='rgba(240, 240, 240, 1)',  # Sfondo del box
    )
    fig.update_traces(hovertemplate='Data: %{x}<br>Somma di Importo: %{y:.2f}<extra></extra>')

    fig.update_traces(line=dict(color='#ceadde', width=4))  # Imposta la larghezza della linea a 3 (puoi modificarla come preferisci)

    col1, col2 = st.columns([2, 1])  # Col1 occupa 2/3 e col2 1/3

    # Mostra il grafico in col1
    col1.markdown("<div class='subtitle-container'>Quantità per mese {}</div>".format(annotazione), unsafe_allow_html=True)
    col1.plotly_chart(fig, use_container_width=True)
    col2.markdown("<div class='subtitle-container'>Dati Raw</div>", unsafe_allow_html=True)

    primo_grafico['Data'] = primo_grafico['Data'].dt.strftime('%d-%m-%Y')
    col2.dataframe(primo_grafico,height=400,width=1000)

    st.divider()
    st.write(" ")
    st.write(" ")
    st.write(" ")

    # Ordina per 'Somma di Q.tà' in ordine decrescente

    col1,col2 = st.columns(2)
    df_prodotto = analitica_scopo[["Articolo","Quantità"]].groupby("Articolo").sum().reset_index()
    df_prodotto = df_prodotto.sort_values(by='Quantità', ascending=False)
    # Prendi i top 5 e raggruppa il resto sotto "Altri"
    top_5 = df_prodotto[:10]
    others = df_prodotto[10:].sum(numeric_only=True)
    # Aggiungi la riga "Altri" se ci sono altri valori
    if len(df_prodotto) > 10:
        altri_df = pd.DataFrame({'Articolo': ['Altri'], 'Quantità': [others['Quantità']]})
        top_5 = pd.concat([top_5, altri_df], ignore_index=True)
    # Crea un donut chart usando Plotly con palette viola e sfondo grigio chiaro
    fig6 = px.pie(top_5, values='Quantità', names='Articolo', hole=0.4)
    # Personalizza i colori e lo sfondo
    fig6.update_traces(marker=dict(colors=['#D1BBE3', '#C39BD3', '#A569BD', '#F5EEF8', '#E8DAEF', '#D5D8DC']),
                      textposition='inside', insidetextorientation='auto')  # Mostra etichette solo se dentro al ring

    # Rimuovi la legenda e imposta hover per mostrare informazioni
    fig6.update_layout(
        showlegend=False,  # Rimuovi la legenda
        plot_bgcolor='lightgrey',  # Sfondo grigio chiaro
        paper_bgcolor='lightgrey',  # Sfondo esterno grigio chiaro
        font=dict(color='black'),
    )
    col1.markdown("<div class='subtitle-container'>Per Prodotto</div>", unsafe_allow_html=True)
    col1.plotly_chart(fig6)
    col2.dataframe(df_prodotto.reset_index(drop=True),width=700,height=510)

    st.write(" ")
    st.write(" ")
    col1,col2 = st.columns(2)

    # Ordina per 'Somma di Q.tà' in ordine decrescente

    df_tipologia = analitica_scopo[["Tipologia","Quantità"]].groupby("Tipologia").sum().reset_index()
    df_tipologia = df_tipologia.sort_values(by='Quantità', ascending=False)
    # Prendi i top 5 e raggruppa il resto sotto "Altri"
    top_5 = df_tipologia[:5]
    others = df_tipologia[5:].sum(numeric_only=True)
    # Aggiungi la riga "Altri" se ci sono altri valori
    if len(df_tipologia) > 5:
        altri_df = pd.DataFrame({'Tipologia': ['Altri'], 'Quantità': [others['Quantità']]})
        top_5 = pd.concat([top_5, altri_df], ignore_index=True)
    # Crea un donut chart usando Plotly con palette viola e sfondo grigio chiaro
    fig2 = px.pie(top_5, values='Quantità', names='Tipologia', hole=0.4)
    # Personalizza i colori e lo sfondo
    fig2.update_traces(marker=dict(colors=['#D1BBE3', '#C39BD3', '#A569BD', '#F5EEF8', '#E8DAEF', '#D5D8DC']),
                      textposition='inside', insidetextorientation='auto')  # Mostra etichette solo se dentro al ring

    # Rimuovi la legenda e imposta hover per mostrare informazioni
    fig2.update_layout(
        showlegend=False,  # Rimuovi la legenda
        plot_bgcolor='lightgrey',  # Sfondo grigio chiaro
        paper_bgcolor='lightgrey',  # Sfondo esterno grigio chiaro
        font=dict(color='black'),
    )
    col1.markdown("<div class='subtitle-container'>Per Canale di Vendita</div>", unsafe_allow_html=True)
    col1.plotly_chart(fig2)
    col1.dataframe(df_tipologia.reset_index(drop=True),width=700,height=350)


    df_nazione = analitica_scopo[["Nazione","Quantità"]].groupby("Nazione").sum().reset_index()
    df_nazione = df_nazione.sort_values(by='Quantità', ascending=False)
    # Prendi i top 5 e raggruppa il resto sotto "Altri"
    top_5 = df_nazione[:5]
    others = df_nazione[5:].sum(numeric_only=True)
    # Aggiungi la riga "Altri" se ci sono altri valori
    if len(df_nazione) > 5:
        altri_df = pd.DataFrame({'Nazione': ['Altri'], 'Quantità': [others['Quantità']]})
        top_5 = pd.concat([top_5, altri_df], ignore_index=True)
    # Crea un donut chart usando Plotly con palette viola e sfondo grigio chiaro
    fig3 = px.pie(top_5, values='Quantità', names='Nazione', hole=0.4)
    # Personalizza i colori e lo sfondo
    fig3.update_traces(marker=dict(colors=['#D1BBE3', '#C39BD3', '#A569BD', '#F5EEF8', '#E8DAEF', '#D5D8DC']),
                      textposition='inside', insidetextorientation='auto')  # Mostra etichette solo se dentro al ring


    # Rimuovi la legenda e imposta hover per mostrare informazioni
    fig3.update_layout(
        showlegend=False,  # Rimuovi la legenda
        plot_bgcolor='lightgrey',  # Sfondo grigio chiaro
        paper_bgcolor='lightgrey',  # Sfondo esterno grigio chiaro
        font=dict(color='black'),
    )
    col2.markdown("<div class='subtitle-container'>Per Nazione</div>", unsafe_allow_html=True)
    col2.plotly_chart(fig3)
    col2.dataframe(df_nazione.reset_index(drop=True),width=700,height=350)

    st.write(" ")
    st.write(" ")
    col1,col2 = st.columns(2)

    df_linea = analitica_scopo[["Linea Prodotto","Quantità"]].groupby("Linea Prodotto").sum().reset_index()
    df_linea = df_linea.sort_values(by='Quantità', ascending=False)
    # Prendi i top 5 e raggruppa il resto sotto "Altri"
    top_5 = df_linea[:5]
    others = df_linea[5:].sum(numeric_only=True)
    # Aggiungi la riga "Altri" se ci sono altri valori
    if len(df_linea) > 5:
        altri_df = pd.DataFrame({'Linea Prodotto': ['Altri'], 'Quantità': [others['Quantità']]})
        top_5 = pd.concat([top_5, altri_df], ignore_index=True)
    # Crea un donut chart usando Plotly con palette viola e sfondo grigio chiaro
    fig4 = px.pie(top_5, values='Quantità', names='Linea Prodotto', hole=0.4)
    # Personalizza i colori e lo sfondo
    fig4.update_traces(marker=dict(colors=['#D1BBE3', '#C39BD3', '#A569BD', '#F5EEF8', '#E8DAEF', '#D5D8DC']),
                      textposition='inside', insidetextorientation='auto')  # Mostra etichette solo se dentro al ring

    # Rimuovi la legenda e imposta hover per mostrare informazioni
    fig4.update_layout(
        showlegend=False,  # Rimuovi la legenda
        plot_bgcolor='lightgrey',  # Sfondo grigio chiaro
        paper_bgcolor='lightgrey',  # Sfondo esterno grigio chiaro
        font=dict(color='black'),
    )
    col1.markdown("<div class='subtitle-container'>Per Linea Prodotto</div>", unsafe_allow_html=True)
    col1.plotly_chart(fig4)
    col1.dataframe(df_linea.reset_index(drop=True),width=700,height=350)



    df_famiglia = analitica_scopo[["Famiglia","Quantità"]].groupby("Famiglia").sum().reset_index()
    df_famiglia = df_famiglia.sort_values(by='Quantità', ascending=False)
    # Prendi i top 5 e raggruppa il resto sotto "Altri"
    top_5 = df_famiglia[:5]
    others = df_famiglia[5:].sum(numeric_only=True)
    # Aggiungi la riga "Altri" se ci sono altri valori
    if len(df_famiglia) > 5:
        altri_df = pd.DataFrame({'Famiglia': ['Altri'], 'Quantità': [others['Quantità']]})
        top_5 = pd.concat([top_5, altri_df], ignore_index=True)
    # Crea un donut chart usando Plotly con palette viola e sfondo grigio chiaro
    fig5 = px.pie(top_5, values='Quantità', names='Famiglia', hole=0.4)
    # Personalizza i colori e lo sfondo
    fig5.update_traces(marker=dict(colors=['#D1BBE3', '#C39BD3', '#A569BD', '#F5EEF8', '#E8DAEF', '#D5D8DC']),
                      textposition='inside', insidetextorientation='auto')  # Mostra etichette solo se dentro al ring

    # Rimuovi la legenda e imposta hover per mostrare informazioni
    fig5.update_layout(
        showlegend=False,  # Rimuovi la legenda
        plot_bgcolor='lightgrey',  # Sfondo grigio chiaro
        paper_bgcolor='lightgrey',  # Sfondo esterno grigio chiaro
        font=dict(color='black'),
    )
    col2.markdown("<div class='subtitle-container'>Per Famiglia</div>", unsafe_allow_html=True)
    col2.plotly_chart(fig5)
    col2.dataframe(df_famiglia.reset_index(drop=True),width=700,height=350)


    st.divider()
