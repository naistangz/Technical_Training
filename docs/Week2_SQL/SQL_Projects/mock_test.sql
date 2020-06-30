/*1. Create a report showing the title of courtesy and the first and last name
of all employees whose title of courtesy is not "Ms." or "Mrs.".*/

SELECT * FROM Employees;

SELECT 
CONCAT(e.FirstName,' ', e.LastName)  AS "Employee Name",
e.TitleOfCourtesy AS "Title of Courtesy"
FROM Employees e
WHERE e.TitleOfCourtesy NOT IN ('Ms.', 'Mrs.');
 
/*2. Create a report that shows the company name, contact title, city and country of all customers 
in Mexico or in any city in Spain except Madrid(in Spain).*/
SELECT * FROM customers;

SELECT c.CompanyName, c.ContactTitle, c.City, c.country
FROM Customers c
WHERE c.Country = 'Mexico'
OR (c.Country = 'Spain' AND c.City != 'Madrid');

 
/*3. Create a report showing the title of courtesy and the first and
last name of all employees whose title of courtesy begins with "M" and
is followed by any character and a period (.).*/
SELECT * FROM Employees;

SELECT 
e.TitleOfCourtesy AS "Title of Courtesy",
CONCAT(e.FirstName, ' ', e.LastName) AS "Employee Name"
FROM Employees e
WHERE e.TitleOfCourtesy LIKE 'm%.';
 
/*4. Create a report showing the first and last names of
all employees whose region is defined.*/
SELECT 
e.region,
CONCAT(e.FirstName, ' ', e.LastName) AS 'Employee Name'
FROM Employees e
WHERE e.Region IS NOT NULL;

 
/*5. Select the Title, FirstName and LastName columns from the Employees table.
  Sort first by Title in ascending order and then by LastName 
   in descending order.*/
SELECT * FROM Employees;

SELECT 
e.LastName,
e.title,
CONCAT(e.FirstName, ' ', e.LastName) AS 'Employee Name'
FROM Employees e
ORDER BY e.Title, e.LastName DESC;

 
/*6. Write a query to get the number of employees with the same job title.*/
 SELECT * FROM Employees;

 SELECT e.Title,
 COUNT(e.EmployeeID) AS 'Number of Employees with Same job title'
 FROM Employees e
 GROUP BY e.title;


/*7.
Create a report showing the Order ID, the name of the company that placed the order,
and the first and last name of the associated employee.
Only show orders placed after January 1, 1998 that shipped after they were required.
Sort by Company Name.
*/

SELECT * FROM Orders;
SELECT * FROM Customers;
SELECT * FROM Employees;

SELECT o.OrderID, c.CompanyName,
CONCAT(e.FirstName, ' ', e.LastName) AS 'Employee Name'
FROM Customers c
JOIN Orders o
ON c.CustomerID = o.CustomerID 
JOIN Employees e
ON  e.EmployeeID = o.EmployeeID
WHERE o.OrderDate > 1998-01-01 AND (o.ShippedDate > o.RequiredDate) 
ORDER BY c.CompanyName;
 
/*8.
Create a report that shows the total quantity of per products (from the OrderDetails table) ordered. Only show records for products for which the quantity ordered is fewer than 200. 
The report should return*/
SELECT * FROM [Order Details];
SELECT * FROM Products;

SELECT 
p.productName AS 'Product', 
SUM(od.Quantity) AS 'Total quantity for each product'
FROM [Order Details] od
INNER JOIN Products p
ON od.ProductID = p.productID
GROUP BY p.ProductName
HAVING SUM(od.Quantity) < 200;

 
/*9.Create a report that shows the total number of orders by Customer since December 31, 1996. The report should only return rows for which the NumOrders is greater than 15. 
*/

SELECT * FROM Orders;
-- ORDER BY CustomerID;
-- SELECT COUNT(orderID) FROM orders
-- SELECT * FROM Customers; -- relationship via customer ID 


-- -- count orders placed after 30 Dec 1996
-- -- only return of number of orders > 15
-- -- grouped by customer

-- -- FINAL ANSWER 

SELECT 
c.CustomerID,
COUNT(o.OrderID) AS "No. of Orders"
FROM Orders o 
JOIN Customers c 
  ON o.CustomerID = c.CustomerID
WHERE o.OrderDate >= '1996-12-31' 
GROUP BY c.CustomerID
HAVING COUNT(o.OrderID) > 15;

-- Correct Answer
SELECT c.CustomerID, COUNT(o.OrderID) AS "NumOrders"
FROM Customers c JOIN Orders o ON
	(c.CustomerID = o.CustomerID)
WHERE OrderDate >= '31-Dec-1996'
GROUP BY c.CustomerID
HAVING COUNT(o.OrderID) > 15
ORDER BY NumOrders DESC;


 
/*10.  SQL statement will return all customers, and number of orders they might have placed. 
Include those customers as well who have not placed any orders.*/
SELECT * FROM customers;
SELECT * FROM orders;

SELECT c.customerID,
COUNT(o.orderID) AS 'Number of Orders Placed by Each Customer'
FROM customers c 
FULL JOIN orders o 
ON o.customerID = c.customerID
GROUP BY c.CustomerID;

-- Correct Answer
SELECT c.CustomerID, COUNT(o.OrderID) AS "Number Of Orders Placed by Customer"
FROM Customers c LEFT JOIN Orders o
ON c.CustomerID=o.CustomerID
GROUP BY c.CustomerID;