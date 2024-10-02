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
    res=r.get(f'https://www.nseindia.com/api/quote-equity?symbol={symbol}', headers=h, cookies='<RequestsCookieJar[<Cookie nsit=5Tr0r7WOWkhbOFJfMi9IvVf- for www.nseindia.com/>, <Cookie nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcyNzg0NDY3MCwiZXhwIjoxNzI3ODUxODcwfQ.3IuxiurDKcrTI3_ZxoFALqLgnA3n5tEGiyQRpEe2qAQ for www.nseindia.com/>, <Cookie _abck=7CBF559000E1561AAF1990304B7A69D2~-1~YAAQTQosF2rbSy2SAQAAW1yRSwyS+MJJh81GdNGsgF2P6UxelkrDDAVNnGIY8M59+Eucq1NwkRhrF8v7faLtTFr9UNdJoDxjM7w/bWdGBdW8B6tIrJ8GjeYcbx8EZh/fLsJLlZ+hjC2W1mE1r5ucdXIBxn4A6ev5J0qxoVw9ERKesy0zuAu7WWmk/4E1hamQvSB/rpjp4IaiTHBwUtI+OKL7O/cMM5izcvbSK+Z9fk6O735zUI8vyznvs9pmzUQtCbDOSYw6Etmd4WDkNsYW9mKF74Ht5gXXc749lbzLwa/+p/Y5W4lvZUCrPNiWhVgDFtZVFBjpJYV9O00K701EfYSWJ/t6pENi4OojMIi34TQztDToVG669yvS4mK2DBGJAHF26lI+Az65/PT4Kpto8C5NxGtfKj2vpZscYdmz0Q==~-1~-1~-1 for .nseindia.com/>, <Cookie bm_sz=58AF66FBA85A40DC143A7ABB9B27CDE2~YAAQTQosF2vbSy2SAQAAW1yRSxkiAxlhRJ3v/4c7HcNzixSLt/Qgy+ZPbqYFbvrkjG5Ocx9E7xLSh2fdED/PxFlbxhIhwyhP3KvARtyJawwfbDim7q0xUl6JuwnT38dsetskL9T8ReSmTpr18nAM+MDLNfHPrvGTDqK6y4FfGF42GIT3vH5efYOeKhRU6PEJp8qdYdm1mz7qOFRWUx5UoqsFErcfsSm7EC4IN28TrHbyLBLJyEX5RnOQucUtek8+rJ4NihbUyo7fi6wZpb12xWWiItcRD9kW040+bBsSob+r9ACPz8KrB4ao0YlyyK3u3ICZKrm95+nZNHXIJYV4Bves3m1jKTJ5JD+CCrK0~4470836~3420470 for .nseindia.com/>]>')
    return res.json()['priceInfo']['lastPrice']
