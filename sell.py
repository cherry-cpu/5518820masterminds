import streamlit as st
from sm_api import last_price
from datetime import datetime
import pandas as pd
from time import sleep
from all_tools import *

if 'sell_data' not in st.session_state:
    st.session_state['sell_data']=[]
df=pd.DataFrame(st.session_state['sell_data'],columns=['Buy Id','Time Stamp','Stock','Buy Price','Sell Price','No.of Shares'])
sdf=st.dataframe(df, hide_index=True)

stock_prices=stocks_thread(st.session_state['data'])
st.write(stock_prices)
def sell_action(i, sell_nos):
#    i[0]- buy_id   i[1]- time   i[2]- symbol   i[3]- price
#    print(f"i[2]=={i[2]}")
    data=[i[0],datetime.now().__str__(),i[2],i[3],stock_prices[i[2]],sell_nos]
    st.session_state['sell_data'].append(data)
    print('sell action')


stock_prices=stocks_thread(st.session_state['data'])

for i in st.session_state['logs']:
    with st.popover(f"{i[0]}--------{i[2]}___{i[3]}_____{i[4]}"):
        st.metric(label=i[1], value=stock_prices[i[2]])
        sell_nos=st.number_input('Sell', key=f'sell_inp_{i[0]}', step=1, min_value=1)
        st.button('Sell', key=f'sell_btn_{i[0]}', on_click=sell_action, args=[i, sell_nos])


sleep(10)
st.rerun()
