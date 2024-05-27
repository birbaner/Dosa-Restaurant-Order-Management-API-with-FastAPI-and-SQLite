# IS-601-moderterm-project
Dosa Restaurant Order Management System

Overview
The Dosa Restaurant Order Management System is designed to enhance the efficiency of order processing and customer management for a Dosa restaurant. By analyzing past orders, the system aims to provide insights into customer preferences and item popularity, ultimately leading to improved customer satisfaction and business performance.

Features
Order Analysis: The system reads JSON orders from a file and extracts relevant information such as customer details and items ordered.

Customer Management: Generates a customers.json file containing customer phone numbers and names in the format xxx-xxx-xxxx.

Item Sales Analysis: Creates an items.json file containing analysis of item sales, including the price and the number of times each item has been ordered.

Usage
Input Data: I have a JSON file containing orders in the specified format. Each order includes details such as timestamp, customer name, phone number, items ordered, and any additional notes.

Running the Script: Execute the Python script with the name of the JSON file containing orders as the first positional argument. This will generate two new JSON files: customers.json and items.json.

Output Files: Review the generated JSON files for insights into customer behavior and item popularity.
