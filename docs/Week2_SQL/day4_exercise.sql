-- Date Functions 


-- Extracting age With decimal
SELECT CONCAT(FirstName, ' ', LastName) AS 'Employee Name',
BirthDate AS 'Birth Date',
DATEDIFF(d, BirthDate, GetDate())/365.25 AS 'Age'
FROM Employees;

--Extracting year 
SELECT YEAR(e.BirthDate) AS 'Year of my Birth'
FROM Employees e;

--Extracting moth 
SELECT MONTH(e.BirthDate) AS 'Month of my Birth'
FROM Employees e;

--Extracting day
SELECT DAY(e.BirthDate) AS 'Day of my Birth'
FROM Employees e;

--Sysdatetime vs Getdate
SELECT * FROM Employees

SELECT DATEDIFF(yy, e.HireDate, SYSDATETIME())
FROM Employees e;

SELECT DATEDIFF(yy, e.HireDate, GetDATE())
FROM Employees e;

-- DATEADD
SELECT 
OrderDate AS 'Order Date',
ShippedDate AS 'Shipped Date',
DATEADD(d, 5, OrderDate) AS 'Due Date', -- Takes the orderdate and adds 5 days
DATEDIFF(d, OrderDate, ShippedDate) AS 'Ship Days' --Difference between Order Date and Shipped Date
FROM Orders;

SELECT * FROM Orders;

-- Output a list of Employees from the Employees table including their Name (concat) and their Age (calculated from BirthDate)

SELECT * FROM Employees;

--Option 1
SELECT CONCAT(FirstName, ' ', LastName) AS 'Employee Name',
BirthDate AS 'Birth Date',
DATEDIFF(d, BirthDate, GetDate())/365 AS 'Age'
FROM Employees;

--Option 2

SELECT CONCAT(FirstName, ' ', LastName) AS 'Employee Name',
BirthDate AS 'Birth Date',
DATEDIFF(YYYY, BirthDate, GetDate()) AS 'Age'
FROM Employees;

--Option 3

SELECT 
CONCAT(FirstName, ' ', LastName) AS 'Employee Name',
BirthDate AS 'Birth Date',
ROUND(DATEDIFF(Year, BirthDate, GetDate()),5) AS 'Age'
FROM Employees;

--Writing conditional statement using CASE
-- CASE statements can be useful when you need varying results output baesd on differing data.
-- Use single quotes for data and double quotes for column aliases
SELECT OrderDate, ShippedDate,
CASE WHEN DATEDIFF(d, o.OrderDate, o.ShippedDate) < 10 
THEN 'On Time'
ELSE 'Overdue'
END AS 'Status'
FROM orders o;

-- CASE Exercise 1
-- Use CASE to add a column to the previous activity solution called Retirement Status as follows:
--1. Age greater than 65 = "Retired"
--2. Age greater than 60= 'Retirement Due'
--3. Age less than 60
SELECT 
CONCAT(FirstName, ' ', LastName) AS "Employee Name",
DATEDIFF(d, BirthDate, GetDate())/365 AS "Age",
CASE 
WHEN DATEDIFF(YEAR, BirthDate, GETDate()) > 65 THEN 'Retired'
WHEN DATEDIFF(YEAR, BirthDate, GETDate()) > 60 THEN 'Retirement Due'
ELSE 'More than 5 years to go'
END AS "Retirement Status"
FROM Employees;

--Aggregate Functions
SELECT * FROM Products;

SELECT p.UnitsOnOrder
FROM products p;

SELECT 
SUM(p.UnitsOnOrder) AS 'Total On Order',
AVG(p.UnitsOnOrder) AS 'Avg On Order',
MIN(p.UnitsOnOrder) AS 'Min On Order',
MAX(p.UnitsOnOrder) AS 'Max On Order'
FROM Products p;

--Calculate units on order using aggregate functions per supplier
--Group by is added to provide subtotals
--Multiple columns can be added as a comma separated list to provide further levels of subtotals.
SELECT supplierID, 
SUM(unitsonorder) AS 'Total on Order',
AVG(Unitsonorder) AS 'AVG on Order',
MAX(UnitsOnorder) AS 'Max on Order'
FROM Products
GROUP BY SupplierID;

--Use GROUP BY to calc the AVG Reorder Level for all products by CategoryID
--Remember the SELECT clause must match the Group By clause apart from any aggregates
--What is highest AVG reorder level use order by with DESC

SELECT * FROM Products;

SELECT 
categoryId,
AVG(reorderLevel) AS "AVG Reorder Level"
FROM Products
GROUP BY CategoryID --Where will not work in group data when using group by therefore need to use HAVING 
ORDER BY 'AVG Reorder Level' DESC;

--Using HAVING instead of WHERE when filtering on subtotals/group data
--Column Aliases cannot be used in the Having clause
--Aggregate functions are not available for use in the WHERE clause due to SQL processing lang 
--WHERE can come before FROM, Before HAVING


SELECT SupplierID,
SUM(unitsonorder) AS 'Total on Order',
AVG(unitsonorder) AS 'AVG on order'
FROM Products
GROUP BY SupplierID
HAVING AVG(unitsonorder) > 5; --cannot use aliasing so have to write AVG(units on order) again

/*SQL SELECT STATEMENT - PROCESSING SEQUENCE
FROM 
WHERE 
GROUP BY 
HAVING 
SELECT 
DISTINCT 
ORDER BY */

--JOINs--

SELECT * FROM  customers;
--customers and orders have a relation (via customerID)

SELECT * FROM Orders;
--customers and orders have a relation (via customerID)

SELECT * FROM employees;
--orders and employees have a relation (via employeeID)

SELECT * FROM Products;
--products and suppliers have a relation (via supplierID)

SELECT * FROM Suppliers;
--products and suppliers have a relation (via supplierID)


--Examples:
--FULL JOIN
SELECT c.customerID, c.contactName, o.employeeID, o.ShipCity
FROM orders o 
FULL JOIN customers c
ON c.customerID = o.CustomerID
ORDER BY EmployeeID;

--INNER JOIN 
SELECT c.customerID, c.contactName, o.employeeID, o.ShipCity
FROM orders o 
INNER JOIN customers c
ON c.customerID = o.CustomerID
ORDER BY EmployeeID;

--LEFT JOIN
SELECT c.customerID, c.contactName, o.employeeID, o.ShipCity
FROM orders o 
LEFT JOIN customers c
ON c.customerID = o.CustomerID
ORDER BY EmployeeID;

--RIGHT JOIN
SELECT c.customerID, c.contactName, o.employeeID, o.ShipCity
FROM orders o 
RIGHT JOIN customers c
ON c.customerID = o.CustomerID
ORDER BY EmployeeID;
