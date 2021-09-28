# 663d60625ed2fd11657b88381354920d
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
import requests

city = 'Balashikha'
parametr = {'q': city, 'appid': '663d60625ed2fd11657b88381354920d' }

url = 'https://api.openweathermap.org/data/2.5/weather'

response = requests.get(url, params=parametr)
info = response.json()
out_file = open('data.txt', 'w', encoding="utf-8")
out_file.write(f'Населенный пункт: {info.get("name")} темпреатура {round((info.get("main").get("temp") - 273.15), 1)} градусов,\nCкорость ветра {round((info.get("wind").get("speed")), 0)} м/сек.')