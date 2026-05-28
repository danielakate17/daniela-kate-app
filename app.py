import streamlit as st

st.title("Mi primera app")

nombre = st.text_input("¿Cómo te llamas?")

if nombre:
    st.write(f"Hola {nombre}, bienvenida a mi aplicación ❤️")
