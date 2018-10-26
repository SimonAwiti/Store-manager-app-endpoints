'''Creating app initializer'''
import os
from flask import Flask
#from datetime import timedelta
#from flask_jwt_extended import JWTManager, jwt_required
from instance.config import configuration
from app.version2.database.connectdb import initializedb

def create_app(config):
    '''creating app'''
 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configuration[config])
    app.secret_key = os.urandom(24)

    #secret = os.getenv('SECRET')
    #app.config['JWT_SECRET_KEY']= secret
    #app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
    #initialize jwt manager
    #jwt = JWTManager(app)
    #app.config.from_object(config[config_name])

    initializedb()
    
    '''importing and registering the blueprints'''
    from app.version2.views import version2users_blueprints, version2products_blueprints
    app.register_blueprint(version2users_blueprints)
    app.register_blueprint(version2products_blueprints)

    #from app.version1.users.views import version1_blueprints
    #app.register_blueprint(version1_blueprints)

    #from app.version1.users.views import version1sales_blueprints
    #app.register_blueprint(version1sales_blueprints)

    #from app.version1.users.views import version1users_blueprints
    #app.register_blueprint(version1users_blueprints)
    
    return app
    


