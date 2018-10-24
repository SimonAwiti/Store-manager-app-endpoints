"""data structures"""
import datetime
from flask import jsonify, request
"""list of all the products"""
products_list = []
salesrec_list = []

def check_if_product_exists(item):
    """ determining if product exist in the store"""
    product = [product for product in products_list if product['description'] == item.rstrip()]
    if product:
        return True
    return False
def check_if_inputs_are_negatives(quantity, price_per_unit):
    """ determing if products numbers are negatives"""
    if quantity < 0 or price_per_unit < 0:
        return True
    return False

def check_for_mumber_of_quantity(item):
    """determining if the quality of products in the list of availabe products is less"""
    product = [product for product in products_list if product['quantity'] < item]
    if product:
        return True
    return False

def get_salesrec_by_description(description):
    """ Fetch salesrec by description """
    salesrec = [salesrec for salesrec in salesrec_list if salesrec['description'] == description]
    return salesrec  

class Products():
    """products class """
    def add_product(self, description, quantity, price_per_unit, total_cost):
        """Add a product to the products list"""
        description = request.json.get('description', None)
        quantity = request.json.get('quantity', None)
        price_per_unit = request.json.get('price_per_unit', None)
        total_cost = quantity * price_per_unit

        product_dictionary={
            "product_id": len(products_list) + 1,
            "description" : description.rstrip(),
            "quantity" : quantity,
            "price_per_unit" : price_per_unit,
            "total_cost" : quantity * price_per_unit
        }

        """check if product already in the list"""
        present = check_if_product_exists(description)
        if present:
            return jsonify({
            "message": "Product already exists"}), 401

        """check if the inputs are negative"""
        size = check_if_inputs_are_negatives(quantity, price_per_unit)
        if size:
            return jsonify({
            "message": "The input cannot be negative"}), 401

        products_list.append(product_dictionary)
        return jsonify({
            "message": "Succesful.",
            "Product": products_list}), 201

    def get_all_products(self):
        """Fetch all products from the list"""
        """check if products list is empty"""
        if len(products_list) == 0:
            return jsonify({
                "message": "No products added yet."}), 200
        return jsonify({
            "message": "Succesful.",
            "Product": products_list}), 201

    def get_one_product(self, product_id):
        """gets a specific product from the products list"""
        product = [product for product in products_list if product['product_id'] == product_id]
        if product:
            return jsonify({
                "message": "Succesful.",
                "Product": product}), 201

        """if not available"""
        return jsonify({
            "message": "No product with that id."}), 404

    def delete_product(self, product_id):
        """ delete product """
        for product in products_list:
            if product['product_id'] == product_id:
                products_list.remove(product)
                return jsonify({
                    "message": "Delete Successful.",
                    "Products": products_list}), 201
            """if not availabe"""
            return jsonify({
                "message": "No product with that id."}), 404

    def update_product(
            self, product_id, description, quantity, price_per_unit, total_cost):
        """ update product """
        for product in products_list:
            if product['product_id'] == product_id:
                product['description'] = description
                product['quantity'] = quantity
                product['price_per_unit'] = price_per_unit
                product['total_cost'] = quantity * price_per_unit
                return jsonify({
                    "message": "Update Successful.",
                    "Product": products_list}), 201
            """if not available"""
            return jsonify({
                "message": "No product with that id."}), 404

class SalesRec(object):
    """sales record test class"""
    def create_salesrec(self, description, date_sold, quantity, unit_price, bill, attendant):
        """Create sales records"""
        description = request.json.get('description', None)
        date_sold = datetime.datetime.now()
        quantity = request.json.get('quantity', None)
        unit_price = request.json.get('unit_price', None)
        bill = quantity * unit_price
        attendant = request.json.get('attendant', None)

        salesrec_dictionary={
            "salesrec_id": len(salesrec_list) + 1,
            "description" : description.rstrip(),
            "quantity" : quantity,
            "unit_price" : unit_price,
            "bill" : quantity * unit_price,
            "attendant" : attendant.rstrip()
        }

        """check if product is in store"""
        result = check_if_product_exists(description)
        if not result:
                return jsonify({
                    "message": "No such product in store."}), 404 
        
        """check if sales record has already been added"""
        present_salesrec = get_salesrec_by_description(description)
        if present_salesrec:
            return jsonify({
                "message": "Sale record already exists."}), 404

        """checks if the number is less than what is in store"""
        available_quality = check_for_mumber_of_quantity(quantity)
        if available_quality:
            return jsonify({
                "message": "Order exceeds the available stock."}), 404

        """add the dictionary in the list"""
        salesrec_list.append(salesrec_dictionary)
        return jsonify({
            "message": "Succesful.",
            "Product": salesrec_list}), 201

    def get_salesrecs(self):
        """ get all sales records """
        return jsonify({
            "message": "Successful.",
            "sales records": salesrec_list}), 200

    def get_salesrec(self, salesrec_id):
        """ get single sales record """
        for salesrec in salesrec_list:
            if salesrec['salesrec_id'] == salesrec_id:
                return jsonify({
                    "message": "Successful.",
                    "sales record": salesrec}), 200
            """if not found"""
            return jsonify({
                "message": "No sale record with that id."}), 404

    def get_salesrec_by_attendant(self, attendant):
        """ Fetch sales rec by attendant """
        for salesrec in salesrec_list:
            if salesrec['attendant'] == attendant:
                return jsonify({
                    "message": "Successful.",
                    "sales record": salesrec}), 200
            """if not found"""
            return jsonify({
                "message": "No sale record by that attendant."}), 404

    def delete_salesrec(self, salesrec_id):
        """ delete a sale record """
        for salesrec in salesrec_list:
            if salesrec['salesrec_id'] == salesrec_id:
                salesrec_list.remove(salesrec)
                return jsonify({
                    "message": "Delete Successful.",
                    "salesrec": salesrec_list}), 201
            """if not found"""
            return jsonify({
                "message": "No sale record with that id."}), 404

    def update_salesrec(
        self, salesrec_id, description, date_sold, quantity, unit_price, bill, attendant):
        """ update sale record """
        for salesrec in salesrec_list:
            if salesrec['salesrec_id'] == salesrec_id:
                salesrec['description'] = description
                salesrec['date_sold'] = datetime.datetime.now()
                salesrec['quantity'] = quantity
                salesrec['unit_price'] = unit_price
                salesrec['bill'] = unit_price * quantity
                salesrec['attendant'] = attendant
                return jsonify({
                    "message": "Update Successful.",
                    "sales record": salesrec_list}), 201
            """if not found"""
            return jsonify({
                "message": "No sale record with that id."}), 404
