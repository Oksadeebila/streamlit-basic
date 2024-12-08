# Data frame
import pandas as pd
import streamlit as st

st.subheader('Nama Mahasiswa Lab Knowledge Engineering ')

st.metric(label="Temperature", value="28 C", delta="1.2 C")

df = pd.DataFrame({
    'Nama': ["Oksa Dwi Nabila", "Ros Dyana Dewi", "Anastia Firyal Nisrina", "Muhammad Irgi", "Annisa Salsabila Cahyani", "Raja Arrahman", "Zahra Fakhirah"],
    'Usia': [21, 21, 20, 20, 20, 19, 19]
})

st.dataframe(data=df, width=500, height=300)

st.table(data=df)
