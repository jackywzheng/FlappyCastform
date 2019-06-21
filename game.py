import pygame, math, requests, json, datetime, time
from random import randint

# pygame.init()


class Castform:
    def __init__(self, dead, score):
        self.dead = False
        self.score = 0


response = requests.get(
    'http://api.openweathermap.org/data/2.5/weather?id=6173331&appid=7a6a3241bdbca3c2360a5fa098746f30')
response.raise_for_status()
vancouver_weather = json.loads(response.text)

if vancouver_weather in ('Rain', 'Drizzle', 'Thunderstorm'):
    print('Rain', 'Drizzle', 'Thunderstorm')
elif vancouver_weather == 'Clouds':
    print("Clouds")
elif vancouver_weather == 'Snow':
    print("Snow")
elif datetime.datetime.now().hour < 6 or datetime.datetime.now().hour > 18:
    print("Night")
else:
    print("Day")