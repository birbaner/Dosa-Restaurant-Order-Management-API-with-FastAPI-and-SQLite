import sys  # Importing sys module for command-line arguments handling
import json  # Importing json module for JSON parsing
from collections import defaultdict  # Importing defaultdict for easy handling of item data

def read_orders_from_file(file_path):
    """Reads JSON orders from a specified file.

    Args:
        file_path (str): Path to the JSON file containing orders.

    Returns:
        list or None: List of orders (dicts) if successful, None otherwise.
    """
    try:
        with open(file_path, 'r') as file:
            orders = json.load(file)  # Load JSON data from file
            return orders  # Return the list of orders
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")  # Print error message if file not found
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{file_path}': {e}")  # Print error message for JSON decoding error
        return None

def process_orders(orders):
    """Processes orders to extract item names, prices, and count orders.

    Args:
        orders (list): List of orders (dicts).

    Returns:
        dict: Dictionary with item names as keys and nested dictionaries with 'price' and 'orders' as values.
    """
    items = defaultdict(lambda: {'price': 0, 'orders': 0})  # Initialize defaultdict with nested structure

    for order in orders:
        for item in order.get('items', []):  # Iterate over items in each order
            item_name = item.get('name')  # Extract item name
            item_price = item.get('price')  # Extract item price

            if item_name and item_price:
                items[item_name]['price'] = item_price  # Set item price in defaultdict
                items[item_name]['orders'] += 1  # Increment order count for the item
    
    return items

def write_items_to_file(items, file_path):
    """Writes item data to a JSON file.

    Args:
        items (dict): Dictionary with item names as keys and nested dictionaries with 'price' and 'orders' as values.
        file_path (str): Path to the output JSON file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(items, file, indent=4)  # Write formatted JSON data to file with indentation
        print(f"Item data successfully written to '{file_path}'")  # Print success message
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")  # Print error message if file writing fails

def main():
    """Main function to execute when script is run."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <json_file_path>")  # Print usage if no file path provided
        return

    input_file_path = sys.argv[1]  # Get input file path from command-line arguments
    output_file_path = 'items.json'  # Define output file name

    orders = read_orders_from_file(input_file_path)  # Read orders from input JSON file
    
    if orders:
        items = process_orders(orders)  # Process orders to extract item data
        write_items_to_file(items, output_file_path)  # Write processed item data to output JSON file
    else:
        print("No orders found or unable to read orders from file.")  # Print message if no orders found

if __name__ == "__main__":
    main()
