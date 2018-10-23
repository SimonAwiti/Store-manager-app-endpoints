def validate_data(data):
    """validate product details"""
    try:
        # check if description is empty
        if data["description"] is False:
            return "product description required"
            # check if product description has content
        elif data["description"] == "":
            return "product description is required"
            # check if product description cannot be words
        elif isinstance(data["description"], int) is True:
            return "Description must be a string"
        elif data["date_sold"] is False: 
            return "date sold required"
        #elif data["date_sold"] == "":
            #return "Date sold is required"
        #elif isinstance(data["date_sold"], int) is True:
            #return "Date must be a string"
        elif data["quantity_sold"] is False: 
            return "product quantity required"
        elif data["quantity_sold"] == "":
            return "product quantity is required"
        elif data["quantity_sold"] > 5:
            return "Sale order must be less than available products"
        elif isinstance(data["quantity_sold"], int) is False:
            return "Quantity must be a number"
        elif data["unit_price"] is False: 
            return "price pern unit required"
        elif data["unit_price"] == "":
            return "price per unit is required"
        elif data["unit_price"] < 0:
            return "The minimum unit price of product must be above 0"
        elif isinstance(data["unit_price"], int) is False:
            return "price per unit must be a number"
        elif data["bill"] is False: 
            return "Bill is required"
        elif data["attendant"] is False: 
            return "Attendant's name is required is required"
        elif data["attendant"] == "":
            return "attendant's name is required"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
        