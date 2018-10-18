def validate_data(data):
    """validate sales records details"""
    try:
        # check if description is empty
        if data["description"] is False:
            return "product description required"
            # check if date sold of product is empty
        elif data["date_sold"] is False: 
            return "date sold of product required"
            # check if the buyer's contact is added
        elif data["buyer_contact"] is False:
            return "The buyer's contact required"
            # check if the saler's name is provided
        elif data["saler"] is False:
            return "The saler's name required"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
        