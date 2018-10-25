from flask import Flask, jsonify, Blueprint, request, make_response
#from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime
from app.version2.models import Users
from app.version1.users.validateusers import validate_data_login

userObject = Users()

version2users_blueprints = Blueprint('version2users', __name__, url_prefix='/api/v2/users')

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
