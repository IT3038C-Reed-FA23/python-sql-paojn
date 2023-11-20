import pytest
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Import the functions to be tested
from e1_sqlite import insert_row, insert_data, select_all_data, update_data, delete_data

@pytest.fixture
def setup_database():
    # Create a test table for orders
    cursor.execute('''
        CREATE TABLE orders (
            order_number INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            total REAL NOT NULL
        )
    ''')
    yield
    # Clean up the test table after each test
    cursor.execute("DROP TABLE orders")
    conn.commit()

def test_insert_row(setup_database):
    insert_row(1, 'John Doe', 100.0)
    result = select_all_data()
    assert len(result) == 1
    assert result[0] == (1, 'John Doe', 100.0)

def test_insert_data(setup_database):
    data = [(1, 'John Doe', 100.0), (2, 'Jane Smith', 150.0)]
    insert_data(data)
    result = select_all_data()
    assert len(result) == 2
    assert result == data

def test_update_data(setup_database):
    insert_row(1, 'John Doe', 100.0)
    update_data(1, 150.0)
    result = select_all_data()
    assert result[0][2] == 150.0

def test_delete_data(setup_database):
    insert_row(1, 'John Doe', 100.0)
    delete_data(1)
    result = select_all_data()
    assert len(result) == 0

# Run the tests
if __name__ == "__main__":
    pytest.main()