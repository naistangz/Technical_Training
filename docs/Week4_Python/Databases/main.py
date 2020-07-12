# 1) DB server connection
from database_OOP import *
import os
server = os.environ.get('db_server')
database = os.environ.get('db_database')
username = os.environ.get('db_username')
password = os.environ.get('db_password')

# OOP
user_input = int(input("Select the operation to execute:\n1. Fetch one row\n2. Fetch many rows\n3. Fetch All rows\n"))

d = database_OOP(server, database, username, password)
oop_connection = d.establish_connection()
d.execute_sql('SELECT * FROM Products', oop_connection, user_input)