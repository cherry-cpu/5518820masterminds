import streamlit as st
from sm_api import last_price
from datetime import datetime
import pandas as pd

symbol=st.text_input('Symbol', value="SBIN").upper()
no_of_shares=st.number_input('No.of Shares', min_value=1, step=1)

def timestamp_to_id(timestamp, symbol, nos):
    return '_'.join(timestamp.replace('-','_').split(':')).split('.')[0]+'_'+'_'.join(timestamp.replace('-','_').split(':')).split('.')[1][:2]+'_'+symbol+'_'+f'{nos}'

def buy():
    global symbol
    symbol=symbol.upper()
    price=last_price(symbol)
    total_price=price*no_of_shares
    time=datetime.now().__str__()
    buy_id=timestamp_to_id(time, symbol, no_of_shares)
    data=(buy_id,time,symbol, price,no_of_shares, total_price)
    st.session_state['logs'].append(data)
    print(st.session_state['logs'])

check_price_btn=st.button('Check Price')
buy_btn=st.button('Buy', on_click=buy)
df=pd.DataFrame(st.session_state['logs'],columns=['Buy Id','Time Stamp','Stock','Price','No.of Shares',"Total Price"])
st.dataframe(df, hide_index=True)
