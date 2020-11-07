from src.utilities.api_call_utility import ApiCallUtility


# import logging as logger
# User class which contains all the variables and methods related to User


class User(object):
    # Constructor
    def __init__(self):
        self.api_call_utility = ApiCallUtility()
        self._endpoint = None

    # This function is for getting userId of a user using the username of the user
    def get_user_id_by_username(self, username):
        self._endpoint = 'user?username=' + str(username)
        user_details = self.api_call_utility.get(self._endpoint)
        # logger.log(user_details)
        user_id = int(user_details[0]['id'])
        return user_id
