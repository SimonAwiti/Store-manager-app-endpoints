[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/SimonAwiti/Store-manager-app-endpoints.svg?branch=master)](https://travis-ci.org/SimonAwiti/Store-manager-app-endpoints)
[![Maintainability](https://api.codeclimate.com/v1/badges/ae5b234ba51274de5e44/maintainability)](https://codeclimate.com/github/SimonAwiti/Store-manager-app-endpoints/maintainability)

# Store-manager-app-endpoints

## The following are API endpoints enabling one to: 
* Get all available products
* Fetch a single product record
* Fetch all sale records 
* Create a product 
* Create a sale order
## Here is a list of the functioning endpoints

| EndPoint                  | Functionality                    |  Actual routes                |
| :---                      |     :---:                        |    :---:                      |
| GET /products             | Get all available products       |  /api/v1/products/            |
| GET /products/<productId> | Fetch a single product record    |  /api/v1/products/<productid> |
| GET /sales                | Fetch all sale records           |  /api/v1/sales/               |
| GET /sales/<saleId>       | Fetch a single sale record       |  /api/v1/sales/<salerecid>    |
| POST /products            | Create a product                 |  /api/v1/products/            |
| POST /sales               | Create a sale order              |  /api/v1/sales/               |
  
## Testing the endpoints

* Install python then using pip instal .. install flask
* clone the repo
* Ensure that postman is installed
* From your terminal locate the repo and run: python run.py
* open postman and test the endpoints
* Use unittest to run the the tests

## Setting up and how to start the application

* Install python then using pip instal .. install flask
* clone the repo
* From your terminal Ensure that the virtual environment is activated
* From the terminal locate the repo and run: python run.py

## Technology used

* Python 2.7
* Flask framework
* Unittest for testing

## Background context 

Published POSTMAN documentation
[Documentation](https://documenter.getpostman.com/view/5353857/RWgtTwtr#intro)

# Written by: Simon Awiti
#### Copyright © Andela 2018 

