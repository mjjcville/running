import requests
from configparser import ConfigParser


config = ConfigParser()
config.read('./config/running_config.cfg')

API_KEY = config.get('weatherapi', 'api_key')
BASE_URL = config.get('weatherapi', 'base_url')
history_url = BASE_URL + '/history.json?key={}&q={}&dt={}'.format(API_KEY, '22901', '2023-11-19')

response = requests.get(history_url)

print (response)
