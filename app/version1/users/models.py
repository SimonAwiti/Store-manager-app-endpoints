"""
models file for the app
import re
import datetime
from flask import jsonify, session

class User(object):
    User Class


    def __init__(self):
        Initialize empty Product list
        self.products_list = []
        self.notfound = None

    def create_user(self, username, email, password, userRole):
        Create users
        if not self.valid_username(username):
            if not self.valid_email(email):
                self.cur.execute(
                        "INSERT INTO users(username, email, password, userRole) VALUES(%s, %s, %s,%s);", (
                         username, email, password, userRole))
                self.connect.commit()
                return jsonify({"message": "Registration Successful"}), 201
        else:
            return jsonify({"message": "Username or Email already in use."}), 400

    def login(self, username, password):
        "login users
        if not self.valid_username(username):
            return jsonify({"message": "Please register first."}), 401
        self.cur.execute("SELECT * FROM users WHERE username='%s'\
        AND password='%s'"%username, password)
        if self.cur.rowcount > 0:
            rows = self.cur.fetchall()
            for user in rows:
                user_id = user[0]
                username = user[1]
                email = user[4]
                userRole = user[5]
                session['token'] = jwt.encode({'userid': user_id,
                                               'username': username, 'userrole': userRole,
                                               'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                                              'SECRET_KEY', algorithm='HS256')
                return jsonify({
                    "message": "You are successfully logged in"}), 200
        return jsonify({
            "message": "Wrong username or password"}), 403
    def valid_username(self, username):
        check if username exist"
        self.cur.execute("SELECT * FROM users WHERE username='%s'"%username)
        numrows = self.cur.rowcount
        if numrows > 0:
            return True
        return False

    def valid_email(self, email):
        check if email exist"
        self.cur.execute("SELECT * FROM users WHERE email='%s'"%email)
        numrows = self.cur.rowcount
        if numrows > 0:
            return True
        return False
        """
