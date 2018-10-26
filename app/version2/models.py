import os
import psycopg2
from flask import request, jsonify, make_response
from auth import admin_required
#from flask_jwt_extended import create_access_token

objectAdmin = admin_required
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

    def sign_attendant(self, username, password,confirmpass, userrole):
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
                return jsonify({"message":"Successful"}), 200
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
        if description == "" or quantity == "" or price_per_unit == "":
            return {'message':'Please fill in the missing field'}, 401

        # Checks for values less than 1
        if quantity < 1 or price_per_unit < 1:
            return {'message':'The inuts cannot be less than 1'}, 401
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        if self.product_existing(description):
            return make_response(jsonify({"Message":"Product has been added already"})), 200
        cursor.execute("INSERT INTO products (description, quantity, price_per_unit, total_cost)\
         VALUES (%(description)s, %(quantity)s, %(price_per_unit)s, %(total_cost)s);",\
         {'description' : description, 'quantity':quantity,'price_per_unit': price_per_unit, 'total_cost': total_cost})
        connection.commit()
        return make_response(jsonify({"message":"Product added succesfully"}),201)

    def get_all_products(self):
        """Gets all products in the list"""
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        all_products = []
        for product in products:
            info = {product[0]: {"category_id": product[1],
                                 "description": product[2],
                                 "quantity": product[4],
                                 "price_per_unit": product[5],
                                 "total_cost": product[5]}}
            all_products.append(info)
        return make_response(jsonify({"All products": all_products}), 200)

    def get_product(self, product_id):
        """Gets a particular product"""
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE product_id=%s", (product_id,))
        product = cursor.fetchall()
        if product != []:
            product = product[0]
            info = {product[0]: {"category_id": product[1],
                                 "description": product[2],
                                 "quantity": product[4],
                                 "price_per_unit": product[5],
                                 "total_cost": product[5]}}
            return make_response(jsonify({"product": info}), 200)
        return make_response(jsonify({"message": "No product with that id"}), 404)

    def edit_product(self, product_id, description, quantity, price_per_unit, total_cost):
        """Editing the product information"""
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE product_id=%(product_id)s",\
            {"product_id":product_id})
        product = cursor.fetchall()
        if product:
            cursor.execute("UPDATE  products SET description=%s, quantity=%s, \
            price_per_unit= %s, total_cost= %s WHERE product_id=%s",\
            (description, quantity, price_per_unit, total_cost))
            connection.commit()
            return make_response(jsonify({'message': 'modified succesfully'}), 200)
        return jsonify({"message":"No product with that id"})

    def delete_product(self, product_id):
        connection = connectdb.dbconnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE product_id=%(product_id)s",\
            {"product_id":product_id})
        product = cursor.fetchall()
        if product:
            cursor.execute("DELETE FROM products WHERE product_id=%(product_id)s",\
                {'product_id':product_id})
            connection.commit()
            return jsonify({'message': 'Product deleted '})
        return jsonify({"message":"No product with that id"}) 
