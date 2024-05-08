#Programming Assignment 2
#CS 457 Prof. Zhao
#10/25/2022
#Written by Isaac Reilly
#main.py

import dbfunctions
import tablefunctions
import selections

TableList = [None]
user_input = None

def parse_input(user_input):
    global currentdb
    
    #States that all commands must end with a ';' if user types invalid command
    if ";" not in user_input and user_input != ".EXIT" and user_input != ".exit":
        print("Invalid command, all commands must end with ';'")

    #Creates a database
    elif "CREATE DATABASE" in user_input.upper():
        dbName = user_input[16:-1]
        dbfunctions.create_db(dbName)
        
    #Deletes a database
    elif "DROP DATABASE" in user_input.upper():
        dbName = user_input[14:-1]
        dbfunctions.remove_db(dbName)

    #Sets current working database 
    elif "USE" in user_input.upper():
        #currentdb = None
        dbName = user_input[4:-1]
        currentdb = user_input[4:-1]
        if dbfunctions.finddb(currentdb):
            print("Using database " + currentdb)
        else:
            print("Unable to use database " + dbName + " because it does not exist.")

    #Creates a table using attributes inputted by user
    elif "CREATE TABLE" in user_input.upper():
        tInput = user_input[13:-1]
        tableName = tInput.split("(")[0]
        tablefunctions.createTable(tInput, tableName, currentdb)

    #Deletes a table
    elif "DROP TABLE" in user_input.upper():
        tableName = user_input[11:-1]
        tablefunctions.dropTable(tableName, currentdb)

    # #Selects data from a user specified table and prints contents to terminal 
    # elif "SELECT * FROM" in user_input.upper():
    #     tableName = user_input[14:-1]
    #     selections.selectAll(tableName, currentdb)

    #Inserts given data into a specified table
    elif "INSERT INTO" in user_input.upper():
        dataInput = user_input[12:-1]
        tableName = dataInput.split()[0]
        tablefunctions.insertData(dataInput, tableName, currentdb)

    #Exits the program
    elif user_input == ".EXIT" or ".exit":
        print("Bye!")
        quit()
    



def get_user_input(user_input):   
    #Loop continously prompts the terminal for an input from the user and then decides what to do based on input.
    while (user_input != ".EXIT" or ".exit"):
        user_input = input("IsaacSQL > ")
        parse_input(user_input)

def main():
    user_input = None
    get_user_input(user_input)

if __name__ == "__main__":
    main()