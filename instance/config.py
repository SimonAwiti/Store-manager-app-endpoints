import os
from os import getenv


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    SECRET_KEY = "SECRET"
    #DATABASE_URL=
   

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}