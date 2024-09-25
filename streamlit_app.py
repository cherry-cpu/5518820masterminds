import streamlit as st

import sqlite3

con=sqlite3.connect('data.db')
cur=con.cursor()
try:
    q='create table test1(username TEXT, password TEXT)'
    cur.execute(q)
    cur.execute('insert into test1 values("asd", "asd")')
    con.commit()
except:
    pass
if 'data' not in st.session_state:
    st.session_state['data']=[]

def make_data(n,t):
    st.session_state['data'].append([n,t])
    dat=cur.execute('select * from test1').fetchall()
    st.write(dat)

with st.sidebar:
    with st.form(key='f'):
        name=st.text_input('name')
        type_=st.text_input('type')
        btn=st.form_submit_button('submit')
        if btn:
            make_data(name,type_)

st.dataframe(st.session_state['data'], column_config={1:'a',2:'b'}, use_container_width=True)
