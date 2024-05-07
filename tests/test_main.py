import unittest
from unittest.mock import patch
import io
import main  # Import your main script to be tested
import os
import shutil
import dbfunctions
import tablefunctions


class TestParseInput(unittest.TestCase):


    #Test for CREATE DATABASE command
    def test_parse_create_database(self):
        test_db = 'test_db'
        user_input = "CREATE DATABASE test_db;"
        captured_output = io.StringIO()
        expected_output = f"Database test_db created.\n"
        with patch('sys.stdout', new=captured_output):
            main.parse_input(user_input)
            self.assertEqual(captured_output.getvalue(), expected_output)
        shutil.rmtree(test_db)

    #Test for invalid command missing semicolon
    def test_parse_invalid_command(self):
        user_input = "CREATE DATABASE test_db"  #Missing ;
        captured_output = io.StringIO()
        expected_output = "Invalid command, all commands must end with ';'\n"
        with patch('sys.stdout', new=captured_output):
            main.parse_input(user_input)
            self.assertEqual(captured_output.getvalue(), expected_output)

    #Test for SELECT command (Integration test that builds database, table, and fails to read entries)
    def test_parse_select_invalid_table(self):
        test_db = 'test_db'
        user_input = "CREATE DATABASE test_db;"
        main.parse_input(user_input)
        user_input = "USE test_db;"
        main.parse_input(user_input)
        user_input = "SELECT * FROM test_table;"
        captured_output = io.StringIO()
        expected_output = "!Failed to query table test_table because it does not exist.\n"
        with patch('sys.stdout', new=captured_output):
            main.parse_input(user_input)
            # Assert that the expected function is called (not testing the function's content here)
            self.assertEqual(captured_output.getvalue(), expected_output)
        #shutil.rmtree(test_db)

    #Test insert data into table (Integration test that writes creates database, table, entry)
    def test_parse_insert_data_into_table(self):
        test_db = 'test_db'
        user_input = "CREATE DATABASE test_db;"
        main.parse_input(user_input)
        user_input = "USE test_db;"
        main.parse_input(user_input)
        user_input = 'CREATE TABLE Product(pid int, name varchar(20), price float);'
        main.parse_input(user_input)
        user_input = "INSERT INTO Product values(1, 'Gizmo', 19.99);"
        captured_output = io.StringIO()
        expected_output = "1 new record inserted.\n"
        with patch('sys.stdout', new=captured_output):
            main.parse_input(user_input)
            # Assert that the expected function is called (not testing the function's content here)
            self.assertEqual(captured_output.getvalue(), expected_output)
        shutil.rmtree(test_db)

    #Test insert data into invalid table (Integration test that creates database, but can't enter data into nonexistent table)
    def test_parse_insert_into_invalid_table(self):
        test_db = 'test_db'
        user_input = "CREATE DATABASE test_db;"
        main.parse_input(user_input)
        user_input = "USE test_db;"
        main.parse_input(user_input)
        # user_input = 'CREATE TABLE Product(pid int, name varchar(20), price float);'
        # main.parse_input(user_input)
        user_input = "INSERT INTO Product values(1, 'Gizmo', 19.99);"
        captured_output = io.StringIO()
        expected_output = "!Failed to insert data into Product because it does not exist.\n"
        with patch('sys.stdout', new=captured_output):
            main.parse_input(user_input)
            self.assertEqual(captured_output.getvalue(), expected_output)
        shutil.rmtree(test_db)

    #Test drop table route, try to delete table that doesn't exist (Integration)
    def test_parse_delete_invalid_table(self):
        test_db = 'test_db'
        user_input = "CREATE DATABASE test_db;"
        main.parse_input(user_input)
        user_input = "USE test_db;"
        main.parse_input(user_input)
        user_input = "DROP TABLE invalid_table;"
        captured_output = io.StringIO()
        expected_output = "!Failed to delete invalid_table because it does not exist.\n"
        with patch('sys.stdout', new=captured_output):
            main.parse_input(user_input)
            self.assertEqual(captured_output.getvalue(), expected_output)
        shutil.rmtree(test_db)

    #Test drop table route successfully(Integration test because it handles relationships between database, tables, and entries in table)
    def test_parse_delete_valid_table(self):
        test_db = 'test_db'
        user_input = "CREATE DATABASE test_db;"
        main.parse_input(user_input)
        user_input = "USE test_db;"
        main.parse_input(user_input)
        user_input = 'CREATE TABLE Product(pid int, name varchar(20), price float);'
        main.parse_input(user_input)
        user_input = "INSERT INTO Product values(1, 'Gizmo', 19.99);"
        main.parse_input(user_input)
        user_input = "DROP TABLE Product;"
        captured_output = io.StringIO()
        expected_output = "Table Product deleted.\n"
        with patch('sys.stdout', new=captured_output):
            main.parse_input(user_input)
            self.assertEqual(captured_output.getvalue(), expected_output)
        shutil.rmtree(test_db)

    #Test for USING non-existent database
    def test_parse_use_non_existent_database(self):
        user_input = "USE non_existent_db;"
        captured_output = io.StringIO()
        expected_output = "Unable to use database non_existent_db because it does not exist.\n"
        with patch('sys.stdout', new=captured_output):
            main.parse_input(user_input)
            self.assertEqual(captured_output.getvalue(), expected_output)

    


if __name__ == '__main__':
    unittest.main()
