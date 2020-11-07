import pytest
from src.helpers.users_helper import User
from src.helpers.posts_helper import Post
from src.helpers.comments_helper import Comment
from src.utilities.email_validator_utility import validate_email
import logging as logger

username = "Delphine"
user_id = None


def test_search_user():
    global user_id
    user = User(username)
    user_id = user.get_user_id()
    logger.info(f"User {username} is present ")
    assert True

@pytest.mark.depends(on=['test_search_user'])
def test_search_posts():
    global user_id
    global all_posts_by_user
    post = Post()
    all_posts_by_user = post.get_post_ids_by_user_id(user_id)
    assert all_posts_by_user != None or len(all_posts_by_user) != 0, "No Post has been published by the user"
    logger.info(f"{len(all_posts_by_user)} no of posts made by the users")
    assert True


@pytest.mark.depends(on=['test_search_posts'])
def test_search_comments():
    global all_posts_by_user
    global all_emails
    emails = []
    comment = Comment()
    for postid in all_posts_by_user:
        all_comments = comment.get_comments_by_post_id(postid)
        assert all_comments != None or len(all_comments) != 0, "No Comment Posted on the post of the user"
        for comm in all_comments:
            emails.append(comm['email'])
    logger.info(f"Comments are present on the posts made by the user {username}")
    all_emails = set(emails)



@pytest.mark.depends(on=['test_search_comments'])
def test_validate_email_in_comments():
    global all_emails
    assert all_emails != None or len(all_emails) != 0, "No email found to evaluate"
    invalid_emails=[]
    for email in all_emails:
        if not validate_email(email):
            invalid_emails.append(email)
    assert len(invalid_emails) == 0, f"{invalid_emails} Not Valid Email"
    logger.info(f"{len(all_emails)} mails evaluated and all the emails are valid")

