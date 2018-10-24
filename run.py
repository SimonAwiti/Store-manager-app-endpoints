import os
"""Runn the app"""
# local import
from app import create_app

config = os.getenv('APP_SETTINGS', 'development')
app = create_app('development')

