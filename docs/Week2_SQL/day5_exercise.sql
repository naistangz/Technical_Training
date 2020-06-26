/*Recap of Date Functions*/
-- Prior to SQL server 2012 convert was used to format dates
-- In 2012 FORMAT() was introduced to make it easer 
-- We are using 2017

SELECT OrderId, CONVERT(VARCHAR(10), OrderDate, 103) AS [dd/MM/yyy]
FROM Orders; /*Before 2012*/

SELECT OrderID, FORMAT(OrderDate,'dd/MM/yyyy') AS [dd/MM/yyyy]
FROM Orders; /*After 2012*/

/*Subqueries*/
-- This is an example of a subquery in the WHERE clause 
-- Check to see which Customers have not placed any orders
-- This could also be achieved using JOINs

SELECT CompanyName AS "Customer"
FROM Customers
WHERE CustomerID NOT IN
    (SELECT CustomerID FROM Orders);

-- This is the same as the following:
-- FULL JOIN subquery
SELECT c.CompanyName AS "Customer"
FROM customers c 
FULL JOIN Orders o ON o.customerID = c.CustomerID
WHERE o.CustomerID IS NULL;

-- LEFT JOIN subquery
SELECT c.CompanyName AS "Customer"
FROM customers c 
LEFT JOIN Orders o ON o.customerID = c.CustomerID
WHERE o.CustomerID IS NULL;

-- RIGHT JOIN subquery
SELECT c.CompanyName AS "Customer"
FROM customers c 
RIGHT JOIN Orders o ON o.customerID = c.CustomerID
WHERE o.CustomerID IS NULL;

-- Example of nested subquery in the SELECT clause (acts like a column)
-- Subqueries MUST be contained by parenthesis (excluding any alias)
-- Outputs the highest price in the table on every row in the result set

SELECT OrderID, ProductID, Quantity, Discount,
    (SELECT MAX(od.UnitPrice) FROM [Order Details]od) AS 'Max Price'
FROM [Order Details]; 
-- Aggregate function must in brackets to avoid conflict 

SELECT OrderID, ProductID, Quantity, Discount
FROM [Order Details];

SELECT MAX(UnitPrice) FROM [Order Details];

-- This is an example of an inline view (SELECT in the FROM clause: acts like a table)
-- The inline view sq1 calculates the total for each product which is used to calculate percent of total
-- This an advanced query

SELECT * FROM [Order Details];

SELECT od.ProductID, sq1.totalamt AS "Total Sold for this Product",
od.UnitPrice, 
ROUND(((od.UnitPrice*od.Quantity)/sq1.totalamt)*100,2) AS "% of Total"
    FROM [Order Details] od
    INNER JOIN
        (SELECT ProductID, SUM(o.UnitPrice*o.Quantity) AS "totalamt"
        FROM [Order Details] o
        GROUP BY o.ProductID) sq1 ON sq1.ProductID = od.ProductID;


-- Using subquery in the WHERE clause, list all orders (OrdersID, productID, Unit price, 
-- quantity and discount) from the order details table 
-- where the product has been discontinued
-- Then repeat same exercise using simple join   

SELECT * FROM [Order Details];

SELECT * FROM Products;

SELECT ProductName, Discontinued
FROM Products
WHERE discontinued != 0;

-- WITH JOIN
SELECT 
od.OrderID, 
od.productID, 
od.UnitPrice, 
od.Quantity, 
od.Discount, 
p.Discontinued
FROM [Order Details] od
INNER JOIN Products p
ON p.ProductID = od.ProductID
WHERE p.Discontinued != 0;

-- With subquery
SELECT od.OrderID, od.ProductID, od.UnitPrice, od.Quantity, od.Discount
FROM [Order Details] od
WHERE od.ProductID IN
    (SELECT p.ProductID FROM Products p WHERE Discontinued != 0);

-- Employee ID is the Same as Supplier ID 
-- Combined all rows, removed duplicates
-- The UNION command combines the result set of two or more SELECT statements (only distinct values)
-- Both select statements must have the same number of columns in SELECT clause (same type)
-- Only the column ALIAS in the first SELECT will be applied

--  returns all rows
SELECT EmployeeID AS "Employee/Supplier"
FROM Employees
UNION ALL 
SELECT SupplierID
FROM Suppliers;

-- removes any duplicates
SELECT EmployeeID AS "Employee/Supplier"
FROM Employees
UNION
SELECT SupplierID
FROM Suppliers;

SELECT * FROM Suppliers;

SELECT * FROM Employees;


