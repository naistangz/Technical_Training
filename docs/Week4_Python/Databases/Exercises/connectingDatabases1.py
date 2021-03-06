import pyodbc
import csv
import os

class Databases:

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    # establish connection
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

    # Execute SQL query
    def execute_query(self, connection):
        # sql_command = "SELECT * FROM Products"
            sql_command = input("Please select a command: ")
            cursor = connection.cursor()
            rows = cursor.execute(sql_command)
            for row in rows:
                print(row)


    # Average unit price for products from product table
    def avg_unitprice(self, connection):
        sql_command = "SELECT FORMAT(AVG(UnitPrice), 'C') FROM Products"
        cursor = connection.cursor()
        rows = cursor.execute(sql_command)
        Average_unit_price = []
        for row in rows:
            Average_unit_price.append(row)
        return f"Average Unit Price:{Average_unit_price}"

    # convert data to csv file
    def dump_to_csv(self, connection):
        sql_command = "SELECT ProductName FROM Products"
        cursor = connection.cursor()
        rows = cursor.execute(sql_command)
        Product_Name = []
        for row in rows:
            Product_Name.append(row)
        with open("testing.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([Product_Name])
        print("""
                ===============================
                | a CSV file has been created |
                ===============================
                """)

    # Function for enhanced user experience
    def user_interface(self):
        object = Databases(server, database, username, password)

        user_exit = False

        while not user_exit:
            def menu():
                options = "\nPlease enter the number for the operation you want to execute:\n1.To select a query (e.g SELECT * FROM Products)\n2.To find average unit price for all products\n3.To save products on CSV file\n4.To exit\n"
                print(options)
            menu()
            try:
                user_input = int(input("Your selection: \n"))
            except ValueError:
                print("Invalid selection. Please select number 1, 2, 3 or 4")
            if user_input == 1:
                print(object.execute_query(connection))
            elif user_input == 2:
                print(object.avg_unitprice(connection))
            elif user_input == 3:
                print(object.dump_to_csv(connection))
            elif user_input == 4:
                print("""
                ========================================
                | Thank you! Goodbye! Closing connection|
                ========================================
                """)
                user_exit = True
            else:
                print("Invalid selection please select the correct number")


# Hardcoded variables
server = os.environ.get('db_server')
database = os.environ.get('db_database')
username = os.environ.get('db_username')
password = os.environ.get('db_password')
cnxn = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
connection = pyodbc.connect(cnxn, timeout=5)

# Instantiated class
d = Databases(server, database, username, password)
d.create_connection()
d.user_interface()