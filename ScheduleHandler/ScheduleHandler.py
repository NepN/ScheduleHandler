print("By now we can manipulate the names.") # 

import sqlite3 

from dbHandler import connect_db, setup_table, add_entry, get_table 

cursor = connect_db("any") 
setup_table(cursor,"staff","staff_id","last_name") 
add_entry(cursor,"staff","William")
add_entry(cursor,"staff")
add_entry(cursor,"staff","Jana")
get_table(cursor,"staff")