'''Creating app initializer'''
import os
from flask import Flask

'''creating app'''
def create_app():
    app = Flask(__name__)
    return app
