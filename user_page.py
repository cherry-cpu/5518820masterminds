import streamlit as st
from all_tools import *

if 'username' not in st.session_state:
	st.session_state['username']=''
	st.session_state['user_id']=''

def user_action():
	st.session_state['username']=username
	st.session_state['user_id']=user_id
	create_user(username, user_id)
#	st.switch_page('buy.py')

username=st.text_input('Username')
user_id=st.text_input('User Id')
btn=st.button('Ok', on_click=user_action)
