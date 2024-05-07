import unittest
import os
import shutil
import subprocess
from unittest.mock import patch
from ..dbfunctions import create_db, remove_db, finddb, getOperand

class TestDBFunctions(unittest.TestCase):

    def setUp(self):
        #Create a test directory for database operations
        self.test_db_name = 'test_db'
        os.makedirs(self.test_db_name)

    def tearDown(self):
        #Clean up test directory after each test
        if os.path.exists(self.test_db_name):
            shutil.rmtree(self.test_db_name)

    def test_create_new_db_success(self):
        new_db_name = 'new_db'
        create_db(new_db_name)
        self.assertTrue(os.path.exists(new_db_name))
        shutil.rmtree(new_db_name)  # Clean up

    def test_create_db_already_exists(self):
        existing_db_name = self.test_db_name
        with patch('builtins.print') as mocked_print:
            create_db(existing_db_name)
            mocked_print.assert_called_with("!Failed to create database {} because it already exists.".format(existing_db_name))

    def test_remove_db_success(self):
        remove_db(self.test_db_name)
        self.assertFalse(os.path.exists(self.test_db_name))

    def test_remove_db_not_exists(self):
        non_existing_db_name = 'non_existing_db'
        with patch('builtins.print') as mocked_print:
            remove_db(non_existing_db_name)
            mocked_print.assert_called_with("!Failed to delete {} because it does not exist.".format(non_existing_db_name))

    #Find existing database
    @patch('subprocess.run')
    def test_find_existing_db(self, mocked_run):
        mocked_run.return_value.stdout = "test_db\nanother_db\n"
        self.assertEqual(finddb('test_db'), 1)

    @patch('subprocess.run')
    def test_find_nonexistent_db(self, mocked_run):
        mocked_run.return_value.stdout = "test_db\nanother_db\n"
        self.assertEqual(finddb('non_existing_db'), 0)

    def test_getOperand(self):
        #Test getOperand function for various operators
        self.assertEqual(getOperand('='), 0)
        self.assertEqual(getOperand('!='), -3)
        self.assertEqual(getOperand('<'), -1)
        self.assertEqual(getOperand('>'), 1)

if __name__ == '__main__':
    unittest.main()
