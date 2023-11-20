import sqlite3
import pandas as pd
import pytest
from e1_sqlite import insert_data
from test_e1_sqlite import setup_database
from e2_pandas import read_sql

# Test the read_sql function
def test_read_sql(setup_database):
    # Call the read_sql function with the test database connection
    insert_data([(1, 'John Doe', 100.0), (2, 'Jane Smith', 150.0)])
    df = read_sql()

    # Check if the DataFrame has the expected structure and content
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert set(df.columns) == {'order_number', 'customer_name', 'total'}
    assert (df['order_number'].values == [1, 2]).all()
    assert (df['customer_name'].values == ['John Doe', 'Jane Smith']).all()
    assert (df['total'].values == [100.0, 150.0]).all()

# Run the tests
if __name__ == "__main__":
    pytest.main()
