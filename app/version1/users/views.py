"""creating bp routes for products"""
from flask import jsonify, Blueprint, request, make_response, session, redirect, url_for
from app.version1.users.models import User
from app.version1.products.models import Products
from app.version1.products.validateproducts import validate_data
#from app.version1.users.validateusers import validate_data_login, validate_data_signup

userObject = User()
ProductsObject = Products()



version1users_blueprints = Blueprint('version1users', __name__, url_prefix='/api/v1/users')
version1_blueprints = Blueprint('version1', __name__, url_prefix='/api/v1/products')

@version1_blueprints.route('/', methods=['GET', 'POST'])
def product():
    """ Method to create and retrieve product."""
    if not session.get("logged_in"):
        return make_response(jsonify({
        "Message": "You are not logged in!"
        }))
    
    if request.method == 'GET':
        response = ProductsObject.get_products()
        return response

    if session["username"] != "administrator":
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }))
    if request.method == "POST":
        data = request.get_json()
        response = validate_data(data)
        if response == "valid":
            description = data['description']
            quantity = data['quantity']
            price_per_unit = data['price_per_unit']
            total_cost = quantity * price_per_unit
            response = ProductsObject.create_product(
                description, quantity, price_per_unit, total_cost)
        return response
    data = ProductsObject.get_products()
    return data

@version1_blueprints.route('/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def product_manipulation(product_id, **kwargs):
    """ GET/PUT/DEL product """
    if not session.get("logged_in"):
        return make_response(jsonify({
        "Message": "You are not logged in!"
        }))
    if request.method == 'GET':
        response = ProductsObject.get_products()
        return response
    if session["username"] != "administrator":
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }))
    if request.method == 'DELETE':
        response = ProductsObject.delete_product(product_id)
        return response

    elif request.method == 'PUT':
        data = request.get_json()
        description = data['description']
        quantity = data['quantity']
        price_per_unit = data['price_per_unit']
        total_cost = quantity * price_per_unit
        response = ProductsObject.update_product(
            product_id,
            description,
            quantity,
            price_per_unit,
            total_cost)
        return response

    else:
        response = ProductsObject.get_product(product_id)
        return response

@version1users_blueprints.route('/login', methods=['GET', 'POST'])
def login():
    """Login users into their accounts"""
    if not session.get("logged_in"):
        request_data = request.get_json()
        if userObject.validate_user(request_data) == "Login Successful!":
            session["logged_in"] = True
            session["username"] = request_data["username"]
            return make_response(jsonify({
                "Message": "Login Successful!"
            }), 200)
        return make_response(jsonify({
            "Message": "Log in failed! Check your details!"
        }))
    return make_response(jsonify({
        "Message": "You are already logged in!"
    }))

@version1users_blueprints.route('/register', methods=['POST'])
def signup():
    """Admin can add a new attendant"""
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in"
        }))
    if session["username"] != "administrator":
        return make_response(jsonify({
            "Message": "You are not an admin"
        }))
    request_data = request.get_json()
    return make_response(jsonify({
        "Message": userObject.add_new_user(request_data)
    }))
