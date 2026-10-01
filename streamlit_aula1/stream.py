import streamlit as st
import pandas as pd

st.write("Olá, mundo!")

nome = "Nina"
idade = 17

st.write(nome)
st.write(idade)

st.title("Meu primeiro dash")
st.subheader(nome)

df = pd.DataFrame({
'first column': ["Portugûes", "Matemática", "Python", "Frame"],
 'second column': [5, 9, 7, 10] }) 
df


