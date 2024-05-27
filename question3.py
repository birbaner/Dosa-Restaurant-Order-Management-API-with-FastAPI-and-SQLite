import json

# Ensure we're starting with a clean slate by checking the content of the input file
with open('example_orders.json', 'r') as file:
    example_orders = json.load(file)

# Initialize a dictionary to hold the items information
items_info = {}

# Process each order in the input data
for order in example_orders:
    for item in order["items"]: #Within each order, we iterate over the items list, which contains the items ordered by the customer.
        #For each item in the order, we extract the name and price. We use this information to update our items_info dictionary, which keeps track of the total number of orders for each item.
        item_name = item["name"] 
        item_price = item["price"]

        # Check if the item already exists in the dictionary
        #If the item is already in the dictionary, we increment the order count. If not, we add it to the dictionary with an initial order count of 1.
        if item_name in items_info:
            # Increment the order count
            items_info[item_name]["orders"] += 1
        else:
            # Add a new item to the dictionary with an initial order count of 1
            items_info[item_name] = {
                "price": item_price,
                "orders": 1
            }

# Print the items_info dictionary to debug the final counts
print(json.dumps(items_info, indent=4))

# Write the final items_info dictionary to the items.json file
with open('items.json', 'w') as json_file:
    json.dump(items_info, json_file, indent=4)

print("items.json file has been created.")
