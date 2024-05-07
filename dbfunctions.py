#Programming Assignment 3
#CS 457 Prof. Zhao
#Written by Isaac Reilly
#dbfunctions.py

import os
import subprocess
import shlex
import shutil


#Function used to create specified database (local directory)
def create_db(dbName):
    try:
        #Tries making directory
        os.makedirs(dbName)    
        print("Database " +  dbName + " created.")
    except FileExistsError:
        #Checks to see if directory already exists, throws exception if it does
        print("!Failed to create database " + dbName + " because it already exists.")

#Function used to remove specified database (local directory)
def remove_db(dbName):
    #Checks to see if specified directory exists and deletes if it does
    if os.path.exists(dbName):
        shutil.rmtree(dbName) 
        print("Database " + dbName + " deleted.")
    #If selected directory does not exists, prints an error message to the screen    
    else:
        print("!Failed to delete " + dbName + " because it does not exist.")

#Checks to make sure that specified database exists
def finddb(dbName):
    if dbName in subprocess.run(['ls', '|', 'grep', dbName], capture_output = True, text = True).stdout:
        return 1
    else:
        return 0

#Returns an integer value based on the operand to be used as a comparison
def getOperand(op):
    operand = None
    if (op == '='):
        operand = 0
    elif (op == '!='):
        operand = -3
    elif (op == '<'):
        operand = -1
    elif (op == '>'):
        operand = 1
    return operand