[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/SimonAwiti/Store-manager-app-endpoints.svg?branch=master)](https://travis-ci.org/SimonAwiti/Store-manager-app-endpoints)

# Store-manager-app-endpoints

## The following are API endpoints enabling one to: 
* Get all available products
* Fetch a single product record
* Fetch all sale records 
* Create a product 
* Create a sale order
## Here is a list of the functioning endpoints

| EndPoint                  | Functionality                    |   
| :---                      |     :---:                        |  
| GET /products             | Get all available products       |  
| GET /products/<productId> | Fetch a single product record    |  
| GET /sales                | Fetch all sale records           | 
| GET /sales/<saleId>       | Fetch a single sale record       | 
| POST /products            | Create a product                 |  
| POST /sales               | Create a sale order              |
  
## Testing the endpoints

* Install python then using pip instal .. install flask
* clone the repo
* Ensure that postman is installed
* From your terminal locate the repo and run: python run.py
* open postman and test the endpoints
* Use unittest to run the the tests

## This application has been deployed on Heroku 


# Written by: Simon Awiti
#### Copyright © Andela 2018 

