import requests

city = input("Enter your city : ")

api = your_api_key

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid='+api

res = requests.get(url)

data = res.json()
temp = data['main']['temp']
wind_speed = data['wind']['speed']
description = data['weather'][0]['description']
latitude = data['coord']['lat']
longitude = data['coord']['lon']

print(f'Temperature: {temp} degree celcius')
print(f'Wind Speed :{wind_speed}')
print(f'Description: {description}')
print(f'Latitude: {latitude}')
print(f'Longitude: {longitude}')
# print(data)
