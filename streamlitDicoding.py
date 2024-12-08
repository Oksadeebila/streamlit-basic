import streamlit as st
import pandas as pd
st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)


df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.dataframe(data=df, width=500, height=150)
