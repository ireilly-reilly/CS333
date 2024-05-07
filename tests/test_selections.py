import unittest
from unittest.mock import patch
from ..selections import selectAll

class TestSelections(unittest.TestCase):

    #Selects all data from a table and prints it (Integration test because it requires a database and table)
    def test_selectAll_success(self):
        #Mocking tablefunctions.findtable to return True (table exists)
        with patch('selections.tablefunctions.findtable', return_value=True):
            with patch('builtins.open', unittest.mock.mock_open(read_data='column1 | column2\nvalue1 | value2\n')):
                with patch('builtins.print') as mocked_print:
                    selectAll('test_table', 'test_db')
                    mocked_print.assert_called_with('column1 | column2\nvalue1 | value2\n')

    #table doesn't exist
    def test_select_all_from_nonexistent_table(self):
        #Mocking tablefunctions.findtable to return False (table does not exist)
        with patch('selections.tablefunctions.findtable', return_value=False):
            with patch('builtins.print') as mocked_print:
                selectAll('non_existing_table', 'test_db')
                mocked_print.assert_called_with('!Failed to query table non_existing_table because it does not exist.')

if __name__ == '__main__':
    unittest.main()
