# Week 2
---
## SQL
---
## What is SQL? ##
**SQL** stands for Structured Query Language. 
>
- It is used for managing data in relational database management system which stores data in the form of tables.
- The relationship between data is also stored in the form of tables. 
- SQL statements are used to retrieve and update data in a database
- SQL operates through simple, declarative statements. This keeps data accurate and secure, and it helps maintain the integrity of databases, regardless of size.
---
## List of common SQL Commands ##

**Create databases:**
```sql
CREATE DATABASES database_name;
```
>CREATE TABLE creates a new table in the database. It allows you to specify the name of the table and the name of each column in the table.

**AND:**
```sql
SELECT column_name(s)
FROM table_name
WHERE column_1 = value_1
  AND column_2 = value_2;
```

`AND` is an operator that combines two conditions. Both conditions must be true for the row to be included in the result set.

**AS:**
```sql
SELECT column_name AS 'Alias'
FROM table_name;
```

`AS` is a keyword in SQL that allows you to rename a column or table using an *alias*.

**AVG:**
```sql
SELECT AVG(column_name)
FROM table_name;
```

`AVG()` is an aggregate function that returns the average value