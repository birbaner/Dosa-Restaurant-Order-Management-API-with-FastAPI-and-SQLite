#Reads the JSON orders from a file whose name is passed as the first positional argument

import json #This library is used for reading and writing JSON dat
import sys #This module provides access to command-line arguments

def read_orders(file_name): #this function takes one parameter 'file_name
    try: #try block to catch any exceptions that might occur while reading the file
        with open(file_name,'r') as file: #opens file in read mode; The with statement ensures the file is automatically closed after its block of code is done, even if an exception is raised.
            orders =json.load(file) #reads the JSON data from the file and parses it intoa Python object (a list of dictionaries, in this case).
        return orders #returns the parsed JSON data
    except Exception as e: #catches any exceptions that occurred in the try block
        print(f"Error reading the file:{e}") #prints an error message if an exception occurs
        return[] #eturns an empty list if there was an error reading the file
    
def process_orders(orders): #function takes one parameter, orders.
    for order in orders: #a loop that iterates over each order in the orders list.
        print(f"Order from {order['name']} ({order['phone']}):") #prints the customer's name and phone number.
        for item in order['items']: #starts a loop that iterates over each item in the items list of the current order.
            print(f" - {item['name']}: ${item['price']:.2f}") #prints the item's name and price 
        if order['notes']: #checks if there are any notes for the order
            print(f" Notes: {order['notes']}") #prints the notes if they exist
            print() #prints a blank line to separate orders visually

if __name__=="__main__": #code block is only executed if the script is run directly (not imported as a module)
    if len(sys.argv) !=2: # checks if sys.argv has two elements: the script name and the file name.
        print("Usage: python process_orders.py<file_name>") #prints the correct usage of the script if the number of arguments is incorrect.
        sys.exit(1) #exits the script with a status code of 1, indicating an error

    file_name = sys.argv[1] #assigns the first command-line argument (the file name) to the variable file_name
    orders =read_orders(file_name) #This calls the read_orders function with file_name and assigns the returned orders list to the variable orders
    process_orders(orders) #calls the process_orders function with the orders list