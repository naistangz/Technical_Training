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

*Tip:* use `DROP` before `CREATE` to remove database that already exists with the same name, allowing you to create database/table.

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
    - Syntax error

**NULL**
- `NULL` is not nothing, does not equate to zero.
- A value can be `NULL`, BUT `NULL` never equals `NULL` because `NULL` is an undefined value.

**UPDATE AND DELETE:**
- `UPDATE` command modifies records in table. Along with `WHERE` clause you can update specific records from the table.
```sql
UPDATE Employee 
SET Full_Name = 'Jane Cross', Date_Of_Birth = '16/03/1992'
WHERE Employee_Id = 2;
```

- `DELETE` command deletes records from the database when they are no longer used.
```sql
DELETE FROM table_name
WHERE [condition]
[/code]
```

**Database Considerations:**
    - Data Security
    - Data Recovery 
    - Data Integrity
    - Normal Form 

## Normal Form 
-Normalisation is the process of organising/designing data in a database so that it avoids redundancies of data (all data stored only in one place)

### 1st Normal Form 
- A database is in First Normal Form when the following conditions are satisfied:
    1. Make everything **Atomic**
        - Data must be presented as small as it can be
        - A value that cannot be divided
   
    2. There should be no repeating groups
        - For example, a table that records data on a book and its author(s) with the following columns:
        [BookID],  [Author1], [Author2], [Author3], is not in 1NF because [Author 1], [Author 2], and [Author 3] are all repeating the same attribute.
         
    **For example:** This **table** is not in **1NF** because the values in **colour** are not **atomic**. the values in the [Colour] column can be divided into 'red' and 'green'.
    
    **Product ID** | **Colour** |**Price**|
    ------|------  |------ 
    1|red, green,|10.99
    2|yellow|12.00
    3|green|14.99
    4|yellow,blue|5.99
    5|red|20.00
    
    **Solution:** 
    
    The table needs to be separated into two separate tables. **Product_ID** will be **5.99**, but can come in both the colours **yellow** and **blue**.
    
    `_table_product_price` **table1**
    
    **product_id**|**price**
    -----|-----
    1|10.99
    2|12.00
    3|14.99
    4|5.99
    5|20.00
    
    **_table_product_colour** **table2**
    
    **product_id**|*colour**
    -----|-----
    1|red
    1|green
    2|yellow
    3|green
    4|yellow
    4|blue
    5|red
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                     
---                                                                                                                                                                                                                                                                                                                                 
### 2nd Normal Form 
- A database in in Second Normal Form when the following conditions are satisfied:
    - It is in 1NF
    - All non-key attributes are fully functional dependent on the Primary Key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        - One-to-one relationship    

**Example 1:**
Suppose a school wants to store the data of teachers and the subjects they teach. Since a teacher can teach more than one subjects, the table can have multiple rows for a same teacher. (One-to-many relationship)

teacher_id|subject|teacher_age
-----|-----|-----
111|maths|38
111|physics|38
222|biology|38
333|physics|40
333|chemistry|40

**Candidate Keys:**{teacher_id, subject}
**Non prime attribute:** teacher_age

* Table is in 1 NF because each attribute has atomic values 
* It is not in 2NF because non prime attribute teacher_age is dependent on teacher_id alone.
* This violates the rule for 2NF *"no non-prime attribute is dependent on the proper subset of any candidate key of the table"*

**Solution:**

`teacher_details_table`

teacher_id|teacher_age
----|----
111|38
222|38
333|40

`teacher_subject_table`

teacher_id|subject
----|----
111|Maths
222|Physics
333|Biology 
333|Physics
333|Chemistry 

**Example 2:** 

**Composite key** is used. **Product_ID** and **store** combine to make a primary key.
In this case **location** only depend on **store** which is part of the primary key.

`_table_purchase_detail`

**product_id**|**store**|**location**
----|----|----
1|1|London
1|3|Tokyo
2|1|London
3|2|New York
4|3|Tokyo

**Solution:**

We need to split the table, **Location** column should only rely on the **primary key**, in this case **store**.

`_table_purchase` **table1**

**product_id**|**store**
----|----
1|1
3|2
4|3  
    
`_table_store` **table2*

**product_id**|**Location**
----|----
1|London
3|New York
4|Tokyo 

---
 
### 3rd Normal Form   
- A database is in Third Normal Form when the following conditions are satisfied:
     - It is in 2NF
     - There no transitive functional dependency
        - i.e. When a non-key column is functionally dependent on another non-key column, which is functionally dependent on the **primary key**

**For example:** **Genre_ID** dependent on  **Book_ID**. **Genre Type** dependent on **Genre_ID** . They are **functionally dependent** on each other

`book_table_detail`

**Book_id** |**Genre_id** |**Genre_type**|**Price**
---|---|---|---
1|1| Fiction| 9.99
2|2|Travel|14.99
3|1|Fiction|24.99

**Solution:**

We need to create separate tables to remove any function dependencies. **Book_id** is the primary key as it does not rely on any other table i.e. **genre_id**. We create another table to track **genre_id** as it is functionally dependent on **GenreType**

`table_book` **table1**

**Book_id**|**Genre_id**|**Price**
----|----|----
1|1|9.99
2|2|14.99
3|1|24.99

`table_genre`

**Genre_id**| **genre_type**
---|---
1|Fiction
2|Travel

**What are non-key attributes?**
    - Attributes or fields of fields, other than candidate *key attributes* 

**What are key attributes?**
    - Uniquely identify a record or an instance on an entity
    - Required to retrieve a particular record from the entity table. 


Week 2 Day 2 (23-06-2020) SQL Exercise [HERE](day2_exercise.sql)
                                                                                             