import sqlite3 

def connect_db(db_name = "any"): # creates db if not existing 
    connection = sqlite3.connect("{}.db".format(db_name))  
    cursor = connection.cursor() 
    return cursor; # return value of 'cursor' to line of fnc-call 

def setup_table(target, table_name = "staff", index_field = "staff_id", name = "last_name"): 
    # pass variables with default value 
    # very basic way, prone to SQL-injections 
    target.execute("""DROP TABLE IF EXISTS {}""".format(table_name) ) 
    target.execute("""
        CREATE TABLE IF NOT EXISTS {} (
        {} INTEGER PRIMARY KEY, 
        {} VARCHAR(20)
        );""" .format(table_name,index_field,name)
        )
    return; # return to line of fnc-call 

def add_column(target,table_name = "staff", column_name = "dateof_entry", data_type = "VARCHAR(20)"): 
#    target.execute("""ALTER TABLE {} ADD {} {};""".format(table_name,column_name,data_type) ) 
    return; 

def add_entry(target,table_name = "staff", name = "TestUser1"):
    target.execute("""INSERT INTO {} (staff_id,last_name)
        VALUES (NULL, '{}');"""
        .format(table_name,name) )
    return; 

def get_table(target,table_name = "staff"): 
    target.execute("SELECT * FROM {}"
        .format(table_name) ) 
    print("Table {}:"
        .format(table_name) ) 
    result = target.fetchall() 
    for r in result:
        print(r)
    return; 