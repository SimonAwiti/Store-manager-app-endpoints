import unittest

from app import create_app
from app.version2.database import connectdb

class DatabasCase(unittest.TestCase):
    """Unit testing the db connection"""
    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(config='testing')
        self.client = self.app.test_client
    
        with self.app.app_context():
            connectdb.dbconnection()
    
           