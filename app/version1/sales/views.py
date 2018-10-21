"""creating bp routes for sales records"""
from flask import Blueprint, request
from app.version1.sales.models import SalesRec
from app.version1.sales.validatesalesrec import validate_data
import datetime

salesrecObject = SalesRec()


version1sales_blueprints = Blueprint('version1sale', __name__, url_prefix='/api/v1/sales')

@version1sales_blueprints.route('/', methods=['GET', 'POST'])
def salesrec():
    """ Method to create and retrieve sale record."""
    if request.method == "POST":
        data = request.get_json()
        response = validate_data(data)
        if response == "valid":
            description = data['description']
            date_sold = datetime.datetime.now()
            quantity_sold = data['quantity_sold']
            unit_price = data['unit_price']
            bill = unit_price * quantity_sold
            attendant = data['attendant']

            response = salesrecObject.create_salesrec(
                description, date_sold, quantity_sold, unit_price, bill, attendant)
        return response
    data = salesrecObject.get_salesrecs()
    return data

@version1sales_blueprints.route('/<int:salesrec_id>', methods=['GET', 'PUT', 'DELETE'])
def salesrec_manipulation(salesrec_id, **kwargs):
    """ GET/PUT/DEL sale records """
    if request.method == 'DELETE':
        response = salesrecObject.delete_salesrec(salesrec_id)
        return response

    elif request.method == 'PUT':
        data = request.get_json()
        response = validate_data(data)
        description = data['description']
        date_sold = datetime.datetime.now()
        quantity_sold = data['quantity_sold']
        unit_price = data['unit_price']
        bill = unit_price * quantity_sold
        attendant = data['attendant']
        response = salesrecObject.update_salesrec(
            salesrec_id,
            description,
            date_sold,
            quantity_sold,
            unit_price,
            bill,
            attendant)
        return response

    else:
        response = salesrecObject.get_salesrec(salesrec_id)
        return response
