'''Creating app initializer'''
import os
from flask import Flask

def create_app():
    '''creating app'''
    app = Flask(__name__)

    '''importing and registering the blueprints'''
    from app.version1.products.views import version1_blueprints
    app.register_blueprint(version1_blueprints)

    return app
