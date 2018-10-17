"""creating bp routes for products"""
from flask import Blueprint, request
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
        response = ProductsObject.create_Product(
            description, quantity, min_quantity_in_store, price_per_roll)
        return response
    data = ProductsObject.get_products()
    return data

@version1_blueprints.route('/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def product_manipulation(product_id, **kwargs):
    """ GET/PUT/DEL product """
    if request.method == 'DELETE':
        response = ProductsObject.delete_product(product_id)
        return response

    elif request.method == 'PUT':
        data = request.get_json()
        description = data['description']
        quantity = data['quantity']
        min_quantity_in_store = data['min_quantity_in_store']
        price_per_roll = data['price_per_roll']
        response = ProductsObject.update_product(
            product_id,
            description,
            quantity,
            min_quantity_in_store,
            price_per_roll)
        return response

    else:
        response = ProductsObject.get_product(product_id)
        return response
