import unittest
import os
import shutil
from ..tablefunctions import findtable, createTable, dropTable, insertData

class TestTableFunctions(unittest.TestCase):

    #Create test database directory for every test
    def setUp(self):
        self.test_db = 'test_db'
        if not os.path.exists(self.test_db):
            os.makedirs(self.test_db)

    #Remove test database directory after each test
    def tearDown(self):
        self.test_db = 'test_db'
        if os.path.exists(self.test_db):
            shutil.rmtree(self.test_db)

    def test_find_existing_table(self):
        self.table_name = 'test_table' 
        self.table_path = os.path.join(self.test_db, f'{self.table_name}.txt')
        with open(self.table_path, 'w') as f:
            f.write('test')

        #Test finding an existing table
        result = findtable(self.table_name, self.test_db)
        self.assertEqual(result, 1)

    def test_find_nonexisting_table(self):
        #Test finding a non-existing table
        result = findtable('non_existing_table', self.test_db)
        self.assertEqual(result, 0)

    def test_createTable_success(self):
        #Test creating a new table
        table_name = 'new_table'
        attributes = 'column1, column2'
        createTable(attributes, table_name, self.test_db)

        #Check if table file was created
        table_path = os.path.join(self.test_db, f'{table_name}.txt')
        self.assertTrue(os.path.exists(table_path))

    def test_drop_table_success(self):
        table_name = 'existing_table'
        table_path = os.path.join(self.test_db, f'{table_name}.txt')
        with open(table_path, 'w') as f:
            f.write('column1 | column2\nvalue1 | value2\n')

        dropTable(table_name, self.test_db)

        self.assertFalse(os.path.exists(table_path))

    def test_insertData_success(self):
        # Create a test table
        table_name = 'table'
        table_path = os.path.join(self.test_db, f'{table_name}.txt')
        with open(table_path, 'w') as f:
            f.write('id int | name varchar(10)\n')

        data_input = "table values(1,'Joe');"
        insertData(data_input, table_name, self.test_db)

        with open(table_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 3)  #Expecting 3 lines (header + 2 records)

    

if __name__ == '__main__':
    unittest.main()
