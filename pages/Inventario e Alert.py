import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
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
        color: red;
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


st.markdown(title_style, unsafe_allow_html=True)
st.markdown(subtitle_style, unsafe_allow_html=True)
# Contenuto principale

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

    previsioni = pd.concat([previsioni_1, previsioni_2, previsioni_3, previsioni_4, previsioni_5,previsioni_6,previsioni_7])
    giacenze = pd.read_excel("Giacenze attuali.xls")


    previsioni["Key"] = previsioni["Articolo"].astype(str) + "__" + previsioni["Canale"].astype(str) + "__" +previsioni["Nazione"].astype(str)
    previsioni = previsioni.drop(["Key"],axis=1)

    previsioni["Quantità"] =previsioni["Quantità"].round(0)

    previsioni['ds'] = pd.to_datetime(previsioni['ds'])

    giacenze = giacenze.rename(columns={
        'Descrizione': 'Articolo',
        'QtaGiac': 'Quantità_giacenza'
    })
    #giacenze['Quantità_giacenza'] = giacenze['Quantità_giacenza'].str.replace(',', '.').astype(float).astype(int)


    st.write(" ")
    st.write(" ")

    st.markdown("<div class='title-container'>Alerting</div>", unsafe_allow_html=True)
    st.markdown(card_css, unsafe_allow_html=True)


    col1,col2 = st.columns(2)
    data_massima = max(previsioni["ds"])
    oggi = datetime.now()
    inizio_prossimo_mese = oggi + timedelta(days=1)
    fine_prossimo_mese = oggi + timedelta(days=31)
    input_data_fine = pd.to_datetime(col1.date_input("Voglio essere coperto fino a",min_value=inizio_prossimo_mese,max_value=data_massima,value=fine_prossimo_mese,key="A"))

    df_prossimo_mese = previsioni[(previsioni['ds'] >= inizio_prossimo_mese) & (previsioni['ds'] <= input_data_fine)]


    df_prossimo_mese_giacenze = df_prossimo_mese[["Articolo","Quantità"]].groupby("Articolo").sum().reset_index()
    df_prossimo_mese_giacenze = pd.merge(df_prossimo_mese_giacenze, giacenze[["Articolo","Quantità_giacenza"]], on='Articolo', how='left')
    df_prossimo_mese_giacenze = df_prossimo_mese_giacenze.dropna(subset="Quantità_giacenza")
    df_prossimo_mese_giacenze["Differenza"] = df_prossimo_mese_giacenze["Quantità"] - df_prossimo_mese_giacenze["Quantità_giacenza"]
    df_prossimo_mese_giacenze = df_prossimo_mese_giacenze.sort_values(by="Differenza",ascending=False)
    numero_alert = df_prossimo_mese_giacenze[df_prossimo_mese_giacenze["Differenza"]>0].count().iloc[0]



    pezzi_mancanti = int(df_prossimo_mese_giacenze[df_prossimo_mese_giacenze["Differenza"]>0]["Differenza"].sum())
    alert = df_prossimo_mese_giacenze[df_prossimo_mese_giacenze["Differenza"]>0]


    create_metric_card("Prodotti di Alert", numero_alert,col1)
    create_metric_card("Pezzi mancanti Totali", pezzi_mancanti,col1)
    col2.dataframe(df_prossimo_mese_giacenze[df_prossimo_mese_giacenze["Differenza"]>0].reset_index(drop=True))


    st.write(" ")
    st.write(" ")
    st.divider()

    st.markdown("<div class='title-container'>Alerting nel tempo</div>", unsafe_allow_html=True)
    st.write(" ")

    articoli_unici = giacenze["Articolo"].unique().tolist()
    scelta_articolo = st.selectbox("Seleziona un Prodotto**:", articoli_unici)

    previsioni_prossime = previsioni[previsioni["Articolo"]==scelta_articolo]
    previsioni_prossime = previsioni_prossime[pd.to_datetime(previsioni_prossime["ds"])>oggi]
    previsioni_prossime = previsioni_prossime[["ds","Articolo","Quantità"]].groupby(["Articolo","ds"]).sum().reset_index()
    previsioni_prossime['Forecast cumulato'] = previsioni_prossime['Quantità'].cumsum()


    giacenza_articolo = giacenze[giacenze["Articolo"]==scelta_articolo]
    giacenza = int(giacenza_articolo["Quantità_giacenza"].iloc[0])

    if len(previsioni_prossime[previsioni_prossime["Forecast cumulato"] > giacenza_articolo["Quantità_giacenza"].iloc[0]])>0:
        stockout_date = str(min(
            previsioni_prossime[previsioni_prossime["Forecast cumulato"] > giacenza_articolo["Quantità_giacenza"].iloc[0]][
                "ds"]))[:10]
        st.warning("Periodo previsto prossimo stockout è " + stockout_date)
    else:
        st.success("Non è stato rilevato pericolo di stockout!")


    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=previsioni_prossime['ds'],
        y=previsioni_prossime['Forecast cumulato'],
        mode='lines+markers',
        name='Forecast Cumulato',
        line=dict(color='blue')
    ))
    fig3.add_trace(go.Scatter(
        x=previsioni_prossime['ds'],  # Stessa asse X del forecast cumulato
        y=[giacenza] * len(previsioni_prossime),  # Ripetiamo la giacenza per ogni punto temporale
        mode='lines',
        name='Giacenza',
        line=dict(color='red', dash='dash')
    ))

    # Personalizzazione del layout
    fig3.update_layout(
        title='Forecast Cumulato e Giacenza',
        xaxis_title='Data',
        yaxis_title='Quantità',
        showlegend=True,
        plot_bgcolor ="#f5f5f5",
        paper_bgcolor='#f5f5f5'      # Sfondo bianco per l'area esterna

    )

    # Mostriamo il grafico
    st.plotly_chart(fig3)




    st.write(" ")
    st.write(" ")
    st.divider()

    st.markdown("<div class='title-container'>Inventario</div>", unsafe_allow_html=True)
    st.write(" ")


    giacenze['Quantità_giacenza'].fillna(0, inplace=True)
    top_10 = giacenze.sort_values(by="Quantità_giacenza",ascending=False).head(10)

    articoli_unici = giacenze["Articolo"].unique().tolist()
    articoli_unici.append("Tutti")
    scelta_prodotto = st.multiselect("Seleziona uno o più **Prodotti**:", articoli_unici,default="Tutti")

    if "Tutti" in scelta_prodotto:
        giacenze_scopo = giacenze
    else:
        giacenze_scopo = giacenze[giacenze["Articolo"].isin(scelta_prodotto)]

    fig = px.bar(giacenze_scopo, x='Articolo', y='Quantità_giacenza',
                 labels={'Quantità_giacenza': 'Quantità_giacenza'},
                 color='Quantità_giacenza',
                 color_continuous_scale=['#ceadde', '#ceadde'])  # Red color
    # Adjust the layout for responsiveness
    fig.update_layout(
        xaxis_title='',
        yaxis_title='Quantità_giacenza',
        xaxis_tickangle=-45,
        height=600,  # You can adjust this as needed
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False,  # Hide the legend,
        coloraxis_showscale=False,
        xaxis=dict(showticklabels=False)  # Hide the labels on the X axis
        # Adjust margins for responsiveness
    )

    col1, col2 = st.columns([2, 1])  # 1:3 ratio to give more space to col2
    st.plotly_chart(fig, use_container_width=True)  # Make the chart responsive
    st.markdown("<div class='subtitle-container'>Dati Raw</div>", unsafe_allow_html=True)
    st.dataframe(giacenze.reset_index(drop=True)[["Articolo","Quantità_giacenza"]],width=1200)

    st.divider()




