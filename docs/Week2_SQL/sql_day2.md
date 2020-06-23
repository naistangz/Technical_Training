# Week 2.2 SQL

## DML DDL DCL TCL

* Data Manipulation Language
* Data Definition Language
* Data Control Language 
* Transaction Control Language

* **DML** 
    - `SELECT`
    - `INSERT`
    - `UPDATE`
    - `DELETE`
> * Used to manipulate data 
    
* **DDL**
    - `CREATE`
    - `ALTER`
    - `DROP`
    - `TRUNCATE`
> * Used to define data structures

* **DCL**
    - `GRANT` 
    - `REVOKE`
> * These privileges are given by the database administrator who will grant users access to the database.
> * Deals with highly private information such as client data


* **TCL**
    - `COMMIT`
    - `ROLLBACK`
    - `SAVEPOINT`
> * Used to manage transactions in the database
> * Used to manage changes made by DML statements 


## Data Types (Part 1)
* **VARCHAR**
    - Adaptable to different lengths of characters. Records MAX size.
    - More memory efficient than `CHAR`

* **CHARACTER or CHAR**
    - Data must be at a **fixed length.** Fixed amount of space used.
    - 50% faster than VARCHAR

* **INT**
    - Holds a whole number/integer value (see also bigint, smallint and tinyint) positive or negative.
    - INT = 32-bit size (4 bytes) 
    - INT = 64-bit size (4 bytes)
    
* **DATE or TIME or DATETIME**
    - Stores Date, Time or both date and time
    
    
## Data Types (Part 2)
* **DECIMAL or NUMERIC**
    - Fixed-point number. Max number for size is 65
    - DECIMAL(p,s) 
        - **p** total number of digits in the value, i.e. on both sides of the decimal point
        - **s** stands for scale, number of digits after the decimal point
    - DECIMAL(6,4) = 12.4567
        - Total 6 numbers
        - 2 digits after decimal point

* **BINARY**
    - Use to store binary data such as an image or file

* **FLOAT**
    - Scientific use (very large numbers)

* **BIT**
    - Equivalent to binary (0,1 or `NULL`)
    
## Comments
```sql
/* This is a comment in sql*/
```

