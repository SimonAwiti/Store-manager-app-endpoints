"""creating tables for the database"""
users_table = """CREATE TABLE IF NOT EXISTS users
            (
                user_id serial PRIMARY KEY, 
                username VARCHAR (50) UNIQUE NOT NULL, 
                password VARCHAR (50) NOT NULL,
                confirmpass VARCHAR (50) NOT NULL,
                userrole VARCHAR (50) NOT NULL
        )"""

salesrec_table = """CREATE TABLE IF NOT EXISTS salesrecs
            (
	            salesrec_id  serial PRIMARY KEY,
	            description varchar(25) UNIQUE NOT NULL,
                datesold timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                unit_price varchar(25) NOT NULL,
                quantity varchar(25) NOT NULL,
                bill varchar(25) NOT NULL,
                attendant varchar(25) NOT NULL,
                user_id INT REFERENCES users(user_id) ON DELETE CASCADE
        )"""
        
products_table = """CREATE TABLE IF NOT EXISTS products
            (
	            product_id  serial PRIMARY KEY,
	            description varchar(25) UNIQUE NOT NULL,
                quantity varchar(25) NOT NULL,
                price_per_unit varchar(25) NOT NULL,
                total_cost varchar(25) NOT NULL,
                user_id INT REFERENCES users(user_id) ON DELETE CASCADE
        )"""

queries = [users_table, salesrec_table, products_table]

droppings = ["DROP TABLE users CASCADE",
        "DROP TABLE products CASCADE",
        "DROP TABLE salesrecs CASCADE"]
