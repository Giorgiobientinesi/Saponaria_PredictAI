import streamlit as st

st.set_page_config(layout="centered")

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
    width:50%;
    margin:0 auto;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
    font-size: 1.5rem;
    font-weight: bold;
    color: #000000; /* Colore blu di Apple */
    text-align: center;
    padding: 0.5rem;
    border-radius: 0.5rem;
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.1);
    background-color: #c7c7c7; /* Colore di sfondo grigio chiaro */
}
</style>
"""

st.markdown("""
    <style>
    body {
        zoom: 1.1; /* Regola il valore per impostare lo zoom, 1.0 è il 100%, 1.2 è il 120% */
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
            padding-top: 10px;
        }
    </style>
    """, unsafe_allow_html=True)



# Inseriamo lo stile del titolo nel frontend usando st.markdown()
st.markdown(title_style, unsafe_allow_html=True)
# Contenuto principale
st.markdown("<div class='title-container'>Login Page</div>", unsafe_allow_html=True)
st.write(" ")
st.write(" ")

if 'Light' not in st.session_state:
    st.session_state['Light'] = 'red'

if st.session_state['Light'] == 'red':
    user = st.text_input(label="Username",value="",key="user")
    password = st.text_input(label="Password",value="",key="password")

    push_credentials = st.button("Login")

    if push_credentials:
        if user =="admin" and password =="admin":
            st.write("Accesso Consentito! Ora puoi visualizzare ogni tab della dashboard!")
            st.session_state['Light'] = 'green'
        else:
            st.error("Username o Password non corretti!")

else:
    st.write(" ")
    st.write(" ")
    st.write("Hai effettuato l'accesso come La Saponaria. Ora puoi visualizzare le tab.")