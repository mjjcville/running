#Oura Ring integration
#Interesting data:
#contributors:
#   deep_sleep
#   efficiency
#   latency
#   rem_sleep
#   restfulness
#   timing
#   total_sleep
#score
#timestamp"

import requests
import json
from configparser import ConfigParser


config = ConfigParser()
config.read('./config/running_config.cfg')

API_TOKEN = config.get('ouraring', 'api_token')
BASE_URL = config.get('ouraring', 'base_url')

def find_sleep_data(activity_start_date: str, activity_end_date) -> dict[str, float]:
    params={ 
        'start_date': activity_start_date, 
        'end_date': activity_end_date 
    }
    headers = { 
        'Authorization': 'Bearer {}'.format(API_TOKEN) 
    }
    
    sleep_range_url = '{}usercollection/sleep'.format(BASE_URL)
    headers = { 
        'Authorization': 'Bearer {}'.format(API_TOKEN) 
    }

    response = requests.request('GET', sleep_range_url, headers=headers, params=params) 
    sleep_range_json = response.json()
    sleep_data_list = []
    for sleep_data in sleep_range_json['data']:
        sleep_url = '{}usercollection/sleep/{}'.format(BASE_URL,sleep_data['id'])
        response = requests.request('GET', sleep_url, headers=headers, params=params) 
        breakpoint()
        sleep_data_list.append(response.json())
        for key in response.json():
            print(key)
    return {
        'data': sleep_data_list
    }

result = find_sleep_data("2023-11-01", "2023-11-20")
breakpoint()
