## Week 2.4 SQL Date Functions, Aggregate and Joins

## Section 1 Date Functions

The following date functions can be used to manipulate dates in various ways in the `SELECT` clause:

`GET DATE`| `SELECT GETDATE()` to return the current date and time (in the session time zone)
------|---------
`SYSDATETIME`|`SELECT SYSDATETIME()` to return the date and time of the computer (server) being used 
`DATEADD`|`DATEADD(D,5,OrderDate) AS 'DUE Date` to add 5 days from the OrderDate.
`DATEDIFF`| `DATEDIFF(d, OrderDate, ShippedDate) AS 'Ship Time'` to add 5 days 
`YEAR`|`SELECT YEAR(OrderDate) AS 'Order Year'` to extract the year from a date
`MONTH`|`SELECT MONTH(OrderDate) AS 'Order Month'` to extract the month from a date.
`DAY`| `SELECT DAY(OrderDate) AS 'Order Day` to extract the day from a date

**Note:** Use `GET DATE` rather than `SYSDATETIME` as system date time may not be updated e.g. when working in a different time zone



---
## Section 2 Joins

RECAP from [Monday](sql_day1.md): 

**Relational Model**

**Orders** table contains two keys: one for **order** and one for **customer** who placed the order. 

The key that refers to the entity described in that table is the **primary** key (*customer_id*), the other key is called a **foreign key** (*customer_id*).

The `PRIMARY` and `FOREIGN` key are essential to describing relations between the tables, and in performing SQL `JOINS`
![relational_model](../../images/relational.png)

**Join Example:**

To find all orders placed by a particular customer, we can join customers and orders tables together using the relationship established by the `customer_id` key:

```sql
SELECT order_date, order_amount
FROM customers
JOIN customers 
    ON customers.customer_id = orders_customer_id
WHERE customer_id = 3
```

This query joins two tables using `join` keyword and specifies the key to use when joining the tables.

## Basic SQL Join Types

Four basic types: 
1. `INNER`
2. `LEFT`
3. `RIGHT`
4. `FULL`

**INNER JOIN:**
```sql
SELECT column_name(s)
FROM table_1
JOIN table_2
  ON table_1.column_name = table_2.column_name;
```
An `INNER JOIN` will combine rows from different tables if there is a match in **both** tables.

![innerjoin](../../images/inner_join.jpg)

---
**LEFT OUTER JOIN**
```sql
SELECT column1, column2...
FROM table_1
LEFT JOIN table_2 on join_condition
WHERE row_condition
```

Also known as SQL left join. If we want to join two tables: A and B, `LEFT JOIN` returns all rows in left table **(A)** and all matching rows found in the right table **(B)**. 

![left_outer_join](../../images/left_outer_join.jpeg)

---
**RIGHT OUTER JOIN**
```sql
SELECT product_name, order_id
FROM sales.order_items o
    RIGHT JOIN production.products p
            ON o.product_id = p.product_id
ORDER BY 
    order_id;
```

**Output:**

![output](../../images/right_join_output.png)

Returns all rows from `RIGHT` table, even if there are **no** matches in the left table. 

Query returned **all** rows from `production.products` (right table) and rows from `sales.order_items` (left table).
If product does not have any sales `order_id` column will have a `NULL`.

`RIGHT JOIN` clause starts selecting data from right table and matching with rows from the left.
`RIGHT JOIN` returns a result set that includes all rows in the right table, whether or not they have matching rows from the left table.
Column from left table in the result set will have `NULL`.


![right_outer_join](../../images/right_join.png)

---
**FULL JOIN:**
```sql
SELECT ID, Name, Age, City
FROM customers
FULL JOIN orders
FROM customers.ID = orders.customers_id;
```

If we consider the following two tables:

**Table 1** 

ID|Name|Age|City
-----|-----|-----|-----
1|Priscilla|21|London
2|Jane|22|Paris
3|Bob|23|Tel-Aviv
4|Muffy|26| Buenos Aires
5|Felicia|29|Lisbon

**Table 2**

