"""products data structures"""
from flask import jsonify

class Products(object):
    """products clas"""
    def __init__(self):
        """ Initialize empty Product list"""
        self.products_list = []
        self.notfound = None

    def create_product(self, description, quantity, min_quantity_in_store, price_per_roll):
        """Create products"""
        self.products = {}

        self.product_id = len(self.products_list)
        self.products['description'] = description
        self.products['quantity'] = quantity
        self.products['min_quantity_in_store'] = min_quantity_in_store
        self.products['price_per_roll'] = price_per_roll
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
            self, product_id, description, quantity, min_quantity_in_store, price_per_roll):
        """ update product """
        for product in self.products_list:
            if product['product_id'] == product_id:
                product['description'] = description
                product['quantity'] = quantity
                product['min_quantity_in_store'] = min_quantity_in_store
                product['price_per_roll'] = price_per_roll
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
