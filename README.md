**Dosa Restaurant Order Management System**

**Overview**
**IS-601 Midterm Project**

This Python project manages orders for a Dosa restaurant using JSON files. The script reads JSON files containing order data, extracts customer information (names and phone numbers), and processes item data (names, prices, and order counts). It outputs the extracted information into separate JSON files (customers.json and items.json). The script is designed to be executed from the command line, allowing users to specify the path to their JSON file as an argument and receive feedback on the success or failure of the operations performed.

**Design**
The script is structured with modularity and clarity in mind, leveraging Python's capabilities to handle JSON data and command-line arguments efficiently. Key functions include:

read_orders_from_file(file_path): Reads JSON orders from a specified file path, handling errors such as file not found or JSON decoding issues.

extract_customers(orders): Extracts customer names and phone numbers from orders, validating phone numbers using regular expressions.

write_customers_to_file(customers, file_path): Writes extracted customer data into a JSON file (customers.json).

process_orders(orders): Processes orders to extract item names, prices, and count orders using defaultdict for efficient data aggregation.

write_items_to_file(items, file_path): Writes processed item data into another JSON file (items.json).

The main() function orchestrates these functions based on command-line input, ensuring clear output messages and comprehensive error handling throughout. This design enables the script to handle various input scenarios, process data accurately, and provide actionable feedback to users, making it suitable for automating order data management tasks.

**Example Usage**
**Prerequisites**
-Python 3.x installed on your system.
-JSON-formatted input files containing order data.

**Running the Script**
**-Download or Clone the Repository**
Clone the repository to your local machine or download the script files.

git clone https://github.com/your-username/IS-601-midterm-project.git

**-Navigate to the Script Directory**
Open a terminal or command prompt and navigate to the directory containing the script files.

cd IS-601-midterm-project

**-Execute the Script**
Run the script using Python, providing the path to your JSON input file as a command-line argument.

python script.py orders.json (Replace orders.json with the actual filename of your JSON input file.)

**Output**

-The script will process the orders and generate two output files:
-customers.json: Contains extracted customer information.
-items.json: Contains processed item data.

**Advanced Usage**
-Saving Output to a File
Redirect script output to a text file for record-keeping or further analysis.

python script.py orders.json > output.txt(This command saves the console output to output.txt.)

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Prerequisites**
-Python 3.x
-JSON-formatted input files

**Notes**
-Update placeholders like your-username in the clone command with your actual GitHub username or repository URL.
-Customize file paths (orders.json, script.py) according to your project's structure.
-Ensure all dependencies are installed (as listed in requirements.txt) before running the script.
-Include additional sections or details specific to your project's requirements or usage scenarios.

