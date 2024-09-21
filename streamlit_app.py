import streamlit as st
import matplotlib.pyplot as plt

st.title("Hello There")

fig,ax=plt.subplots()
ax.plot([1,2,3],[3,2,1])
st.pyplot(fig)
st.help(st.pyplot)
