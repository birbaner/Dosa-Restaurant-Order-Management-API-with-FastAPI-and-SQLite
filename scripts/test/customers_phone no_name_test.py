import unittest
from unittest.mock import patch, mock_open
import sys
import json
import re
from io import StringIO
from script import main, read_orders_from_file, extract_customers, write_customers_to_file

class TestMainFunction(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.open', new_callable=mock_open, read_data='[{"name": "John Doe", "phone": "123-456-7890"}]')
    def test_main_success(self, mock_file, mock_stdout):
        sys.argv = ['script.py', 'test.json']  # Simulate command-line arguments
        main()
        expected_output = "Customer data successfully written to 'customers.json'\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stderr', new_callable=StringIO)
    def test_main_missing_file(self, mock_stderr):
        sys.argv = ['script.py']  # Simulate command-line arguments without file path
        main()
        expected_error = "Usage: python script.py <json_file_path>\n"
        self.assertEqual(mock_stderr.getvalue(), expected_error)

    @patch('sys.stderr', new_callable=StringIO)
    def test_main_file_not_found(self, mock_stderr):
        sys.argv = ['script.py', 'non_existent_file.json']  # Simulate command-line arguments with non-existent file
        main()
        expected_error = f"Error: The file 'non_existent_file.json' was not found.\n"
        self.assertEqual(mock_stderr.getvalue(), expected_error)

    @patch('sys.stderr', new_callable=StringIO)
    @patch('builtins.open', side_effect=json.JSONDecodeError('Error message', '', 0))
    def test_main_json_decode_error(self, mock_open, mock_stderr):
        sys.argv = ['script.py', 'invalid_json.json']  # Simulate command-line arguments with invalid JSON file
        main()
        expected_error = f"Error decoding JSON from file 'invalid_json.json': Error message\n"
        self.assertEqual(mock_stderr.getvalue(), expected_error)

class TestFunctions(unittest.TestCase):

    def test_read_orders_from_file_success(self):
        test_data = '[{"name": "John Doe", "phone": "123-456-7890"}]'
        mock_open_func = mock_open(read_data=test_data)
        with patch('builtins.open', mock_open_func):
            orders = read_orders_from_file('test.json')
            self.assertIsNotNone(orders)
            self.assertEqual(len(orders), 1)
            self.assertEqual(orders[0]['name'], 'John Doe')

    def test_read_orders_from_file_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            orders = read_orders_from_file('non_existent_file.json')
            self.assertIsNone(orders)

    def test_extract_customers(self):
        orders = [{'name': 'John Doe', 'phone': '123-456-7890'}, {'name': 'Jane Smith', 'phone': '234-567-8901'}]
        customers = extract_customers(orders)
        self.assertEqual(len(customers), 2)
        self.assertIn('123-456-7890', customers)
        self.assertIn('234-567-8901', customers)
        self.assertEqual(customers['123-456-7890'], 'John Doe')
        self.assertEqual(customers['234-567-8901'], 'Jane Smith')

    @patch('sys.stderr', new_callable=StringIO)
    def test_write_customers_to_file(self, mock_stderr):
        customers = {'123-456-7890': 'John Doe', '234-567-8901': 'Jane Smith'}
        mock_file = mock_open()
        with patch('builtins.open', mock_file):
            write_customers_to_file(customers, 'test_customers.json')
            mock_file.assert_called_once_with('test_customers.json', 'w')
            handle = mock_file()
            handle.write.assert_called_once_with(json.dumps(customers, indent=4))

if __name__ == '__main__':
    unittest.main()

