import streamlit as st
from sm_api import last_price
from datetime import datetime
import pandas as pd
from time import sleep

df=pd.DataFrame(st.session_state['logs'],columns=['Time Stamp','Stock','Price','No.of Shares','Total Price'])

sdf=st.dataframe(df, hide_index=True)

if 'aa' not in st.session_state:
    st.session_state['aa']=0

def asdasd(i):
    print(f'asdasd {i}')

for i in st.session_state['logs']:
    print(i)
    with st.popover(f"{i[0]}--------{i[1]}----{i[2]}---{i[3]}"):
        st.write(i)
        st.number_input('Sell', key=f'sell_inp_{i[0]}')
        st.button('Sell', key=f'sell_btn_{i[0]}')
        st.metric(i[1], st.session_state['aa'])
st.session_state['aa']+=1
sleep(2)
st.rerun()
