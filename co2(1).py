import requests
from bs4 import BeautifulSoup
import os
from pyquery import PyQuery as pq
from datetime import datetime, timedelta
import pandas as pd
import json
import numpy as np
from pandas import Series, DataFrame

url=('https://www.eex.com/data//view/data/detail/emission-eua-spot-v2/2019/02.05.json')
res=requests.get(url)
result=json.loads(res.text)
decoderJson = result['data'][0]['rows'][0]['data']

settlementprice  = decoderJson['settlementPrice']
lastTradeTime = decoderJson['lastTradeTime']

print('settlementprice is: ', settlementprice)
print('lastTradeTime is: ', lastTradeTime)