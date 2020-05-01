import sqlite3 

def connect_db(db_name = "any"): # creates db if not existing 
    connection = sqlite3.connect("'%s'.db" % db_name)  
    cursor = connection.cursor() 
    return cursor; # return value of 'cursor' to line of fnc-call 

def setup_table(target, table_name = "staff", index_field = "staff_id", name = "last_name"): 
    # pass variables with default value 
    # very basic way, prone to SQL-injections 
    target.execute("""DROP TABLE IF EXISTS '%s'""" % table_name) 
    target.execute("""
        CREATE TABLE IF NOT EXISTS '%s' (
        '%s' INTEGER PRIMARY KEY, 
        '%s' VARCHAR(20)
        );""" % (table_name,index_field,name)
        )
    return; # return to line of fnc-call 

def add_entry(target,table_name = "staff", name = "TestUser1"):
    target.execute("""INSERT INTO '%s' (staff_id,last_name)
        VALUES (NULL, '%s');""" % (table_name,name) )
    return; 

def get_table(target,table_name = "staff"): 
    target.execute("SELECT * FROM '%s'" % table_name) 
    print("Table '%s':" % table_name) 
    result = target.fetchall() 
    for r in result:
        print(r)
    return; 