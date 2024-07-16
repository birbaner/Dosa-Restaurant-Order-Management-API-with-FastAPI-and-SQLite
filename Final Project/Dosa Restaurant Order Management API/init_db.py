import json
import sqlite3

def initialize_database(json_file):
    """
    Initializes the SQLite database with data from a JSON file.

    Args:
        json_file (str): Path to the JSON file containing the orders data.

    Raises:
        Exception: If an error occurs during database initialization.
    """
    try:
        # Load data from the JSON file
        with open(json_file, 'r') as file:
            orders = json.load(file)

        # Connect to the SQLite database
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()

        # Create tables if they do not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            phone TEXT NOT NULL UNIQUE
                        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            price REAL NOT NULL
                        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                            id INTEGER PRIMARY KEY,
                            customer_id INTEGER NOT NULL,
                            item_id INTEGER NOT NULL,
                            quantity INTEGER NOT NULL,
                            timestamp INTEGER NOT NULL,
                            notes TEXT,
                            FOREIGN KEY (customer_id) REFERENCES customers (id),
                            FOREIGN KEY (item_id) REFERENCES items (id)
                        )''')

        # Insert data into the database
        for order in orders:
            # Insert or retrieve customer ID based on phone number
            cursor.execute("SELECT id FROM customers WHERE phone = ?", (order['phone'],))
            customer = cursor.fetchone()

            if customer is None:
                cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (order['name'], order['phone']))
                customer_id = cursor.lastrowid
            else:
                customer_id = customer[0]

            for item in order['items']:
                # Insert or retrieve item ID based on item name
                cursor.execute("SELECT id FROM items WHERE name = ?", (item['name'],))
                item_data = cursor.fetchone()

                if item_data is None:
                    cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (item['name'], item['price']))
                    item_id = cursor.lastrowid
                else:
                    item_id = item_data[0]

                # Insert order with customer_id, item_id, and other details
                cursor.execute('''INSERT INTO orders (customer_id, item_id, quantity, timestamp, notes) 
                                  VALUES (?, ?, 1, ?, ?)''', (customer_id, item_id, order['timestamp'], order['notes']))

        # Commit the transaction
        conn.commit()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()

if __name__ == "__main__":
    initialize_database('C:\\Users\\user\\Desktop\\Web_System_Final_project\\dosa_restaurant\\example_orders.json')
