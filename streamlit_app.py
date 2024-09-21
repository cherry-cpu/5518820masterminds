import streamlit as st

st.title("Hello There, 121192051812913419")

import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.plot([1,2,3],[3,2,1])
st.pyplot(fig)
st.help(st.pyplot)
