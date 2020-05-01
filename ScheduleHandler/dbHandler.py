import sqlite3 

def ConnectDB(db_name = "any"): # creates db if not existing 
    connection = sqlite3.connect(db_name + ".db")  
    cursor = connection.cursor() 
    return cursor; # return value of 'cursor' to line of fnc-call 

def SetUpTable(cursor, table_name = "staff", index_field = "staff_id", name = "last_name"): 
    # pass variables with default value 
    # very basic way, prone to SQL-injections 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS """ + table_name + """(
        """ + index_field + """ INTEGER PRIMARY KEY, 
        """ + name + """ VARCHAR(20)
        );"""
        )
    return; # return to line of fnc-call 
