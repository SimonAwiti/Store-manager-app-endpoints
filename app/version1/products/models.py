"""products data structures"""
from flask import jsonify
#from flask_jwt_extended import create_access_token

class Products(object):
    """products class"""
    def __init__(self):
        """ Initialize empty Product list"""
        self.products_list = []
        self.notfound = None

    def get_product_by_description(self, description):
        """ Fetch product by description """
        product = [product for product in self.products_list if product['description'] == description]
        return product   

    def minimum_quantity(self, min_quantity_in_store):
        min_quantity = self.products['min_quantity_in_store']
        return min_quantity


    def create_product(self, description, quantity, price_per_unit, total_cost):
        """Create products"""
        present_product = self.get_product_by_description(description)
        if present_product:
            return jsonify({
                "message": "Product already exists."}), 404
        self.products = {}

        self.product_id = len(self.products_list)
        self.products['description'] = description
        self.products['quantity'] = quantity
        self.products['price_per_unit'] = price_per_unit
        self.products['total_cost'] = quantity * price_per_unit
        self.products['product_id'] = self.product_id + 1
        self.products_list.append(self.products)
        return jsonify({
            "message": "Successful.",
            "Product": self.products_list}), 201

    def get_products(self):
        """ get all products """
        return jsonify({
            "message": "Successful.",
            "Products": self.products_list}), 200

    def delete_product(self, product_id):
        """ delete product """
        for product in self.products_list:
            if product['product_id'] == product_id:
                self.products_list.remove(product)
                return jsonify({
                    "message": "Delete Successful.",
                    "Products": self.products_list}), 201
            self.notfound = True
        if self.notfound is True:
            return jsonify({
                "message": "No product with that id."}), 404

    def update_product(
            self, product_id, description, quantity, price_per_unit, total_cost):
        """ update product """
        for product in self.products_list:
            if product['product_id'] == product_id:
                product['description'] = description
                product['quantity'] = quantity
                product['price_per_unit'] = price_per_unit
                product['total_cost'] = quantity * price_per_unit
                return jsonify({
                    "message": "Update Successful.",
                    "Product": self.products_list}), 201
            self.notfound = True
        if self.notfound is True:
            return jsonify({
                "message": "No product with that id."}), 404

    def get_product(self, product_id):
        """ get single product """
        for product in self.products_list:
            if product['product_id'] == product_id:
                return jsonify({
                    "message": "Successful.",
                    "Product": product}), 200
            self.notfound = True
        if self.notfound is True:
            return jsonify({
                "message": "No product with that id."}), 404
