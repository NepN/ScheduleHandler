import sqlite3 

def connect_db(db_name = "any"): # creates db if not existing 
    connection = sqlite3.connect(db_name + ".db")  
    cursor = connection.cursor() 
    return cursor; # return value of 'cursor' to line of fnc-call 

def setup_table(target, table_name = "staff", index_field = "staff_id", name = "last_name"): 
    # pass variables with default value 
    # very basic way, prone to SQL-injections 
    target.execute("""DROP TABLE IF EXISTS""" + table_name) 
    target.execute("""
        CREATE TABLE IF NOT EXISTS """ + table_name + """(
        """ + index_field + """ INTEGER PRIMARY KEY, 
        """ + name + """ VARCHAR(20)
        );"""
        )
    return; # return to line of fnc-call 

def add_entry(target,table_name = "staff", name = "TestUser1"):
    target.execute("""INSERT INTO """ + table_name + """(staff_id,last_name)
        VALUES (NULL, '""" + name + """');""")
    return; 

def get_table(target,table_name = "staff"): 
    target.execute("SELECT * FROM " + table_name) 
    print("Table " + table_name + ":") 
    result = target.fetchall() 
    for r in result:
        print(r)
    return; 