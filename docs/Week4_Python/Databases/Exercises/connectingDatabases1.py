import pyodbc
import os

class Databases:  # create class to initialise the connection

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def create_connection(self):

        # cnxn = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        try:
            with pyodbc.connect(cnxn, timeout=5) as connection:
                print("""
                =========================================
                | Connection to the database successful!|
                =========================================
                """)
        except ConnectionError:
            print("""
                ==========================
                | Connection has time out |
                ==========================
                """)
            return
        except pyodbc.DatabaseError:
            print("""
                =====================================
                | Connection to the database failed |
                =====================================
                """)
            return
        else:
            cursor = connection.cursor()
            return cursor

    def execute_query(self, connection):
        sql_command = "SELECT * FROM Products"
        cursor = connection.cursor()
        rows = cursor.execute(sql_command)
        for row in rows:
            print(row)


    def avg_unitprice(self, connection):
        sql_command = "SELECT FORMAT(AVG(UnitPrice), 'C') FROM Products"
        cursor = connection.cursor()
        rows = cursor.execute(sql_command)
        Average_unit_price = []
        for row in rows:
            Average_unit_price.append(row)
        return f"Average Unit Price:{Average_unit_price}"

    def user_interface(self):
        object = Databases(server, database, username, password)

        user_exit = False

        while not user_exit:
            def menu():
                options = "\nPlease enter the number for the operation you want to execute:\n1.SELECT * FROM products\n2.Find Average unit price for all products\n3.To exit\n"
                print(options)
            menu()
            try:
                user_input = int(input("Your selection:\n"))
            except ValueError:
                print("Invalid selection. Please select number 1, 2, or 3")
            if user_input == 1:
                print(object.execute_query(connection))
            elif user_input == 2:
                print(object.avg_unitprice(connection))
            elif user_input == 3:
                print("""
                ========================================
                | Thank you! Goodbye! Closing connection|
                ========================================
                """)
                user_exit = True
            else:
                print("Invalid selection please select the correct number")




server = os.environ.get('db_server')
database = os.environ.get('db_database')
username = os.environ.get('db_username')
password = os.environ.get('db_password')

cnxn = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
connection = pyodbc.connect(cnxn, timeout=5)
d = Databases(server, database, username, password)
d.create_connection()
d.user_interface()

