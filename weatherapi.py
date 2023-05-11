import datetime as dt
import requests as req

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('apikey.txt','r').read() #need  git status a accountapikey on https://home.openweathermap.org/api_keys website
CITY = "Baku"


def  kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit  = celsius * (9/5) * 32
    return celsius, fahrenheit


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = req.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin =  response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time  = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time   = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])



print(f"Temperature in {CITY}: {temp_celsius:.2f}C or {temp_fahrenheit}F")
print(f"Temperature in {CITY} feels_like: {feels_like_celsius:.2f}")
print(f"Humidity  in {CITY}: {humidity}%")
print(f"Wind Speed   in {CITY}: {wind_speed}km")
print(f"SunRise  in {CITY}: {sunrise_time}")
print(f"SunSet  in {CITY}: {sunset_time}")
print(f"Description  in {CITY}: {description}")

#print(response)
