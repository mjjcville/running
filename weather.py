import requests
from configparser import ConfigParser


config = ConfigParser()
config.read('../config/running_config.cfg')

API_KEY = config.get('weatherapi', 'api_key')

