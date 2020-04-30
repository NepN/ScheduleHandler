print("Now we are creating a table within a database...") # 

import sqlite3 
connection = sqlite3.connect("any.db") 
cursor = connection.cursor() 

cursor.execute("""
    CREATE TABLE employee (
    staff_number INTEGER PRINMARY KEY, 
    fname VARCHAR(20)
    );"""
    )

cursor.execute("""DROP TABLE employee;""")
