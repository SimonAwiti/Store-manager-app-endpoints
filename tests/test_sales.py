'''test cases for sales records views'''
import unittest
import json
from app import create_app
from app.version1.sales.models import salesrec

class TestBase(unittest.TestCase):
    """ Tests Base """

    def create_app(self):
        """ Instantiate tests"""

class TestSalesrec(TestBase):
    """ Tests base"""
    
    def setUp(self):
        '''instanciate tests'''
        app = create_app()
        
        self.create_salesrecs = json.dumps(dict(
            description="wall pass",
            date_sold="1/1/2019",
            buyer_contact="0723445673",
            saler="james kinn"))

        self.create_salesrecs2 = json.dumps(dict(
            salesrec_id=2,
            description="nails",
            date_sold="1/1/2019",
            buyer_contact="0723445673",
            saler="james kinn"))

        self.client = app.test_client()
        self.client.post(
            '/api/v1/sales/',
            data=self.create_salesrecs,
            content_type='application/json')

    def test_salesrecs_creation(self):
        """ Test for sales records creation """
        resource = self.client.post(
            '/api/v1/sales/',
            data=self.create_salesrecs,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')

    def test_get_all_salesrecs(self):
        """ Test for getting all sales records """
        resource = self.client.get(
            '/api/v1/sales/',
            data=json.dumps(dict()),
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')

    def test_get_salesrec_by_rec_id(self):
        """ Test for getting specific sale record """
        resource = self.client.get('/api/v1/sales/1')
        self.assertEqual(resource.status_code, 200)

    def test_salesrec_deletion(self):
        """Test API can delete an existing sales record"""
        res = self.client.delete('/api/v1/sales/1')
        self.assertEqual(res.status_code, 201)

    def test_salesrec_editing(self):
        """ Test for sales records editing """
        resource = self.client.put(
            '/api/v1/sales/2',
            data=self.create_salesrecs2,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Update Successful.')

if __name__ == '__main__':
    unittest.main()
