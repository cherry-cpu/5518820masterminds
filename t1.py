import streamlit as st
import requests as r
h={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
}
s=r.Session()
symbol='SBIN'
s.get('https://www.nseindia.com', headers=h)
res=s.get(f'https://www.nseindia.com/api/quote-equity?symbol={symbol}', headers=h)
#resè=res.json()['priceInfo']['lastPrice']

st.write(res)
