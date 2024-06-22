import unittest
from unittest.mock import patch, mock_open
import sys
import json
from collections import defaultdict
from script import main, read_orders_from_file, process_orders, write_items_to_file

class TestMainFunction(unittest.TestCase):

    @patch('sys.stdout', new_callable=unittest.mock._StringIO)
    @patch('builtins.open', new_callable=mock_open, read_data='[{"name": "John Doe", "items": [{"name": "Item1", "price": 10.0}, {"name": "Item2", "price": 20.0}]}]')
    def test_main_success(self, mock_file, mock_stdout):
        sys.argv = ['script.py', 'test.json']  # Simulate command-line arguments
        main()
        expected_output = "Item data successfully written to 'items.json'\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stderr', new_callable=unittest.mock._StringIO)
    def test_main_missing_file(self, mock_stderr):
        sys.argv = ['script.py']  # Simulate command-line arguments without file path
        main()
        expected_error = "Usage: python script.py <json_file_path>\n"
        self.assertEqual(mock_stderr.getvalue(), expected_error)

    @patch('sys.stderr', new_callable=unittest.mock._StringIO)
    def test_main_file_not_found(self, mock_stderr):
        sys.argv = ['script.py', 'non_existent_file.json']  # Simulate command-line arguments with non-existent file
        main()
        expected_error = f"Error: The file 'non_existent_file.json' was not found.\n"
        self.assertEqual(mock_stderr.getvalue(), expected_error)

    @patch('sys.stderr', new_callable=unittest.mock._StringIO)
    @patch('builtins.open', side_effect=json.JSONDecodeError('Error message', '', 0))
    def test_main_json_decode_error(self, mock_open, mock_stderr):
        sys.argv = ['script.py', 'invalid_json.json']  # Simulate command-line arguments with invalid JSON file
        main()
        expected_error = f"Error decoding JSON from file 'invalid_json.json': Error message\n"
        self.assertEqual(mock_stderr.getvalue(), expected_error)

class TestFunctions(unittest.TestCase):

    def test_read_orders_from_file_success(self):
        test_data = '[{"name": "John Doe", "items": [{"name": "Item1", "price": 10.0}]}]'
        mock_open_func = mock_open(read_data=test_data)
        with patch('builtins.open', mock_open_func):
            orders = read_orders_from_file('test.json')
            self.assertIsNotNone(orders)
            self.assertEqual(len(orders), 1)
            self.assertEqual(orders[0]['name'], 'John Doe')
            self.assertIn('items', orders[0])

    def test_read_orders_from_file_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            orders = read_orders_from_file('non_existent_file.json')
            self.assertIsNone(orders)

    def test_process_orders(self):
        orders = [{'name': 'John Doe', 'items': [{'name': 'Item1', 'price': 10.0}, {'name': 'Item2', 'price': 20.0}]}, {'name': 'Jane Smith', 'items': [{'name': 'Item1', 'price': 10.0}]}]
        items = process_orders(orders)
        self.assertEqual(len(items), 2)
        self.assertIn('Item1', items)
        self.assertIn('Item2', items)
        self.assertEqual(items['Item1']['price'], 10.0)
        self.assertEqual(items['Item1']['orders'], 2)
        self.assertEqual(items['Item2']['price'], 20.0)
        self.assertEqual(items['Item2']['orders'], 1)

    @patch('sys.stderr', new_callable=unittest.mock._StringIO)
    def test_write_items_to_file(self, mock_stderr):
        items = {'Item1': {'price': 10.0, 'orders': 2}, 'Item2': {'price': 20.0, 'orders': 1}}
        mock_file = mock_open()
        with patch('builtins.open', mock_file):
            write_items_to_file(items, 'test_items.json')
            mock_file.assert_called_once_with('test_items.json', 'w')
            handle = mock_file()
            handle.write.assert_called_once_with(json.dumps(items, indent=4))

if __name__ == '__main__':
    unittest.main()

