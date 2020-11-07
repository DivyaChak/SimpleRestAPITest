import re

# Regular expression/Pattern for validating email
regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


# Validates email using the variable - regex. Return True if the email is valid else returns False
def validate_email(email):
    if re.search(regex, email):
        return True
    else:
        return False
