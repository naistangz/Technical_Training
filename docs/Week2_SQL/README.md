# SQL Training :bar_chart:

**Topics Covered In This Course:**

- [x] [Introduction](sql_day1.md)
- [x] [DDL, DML, DCL, TCL](sql_day2.md)
- [x] [Data Types](sql_day2.md)
- [x] [Normalisation](sql_day2.md)
- [x] [Constraints](sql_day3.md)
- [x] [Date Functions](sql_day4.md)
- [x] [Arithmetic Operators](day4_exercise.sql)
- [x] [Joins](sql_day4.md)
- [x] [Having Vs Where](sql_day4.md)
- [x] [Formatting](sql_day5.md)
- [x] [Subqueries](sql_day5.md)

---

**SQL Projects and Exams**
1. [Northwind Database Data Analysis](/docs/Week2_SQL/SQL_Projects)

# Terminology

##  What is SQL?
Structured Query Language. Used to communicate with a database. Standard language for relational database management systems, meaning SQL can draw relationships between different tables as long as they have a relationship through a primary and foreign key relationship.

## Types of relationships
1. One to One
2. One to Many
3. Many to Many - uses technique called junction table which stores attributes of the relationships between two lists of entities. They use `PRIMARY KEYS` of each data table.

## Primary key
- Uniquely identify a record in the table 

## Composite key
- Combination of two or more columns in a table to uniquely identify each row when taken individually, it does not guarantee uniqueness.

## Foreign key 
- Acts as a cross-reference between tables where the primary key of another table is linked to the primary of key of the current table.
- Establishing a link between the two tables.
- Primary key in another table

## **DELETE vs TRUNCATE vs DROP**:

**`DELETE`** vs **`TRUNCATE`**: `DELETE` used to remove records using `WHERE` clause. `TRUNCATE` removes all records. `TRUNCATE` is not possible when a table is referenced by a foreign key.

**`DELETE`** vs **`DROP`**: `DROP` DDL command removes a table from the database. Removes **all** named elements of the schema like relations, domains or constraints. `DELETE` removes only those tuples which satisfy the `WHERE` clause condition. If `WHERE` clause is missing then by default all tuples present in relation are *removed (same as `TRUNCATE`)*

**`TRUNCATE`** vs **`DROP`**: `DROP` Removes table definition, indexes, data, constraints, triggers. Cannot be rolled back (must be recreated) `TRUNCATE` removes all data but preserves structure of table and remain in the memory for further operations unlike `DROP` table.


## **Null**
- Undefined values 
- `NULL` does not equal to zero 

## Joins
- A method of combining two tables together through a foreign and primary key relationship.

## Normalisation
- Approach of eliminating data redundancy 
- Approach of organising data and dividing larger tables into smaller tables and linking them through relationships
- Ensures that data is stored logically.

## Key 
- A value used to identify a record in a table uniquely

## Primary key 
- Used to identify a database record uniquely
- A primary key cannot be `NULL`
- A primary key value must be unique

## Composite key
- A Primary key composed of multiple columns to identify a record
