"""sales records data structures"""
from flask import jsonify
import datetime

class SalesRec(object):
    """sales record test class"""
    def __init__(self):
        """ Initialize empty sales record list"""
        self.salesrec_list = []
        self.notfound = None

    def get_salesrec_by_description(self, description):
        """ Fetch product by description """
        salesrec = [salesrec for salesrec in self.salesrec_list if salesrec['description'] == description]
        return salesrec  

    def create_salesrec(self, description, date_sold, quantity_sold, unit_price, bill, attendant):
        """Create sales records"""
        present_salesrec = self.get_salesrec_by_description(description)
        if present_salesrec:
            return jsonify({
                "message": "Sale record already exists."}), 404
        self.salesrec = {}

        self.salesrec_id = len(self.salesrec_list)
        self.salesrec['description'] = description
        self.salesrec['date_sold'] = datetime.datetime.now()
        self.salesrec['quantity_sold'] = quantity_sold
        self.salesrec['unit_price'] = unit_price
        self.salesrec['bill'] = unit_price * quantity_sold
        self.salesrec['attendant'] = attendant
        self.salesrec['salesrec_id'] = self.salesrec_id + 1
        self.salesrec_list.append(self.salesrec)
        return jsonify({
            "message": "Successful.",
            "sale record": self.salesrec_list}), 201

    def get_salesrecs(self):
        """ get all sales records """
        return jsonify({
            "message": "Successful.",
            "sales records": self.salesrec_list}), 200

    def delete_salesrec(self, salesrec_id):
        """ delete a sale record """
        for salesrec in self.salesrec_list:
            if salesrec['salesrec_id'] == salesrec_id:
                self.salesrec_list.remove(salesrec)
                return jsonify({
                    "message": "Delete Successful.",
                    "salesrec": self.salesrec_list}), 201
            self.notfound = True
        if self.notfound is True:
            return jsonify({
                "message": "No sale record with that id."}), 404

    def update_salesrec(
        self, salesrec_id, description, date_sold, quantity_sold, unit_price, bill, attendant):
        """ update sale record """
        for salesrec in self.salesrec_list:
            if salesrec['salesrec_id'] == salesrec_id:
                salesrec['description'] = description
                salesrec['date_sold'] = datetime.datetime.now()
                salesrec['quantity_sold'] = quantity_sold
                salesrec['unit_price'] = unit_price
                salesrec['bill'] = unit_price * quantity_sold
                salesrec['attendant'] = attendant
                return jsonify({
                    "message": "Update Successful.",
                    "sales record": self.salesrec_list}), 201
            self.notfound = True
        if self.notfound is True:
            return jsonify({
                "message": "No sale record with that id."}), 404

    def get_salesrec(self, salesrec_id):
        """ get single sales record """
        for salesrec in self.salesrec_list:
            if salesrec['salesrec_id'] == salesrec_id:
                return jsonify({
                    "message": "Successful.",
                    "sales record": salesrec}), 200
            self.notfound = True
        if self.notfound is True:
            return jsonify({
                "message": "No sale record with that id."}), 404
