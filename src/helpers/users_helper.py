from src.utilities.api_call_utility import ApiCallUtility


import logging as logger
# User class which contains all the variables and methods related to User


class User(object):
    # Constructor
    def __init__(self, username):
        self.api_call_utility = ApiCallUtility()
        self._endpoint = "users"
        self._username = username

    # This function is for getting userId of a user using the username of the user
    def get_user_id(self):
        payload={
            "username": self._username
        }
        user_details = self.api_call_utility.get(self._endpoint,payload)
        user_id = user_details[0]['id']

        return user_id


