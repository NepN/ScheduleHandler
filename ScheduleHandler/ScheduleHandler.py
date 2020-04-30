print("And now outsourcing them to their own file.") # 

import sqlite3 

from dbHandler import ConnectDB, SetUpTable

cursor = ConnectDB() 
SetUpTable(cursor) 
