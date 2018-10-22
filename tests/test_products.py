'''test cases for products views'''
import unittest
import os
import json
from app import create_app
from app.version1.products.models import Products
from app.version1.users.models import User, users
from app.version1.users.views import Products

class TestProducts(unittest.TestCase):

    """ Tests for the products creation"""
    def setUp(self):
        '''instanciate'''
        app = create_app(config='testing')
        self.client = app.test_client()

        self.create_products = json.dumps(dict(
            description="wall pass",
            quantity=10,
            price_per_unit=20,
            total_cost= 200))

        self.create_products2 = json.dumps(dict(
            #description="wall pass",
            quantity=10,
            price_per_unit=20,
            total_cost= 200))

    def test_products_creation(self):
        """ Test for products creation """
        resource = self.client.post(
            '/api/v1/products/',
            data=self.create_products,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['Message'].strip(),  'You are not logged in!')
        self.assertNotIn((
            data.get("description"),
            data.get("quantity"),
            data.get("price_per_unit"),
            data.get("total_cost")), data)

    def test_get_product_by_product_id(self):
        """ Test for getting specific product """
        resource = self.client.get('/api/v1/products/1')
        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['Message'].strip(),  'You are not logged in!')
        self.assertNotIn((
            data.get("description"),
            data.get("quantity"),
            data.get("price_per_unit"),
            data.get("total_cost")), data)

    def test_products_editing(self):
        """ Test for products editing """
        resource = self.client.put(
            '/api/v1/products/2',
            data=self.create_products,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['Message'].strip(), 'You are not logged in!')
        self.assertNotIn((
            data.get("description"),
            data.get("quantity"),
            data.get("price_per_unit"),
            data.get("total_cost")), data)

    def test_posting_invalid_product(self):
        """ Test for posting invalid products"""

        resource = self.client.post(
            '/api/v1/products/',
            data=self.create_products2,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertTrue(data['Message'].strip(), 'You are not logged in!')
        self.assertTrue(resource.content_type, 'application/json')
        self.assertTrue(resource.status_code, 200)
        self.assertNotIn((
            data.get("quantity"),
            data.get("price_per_unit"),
            data.get("total_cost")), data)

    def test_get_product_by_wrong_product_id(self):
        """ Test for getting specific product with wrong id"""
        resource = self.client.get('/api/v1/products/100')
        data = json.loads(resource.data.decode())
        print data
        self.assertTrue(data['Message'].strip(), 'You are not logged in!')

if __name__ == '__main__':
    unittest.main()
