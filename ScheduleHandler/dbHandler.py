import sqlite3 

def ConnectDB(): # creates db if not existing 
    connection = sqlite3.connect("any.db") 
    cursor = connection.cursor() 
    return cursor; # return value of 'cursor' to line of fnc-call 

def SetUpTable(cursor): # create necessary tables 
    cursor.execute("""
        CREATE TABLE employee (
        staff_number INTEGER PRINMARY KEY, 
        fname VARCHAR(20)
        );"""
        )
    cursor.execute("""DROP TABLE employee;""") # clean up after use 
    return; # return to line of fnc-call 