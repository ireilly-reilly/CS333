import tablefunctions
import dbfunctions

def selectAll(tableName, currentdb):
    if currentdb == None:
        print("No specified database, enter 'USE <database_name>;'")
    else:
        if tablefunctions.findtable(tableName, currentdb):
            fedit = open(f'{currentdb}/{tableName}.txt', 'r')
            print(fedit.read())
            fedit.close()
        else:
            print("!Failed to query table " + tableName + " because it does not exist.")

