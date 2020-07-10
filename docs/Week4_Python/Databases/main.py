# 1) DB server connection
from database_OOP import *

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# OOP
user_input = int(input("Select the operation to execute:\n1. Fetch one row\n2. Fetch many rows\n3. Fetch All rows\n"))

d = database_OOP(server, database, username, password)
oop_connection = d.establish_connection()
d.execute_sql('SELECT * FROM Products', oop_connection, user_input)