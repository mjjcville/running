#Oura Ring integration

import requests
from configparser import ConfigParser


config = ConfigParser()
config.read('./config/running_config.cfg')

API_TOKEN = config.get('ouraring', 'api_token')
BASE_URL = config.get('ouraring', 'base_url')

def find_sleep_data(activity_start_date: str, activity_end_date) -> dict[str, float]:
    document_url = '{}usercollection/personal_info'.format(BASE_URL)
    params={ 
        'start_date': activity_start_date, 
        'end_date': activity_end_date 
    }
    headers = { 
        'Authorization': 'Bearer {}'.format(API_TOKEN) 
    }
    response = requests.request('GET', document_url, headers=headers, params=params) 
    print(response.text)
    
    document_json = response.json()
    breakpoint()
    document_id = document_json['id']
    print (f"document_id ?",document_id)

    sleep_url = '{}usercollection/daily_sleep/{}'.format(BASE_URL, document_id)
    headers = { 
        'Authorization': 'Bearer {}'.format(API_TOKEN) 
    }
    response = requests.request('GET', sleep_url, headers=headers, params=params) 
    print(response.text)
    
    return {
        'data': 5.1
    }

result = find_sleep_data("2023-11-19", "2023-11-20")

