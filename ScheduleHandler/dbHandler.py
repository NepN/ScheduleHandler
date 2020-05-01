import sqlite3 

def ConnectDB(): # creates db if not existing 
    connection = sqlite3.connect("any.db") 
    cursor = connection.cursor() 
    return cursor; # return value of 'cursor' to line of fnc-call 

def SetUpTable(cursor, table_name = "staff", index_field = "staff_id", name = "last_name"): 
    # add customizability with variables with default value 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS """ + table_name + """(
        """ + index_field + """ INTEGER PRIMARY KEY, 
        """ + name + """ VARCHAR(20)
        );"""
        )
    return; # return to line of fnc-call 
