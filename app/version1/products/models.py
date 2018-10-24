"""products data structures"""
from flask import jsonify

class Products(object):
    """products class"""
    def __init__(self):
        """ Initialize empty Product list"""
        self.products_list = []
        self.notfound = None
    def check_product_availability(self, description):
        """checks if the product is availabe"""
        product = [product for product in self.products_list if product['description'] == description]
        if product:
            return True
        return False

    def check_min_quantity(self, quantity):
        """checks if the min quantiry is exeeded"""
        quantity = [quantity for quantity in self.products_list if quantity['quantity'] < 5]
        if quantity:
            return True
        return False

    def get_product_by_description(self, description):
        """ Fetch product by description """
        product = [product for product in self.products_list if product['description'] == description]
        if product:
            return True
        return False 

    def added_products(self, description):
        posted_products =self.products_list
        return posted_products
  


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

    def my_product_list(self, products_list):
        my_products =products_list
        return my_products
