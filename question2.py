#Creates a new JSON file named customers.json that contains an object with phone numbers as keys and customers names as values.
#The phone number and customer name should both be strings and the phone number should be of the form xxx-xxx-xxxx

import json
import sys

def read_orders(file_name):
    try:
        with open(file_name, 'r') as file:
            orders = json.load(file)
        return orders
    except Exception as e:
        print(f"Error reading the file: {e}")
        return []

def process_orders(orders):
    for order in orders:
        print(f"Order from {order['name']} ({order['phone']}):")
        for item in order['items']:
            print(f" - {item['name']}: ${item['price']:.2f}")
        if order['notes']:
            print(f" Notes: {order['notes']}")
        print()

def create_customers_file(orders, output_file_name): #akes two parameters: orders (the list of orders) and output_file_name (the name of the output file).
    customers = {} # initializes an empty dictionary to store phone numbers and names
    #loop goes through each order and extracts the phone number and name, adding them to the customers dictionary.
    for order in orders:
        phone = order['phone']
        name = order['name']
        customers[phone] = name
    
    try:
        with open(output_file_name, 'w') as file: #opens the file specified by output_file_name in write mode
            json.dump(customers, file, indent=4) #This line writes the contents of the customers dictionary to the file in JSON format. 
        print(f"Customers data has been written to {output_file_name}") #If writing to the file is successful, this line prints a message indicating that the operation was successful, along with the name of the file to which the data was written.


    except Exception as e: # if it catches any exception that occurs within the try block and assigns it to the variable e.
        print(f"Error writing the file: {e}") # If an exception occurs during the execution of the try block, this line prints an error message indicating the nature of the error 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_orders.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    orders = read_orders(file_name)
    process_orders(orders)
    create_customers_file(orders, 'customers.json')
