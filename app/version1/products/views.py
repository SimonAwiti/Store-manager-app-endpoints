"""creating bp routes for products"""
#from flask import Blueprint, request
#from app.version1.products.models import Products
##from app.version1.products.validateproducts import validate_data

#ProductsObject = Products()


#version1_blueprints = Blueprint('version1', __name__, url_prefix='/api/v1/products')

"""@version1_blueprints.route('/', methods=['GET', 'POST'])
def product():
    # Method to create and retrieve product.
    if request.method == "POST":
        data = request.get_json()
        response = validate_data(data)
        if response == "valid":
            description = data['description']
            quantity = data['quantity']
            price_per_unit = data['price_per_unit']
            total_cost = quantity * price_per_unit
            response = ProductsObject.create_product(
                description, quantity, price_per_unit, total_cost)
        return response
    data = ProductsObject.get_products()
    return data"""

'''@version1_blueprints.route('/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def product_manipulation(product_id, **kwargs):
    """ GET/PUT/DEL product """
    if request.method == 'DELETE':
        response = ProductsObject.delete_product(product_id)
        return response

    elif request.method == 'PUT':
        data = request.get_json()
        description = data['description']
        quantity = data['quantity']
        price_per_unit = data['price_per_unit']
        total_cost = quantity * price_per_unit
        response = ProductsObject.update_product(
            product_id,
            description,
            quantity,
            price_per_unit,
            total_cost)
        return response

    else:
        response = ProductsObject.get_product(product_id)
        return response'''
