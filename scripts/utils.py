# utils.py

import json

def read_json_file(file_path):
    """Reads JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict or None: JSON data if successful, None otherwise.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{file_path}': {e}")
        return None

def write_json_file(data, file_path):
    """Writes data to a JSON file.

    Args:
        data (dict): Data to write to the JSON file.
        file_path (str): Path to the output JSON file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully written to '{file_path}'")
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")
