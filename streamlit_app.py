import streamlit as st

# https://github.com/cherry-cpu/5518820masterminds/blob/main/buy.py

pages=st.navigation([st.Page('user_page.py', title='User'),st.Page('buy.py',title='Buy'),st.Page('sell.py',title="Sell"),st.Page('t1.py',title='T1')])
pages.run()
