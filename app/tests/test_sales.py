'''test cases for sales records views'''
import unittest
import json
from app import create_app

class TestBase(unittest.TestCase):
    """ Tests Base """

    def create_app(self):
        """ Instantiate tests"""
        app = create_app(self)
        return app

class TestProducts(TestBase):
    """ Tests for the Sales creation"""
    def setUp(self):
        '''instanciate'''
        app = create_app()
        self.create_salesrecs = json.dumps(dict(
            description="wall pass",
            date_sold="1/1/2019",
            buyer_contact="0723445673",
            saler="james kinn"))
        self.client = app.test_client()
        self.client.post(
            '/v1/sales',
            data=self.create_salesrecs,
            content_type='application/json')

    def test_salesrecs_creation(self):
        """ Test for sales records creation """
        resource = self.client.post(
            '/v1/sales',
            data=self.create_salesrecs,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')

    def test_get_all_salesrecs(self):
        """ Test for getting all sales records """
        resource = self.client.get(
            '/v1/sales',
            data=json.dumps(dict()),
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')

    def test_get_salesrec_by_rec_id(self):
        """ Test for getting specific sale record """
        resource = self.client.get('/v1/sales/1')
        self.assertEqual(resource.status_code, 200)

if __name__ == '__main__':
    unittest.main()
