"""creating bp routes for products"""
from flask import jsonify, Blueprint, request, make_response, session, redirect, url_for
from app.version1.users.models import User
#from app.version1.users.validateusers import validate_data_login, validate_data_signup

userObject = User()


version1users_blueprints = Blueprint('version1users', __name__, url_prefix='/api/v1/users')

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
