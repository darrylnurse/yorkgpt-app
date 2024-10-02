import json
import requests
import os
import re

class DataHelper:

    @staticmethod
    def get_data(endpoints, base_url):
        responses = []

        for endpoint in endpoints:
            try:
                response = requests.get(base_url + endpoint)
                response.raise_for_status()
                data = response.json()
                responses.append(data)
            except requests.RequestException as e:
                print(f"Error fetching data from {endpoint}: {e}")
                continue
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {endpoint}: {e}")
                continue

        return responses
    
    @staticmethod
    def find_values(json_obj, *keys):
        values = []

        if isinstance(json_obj, dict):
            for k, v in json_obj.items():
                if k in keys and isinstance(v, str):
                    trimmed_value = v.strip()
                    if trimmed_value.endswith('.'):
                        values.append(trimmed_value)
                if isinstance(v, (dict, list)):
                    values.extend(DataHelper.find_values(v, *keys))
        elif isinstance(json_obj, list):
            for item in json_obj:
                values.extend(DataHelper.find_values(item, *keys))

        return values
    
    @staticmethod
    def read_txt_file(file_name):

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path =  os.path.join(dir_path, file_name)

        with open(file_path, 'r') as file:
            lines = file.readlines()

        return [line.strip() for line in lines]
    
    @staticmethod
    def is_valid_string(text):

        return re.match(r'^[A-Za-z.,\s]+$', text) is not None