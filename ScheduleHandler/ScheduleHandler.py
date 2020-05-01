print("By now we can manipulate the names.") # 

import sqlite3 

from dbHandler import ConnectDB, SetUpTable, GetTable 

cursor = ConnectDB("any") 
SetUpTable(cursor,"staff","staff_id","last_name") 
GetTable(cursor,"staff")