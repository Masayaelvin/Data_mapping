"""This module involes functions that extracts the combined customer data  from json file
 The data is transformed to a python object and stored in database using ponyORM"""
from data_combine import combine
from pony.orm import Database, Optional, Required, db_session
import json

db = Database()
# Set the MySQL database connection string
db.bind(provider='mysql', host='localhost', user='mainanorbert', passwd='pope@2019', db='customer_data')

class Customer(db.Entity):
    """Defining a class entity for customer fields"""
    __table__ = 'Customers'
    firstName = Required(str)
    lastName = Required(str)
    age = Required(int)
    iban = Required(str)
    credit_card_number = Required(str)
    credit_card_security_code = Required(str)
    credit_card_start_date = Required(str)
    credit_card_end_date = Required(str)
    address_main = Required(str)
    address_city = Required(str)
    address_postcode = Required(str)
    Sex = Required(str)
    Vehicle_Make = Required(str)
    Vehicle_Model = Required(str)
    Vehicle_Year = Required(str)
    Vehicle_Type = Required(str)
    Retired = Required(str)
    Dependants = Required(str)
    Marital_Status = Required(str)
    Salary = Required(str)
    Pension = Required(str)
    Company = Required(str)
    Commute_Distance = Required(str)
    Address_Code = Required(str)
    debt_amount = Optional(str, nullable=True)
    debt_period_in_years = Optional(int, nullable=True)

# Generate the database schema
db.generate_mapping(create_tables=True)

with open("combined_data.json", 'r') as json_file:
    json_data = json.load(json_file)
# Insert data into the MySQL database
with db_session:
    for data in json_data:
        Customer(**data)

# Commit changes to the database
db.commit()

