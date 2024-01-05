import json
import requests
from services.MakeRequest import MakeRequest
from services.Config import ConfigurationManager


class UserAccount:
    def __init__(self):
        self.token = ''
        self.api_url = ''
        self.config_data = {}

    def set_token(self, token):
        self.token = token

    def set_api_url(self, api_url):
        self.api_url = api_url

    def get_config_data(self):
        config_manager = ConfigurationManager()
        return config_manager.read_config()

    def get_api_url(self):
        return self.api_url

    def get_config_env(self):
        config_manager = ConfigurationManager()
        return config_manager.is_sandbox()

    def get_token(self):
        if not self.token:  # Only fetch token if it's not already set
            config_data = self.get_config_data()
            print(config_data)
            key_get = "ACCOUNT_INFO_SANDBOX" if self.get_config_env() else "ACCOUNT_INFO_LIVE"
            print("Key-Get ==> " + key_get)

            user = config_data[key_get]['account_number']
            password = config_data[key_get]['password']
            host = config_data[key_get]['host']
            port = config_data[key_get]['port']

            self.api_url = config_data['API']['url']
            path_token = config_data['API_REST']['path_connect']
            domain_get_token = self.api_url + path_token
            params_token = {
                'user': user,
                'password': password,
                'host': host,
                'port': port
            }
            headers = {
                "accept": "text/plain",
            }
            response = MakeRequest(domain_get_token, params_token, headers)
            self.set_token(response.text)
        return self.token

    def get_account_summary(self):
        token = self.get_token()

        config_data = self.get_config_data()
        api_url = config_data['API']['url']
        path_account_summary = config_data['API_REST']['path_account_summary']
        url = api_url + path_account_summary

        param = {
            "id": token
        }
        headers = {
            "accept": "text/plain",
        }
        res = MakeRequest(url, param, headers)
        return res.json()

    def get_account_opened_order(self):
        token = self.get_token()
        config_data = self.get_config_data()
        api_url = config_data['API']['url']
        path_account_summary = config_data['ORDER']['path_opened_order']
        url = api_url + path_account_summary

        param = {
            "id": token
        }
        headers = {
            "accept": "text/plain",
        }
        res = MakeRequest(url, param, headers)
        return res.json()
