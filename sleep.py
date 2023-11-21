#Oura Ring integration

import requests
from configparser import ConfigParser


config = ConfigParser()
config.read('./config/running_config.cfg')

API_TOKEN = config.get('ouraring', 'api_token')
BASE_URL = config.get('ouraring', 'base_url')

def find_sleep_data(activity_date: str) -> dict[str, float]:
    url = '{}usercollection/daily_activity'.format(BASE_URL)
    params={ 
        'start_date': '2023-11-01', 
        'end_date': '2023-11-02' 
    }
    headers = { 
        'Authorization': 'Bearer {}'.format(API_TOKEN) 
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    print(response.text)
    
    sleep_json = response.json()

    return {
        'data': 5.1
    }

result = find_sleep_data("2023-11-19")

