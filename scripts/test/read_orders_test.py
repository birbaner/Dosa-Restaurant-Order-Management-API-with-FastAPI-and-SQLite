import unittest
from unittest.mock import patch, mock_open
import sys
import json
from io import StringIO
from script import main, read_orders_from_file

class TestMainFunction(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.open', new_callable=mock_open, read_data='[{"name": "John Doe", "phone": "123-456-7890", "items": [{"name": "Item1", "price": 10.0}]}]')
    def test_main_success(self, mock_file, mock_stdout):
        sys.argv = ['script.py', 'test.json']  # Simulate command-line arguments
        main()
        expected_output = """Orders read successfully:
Name: John Doe
Phone: 123-456-7890
Items:
- Item1: $10.00
"""
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

if __name__ == '__main__':
    unittest.main()

