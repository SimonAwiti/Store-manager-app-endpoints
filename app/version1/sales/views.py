"""creating bp routes for sales records"""
from flask import Blueprint, jsonify
from models import salesrec

salesrecObject = salesrec()


version1_blueprints = Blueprint('version1', __name__, url_prefix='/api/v1/sales')

@version1_blueprints.route('/', methods=['GET', 'POST'])
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
    data = salesrecObject.get_salesrec()
    return data