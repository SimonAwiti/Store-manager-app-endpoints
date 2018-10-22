'''test cases for sales records views'''
import unittest
import datetime
import json
from app import create_app
from app.version1.sales.models import SalesRec
from app.version1.users.models import User, users
from app.version1.users.views import SalesRec

class TestSalesRec(unittest.TestCase):
    """ Tests Records"""
    
    def setUp(self):
        '''instanciate tests'''
        app = create_app(config='testing')
        self.client = app.test_client()
        
        self.create_salesrecs = json.dumps(dict(
            description = "wall pass",
            date_sold = datetime.datetime.now(),
            quantity_sold = 4,
            unit_price = 90,
            bill = 360,
            attendant = "james kinn"))

        self.create_salesrecs2 = json.dumps(dict(
            #description = "wall pass",
            date_sold = datetime.datetime.now(),
            quantity_sold = 4,
            unit_price = 90,
            bill = 360,
            attendant = "james kinn"))

        self.client.post(
            '/api/v1/sales/',
            data=self.create_salesrecs,
            content_type='application/json')

    def test_create_salesrec(self):
        """ Test for sales records creation """
        resource = self.client.post(
            '/api/v1/sales/',
            data=self.create_salesrecs,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')
        print data
        self.assertNotIn((
            data.get("description"),
            data.get("date_sold"),            
            data.get("quantity_sold"),
            data.get("price_per_unit"),
            data.get("bill"),
            data.get("attendant")), data)
   
    def test_get_all_salesrecs(self):
        """ Test for getting all sales records """
        resource = self.client.get(
            '/api/v1/sales/',
            data=json.dumps(dict()),
            content_type='application/json')

        data = json.loads(resource.data.decode())
        print data
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')
        self.assertNotIn((
            data.get("description"),
            data.get("quantity"),
            data.get("price_per_unit"),
            data.get("total_cost")), data)

if __name__ == '__main__':
    unittest.main()
