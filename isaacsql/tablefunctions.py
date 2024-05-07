#Programming Assignment 3
#CS 457 Prof. Zhao
#Written by Isaac Reilly
#tablefunctions.py

import subprocess
import os

#Checks to make sure that specified table exists
def findtable(tableName, currentdb):
    if tableName in subprocess.run(['ls', currentdb,  '|', 'grep', tableName], capture_output = True, text = True).stdout:
        return 1
    else:
        return 0

#Creates table with specified headers
def createTable(dataInput, tableName, currentdb):
    unformattedAttributes = dataInput.replace(tableName, "")
    print(unformattedAttributes)
    tableAttributes1 = unformattedAttributes[1:]
    tableAttributes2 = tableAttributes1[:-1]
    formattedAttributes = tableAttributes2.split(",")

    if (currentdb != None):
        if findtable(tableName, currentdb) == 0:
            os.system(f'touch {currentdb}/{tableName}.txt')
            filename = currentdb + '/' + tableName + '.txt'
            fedit = open(filename, 'w')
            fedit.write(" |".join(formattedAttributes))
            fedit.close()
            print(f"Created table {tableName}.")
        else:
            print("!Failed to create " + tableName + " because it already exists.")
    else:
        print("Please specify which database to use.")

#Deletes specified table
def dropTable(tableName, currentdb):
    if (currentdb != None):
        if findtable(tableName, currentdb) != 0:
            os.system(f'rm {currentdb}/{tableName}.txt')
            print("Table " + tableName + " deleted.")
        else:
            print("!Failed to delete " + tableName + " because it does not exist.")
    else:
        print("No specified database, enter 'USE <database_name>;'")

#Inserts data into specified table
def insertData(dataInput, tableName, currentdb):
    unformattedInput = dataInput.replace(tableName, "")
    cleanedInput1 = unformattedInput.replace("'", "")
    cleanedInput2 = cleanedInput1.replace(" ", "")
    unformattedAttributes = cleanedInput2[7:-1]
    formattedAttributes = unformattedAttributes.split(",")

    if (currentdb != None):
        if findtable(tableName, currentdb):
            fedit = open(f'{currentdb}/{tableName}.txt', 'a')
            fedit.write("\n" + " | ".join(formattedAttributes))
            fedit.close()
            print("1 new record inserted.")
        else:
            print("!Failed to insert data into " + tableName + " because it does not exist.")
    else:
        print("No specified database, enter 'USE <database_name>;'")

