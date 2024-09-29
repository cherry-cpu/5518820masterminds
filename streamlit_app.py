import streamlit as st

# https://github.com/cherry-cpu/5518820masterminds/blob/main/buy.py

if 'logs' not in st.session_state:
    st.session_state['logs']=[]
if 'sell_data' not in st.session_state:
    st.session_state['sell_data']=[]

pages=st.navigation([st.Page('buy.py',title='Buy'),st.Page('sell.py',title="Sell"),st.Page('t1.py',title='T1')])
pages.run()
