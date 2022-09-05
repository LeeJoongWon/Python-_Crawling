# API를 이용하여 전세계 날씨정보 얻기

import requests

import json

-> 파이썬의 requests ,json 모듈을 사용합니다

전세계의 날씨정보를 API로 제공하는 사이트입니다 (회원가입 필요) 

https://openweathermap.org/

가입 후 My API keys로 들어가서 API key 값을 확인합니다

확인한 키값을 복사해서 코드내의 apikey 변수에 넣으세요

apikey = "API키 값을 입력하세요"

cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

-> 날씨정보를 확인하고 싶은 도시명을 입력하세요

-> api에는 api를 제공하는 제공자가 알려준 방식대로 데이터를 요청해야됩니다

# 아래의 페이지를 참고하세요
  
https://openweathermap.org/current

k2c = lambda k : k - 273.15

->켈빈온도를(절대온도) 섭씨온도로 변환합니다

for name in cities:

url = api.format(city=name, key=apikey)

r = requests.get(url)

data = json.loads(r.text)

->cities 변수에 들어있는 도시 수 만큼 반복합니다

api.format은

(api = api.openweathermap.org/data/2.5/weather?q={city}&APPID={key})

에서 {city}에는 cities에 들어있는 도시가 , {key}에는 apikey에 넣은 apikey값이 들어갑니다)

그 후에 url에 넣습니다

r = requests.get(url) 으로 api요청을 보냅니다

json형식의 파일로 로드하고 data 변수에 저장합니다

data 변수에는 아래 내용이 저장될껍니다

'coord': {'lon': 126.9778, 'lat': 37.5683}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 294.62, 'feels_like': 294.49, 'temp_min': 293.81, 'temp_max': 295.86, 'pressure': 1011, 'humidity': 64, 'sea_level': 1011, 'grnd_level': 1004}, 'visibility': 10000, 'wind': {'speed': 2.95, 'deg': 147, 'gust': 3.31}, 'clouds': {'all': 75}, 'dt': 1622437942, 'sys': {'type': 1, 'id': 8105, 'country': 'KR', 'sunrise': 1622405587, 'sunset': 1622458002}, 'timezone': 32400, 'id': 1835848, 'name': 'Seoul', 'cod': 200}

* data에 들어있는 내용중 필요한 정보를 출력합니다

print(" # 도시=", data["name"])

print(" | 날씨 =", data["weather"][0]["description"])

print(" | 최저 기온 =", k2c(data["main"]["temp_min"]))

print(" | 최고 기온 =", k2c(data["main"]["temp_max"]))

print(" | 습도 =", k2c(data["main"]["humidity"]))

print(" | 기압 =", k2c(data["main"]["pressure"]))

print(" | 풍향 =", data["wind"]["deg"])

print(" | 풍속 =", data["wind"]["speed"])
