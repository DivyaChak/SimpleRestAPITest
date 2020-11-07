import src.config.api_config
import requests
import os
import json
import logging as logger

# This class holds all the variables and methods for interacting with the api endpoint
class ApiCallUtility(object):
    # constructor
    def __init__(self):
        # reads the environment variable 'ENV' if not present take 'test' as a default value
        self._env = os.environ.get('ENV', 'test')
        #reads the api url for config file
        self._base_url = src.config.api_config.API_URLS[self._env]

    # that function checks the satus code and asserts
    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status code. Seached user/post/comment not present Expected {self.expected_status_code}, Actual status code: {self.status_code},URL: {self.url}"
   # get call to api end pint
    def get(self, endpoint=None, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self._base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        logger.debug(f"GET API response: {self.status_code}")
        self.assert_status_code()
        self.rs_json = rs_api.json()
        return self.rs_json