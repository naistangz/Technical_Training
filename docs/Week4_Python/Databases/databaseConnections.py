import pyodbc
import os



server = os.environ.get('db_server')
database = os.environ.get('db_database')
username = os.environ.get('db_username')
password = os.environ.get('db_password')

connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' + database +';UID='+ username +';PWD='+ password)

cursor = connections.cursor()

# print(connections)
# print(cursor)

# Testing query
# cursor.execute('SELECT * FROM Customers')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

query_result = cursor.execute('SELECT * FROM Products')

print("Printing query_result object:",query_result)

# Printing row count from products
count = cursor.execute('SELECT * FROM Products').rowcount
print("Count", count)

# fetchone() ---> output next 1 pyodbc. Row -- remember cursor maintains state
# If you want to get back to the start, you need a new cursor or to run the execute command again
# fetchone row -fetchone, if fetch many rows if fetchmany(), if fetch all rows that is fetchall()

# rows = query_result.fetchone()
print("-----------FETCH MANY-----------")
rows = query_result.fetchmany(30)
for row in rows:
    print(row.ProductName)

# print("-----------FETCH ALL-----------")
# rows = query_result.fetchall() # fetching everything
# for row in rows:
#     print("ProductName:" + row.ProductName)
# # fetch maintains its state
# print(type(rows)) # pyodgc row object
# print(rows[1]) # second column of rows
# print(rows.ProductName)

