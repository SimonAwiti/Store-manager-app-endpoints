"""/app/version1/sales/models.py"""
from flask import jsonify

class salesrec(object):
    def __init__(self):
        """ Initialize empty sales record list"""
        self.salesrec_list = []
        self.notfound = None

    def create_salesrec(self, description, date_sold, buyer_contact, saler):
        """Create sales records"""
        self.salesrec = {}

        self.salesrecId = len(self.salesrec_list)
        self.salesrec['description'] = description
        self.salesrec['date_sold'] = date_sold
        self.salesrec['buyer_contact'] = buyer_contact
        self.salesrec['saler'] = saler
        self.salesrec['salesrec_id'] = self.salesrecId + 1
        self.salesrec_list.append(self.salesrec)
        return jsonify({
            "message": "Successful.",
            "sale record": self.salesrec_list}), 201

    def get_salesrec(self):
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
                "message": "No sale record with that id.",
                "Product": self.salesrec_list}), 404

    def update_salesrec(self, product_id, description, date_sold, buyer_contact, saler):
        """ update sale record """
        for salesrec in self.salesrec_list:
            if salesrec['salesrec_id'] == salesrec_id:
                salesrec['description'] = description
                salesrec['date_sold'] = date_sold
                salesrec['buyer_contact'] = buyer_contact
                salesrec['saler'] = saler
                return jsonify({
                    "message": "Update Successful.",
                    "sales record": self.salesrec_list}), 201
            self.notfound = True
        if self.notfound is True:
            return jsonify({
                "message": "No sale record with that id.",
                "Product": self.salesrec_list}), 404

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
                "message": "No sale record with that id.",
                "Product": self.salesrec_list}), 404
