from src.utilities.api_call_utility import ApiCallUtility
# import logging as logger
# User class which contains all the variables and methods related to Comment

class Comment(object):
    # Constructor
    def __init__(self):
        self.api_call_utility = ApiCallUtility()
        self._endpoint = None

    # This function is for getting all comments of a specific post using postId of that post
    def get_comments_by_post_id(self, post_id):
        self._endpoint = "comments?postId=" + str(post_id)
        comments = self.api_call_utility.get(self._endpoint)
        return comments
