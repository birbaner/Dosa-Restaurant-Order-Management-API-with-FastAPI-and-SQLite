import sys  # Importing sys module for command-line arguments handling
import json  # Importing json module for JSON parsing

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
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{file_path}': {e}")
        return None

def main():
    """Main function to execute when script is run."""
    # Checking if the script is provided with the JSON file path as a command-line argument
    if len(sys.argv) < 2: #checks if sys.argv has two elements: the script  and the file path.
        print("Usage: python script.py <json_file_path>")
        return

    file_path = sys.argv[1]  # Getting the JSON file path from command-line arguments;

    orders = read_orders_from_file(file_path)  # Reading orders from the specified file
    if orders:
        print("Orders read successfully:")
        # Iterating through each order and printing its details
        for order in orders:
            print(f"Name: {order['name']}")
            print(f"Phone: {order['phone']}")
            print("Items:")
            for item in order['items']:
                print(f"- {item['name']}: ${item['price']:.2f}")  # Formatting price to 2 decimal places
            if order['notes']:
                print(f"Notes: {order['notes']}")
            print()

if __name__ == "__main__":
    main()
