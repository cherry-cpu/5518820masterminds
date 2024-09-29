import streamlit as st
from sm_api import last_price
from datetime import datetime
import pandas as pd

df=pd.DataFrame(st.session_state['logs'],columns=['Time Stamp','Stock','Price','No.of Shares','Total Price'])

sdf=st.dataframe(df, hide_index=True)

@st.experimental_dialog('ok')
def asd():
    def asdasd():
        print('asdasd')
    st.button('asdasd', on_click=asdasd)

st.button('Asd', on_click=asd)
def asdasd(i):
    print(f'asdasd {i}')

for i in st.session_state['logs']:
    print(i)
    with st.popover(i[1]):
        st.write(i)
        st.number_input('Sell', key=f'sell_inp_{i[0]}')
        st.button('Sell', key=f'sell_btn_{i[0]}')