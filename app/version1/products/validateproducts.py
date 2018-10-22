def validate_products_data(data):
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
        elif data["quantity"] is False: 
            return "product quantity required"
        elif data["quantity"] == "":
            return "product quantity is required"
        elif data["quantity"] < 5:
            return "The minimum unit quantity of product must be above 5"
        elif isinstance(data["quantity"], int) is False:
            return "Quantity must be a number"
        elif data["price_per_unit"] is False: 
            return "price pern unit required"
        elif data["price_per_unit"] == "":
            return "price per unit is required"
        elif data["price_per_unit"] < 0:
            return "The minimum unit price of product must be above 0"
        elif isinstance(data["price_per_unit"], int) is False:
            return "price per unit must be a number"
        else:
            return "valid product"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
        