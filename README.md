"# SimpleRestAPITest"
This is simple framework is for testing API End Point -
https://jsonplaceholder.typicode.com/
But you can change the api url in the src/config/api_config.py file


WorkFlow of the tests -
1. It searches for user if that user present in API/Database
2. It Searches if any posts posted by that user
3. It seraches for comments made of each post made by the user
4. It validates emails of of every user who made comment

Directory Structure -
src : holdes all the neccessary modules to make call to api , fetch data , extract data and other utility functions
|--- config  -> api_config.py : api endpoint url is mentioned
|--- helper  -> comments_helper.py : includes class and methods related comment entity for fetching and extrcting data
|            -> posts_helper.py : includes class and methods related pots entity for fetching and extrcting data
|            -> user_helper.py : includes class and methods related user entity for fetching and extrcting data 
|--- utilities -> api_call_utility.py : makes get call to the api depending on the parameter passed and returns responce data
|              -> email_validator_utility.py : validates emails using regex 
|--- tests     -> test_user_comment_email_flow.py : tests the flow of execution      
|--- pytest.ini -> hold pytest config for logging
|--- requirement.txt -> all package details are there and used for installing the dependencies
|--- testReport.html -> its the latest test report ran against the user "Delphine"

How to use this program and run pytest
[Make sure python 3 (3.8.4) & pip are  already installed ]
1. Please install all packages using requirement.txt file
pip install requirements.txt 

2. After installation you good to run test 
pytest tests --log-cli-level=20 

3. And to generate report run
pytest --log-cli-level=20 --html=testReport.html


To run the test against a different user change the username variable value in the tests/test_user_comment_email_flow.py file