OID|Date|Customer_ID|Amount
-----|-----|-----|-----
102|2009-10-08|3|3049
100|2009-07-08|5|3000
101|2008-11-20|3|1500
103|2004-05-20|4|2000

We can use `FULL JOIN` to combine the two tables on `ID` in table1 and `customer_ID` in table2.

Which would produce the following outcome:

ID|Name|Amount|Date
---|---|---|-----
1|Priscilla|NULL|NULL
2|Jane|NULL|NULL
3|Bob |3049|2009-10-08
3|Bob |1500|2008-11-20
4|Muffy|2000|2004-05-205
5|Felicia|3000|2009-07-08

---

**SELF JOIN**

- A join in which a table is joined with itself (also called Unary relationship)
- To join a table itself means that each row of the table is combined with itself and with every other row of the table. 

**For example:**

Name|ID|ManagerID |Manager
-----|------|-----|------
Robert|456| - | -
Cook|383|222|William
Daniel|777|222|William
Smith|123|456|Robert
William|222|456|Robert

In this example, the condition is ID = ManagerID

**Example 2:**
```sql
SELECT o.customerID, o.employeeID, b.ShipCity, b.CustomerID
FROM orders o, orders b
WHERE o.customerID = b.CustomerID;
```


---
**CROSS JOIN**

- A `CROSS JOIN` also known as `cartesian` is used to generate a paired combination of each row of the first table with each row of the first table with each row of the second table.
- The output table is the product of the number of rows in the input tables.

> i.e Table1 contains 15 rows, Table2 contains 20 rows, a cross join would produce the product of table1 and table2 = 300 rows

![cross_join](../../images/cross_join.png)

In the above example, there are two tables, each with three rows. A Cross join would produce the product of the two tables = 3 * 3 = 9 rows

```sql
SELECT
COUNT(o.CustomerID)
FROM orders o
 
SELECT
COUNT(o.CustomerID)
FROM Customers o;

SELECT 91*830
 
SELECT *
FROM Orders o 
CROSS JOIN customers c;
```

---
## Section 3 Having vs Where

- `WHERE` clause introduces a condition on *individual* rows

- `HAVING` clause introduces a condition on *aggregations*, i.e. results of selection where a single result, such as `COUNT`, `AVG`, `MIN`,`MAX` or `SUM`
has been produced from *multiple* rows. 
    > When using aggregations, the `WHERE` clause will not work. E.g. `SUM()` applies ONLY to rows that satisfy the `WHERE` conditions. If you put `SUM()` in the `WHERE` clause, the query will keep looping back and forth whenever conditions are not met.

- The `HAVING` clause filters the data on the group row but not the individual row.

**Note:** Use `WHERE` before `GROUP BY` and `HAVING` after `GROUP BY`

- Column Aliases cannot be used in `HAVING` clause

**For example**
```sql
USE NORTHWIND 
SELECT COUNT(c.customerID) AS 'Number in Country', c.country
FROM customers c 
WHERE COUNTRY != 'USA' /* or <> */
GROUP BY c.Country
HAVING COUNT(c.customerID) > 9;
```

**Compare with the following which will return an error:**

```sql
SELECT COUNT(c.customerID), c.country
FROM Customers c 
GROUP BY c.Country
WHERE COUNT(c.customerID) > 10;
```

---
**Exercise:**

- List order from the orders table and JOIN to the Customers and Employees tables to include 
Customer Name (Company Name) and Employee Name (First and Last Name)

- From the orders table, include OrderID, OrderDate and Freight

```sql
SELECT * FROM orders;
SELECT * FROM customers;
SELECT * FROM Employees;

SELECT 
CONCAT(FirstName, ' ', LastName) AS 'Employee Name', 
c.CompanyName as 'Customer Name', 
o.orderID,
o.OrderDate,
o.Freight
FROM customers c
INNER JOIN Orders o
ON o.CustomerID = c.CustomerID
INNER JOIN employees e
ON o.employeeID = e.employeeID
ORDER BY OrderID;
```



> Week 2 Day 4 (25-06-2020) SQL exercise: *Date Functions, Case Statement, Aggregate Functions, Joins* [HERE](day4_exercise.sql)
