'''Creating app initializer'''
import os
from flask import Flask

def create_app():
    '''creating app'''
    app = Flask(__name__)
    return app
