from src.utilities.api_call_utility import ApiCallUtility
# import logging as logger
# User class which contains all the variables and methods related to Post

class Post(object):
    # Constructor
    def __init__(self):
        self.api_call_utility = ApiCallUtility()
        self._endpoint = None

    # This function is for getting all the post posted by a user using userId of the user
    def get_posts_by_user_id(self, user_id):
        self._endpoint = "posts?userId=" + str(user_id)
        posts = self.api_call_utility.get(self._endpoint)
        return posts
