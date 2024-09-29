import streamlit as st

pages=st.navigation([st.Page('buy.py',title='Buy'),st.Page('sell.py',title="Sell"),st.Page('t1.py',title='T1')])
pages.run()
