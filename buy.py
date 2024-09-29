import streamlit as st
from sm_api import last_price
from datetime import datetime
import pandas as pd

if 'logs' not in st.session_state:
    st.session_state['logs']=[('2024-09-29 20:52:32.632811', 'SBIN', 802.3, 1, 802.3), ('2024-09-29 20:52:32.903548', 'SBIN', 802.3, 1, 802.3), ('2024-09-29 20:52:35.073048', 'SBIN', 802.3, 1, 802.3), ('2024-09-29 20:52:42.143048', 'SBIN', 802.3, 1, 802.3)]      

symbol=st.text_input('Symbol', value="SBIN").upper()
no_of_shares=st.number_input('No.of Shares', min_value=1, step=1)

def buy():
    global symbol
    symbol=symbol.upper()
    price=last_price(symbol)
    total_price=price*no_of_shares
    data=(datetime.now().__str__(),symbol, price,no_of_shares, total_price)
    st.session_state['logs'].append(data)
    print(st.session_state['logs'])
check_price_btn=st.button('Check Price')
buy_btn=st.button('Buy', on_click=buy)
df=pd.DataFrame(st.session_state['logs'],columns=['Time Stamp','Stock','Price','No.of Shares',"Total Price"])
st.dataframe(df, hide_index=True)
