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
    
**Comments**
```sql
/* This is a comment in sql*/
```
### Insert Breakdown 

### Variations of Insert
- **Changing the order of the columns**
    - If you've already created a table, the order in which you add the data doesn't have to be the same as the original column order as long as the values match the order you are inserting.
- **Omitting column names**
    - You don't have to put the column names in, but the values have to be in the same order as the original columns.
- **Leaving some columns out**
    - You can leave some information out, it doesn't have to be inserted with the rest. For this you will have to specify the column names the values are going into. 

**What error do you get with:**
- A missing **VALUE?**
- A missing **column?**
- A missing **single quote mark?**

**NULL**
- `NULL` is not nothing, does not equate to zero.
- A value can be `NULL`, BUT `NULL` never equals `NULL` because `NULL` is an undefined value.

**UPDATE AND DELETE:**

**Database Considerations:**
    - Data Security
    - Data Recovery 
    - Data Integrity
    - Normal Form 

## Normal Form 
- Through normalisation, we achieve better design because we are removing redundancies 

### 1st Normal Form 
- A database is in First Normal Form when the following conditions are satisfied:
    - Make everything **Atomic**
    > Data must be presented as small as it can be.
                                                                                                                     
    - There should be no repeating groups
    > For example, a table that records data on a book and its author(s) with the following columns:
    > [BookID],  [Author1], [Author2], [Author3], is not in 1NF because 
                                                                                                                                                                                                                                                                                                                                         
### 2nd Normal Form 
- A database in in Second Normal Form when the following conditions are satisfied:
    - It is in 1NF
    - All non-key attributes are fully functional dependent on the Primary Key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
       
### 3rd Normal Form   
- A database is in Third Normal Form when the following conditions are satisfied:
     - It is in 2NF
     - There no transitive functional dependency
        - i.e. When a non-key column is functionally dependent on another non-key column, which is functionally dependent on the **primary key**



**What are non-key attributes?**
**What are key attributes?**

                                                                                             