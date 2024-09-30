import streamlit as st
from sm_api import last_price

st.write(last_price('SBIN'))
