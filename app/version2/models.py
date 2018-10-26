import os
import psycopg2
from flask import request, jsonify, make_response
#from functools import wraps
#from flask_jwt_extended import create_access_token

from flask import current_app
from app.version2.database import connectdb

class Users():

    def invalid_user(self, username):
        """Checks if user exist in the db"""
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%(username)s",\
         {'username':username})
        rows = cursor.rowcount
        if rows > 0: #if the number of such users are in the row
            return True
        return False

    def is_administrator(self, username):
        """looking if the user is administrator"""
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%(username)s",\
            {"username":username})
        response = cursor.fetchone()#looks for the role of admin in the db using the name
        if response.lower() == 'administrator':
            return True
        return False

    def create_admin(self, username, password, confirmpass, userrole):
        """Create admin"""
        if password != confirmpass:
            return jsonify({"message" : "Password not matching"}),401
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

    def reg_attendant(self, username, password,confirmpass, userrole):
        """creating attendant"""
        #if self.is_administrator is False:
            #return jsonify({"message" : "only admin can add a user"}),401
        if password != confirmpass:
            return jsonify({"message" : "Password not matching"}),401
        if self.invalid_user(username):
            return jsonify({"message":"Username already taken"}),400
        else:
            connection = connectdb.dbconnection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password, confirmpass, \
                 userrole) VALUES (%(username)s,%(password)s,\
                %(confirmpass)s,%(userrole)s);",\
                {'username':username,'password':password,'confirmpass':confirmpass,\
                'userrole':userrole})
            connection.commit()
            return make_response(jsonify({"message":"user created successfully"}), 201)

    def login(self, username, password):
        if self.invalid_user(username):
            connection = connectdb.dbconnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%(username)s \
                and password=%(password)s",{'username':username, 'password':password})
            user = cursor.fetchone()
            if user:
                return jsonify({"create token":"to be created"}), 200
            return jsonify({"message":"Wrong password"})
        return jsonify({"message":"No such user name, register first"})

class Product():

    def product_existing(self, description):
        """check if the product exists already"""
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE description=%(description)s",\
        {"description":description})
        available = cursor.fetchall()
        if available:
            return True
        return False

    def create_product(self, description, quantity, price_per_unit, total_cost):
        """Create new product"""
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        if self.product_existing(description):
            return make_response(jsonify({"Message":"Product has been added already"})), 200
        cursor.execute("INSERT INTO products (description, quantity, price_per_unit, total_cost)\
         VALUES (%(description)s, %(quantity)s, %(price_per_unit)s, %(total_cost)s);",\
         {'description' : description, 'quantity':quantity,'price_per_unit': price_per_unit, 'total_cost': total_cost})
        connection.commit()
        return make_response(jsonify({"message":"Product added succesfully"}),201)
