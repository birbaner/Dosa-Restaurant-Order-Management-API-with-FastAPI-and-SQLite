import sys # Importing sys module for command-line arguments handling
import json # Importing json module for JSON parsing
import re # Importing re module for regular expressions

def read_orders_from_file(file_path):
    """Reads JSON orders from a specified file.

    Args:
        file_path (str): Path to the JSON file containing orders.

    Returns:
        list or None: List of orders (dicts) if successful, None otherwise.
    """
    try:
        with open(file_path, 'r') as file:
            orders = json.load(file) # Load JSON data from file
            return orders # Return the list of orders
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.") # Print error message if file not found
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{file_path}': {e}") # Print error message for JSON decoding error
        return None

def extract_customers(orders):
    """Extracts customer names and phone numbers from orders.

    Args:
        orders (list): List of orders (dicts).

    Returns:
        dict: Dictionary with phone numbers as keys and customer names as values.
    """
    customers = {}
    phone_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$') # Regular expression pattern for phone number format
    
    for order in orders:
        phone = order.get('phone') # Extract phone number from order
        name = order.get('name')# Extract customer name from order
        if phone and name and phone_pattern.match(phone):  # Check if phone and name exist and phone matches pattern
            customers[phone] = name # Add phone number as key and customer name as value to dictionary
    return customers

def write_customers_to_file(customers, file_path):
    """Writes customer data to a JSON file.

    Args:
        customers (dict): Dictionary with phone numbers as keys and customer names as values.
        file_path (str): Path to the output JSON file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(customers, file, indent=4) # Write formatted JSON data to file
        print(f"Customer data successfully written to '{file_path}'") # Print success message
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}") # Print error message if file writing fails

def main():
    """Main function to execute when script is run."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <json_file_path>") # Print usage if no file path provided
        return

    input_file_path = sys.argv[1]  # Get input file path from command-line arguments
    output_file_path = 'customers.json' # Define output file name

    orders = read_orders_from_file(input_file_path) # Read orders from input JSON file
    
    if orders:
        customers = extract_customers(orders) # Extract customer data from orders
        write_customers_to_file(customers, output_file_path) # Write customer data to output JSON file
    else:
        print("No orders found or unable to read orders from file.") # Print message if no orders found

if __name__ == "__main__":
    main()
