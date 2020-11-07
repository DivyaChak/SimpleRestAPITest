import pytest
from src.helpers.users_helper import User
from src.helpers.posts_helper import Post
from src.helpers.comments_helper import Comment
from src.utilities.email_validator_utility import validate_email


username = "Delphi"
user_id = None
def test_search_user():
    global user_id
    user=User(username)
    user_id=user.get_user_id()


@pytest.mark.depends(on=['test_search_user'])
def test_serach_posts():
    global user_id
    global all_posts_by_user
    post = Post()
    all_posts_by_user = post.get_post_ids_by_user_id(user_id)

@pytest.mark.depends(on=['test_serach_posts'])
def test_search_comments():
    global all_posts_by_user
    global all_emails
    emails = []
    comment = Comment()
    for postid in all_posts_by_user:
        all_comments = comment.get_comments_by_post_id(postid)
        for comm in all_comments:
            emails.append(comm['email'])
    all_emails = emails
@pytest.mark.depends(on=['test_search_comments'])
def test_validate_email_in_comments():
    global all_emails
    for email in all_emails:
        validate_email(email)