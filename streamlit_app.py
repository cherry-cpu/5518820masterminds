import streamlit as st
from random import random
from time import sleep
from threading import Thread
import requests
from streamlit.components.v1 import html

st.text_input('asda')

if not st.session_state.get('data'):
    st.session_state['data'] = []
data = st.session_state['data']
data.append(random())
if len(data) > 30:
    data = data[-30:]
st.session_state['data'] = data
st.line_chart(data)
if st.toggle("Show message"):
    st.write("Meggase")
d=['a','b','c']
dd=[]
def asd():
    global dd
    r=requests.get('https://meowfacts.herokuapp.com/')
    dd.append(r.json())
    return r.json()
for i in d:
    st.write(i)
t=[]
for j in range(50):
    t.append(Thread(target=asd))
for k in t:
    k.start()
for asd in t:
    asd.join()

st.write(dd)
print(dd)
st.text_input('asd')
st.markdown(
"""
<style>
#root > div:nth-child(1) > div.withScreencast > div > div > header > div.st-emotion-cache-15ecox0.ezrtsby0 > div.st-emotion-cache-19or5k2.en6cib61.StatusWidget-enter-done > div > img{
display:none;}
</style>
""",
    unsafe_allow_html=True,
)
sleep(5)
st.rerun()
