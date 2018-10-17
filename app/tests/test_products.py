'''test cases for products views'''
import unittest
import json
from app import create_app
from app.version1.products.models import Products

class TestBase(unittest.TestCase):
    """ Tests Base """

    def create_app():
        """ Instantiate tests"""

class TestProducts(TestBase):
    """ Tests for the products creation"""
    def setUp(self):
        '''instanciate'''
        app = create_app()
        
        self.create_products = json.dumps(dict(
            description="wall pass",
            quantity="10 rolls",
            min_quantity_in_store="5 rolls",
            price_per_roll="Ksh 400"))

        self.create_Product2 = json.dumps(dict(
                product_id=2,
                description='ironsheet',
                quantity='30 pieces',
                min_quantity_in_store='5 pieces',
                price_per_roll='ksh 400'))

        self.client = app.test_client()
        self.client.post(
            '/api/v1/products/',
            data=self.create_products,
            content_type='application/json')

    def test_products_creation(self):
        """ Test for products creation """
        resource = self.client.post(
            '/api/v1/products/',
            data=self.create_products,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')

    def test_get_all_products(self):
        """ Test for getting all products """
        resource = self.client.get(
            '/api/v1/products/',
            data=json.dumps(dict()),
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')


    def test_get_product_by_product_id(self):
        """ Test for getting specific product """
        resource = self.client.get('/api/v1/products/1')
        self.assertEqual(resource.status_code, 200)

    def test_product_deletion(self):
        """Test API can delete an existing product"""
        res = self.client.delete('/api/v1/products/1')
        self.assertEqual(res.status_code, 201)

    def test_products_editing(self):
        """ Test for products editing """
        resource = self.client.put(
            '/api/v1/products/2',
            data=self.create_Product2,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Update Successful.')

if __name__ == '__main__':
    unittest.main()
