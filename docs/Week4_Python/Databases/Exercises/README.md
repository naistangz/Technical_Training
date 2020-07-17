# Using databases with Python and implementing OOP 


To run program:

```python
from connectingDatabases1 import *
```

Check if connection to the database is successful:

```bash
                =========================================
                | Connection to the database successful!|
                =========================================
```

Menu Options:

```bash

Please enter the number for the operation you want to execute:
====================================================
1.To select a query (e.g. SELECT * FROM Products)
2.Find Average unit price for all products
3.To save product names onto a CSV file
4.To exit
====================================================

```

Type in 3 to exit the program

```bash
                ========================================
                | Thank you! Goodbye! Closing connection|
                ========================================

```

---

## Objectives
- To connect to a database using Python and use the [documentation](https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15) to interact with the Northwind database
- To implement object oriented programming to create a program that executes SQL queries according to user-input, thereby eliminating hard-coded functions.
- Implement the `os module` to fetch OS private environment variables (e.g Database, Server, Username and Password)

## Review
- The code does not fully comply to PEP 8 guidelines and layout is not always clear 
- Requires an additional layer of abstraction to ensure that code is kept clean (e.g Instantiating the Database class in a different file)
- The program successfully avoids any hardcoded values
- Good user interface and delivers straightforward and clear user experience
- Good use of variable names
- I created a function that saves `user_input` and the following SQL command to a csv file. 

## Changes and improvements to work on
- Enhance my knowledge of the `pandas module` to improve the layout of SQL queries using dataframes
- Further develop exception handling and errors to improve user experience
- Keep functions and classes in separate files where possible to avoid confusion
- Create a file that will allow me to select all tables and improve user experience as the program only allows users to select and run a query until it exits the program


