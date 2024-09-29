import streamlit as st
from sm_api import last_price
from datetime import datetime
import pandas as pd
from time import sleep

#df=pd.DataFrame(st.session_state['logs'],columns=['Buy Id','Time Stamp','Stock','Price','No.of Shares','Total Price'])
#sdf=st.dataframe(df, hide_index=True)

def sell_action(i):
    print(i[0])
    print(i[1])
    print(i[2])
    print(i[3])


for i in st.session_state['logs']:
    with st.popover(f"{i[0]}--------{i[2]}___{i[3]}_____{i[4]}"):
        st.metric(i[1], last_price(i[2]))
        sell_nos=st.number_input('Sell', key=f'sell_inp_{i[0]}', step=1, min_value=1)
        st.button('Sell', key=f'sell_btn_{i[0]}', on_click=sell_action, args=[i])


sleep(5)
st.rerun()
