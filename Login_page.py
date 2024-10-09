import streamlit as st
import warnings

# Disabilita i warnings
warnings.filterwarnings("ignore")
# Inizializza lo stato della variabile 'Light' se non esiste
if 'Light' not in st.session_state:
    st.session_state['Light'] = 'red'

# Se 'Light' è rosso, mostra il form di login
if st.session_state['Light'] == 'red':
    st.set_page_config(initial_sidebar_state="collapsed")  # Collassa la sidebar inizialmente
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
    st.markdown(title_style, unsafe_allow_html=True)
    st.markdown("<div class='title-container'>Login Page</div>", unsafe_allow_html=True)
    st.write(" ")

    user = st.text_input(label="Username", value="", key="user")
    password = st.text_input(label="Password", value="", key="password",type="password")

    if st.button('Login'):
        if user == "dashboard@predictai.it" and password == "predict_saponaria_2024":
            st.session_state['Light'] = 'green'  # Cambia lo stato a verde
            st.rerun()  # Ricarica la pagina per applicare il cambiamento
        else:
            st.error("Username o Password non corretti!")
else:
    st.set_page_config(initial_sidebar_state="expanded")  # Espandi la sidebar quando l'accesso è riuscito


    # Inserisci il logo nella sidebar
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

    # Inizializza la sidebar con uno sfondo personalizzato
    st.markdown("""
        <style>
            [data-testid=stSidebar] {
                background-color: #CEADDE;
                padding-top: 10px;
            }
        </style>
        """, unsafe_allow_html=True)

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
    st.markdown(subtitle_style, unsafe_allow_html=True)
    st.markdown("<div class='subtitle-container'>Hai effettuato l'accesso come La Saponaria!</div>", unsafe_allow_html=True)

