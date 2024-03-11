import json

import requests


class APIWrapper:
    PATH_JSON = r"C:\Users\mhmdh\Desktop\new_final\final_automation_project\final_project_code\config_api.json"

    def __init__(self):
        self.response = None
        self.my_request = requests
        self.load_config()

    def load_config(self):
        with open(self.PATH_JSON, 'r') as file:
            json_content = json.load(file)

        self.url = json_content.get('url')
        self.api_key = json_content.get('api_key')  # Add this line to load the API key
        self.text=json_content.get('words')



    def api_get_request(self, url,reqBody=None):
        headers = {'X-API-KEY': self.api_key}  # Add API key to the headers
        self.response = self.my_request.get(url, headers=headers)

        if self.response.ok:

            return self.response
        else:
            return self.response.status_code


    def api_post_request(self,url,reqBody):
        headers = {'X-API-KEY': self.api_key}  # Add API key to the headers
        self.response = requests.post(url, json=reqBody, headers=headers)
        if self.response.ok:

            return self.response
        else:
            return self.response.status_code




