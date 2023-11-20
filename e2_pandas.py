import sqlite3
import pandas as pd

# Create a connection to a database called database.db
conn = None

# NOTE: Until you complete insert_data from e1, the tests will fail.

def read_sql():
  query = "SELECT * FROM orders"
  # use pandas to read the query results into a dataframe
  df = None
  return df