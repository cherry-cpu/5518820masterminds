import requests as r
h={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
}
r1=r.get('https://www.nseindia.com', headers=h)
cookies=r1.cookies
def last_price(symbol):
    res=r.get(f'https://www.nseindia.com/api/quote-equity?symbol={symbol}', headers=h,cookies=cookies)
    return res.json()['priceInfo']['lastPrice']

# res=s.get(f'https://api.nasdaq.com/api/quote/{symbol}/info?assetclass=stocks', headers=h)
# return res.json()['data']['primaryData']['lastSalePrice']
