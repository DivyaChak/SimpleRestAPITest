import src.config.api_config
import requests
import os


class ApiCallUtility(object):
    def __init__(self):
        self._env = os.environ.get('ENV', 'test')
        self._base_url = src.config.api_config.API_URLS[self._env]

    def get(self, endpoint):
        url = self._base_url + endpoint
        response = requests.get(url)
        return response
