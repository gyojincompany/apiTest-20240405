import requests

import pyupbit  # 파이썬용 upbit api 라이브러리


url = "https://api.upbit.com/v1/market/all?isDetails=false"

headers = {"accept": "application/json"}

res = requests.get(url, headers=headers)

result = res.json()

print(result[0]['market'])

coinTicker = pyupbit.get_tickers(fiat="KRW")

print(coinTicker)

