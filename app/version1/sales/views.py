"""creating bp routes for sales records"""
from flask import Blueprint, jsonify, request
from models import salesrec

salesrecObject = salesrec()


version1sales_blueprints = Blueprint('version1sale', __name__, url_prefix='/api/v1/sales')

@version1sales_blueprints.route('/', methods=['GET', 'POST'])
def salesrec():
    """ Method to create and retrieve sale record."""
    if request.method == "POST":
        data = request.get_json()
        description = data['description']
        date_sold = data['date_sold']
        buyer_contact = data['buyer_contact']
        saler = data['saler']
        response = salesrecObject.create_salesrec(description, date_sold, buyer_contact, saler)
        return response
    data = salesrecObject.get_salesrecs()
    return data

@version1sales_blueprints.route('/<int:salesrec_id>', methods=['GET', 'PUT', 'DELETE'])
def salesrec_manipulation(salesrec_id, **kwargs):
    """ GET/PUT/DEL product """
    if request.method == 'DELETE':
        '''DELETE'''
        response = salesrecObject.delete_salesrec(salesrec_id)
        return response

    elif request.method == 'PUT':
        '''PUT'''
        data = request.get_json()
        description = data['description']
        date_sold = data['date_sold']
        buyer_contact = data['buyer_contact']
        saler = data['saler']
        response = salesrecObject.update_salesrec(
            salesrec_id,
            description,
            date_sold,
            buyer_contact,
            saler)
        return response

    else:
        '''GET'''
        response = salesrecObject.get_salesrec(salesrec_id)
        return response