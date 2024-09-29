import streamlit as st
from sm_api import last_price
from datetime import datetime

if 'logs' not in st.session_state:
    st.session_state['logs']=[]

symbol=st.text_input('Symbol', value="SBIN").upper()
no_of_shares=st.number_input('No.of Shares', min_value=1, step=1)


def buy():
    global symbol
    symbol=symbol.upper()
    price=last_price(symbol)
    data=(datetime.now().__str__(),symbol, price,no_of_shares)
    st.session_state['logs'].append(data)

check_price_btn=st.button('Check Price')
buy_btn=st.button('Buy', on_click=buy)
st.table(st.session_state['logs'])
