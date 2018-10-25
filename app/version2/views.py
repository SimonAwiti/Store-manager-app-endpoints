from flask import jsonify, Blueprint, request, make_response, session, redirect, url_for
import datetime
from app.version2.models import Users
from app.version1.users.validateusers import validate_data_login

userObject = Users()

version2users_blueprints = Blueprint('version2users', __name__, url_prefix='/api/v2/users')

@version2users_blueprints.route('admin/login', methods=['POST'])
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

@version2users_blueprints.route('admin/login', methods=['POST'])
def login():
    """Login users into their accounts"""
    data = request.get_json()
    response = validate_data_login(data)
    if response == "valid":
        username = data['username']
        password = data['password']
        response = userObject.login_user(username, password)
        return response
    return jsonify({"message": response}), 401
