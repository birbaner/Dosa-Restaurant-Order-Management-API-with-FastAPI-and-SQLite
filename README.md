# IS-601-moderterm-project

**TOPIC:Dosa Restaurant Order Management System**

**Order Processing Script**
This Python script processes JSON files containing order data. It reads the orders, extracts customer information (names and phone numbers), and processes item data (names, prices, and order counts). The extracted information is then written into separate JSON files (`customers.json` and `items.json`). Users can execute the script from the command line, providing the path to their JSON file as an argument, and receive clear feedback on the success or failure of the operations performed.

**Design**
The script is designed with modularity and clarity in mind, utilizing Python's capabilities to handle JSON data and command-line arguments effectively. It comprises several key functions: `read_orders_from_file()` reads JSON-formatted order data from a specified file, handling errors such as file not found or JSON decoding issues. `extract_customers()` extracts customer names and phone numbers from the orders, validating phone numbers using regular expressions. `write_customers_to_file()` writes extracted customer data into a JSON file. `process_orders()` processes orders to extract item names, prices, and count orders using a `defaultdict` for efficient data aggregation. `write_items_to_file()` writes processed item data into another JSON file. The main function `main()` coordinates these functions based on command-line input, ensuring clear output messages and error handling throughout. This design ensures the script can robustly handle input variations, process data accurately, and provide clear feedback to users, making it suitable for automating order data management tasks in a variety of scenarios.
**Example**
-read_orders_from_file(file_path): Reads JSON orders from a specified file path.
-extract_customers(orders): Extracts customer names and phone numbers from orders.
-write_customers_to_file(customers, file_path): Writes customer data to a JSON file.
-process_orders(orders): Processes orders to extract item names, prices, and count orders.
-write_items_to_file(items, file_path): Writes item data to a JSON file.

**The main function main() orchestrates the entire process:**

-It checks if a JSON file path is provided as a command-line argument.
-It reads orders from the input file.
-Depending on the task, it either extracts customer information or processes item data.
-Results are written to separate JSON files (customers.json and items.json).

**Usage**
To use the script, first ensure to have Python 3.x installed on the system. Download or clone the script files from the repository. Open a terminal or command prompt, navigate to the directory containing the script, and execute it with Python, providing a path to the JSON input file as a command-line argument.For example, run python script.py orders.json where orders.json is the JSON file containing order details. Follow the console output for status messages, including successful data processing or error notifications if issues arise during file reading, JSON decoding, or data extraction. The script will generate customers.json containing extracted customer information and items.json with processed item data, making it easy to manage and analyze order information programmatically. 

**Prerequisites**
-Python 3.x
-JSON-formatted input files

**Running the Script**
-download the script files.
-Open a terminal or command prompt.
-Navigate to the directory containing the script files.

**Execute the script with the following command:**
-python script.py <json_file_path>
**example:**
python read_orders.py example_orders.json

saving output file into .txt file:
-python script.py <json_file_path> > output.txt
**Example:**
python read_orders.py example_orders.json > read_orders_output.txt 

