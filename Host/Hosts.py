from services.MakeRequest import MakeRequest
from services.Config import ConfigurationManager


class Hosts:
    def __init__(self):
        self.token = ''
        self.api_url = ''
        self.config_data = {}

    def ping_host(self):
        config_data = self.get_config_data()
        api_url = config_data['API']['url']
        host = config_data['API_REST']['path_ping']
        url = api_url + host

        key_get = "ACCOUNT_INFO_SANDBOX" if self.get_config_env() else "ACCOUNT_INFO_LIVE"
        host = config_data[key_get]['host']
        param = {
            "host": host
        }
        headers = {
            "accept": "text/plain",
        }

        res = MakeRequest(url, param, headers)
        resp = {
            'host_ping': res.text,
            'host_name': host,
            'env': "Sandbox" if self.get_config_env() else "Live"
        }
        return resp

    def get_config_env(self):
        config_manager = ConfigurationManager()
        return config_manager.is_sandbox()

    def get_config_data(self):
        config_manager = ConfigurationManager()
        return config_manager.read_config()
