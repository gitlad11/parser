import requests
from bs4 import BeautifulSoup
import config
import json

city = config.city
api_key = config.api_key

url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + api_key + "&q=" + city

req = requests.get(url)
if req == 404:
    print('город был ненайден')
if req == 401:
    print('вы не авторизованы')

data = req.json()
print(data)
with open('dump.json', 'w') as jf:
    json.dump(data , jf)