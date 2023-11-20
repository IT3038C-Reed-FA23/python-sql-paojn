import sqlite3

# Create a connection to a database called database.db
conn = None

# Create a cursor to perform database operations
cursor = None

# NOTE: Until you complete both insert_row and select_all_data, the tests will fail.

def insert_row(order_number, customer_name, total):
  "INSERT INTO orders (order_number, customer_name, total) VALUES ()"

def select_all_data():
  "SELECT * FROM orders"

def insert_data(data):
  "INSERT INTO orders (order_number, customer_name, total) VALUES ()"


def update_data(order_number, total):
  "UPDATE orders SET total =  WHERE order_number = "

def delete_data(order_number):
  "DELETE FROM orders WHERE order_number = "
