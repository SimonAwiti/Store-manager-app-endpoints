"""creating bp routes for products"""
from flask import Blueprint, request, jsonify
from models import Products

ProductsObject = Products()

version1_blueprints = Blueprint('version1', __name__, url_prefix='/api/v1/products')

@version1_blueprints.route('/', methods=['GET', 'POST'])
def product():
    """ Method to create and retrieve product."""
    if request.method == "POST":
        data = request.get_json()
        description = data['description']
        quantity = data['quantity']
        min_quantity_in_store = data['min_quantity_in_store']
        price_per_roll = data['price_per_roll']
        response = ProductsObject.create_Product(description, quantity, min_quantity_in_store, price_per_roll)
        return response
    data = ProductsObject.get_products()
    return data