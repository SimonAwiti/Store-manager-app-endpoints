import psycopg2
from flask import request, jsonify, make_response
#from flask_jwt_extended import create_access_token

from flask import current_app
from app.version2.database import connectdb

class Users():

    def invalid_user(self, username):
        """Checks if user exists"""
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%(username)s",\
         {'username':username})
        rows = cursor.rowcount
        if rows > 0:
            return True
        return False

    def create_admin(self, username, password, confirmpass, userrole):
        """Create admin"""
        if self.invalid_user(username):
            return jsonify({"message" : "Username already taken"}),400
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        #if admin already exists
        cursor.execute("SELECT * FROM users WHERE userrole=%(userrole)s",\
            {"userrole":userrole})
        available = cursor.fetchall()
        if available:
            return make_response(jsonify({"Message" : "administrator exists"})), 400
        cursor.execute("INSERT INTO users (username, password, confirmpass, userrole) \
            VALUES (%(username)s,%(password)s,%(confirmpass)s,%(userrole)s);",\
            {'username':username,'password':password, \
            'confirmpass':confirmpass,'userrole':userrole})
        connection.commit()
        return make_response(jsonify({"message":"Administrator created"}), 201)

    """manupilate users"""
    def login_user(self, username, password):
        """sings in a user"""
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        
        try:
            get_user = "SELECT username, password, administrator \
                        FROM users \
                        WHERE username = '" + username + "' AND password = '" + password + "'"
            connection = connectdb.dbconnection()
            cursor = connection.cursor()
            cursor.execute(get_user)
            row = cursor.fetchone()
            if row is not None:                
                #access_token = create_access_token(identity={"username": row[0] , "administrator": row[2]})
                response = jsonify({"message":"User Successfully logged in", "access_token":"access_token"})
                response.status_code = 200
                return response
            response = jsonify({"message" : "No details found"})
            response.status_code = 401
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print("DB Error")
            print(error)
            response = jsonify({'message':'Database issues at hand'})
            response.status_code = 400
            return response
            