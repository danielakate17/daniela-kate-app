import streamlit as st

st.title("Calculadora Básica")

num1 = st.number_input("Primer número")
num2 = st.number_input("Segundo número")

suma = num1 + num2

st.write("La suma es:", suma)
