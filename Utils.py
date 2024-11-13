import streamlit as st
import base64

def add_logo():
    # Read and encode the SVG file in base64 format
    with open("assets/Logo.svg", "rb") as image_file:  # Replace with the actual path
        svg_base64 = base64.b64encode(image_file.read()).decode("utf-8")

    # Generate the CSS for the sidebar logo
    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"]::before {{
                content: "";
                display: block;
                margin-left: 20px;
                margin-top: 20px;
                width: 100%;
                height: 50px;
                background-image: url("data:image/svg+xml;base64,{svg_base64}");
                background-size: contain;
                background-repeat: no-repeat;
                position: relative;
                top: -10px;
            }}
            [data-testid="stSidebarNav"]::after {{
                content: "";
                font-size: 35px;
                font-weight: bold;
                margin-left: 10px;
                position: relative;
                top: -10px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )