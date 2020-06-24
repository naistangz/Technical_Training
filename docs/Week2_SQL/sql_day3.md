# Week 2.3 SQL

## Constraints

Constraints are used to make sure that the integrity of data is maintained in the database. Following are most used constraints that can be applied to a table.

- `NOT NULL` 
    - Restricts a column from having a `NULL` value.
    - Once `NOT NULL` constraint is applied to a column, you cannot pass a `NULL` value to that column. It enforces a column to contain a **proper value.**
    - This constraint cannot be defined at table level.

**For example:**
```sql
CREATE TABLE Student(s_id int NOT NULL, Name varchar(60), Age int);
```

The above query will declare that the s_id field of **Student table** will not take `NULL` value.

---
- `UNIQUE`
    - Ensures field or column will only have unique values. A `UNIQUE` constraint field will not have duplicate data.
    - Can be applied at column level or table level.

**For example:**
```sql
ALTER TABLE Student ADD UNIQUE(s_id);
```

The above query specifies that **s_field** of **Student** table will only have unique value.

---
- `PRIMARY KEY`
    - Uniquely identifies each record in a database. A Primary Key must contain unique value and it must not contain `NULL` value. Usually Primary Key is used to index the data inside the table.
    
**For example:**

```sql
ALTER table Student ADD PRIMARY KEY (s_id);
```

This will create a `PRIMARY KEY` on the `s_id`

 ---
 
- `FOREIGN KEY`
    - Used to relate two tables. `FOREIGN KEY` constraint is also used to restrict actions that would destroy links between tables.

**For example:**

**Customer_Detail_Table**

**c_id** | **Customer_Name** | **address** 
----|----|----
101| Adam| Noida
102| Alex| Delhi
103| Stuart|Rohtak

**Order_Detail_Table**

**order_id**|**order_name**|**c_id**
-----|-----|-----
10|order1|101
11|order2|103
12|order3|102

**customer_detail_table**, **c_id** is the primary key which is set as foreign key in **order_detail_table** table.

Value for **c_id** is set as foreign key in **order_detail_table** **MUST** be present in **customer_detail** table where it is set as primary key.

This prevents *invalid* data to be inserted into **c_id** column of **order_detail_table**

```sql
ALTER TABLE order_detail ADD FOREIGN KEY (c_id) REFERENCES Customer_Detail(c_id);
```

---

- `CHECK`
    - This is used to restrict the value of a column between a range. 
    - Performs check on the values, before storing them into the database.
    - Like condition checking before saving data in a column.

**For example:**
```sql
ALTER table Student ADD CHECK(s_id > 0);
```

This query restricts **s_id** value to be greater than zero.

---
- `DEFAULT`
    - The following sets a `DEFAULT` value for the 'City' column when the 'Persons' table is created 
```sql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255) DEFAULT 'Sandnes'
);
```
---
    
## Behaviour of Foreign Key Column `ON DELETE`

`ON DELETE` maintains integrity of data in Child table, when a particular record in deleted in main table (table_1).

**For example:** When two tables are connected by `FOREIGN KEY` and certain data in main table is deleted, for which record exits in the child table we need the following:

1. `ON DELETE CASCADE` : This removes record from child table, if value of foreign key is deleted from the main table
2. `ON DELETE NULL`: This sets all values in that record of child table as `NULL`, for which the value of foreign key is deleted from the main table. 

If we don't use the above, we cannot delete data from the main table for which data in child table exists. We get the following:

**Example:**

```sql
ALTER TABLE director
ADD CONSTRAINT film_id
FOREIGN KEY (film_id) 
REFERENCES film_table (film_id) ON DELETE CASCADE
```

This query deletes `film_id` on parent table **and** child table.

```sql
ERROR: Record in child table exist
```
