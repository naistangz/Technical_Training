## Exercise 1

##### Library_db
table_books
table_library_patron:

##### Bank_db
table_customer_info:
table_bank_account:

Which categories of data might you find in each table? 
---
**Primary Keys**
- Primary key is a field in a table which uniquely identifies each row/record in a database table.
- Primary keys must contain unique values
- Primary keys cannot have `NULL` values
- Bank account would **not** be an ideal primary key as a good relational database should contain a primary key that should not change  

**Foreign Keys**
- A column that references a column (primary key)
of another table