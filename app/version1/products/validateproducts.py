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
        elif not data["description"].isalpha():
            return "Product description should be aphabetic"
            # check if product quantity is empty
        elif data["quantity"] is False: 
            return "product quantity required"
            # check if min_quantity_in_store
        elif data["min_quantity_in_store"] is False:
            return "minimum quantity of product in store required"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
        