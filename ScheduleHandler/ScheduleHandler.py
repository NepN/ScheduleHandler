print("By now we can manipulate the names.") # 

import sqlite3 

from dbHandler import connect_db, setup_table, add_column, add_entry, get_table 

cursor = connect_db("any") 
setup_table(cursor,"staff","staff_id","last_name") 

add_entry(cursor,"staff","William")
add_entry(cursor,"staff")

add_column(cursor,"staff","entry_date","TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL")
add_column(cursor,"staff","position",)
add_entry(cursor,"staff","Jana")
cursor.execute("""UPDATE staff 
    SET entry_date = {} 
    WHERE name = {} """
    .format("2017-01-01","Jana") )

get_table(cursor,"staff")