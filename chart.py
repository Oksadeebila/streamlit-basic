import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=3)
st.pyplot(fig)
