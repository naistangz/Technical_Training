# Exercise 1

##### Library_db
table_books
table_library_patron:

##### Bank_db
table_customer_info:
table_bank_account:

### Which categories of data might you find in each table? 

**Possible answers:** isbn code, date published, title of book, bank accounts, customer id, 

---
**Primary Keys**
- Primary key is a field in a table which uniquely identifies each row/record in a database table.
- Primary keys must contain unique values
- Primary keys cannot have `NULL` values
- Bank account would **not** be an ideal primary key as a good relational database should contain a primary key that should not change  

**Foreign Keys**
- A column that references a column (primary key)
of another table


# Activity Day 2
Column Name | Description | Example | Data Type 
----------------| ------------|------------ |------------
Post Code | 6 to 8 Characters| WV1 8JD | VARCHAR(10)
Phone Number | 11 Digits, no punctuation| 07956283593 | CHAR(11)
Birth Date | dd/mm/yyyy | 31/01/1980 | DATE or DATETIME
Weight in Kg | A number with decimal place | 63.5029 | DECIMAL(6, 4)
Comments |Lorem ipsum dolor sit amet, consectetur adipiscing elit.| Large block of text, more than 255 characters | VARCHAR(8000) or VARCHAR(MAX)

# Activity Day 2.2

Why is this table NOT in 1NF?
Product ID | Colour | Price
----------|----------|----------
1| red, green|10.99
2| yellow|  12.00
3| green | 14.99
4| yellow, blue| 5.99
5| red| 20.00

>Reason: Colour contains multiple values 
>Solution: Break into two tables to avoid repeating values




