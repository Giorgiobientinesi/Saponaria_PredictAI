import streamlit as st
import pandas as pd
from datetime import datetime, timedelta,date
import plotly.graph_objects as go
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

    previsioni_1 = pd.read_csv("File_forecaster_1.csv")
    previsioni_2 = pd.read_csv("File_forecaster_2.csv")
    previsioni_3 = pd.read_csv("File_forecaster_3.csv")
    previsioni_4 = pd.read_csv("File_forecaster_4.csv")
    previsioni_5 = pd.read_csv("File_forecaster_5.csv")
    previsioni_6 = pd.read_csv("File_forecaster_6.csv")
    previsioni_7 = pd.read_csv("File_forecaster_7.csv")

    giacenze = pd.read_csv("Giacenze attuali.csv",sep=';', encoding='latin-1')


    previsioni = pd.concat([previsioni_1, previsioni_2, previsioni_3, previsioni_4, previsioni_5,previsioni_6,previsioni_7])

    previsioni["Key"] = previsioni["Articolo"].astype(str) + "__" + previsioni["Canale"].astype(str) + "__" +previsioni["Nazione"].astype(str)

    previsioni = previsioni.dropna(subset="Quantità")

    previsioni["Quantità"].fillna(0)


    previsioni["Quantità"] = previsioni["Quantità"].round(0)
    previsioni["Volume finanziario"] = previsioni["Volume finanziario"].round(0)

    # Inseriamo lo stile del titolo nel frontend usando st.markdown()
    st.markdown(title_style, unsafe_allow_html=True)
    # Contenuto principale
    st.markdown("<div class='title-container'>Home</div>", unsafe_allow_html=True)
    st.divider()
    st.write(" ")
    st.write(" ")
    st.write(" ")

    import pandas as pd
    from datetime import datetime

    # Imposta la data limite (es. 28 ottobre 2024)
    data_limite = pd.Timestamp("2024-11-25") #mese giorno
    st.write("Ultima modifica di vendite: "+str(data_limite)[:10] + ". Quindi la settimana che va fino al 02/12.")

    # Converti la colonna 'ds' in formato datetime, se non lo è già
    previsioni['ds'] = pd.to_datetime(previsioni['ds'])

    # Aggiungi una colonna che classifica le righe come "sales" o "previsioni"
    previsioni['tipo'] = previsioni['ds'].apply(lambda x: 'sales' if x <= data_limite else 'previsioni')

    # Ottieni la data di oggi
    oggi = pd.Timestamp(datetime.today())
    mese_attuale = oggi.month
    anno_attuale = oggi.year

    # Filtra le vendite registrate come sales fino alla data di oggi
    df_mese_adoggi = previsioni[
        (previsioni['ds'].dt.month == mese_attuale) &
        (previsioni['ds'].dt.year == anno_attuale) &
        (previsioni['tipo'] == 'sales') &
        (previsioni['ds'] <= oggi)
        ]

    # Filtra tutte le righe (sales e previsioni) per il mese corrente
    df_mese_totale = previsioni[
        (previsioni['ds'].dt.month == mese_attuale) &
        (previsioni['ds'].dt.year == anno_attuale)
        ]

    value_1 = "{:,.0f}".format(df_mese_adoggi["Quantità"].sum().round(3))
    value_2 = "{:,.0f}".format(df_mese_totale["Quantità"].sum().round(3))
    value_3 = "{:,.0f}".format(df_mese_adoggi["Volume finanziario"].sum().round(3))
    value_4 = "{:,.0f}".format(df_mese_totale["Volume finanziario"].sum().round(3))

    # Use a metric value from your app
    col1, col2,col3,col4 = st.columns(4)

    # Esempio di utilizzo della funzione
    create_metric_card("Quantità registrate mese Corrente", value_1,col1)
    create_metric_card("Quantità previste mese Corrente",value_2,col2)
    create_metric_card("Fatturato registrato mese Corrente", "€" +value_3,col3)
    create_metric_card("Fatturato previsto Mese corrente","€" +value_4,col4)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.divider()

    oggi = datetime.now()
    un_mese_fa = oggi - timedelta(days=30)
    df_ultimo_mese = previsioni[previsioni['ds'] >= un_mese_fa]
    df_ultimo_mese = df_ultimo_mese[df_ultimo_mese['ds'] < oggi]



    inizio_prossimo_mese = oggi + timedelta(days=1)
    fine_prossimo_mese = oggi + timedelta(days=31)
    df_prossimo_mese = previsioni[(previsioni['ds'] >= inizio_prossimo_mese) & (previsioni['ds'] <= fine_prossimo_mese)]



    col1,col2 = st.columns(2)
    articoli_esclusi = col1.multiselect("Escludi Articoli",df_prossimo_mese["Articolo"].unique())
    linea_esclusi = col2.multiselect("Escludi Linea", df_prossimo_mese["Linea Prodotto"].unique())
    canale_esclusi = col1.multiselect("Escludi Canale",df_prossimo_mese["Canale"].unique())
    famiglia_esclusi = col2.multiselect("Escludi Famiglia", df_prossimo_mese["Famiglia"].unique())

    giacenze = giacenze.rename(columns={
        'Descrizione': 'Articolo',
        'QtaGiac': 'Quantità_giacenza'
    })

    giacenze['Quantità_giacenza'] = giacenze['Quantità_giacenza'].str.replace(',', '.').astype(float).astype(int)

    df_prossimo_mese = df_prossimo_mese[~df_prossimo_mese['Articolo'].isin(articoli_esclusi)]
    df_ultimo_mese = df_ultimo_mese[~df_ultimo_mese['Articolo'].isin(articoli_esclusi)]
    df_prossimo_mese = df_prossimo_mese[~df_prossimo_mese['Linea Prodotto'].isin(linea_esclusi)]
    df_ultimo_mese = df_ultimo_mese[~df_ultimo_mese['Linea Prodotto'].isin(linea_esclusi)]
    df_prossimo_mese = df_prossimo_mese[~df_prossimo_mese['Canale'].isin(canale_esclusi)]
    df_ultimo_mese = df_ultimo_mese[~df_ultimo_mese['Canale'].isin(canale_esclusi)]
    df_prossimo_mese = df_prossimo_mese[~df_prossimo_mese['Famiglia'].isin(famiglia_esclusi)]
    df_ultimo_mese = df_ultimo_mese[~df_ultimo_mese['Famiglia'].isin(famiglia_esclusi)]

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

    df_prossimo_mese_giacenze_tail['Articolo_abbr'] = df_prossimo_mese_giacenze_tail['Articolo'].apply(
        lambda x: x[:40] + '...' if len(x) > 20 else x)
    df_prossimo_mese_giacenze_head['Articolo_abbr'] = df_prossimo_mese_giacenze_head['Articolo'].apply(
        lambda x: x[:40] + '...' if len(x) > 20 else x)

    fig2 = go.Figure()
    # Aggiunta delle barre per Quantità
    fig2.add_trace(go.Bar(
        x=df_prossimo_mese_giacenze_head['Articolo_abbr'],
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
        x=df_prossimo_mese_giacenze_head['Articolo_abbr'],
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

    df_ultimo_mese["Quantità"] = df_ultimo_mese["Quantità"].astype(int)
    df_prossimo_mese["Quantità"] = df_prossimo_mese["Quantità"].astype(int)

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


