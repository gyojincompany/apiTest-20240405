import requests
import json

import time

while True:
    url = "https://api.upbit.com/v1/ticker?markets=KRW-BCH"

    response = requests.get(url)

    # print(response.text)

    result = response.json()  # 리스트 타입으로 변환
    print(result[0]["trade_price"])
    time.sleep(2)







