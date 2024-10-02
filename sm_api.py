import requests as r
#h={
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#    'Accept-Encoding': 'gzip, deflate',
#    'Accept': '*/*',
#    'Connection': 'keep-alive',
#}
s=r.Session()
s.get('https://www.nseindia.com', headers=h)

def last_price(symbol):
#    global s
#    s=r.Session()
    h={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    }
 #   s.get('https://www.nseindia.com', headers=h)
 #   res=s.get(f'https://www.nseindia.com/api/quote-equity?symbol={symbol}', headers=h)
    res=s.get(f'https://api.nasdaq.com/api/quote/{symbol}/info?assetclass=stocks', headers=h)
#    return res.json()['priceInfo']['lastPrice']

    return res.json()['data']['primaryData']['lastSalePrice']
