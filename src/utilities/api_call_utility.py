import src.config.api_config
import requests
import os
import json
import logging as logger


class ApiCallUtility(object):
    def __init__(self):
        self._env = os.environ.get('ENV', 'test')
        self._base_url = src.config.api_config.API_URLS[self._env]


    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status code. Seached user/post/comment not present Expected {self.expected_status_code}, Actual status code: {self.status_code},URL: {self.url}"
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
        logger.debug(f"GET API response: {self.rs_json}")
        return self.rs_json
