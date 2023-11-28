import requests
import json
def weather():
    city_name=input('Enter city name : ')
    api_key="5a3fd7537ce0abc9405aff0aa8e32d0e"
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city_name + "&units=metric&appid="+api_key)
    api = json.loads(api_request.content)
    current_temperature = api['main']['temp']
    print('Current Temperature :',current_temperature)
    humidity = api['main']['humidity']
    print('Humidity :',humidity)
    pressure = api['main']['pressure']
    print('Pressure:',pressure)
weather()
