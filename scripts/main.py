# scripts/main.py

from scripts.read_orders import read_orders_from_file
from scripts.customers_phone_no_name import extract_customers, write_customers_to_file
from scripts.items_price_num_order import process_orders, write_items_to_file

def main():
    input_file_path = 'IS-601-midterm-project/data/orders.json'  
    output_customers_path = 'IS-601-midterm-project/data/customers.json'
    output_items_path = 'IS-601-midterm-project/data/items.json'

    # Read orders from file
    orders = read_orders_from_file(input_file_path)

    if orders:
        # Extract customers and write to customers.json
        customers = extract_customers(orders)
        write_customers_to_file(customers, output_customers_path)

        # Process orders and write to items.json
        items = process_orders(orders)
        write_items_to_file(items, output_items_path)
    else:
        print("No orders found or unable to read orders from file.")

if __name__ == "__main__":
    main()
