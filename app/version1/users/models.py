"""users data structures"""
import re 
import datetime

"""defining global variables"""
users = [{
            "user_id":0,
            "email": "theadmin@gmail.com",
            "username": "administrator",
            "password": "simon12",
            "role": "admin"
            }]
user_id = 1

class User:
    def __init__(self):
        """initializing user constructor"""
        self.email = ""
        self.username = ""
        self.password = ""
        self.role = ""

    @staticmethod
    def validate_details(details):
        """checks if the user details are relevant before registering"""
        if not details:
            return "Please enter data for registration"
        #if  bool(re.search(r'@', details["email"])) is False:
            #return "Your email should have an @ in it"
        for user in range(len(users)):
            if users[user]["email"] == details["email"]:
                return "Email already in use, register with another email"
        if details["role"] != "admin" and details["role"] != "attendant":
            return "You can only register as an admin or attendant"
        return True

    def add_new_user(self, details):
        """registering a new user"""
        # global variable
        global user_id
        # check details for data
        if not details:
            return "Please enter information for registration"
            # check validity of data
        if self.validate_details(details) is True:
            users.append({
                    "user_id": user_id,
                    "email": self.email,
                    "username": self.username,
                    "password": self.password,
                    "role": self.role
                })
            user_id += 1
            return "User added Successfully!"
        return "Ensure that the details are relevant before adding a user!"

    def get_users(self):
        """get all users"""
        if not users:
            return "There are no users registered!"
        return users

    def get_one_user(self, user_id):
        """fetch a specific user"""
        if isinstance(user_id, int) is False:
            return "User Id should be a number"
        for user in range(len(users)):
            if user_id != users[user]["user_id"]:
                continue
            return users[user]

    def validate_user(self, details):
        """validate user details while loging in"""
        if not details:
            return "Please enter data for registration"
        if not users:
            return "No registered users"
        for user in range(len(users)):
            if users[user]['username'] != details["username"] and users[user]['password'] != details["password"]:
                continue
            return "Login Successful!"

    def edit_user_role(self, user_id, role):
        """Admin changes attendant role to admin"""
        if not users:
            return "No registered users"
        if isinstance(user_id, int) is False:
            return "User Id should be a number"
        for user in range(len(users)):
            if user_id != users[user]["user_id"]:
                continue
            user["role"] = "administrator"
            return "Attendant was promoted to admin"
