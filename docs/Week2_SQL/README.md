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

## **DELETE vs TRUNCATE vs DROP**:

**`DELETE`** vs **`TRUNCATE`**: `DELETE` used to remove records using `WHERE` clause. `TRUNCATE` removes all records. `TRUNCATE` is not possible when a table is referenced by a foreign key.

**`DELETE`** vs **`DROP`**: `DROP` DDL command removes a table from the database. Removes **all** named elements of the schema like relations, domains or constraints. `DELETE` removes only those tuples which satisfy the `WHERE` clause condition. If `WHERE` clause is missing then by default all tuples present in relation are *removed (same as `TRUNCATE`)*

**`TRUNCATE`** vs **`DROP`**: `DROP` Removes table definition, indexes, data, constraints, triggers. Cannot be rolled back (must be recreated) `TRUNCATE` removes all data but preserves structure of table and remain in the memory for further operations unlike `DROP` table.


## **Null**
- Undefined values 
- `NULL` does not equal to zero 