def validate_data_signup(data):
    """validate user details"""
    try:
        # check if the username is more than 3 characters
        if len(data['username'].strip()) < 3:
            return "username must be more than 3 characters"
        # check if password has spaces
        elif " " in data["password"]:
            return "password should be one word, no spaces"
        # check if password is empty
        elif data["password"] == "":
            return "password required"
        # check if username has spaces
        elif " " in data["username"]:
            return "username should be one word, no spaces"
        # check if username is empty
        elif data["username"] == "":
            return "username required"
        # check if email has spaces
        elif " " in data["email"]:
            return "email should be one word, no spaces"
        # check if email empty
        elif data["email"] == "":
            return "email required"
        # check if user Role has spaces
        elif " " in data["role"]:
            return "user role should be one word, no spaces"
        # check if Role is empty
        elif data["role"] == "":
            return "user Role required"
        elif len(data['password'].strip()) < 5:
            return "Password should have atleast 5 characters"
        # check if the passwords match
        elif data['password'] != data['confirmpass']:
            return "passwords do not match"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)


def validate_data_login(data):
    """validate user details"""
    try:
        # check if the username is more than 3 characters
        if len(data['username'].strip()) < 3:
            return "username must be more than 3 characters"
        # check if password has spaces
        elif " " in data["password"]:
            return "password should be one word, no spaces"
        # check if password is empty
        elif data["password"] == "":
            return "password required"
        # check if username has spaces
        elif " " in data["username"]:
            return "username should be one word, no spaces"
        # check if username is empty
        elif data["username"] == "":
            return "username required"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
