print("By now we can manipulate the names.") # 

import sqlite3 

from dbHandler import ConnectDB, SetUpTable, AddEntry, GetTable 

cursor = ConnectDB("any") 
SetUpTable(cursor,"staff","staff_id","last_name") 
AddEntry(cursor,"staff","William")
AddEntry(cursor,"staff")
GetTable(cursor,"staff")