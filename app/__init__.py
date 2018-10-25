'''Creating app initializer'''
import os
from flask import Flask
#from flask_jwt_extended import jwt_manager, jwt_required
from instance.config import configuration
from app.version2.database.connectdb import initializedb

def create_app(config):
    '''creating app'''
 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configuration[config])
    app.secret_key = os.urandom(24)

    initializedb()
    
    '''importing and registering the blueprints'''
    from app.version2.views import version2users_blueprints
    app.register_blueprint(version2users_blueprints)

    from app.version1.users.views import version1_blueprints
    app.register_blueprint(version1_blueprints)

    from app.version1.users.views import version1sales_blueprints
    app.register_blueprint(version1sales_blueprints)

    from app.version1.users.views import version1users_blueprints
    app.register_blueprint(version1users_blueprints)
    
    return app
    


