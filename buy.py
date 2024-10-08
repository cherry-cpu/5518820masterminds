import streamlit as st
from datetime import datetime
import pandas as pd
from sm_api import last_price
from streamlit_app import *
from all_tools import *

if 'logs' not in st.session_state:
    st.session_state['logs']=[]

st.write(f"Username : {st.session_state['username']}")
st.write(f"User Id  : {st.session_state['user_id']}")

symbol=st.text_input('Symbol', value="SBIN").upper()
no_of_shares=st.number_input('No.of Shares', min_value=1, step=1)

if 'data' not in st.session_state:
    st.session_state['data']=[]

all_stock_names=[]
for stock_name in cur.execute(f"select stock from {st.session_state['username']}_{st.session_state['user_id']}_holdings").fetchall():
    all_stock_names.append(stock_name[0])
st.session_state['data']=set(all_stock_names)
def timestamp_to_id(timestamp, symbol, nos):
    return '_'.join(timestamp.replace('-','_').split(':')).split('.')[0]+'_'+'_'.join(timestamp.replace('-','_').split(':')).split('.')[1][:2]+'_'+symbol+'_'+f'{nos}'

def buy():
    global symbol
    symbol=symbol.upper()
    price=last_price(symbol)
    buy_action(st.session_state['username'],st.session_state['user_id'],stock_name=symbol, buy_price=price,no_of_shares=no_of_shares,current_holdings=no_of_shares, soldout_shares=0)

r=get_holdings_data(st.session_state['username'],st.session_state['user_id'])
print(r)

st.session_state['logs']=r
check_price_btn=st.button('Check Price')
buy_btn=st.button('Buy', on_click=buy)

df=pd.DataFrame(st.session_state['logs'],columns=['Buy Id','Time Stamp','Stock','Price','No.of Shares',"Total Price"])
st.dataframe(df, hide_index=True)
