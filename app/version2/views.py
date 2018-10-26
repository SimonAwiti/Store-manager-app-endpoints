from flask import Flask, jsonify, Blueprint, request, make_response
#from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime
from app.version2.models import Users, Product
from app.version1.users.validateusers import validate_data_login
from app.version1.products.validateproducts import validate_products_data

userObject = Users()
ProductsObject = Product()

version2users_blueprints = Blueprint('version2users', __name__, url_prefix='/api/v2/users')
version2products_blueprints = Blueprint('version1', __name__, url_prefix='/api/v2/products')

@version2users_blueprints.route('admin/register', methods=['POST'])
def reg_admin():
  """method to place an order"""
  data = request.get_json()
  response = validate_data_login(data)
  username = data['username']
  password = data['password']
  confirmpass = data['confirmpass']
  userrole = data['userrole']
  if response == "valid":
    if userrole.lower() == 'administrator':
      return userObject.create_admin(username, password, confirmpass, userrole)
    return jsonify({"message":"User role can only be administrator"})
  return jsonify({"message":response}), 400

@version2users_blueprints.route('/register', methods=['POST'])
#@jwt_required
def signup():
    """Admin can add a new attendant"""
    data = request.get_json()
    response = validate_data_login(data)
    username = data['username']
    password = data['password']
    confirmpass = data['confirmpass']
    userrole = data['userrole']
    if response == "valid":
      if userrole.lower() == 'administrator':
        return userObject.reg_attendant(username, password, confirmpass, userrole)
      return jsonify({"message":"User role can only be administrator"})
    return jsonify({"message":response}), 400

@version2users_blueprints.route('/login', methods=['POST'])
def login():
    """ Method to login user """
    data = request.get_json()
    response = validate_data_login(data)
    if response == "valid":
        username = data['username']
        password = data['password']
        response = userObject.login(username, password)
        return response
    return jsonify({"message": response}), 401

@version2products_blueprints.route('/', methods=['GET', 'POST'])
def post_product():
    """posting a new product"""

    if request.method == 'GET':
        response = ProductsObject.get_all_products()
        return response

    if request.method == 'POST':
        data = request.get_json()
        response = validate_products_data(data)
        if response == "valid product":
            description = data['description']
            quantity = data['quantity']
            price_per_unit = data['price_per_unit']
            total_cost = quantity * price_per_unit
            response = ProductsObject.create_product(
                description, quantity, price_per_unit, total_cost)
            return response
    data = ProductsObject.get_all_products()
    return data

@version2products_blueprints.route('/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def product_manipulation(product_id, **kwargs):
    """ GET/PUT/DEL product """
    if request.method == 'DELETE':
        response = ProductsObject.delete_product(product_id)
        return response

    elif request.method == 'PUT':
        data = request.get_json()
        description = data['description']
        quantity = data['quantity']
        price_per_unit = data['price_per_unit']
        total_cost = quantity * price_per_unit
        response = ProductsObject.edit_product(
            product_id,
            description,
            quantity,
            price_per_unit,
            total_cost)
        return response
    else:
        response = ProductsObject.get_product(product_id)
        return response
        