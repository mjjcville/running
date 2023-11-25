import requests
from configparser import ConfigParser


config = ConfigParser()
config.read('./config/running_config.cfg')

API_KEY = config.get('weatherapi', 'api_key')
BASE_URL = config.get('weatherapi', 'base_url')


def find_historical_weather(location_zip: str, activity_date: str)->dict[str, int]:

    history_url = BASE_URL + '/history.json?key={}&q={}&dt={}'.format(API_KEY, location_zip, activity_date)

    response = requests.get(history_url)

    weather_json = response.json()
   
    return { 
        'low_temperature': weather_json['day']['mintemp_f'],
        'humidity': weather_json['day']['avghumidity'],
        'wind': weather_json['day']['maxwind_mph']
    }

result = find_historical_weather('22901', '2023-11-20')

print(result)