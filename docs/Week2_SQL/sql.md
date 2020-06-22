# Week 2.1 SQL

## What is SQL? ##
**SQL** stands for Structured Query Language. 
>
- It is used for managing data in relational database management system which stores data in the form of tables.
- The relationship between data is also stored in the form of tables. 
- SQL statements are used to retrieve and update data in a database
- SQL operates through simple, declarative statements. This keeps data accurate and secure, and it helps maintain the integrity of databases, regardless of size.

**What is a database?**
- An organised repository of data in order to efficiently retrieve data 
- It is held in a computer

**Examples of databases:**
- eCommerce
- Finances
- Customer Bank Accounts
- Sales information

> We must be able to structure tables to contain the right type of information, so that we can query it

**We have to label *raw data* in order to process our data and information efficiently**

---
## Terminology 
- **Column** - Database tables are composed of individual columns corresponding to the attributes of the object
- **Row** - A row consists of one set of attributes corresponding to one instance that a table describes. Also known as Records or Tuples.
- **Table** - A predefined format of rows and columns that define an entity. Also known as a File.
- **Entity** - Anything you want to model in a table
- **DBMS** - A **D**ata **B**ase **M**anagement **S**ystem allows a computer to perform database functions of storing, retrieving, adding, deleting and modifying data.
---
## List of common SQL Commands ##

### Section 1: Basic Commands ###
**Create databases:**
```sql
CREATE DATABASES database_name;
```
`CREATE TABLE` creates a new table in the database. It allows you to specify the name of the table and the name of each column in the table.


**SELECT:**
```sql
SELECT column_name 
FROM table_name;
```
`SELECT` statements are used to fetch data from a database. Every query will begin with `SELECT`.

**SELECT DISTINCT:**
```sql
SELECT DISTINCT column_name
FROM table_name;
```
`SELECT DISTINCT` specifies that the statement is going to be a query that returns unique values in the specified column(s).

**SUM:**
```sql
SELECT SUM(column_name)
FROM table_name;
```
`SUM()` is a function that takes the name of a column as an argument and returns the sum of all the values in that column.

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

**BETWEEN:**
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value_1 AND value_2;
```

The `BETWEEN` operator is used to filter the result set within a certain range. The values can be numbers, text or dates

**CASE:**
```sql
SELECT column_name,
  CASE
    WHEN condition THEN 'Result_1'
    WHEN condition THEN 'Result_2'
    ELSE 'Result_3'
  END
FROM table_name;
```

`CASE` statements are used to create different outputs (usually in the `SELECT` statement). It is SQL’s way of handling if-then logic.

**COUNT():**
```sql
SELECT COUNT(column_name)
FROM table_name;
```

`COUNT()` is a function that takes the name of a column as an argument and counts the number of rows where the column is not `NULL.`
 
 **CREATE TABLE:**
 ```sql
CREATE TABLE table_name (
  column_1 datatype, 
  column_2 datatype, 
  column_3 datatype
);
 ```

`CREATE TABLE` creates a new table in the database. It allows you to specify the name of the table and the name of each column in the table.
 
 **DELETE:**
 ```sql
DELETE FROM table_name
WHERE some_column = some_value;
```

`DELETE` statements are used to remove rows from a table.

**GROUP BY:**
```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name;
```
`GROUP BY` is a clause in SQL that is only used with aggregate functions. It is used in collaboration with the `SELECT` statement to arrange identical data into groups.

**HAVING:**
```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name
HAVING COUNT(*) > value;
```

`HAVING` was added to SQL because the `WHERE` keyword could not be used with aggregate functions.

**INSERT:**
```SQL
INSERT INTO table_name (column_1, column_2, column_3) 
VALUES (value_1, 'value_2', value_3);
```

`INSERT` statements are used to add a new row to a table.

**IS NULL / IS NOT NULL:**
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IS NULL;
```

`IS NULL` and `IS NOT NULL` are operators used with the `WHERE` clause to test for empty values.

**LIKE:**
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name LIKE pattern;
```

`LIKE` is a special operator used with the WHERE clause to search for a specific pattern in a column.

**LIMIT:**
```sql
SELECT column_name(s)
FROM table_name
LIMIT number;
```

`LIMIT` is a clause that lets you specify the maximum number of rows the result set will have.

**MAX():**
```sql
SELECT MAX(column_name)
FROM table_name;
```

`MAX()` is a function that takes the name of a column as an argument and returns the largest value in that column.

**MIN():**
```sql
SELECT MIN(column_name)
FROM table_name;
```

`MIN()` is a function that takes the name of a column as an argument and returns the smallest value in that column.

**OR:**
```sql
SELECT column_name
FROM table_name
WHERE column_name = value_1
   OR column_name = value_2;
```

`OR` is an operator that filters the result set to only include rows where either condition is true.

**ORDER BY:**
```sql
SELECT column_name
FROM table_name
ORDER BY column_name ASC | DESC;
```

`ORDER BY` is a clause that indicates you want to sort the result set by a particular column either alphabetically or numerically.

### Section 2: Joins ###

**INNER JOIN:**
```sql
SELECT column_name(s)
FROM table_1
JOIN table_2
  ON table_1.column_name = table_2.column_name;
```
An `INNER JOIN` will combine rows from different tables if the *join condition* is true.

![innerjoin](../../images/inner_join.jpg)

