import requests
import config
import json
import vk_api
from vk_api.utils import get_random_id
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

email = config.email
password = config.password 
session = requests.Session()
session.verify = False

vk_session = vk_api.VkApi(login=email, password=config.password)
vk_session.auth(token_only=True)
print(vk_session.token)

vk = vk_session.get_api()
print(vk.account.getProfileInfo())
print(vk.account.getAppPermissions())
try:
    vk.messages.send(user_id= config.userid, message="{}".format(data),random_id=get_random_id())
except Exception:
    print('Нет доступа к сообщениям')
    vk.friends.add(user_id=config.userid)

#res = session.post("https://vk.com/login", data={'email' : email , 'password' : password})
#res.raise_for_status()

#print(res.status_code)

#res = session.get("https://vk.com/feed")

