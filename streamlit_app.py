import streamlit as st

st.text('Koushik')
if 'data' not in st.session_state:
    st.session_state['data']=[]

def make_data(n,t):
    st.session_state['data'].append([n,t])

with st.sidebar:
    with st.form(key='f'):
        name=st.text_input('name')
        type_=st.text_input('type')
        btn=st.form_submit_button('submit')
        if btn:
            make_data(name,type_)

st.dataframe(st.session_state['data'], column_config={1:'a',2:'b'}, use_container_width=True)
