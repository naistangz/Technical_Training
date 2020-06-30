-- SQL Northwind Database Project 

-- Exercise 1 – Northwind Queries (40 marks: 5 for each question)
-- 1.1	Write a query that lists all Customers in either Paris or London. Include Customer ID, Company Name and all address fields.
SELECT 
    c.CustomerID,
    c.city as "City",
    c.CompanyName AS "Company Name",  
    CONCAT(c.Address, ', ', c.City,', ',c.PostalCode,', ', c.Country) AS "Full Address"
FROM Customers c
WHERE City IN ('Paris', 'London')
ORDER BY City; 



-- 1.2	List all products stored in bottles.
SELECT * FROM Products;

SELECT 
    p.productID,
    p.productName AS "Product Name",
    p.QuantityPerUnit AS "Products Stored in Bottles" 
FROM Products p
WHERE p.QuantityPerUnit LIKE '%bottle%';  


-- 1.3	Repeat question above, but add in the Supplier Name and Country.
SELECT * FROM Products;
SELECT* FROM Suppliers;

SELECT 
    s.CompanyName AS "Supplier Name", 
    s.Country,
    p.ProductName AS "Product Name", 
    p.QuantityPerUnit AS "Products Stored in Bottles"
FROM Products p 
INNER JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE p.QuantityPerUnit LIKE '%bottle%';
 
-- 1.4	Write an SQL Statement that shows how many products there are in each category. Include Category Name in result set and list the highest number first.
SELECT * FROM Products;
SELECT * FROM Categories; 

SELECT 
    c.CategoryName AS "Category Name", 
    COUNT(c.CategoryID) "Number of Products in Each Category" 
FROM Categories c
INNER JOIN Products p 
    ON p.CategoryID = c.CategoryID 
GROUP BY c.CategoryName, c.CategoryID
ORDER BY COUNT(c.CategoryID) DESC; 


-- 1.5	List all UK employees using concatenation to join their title of courtesy, first name and last name together. Also include their city of residence.
SELECT * FROM Employees;

SELECT 
    CONCAT(e.TitleOfCourtesy, ' ',e.Firstname,' ',e.LastName) AS "Employee Name",
    e.City, 
    e.Country
FROM Employees e
WHERE e.Country = 'UK'; 


-- 1.6	List Sales Totals for all Sales Regions (via the Territories table using 4 joins) with a Sales Total greater than 1,000,000. Use rounding or FORMAT to present the numbers. 
SELECT * FROM Territories;
SELECT DISTINCT RegionID FROM Territories;
SELECT * FROM Orders; 
SELECT * FROM Region;
SELECT * FROM Customers; 
SELECT * FROM Employees; 
SELECT * FROM EmployeeTerritories; 
SELECT * FROM [Order Details]; 

SELECT 
    r.RegionDescription AS "Region", 
    t.RegionID, 
    ROUND(SUM(od.UnitPrice * od.Quantity * (1.00-od.Discount)),2) AS "Net Sales" 
FROM [Order Details] od 
INNER JOIN Orders o 
    ON o.OrderID = od.OrderID 
INNER JOIN EmployeeTerritories et 
    ON et.EmployeeID = o.EmployeeID
INNER JOIN Territories t 
    ON t.TerritoryID = et.TerritoryID
INNER JOIN Region r 
    ON t.RegionID = r.RegionID
GROUP BY 
    t.RegionID,
    r.RegionDescription
HAVING 
    ROUND(SUM(od.UnitPrice * od.Quantity),2) > 1000000 
ORDER BY [Net Sales] DESC;



-- 1.7	Count how many Orders have a Freight amount greater than 100.00 and either USA or UK as Ship Country.
SELECT * FROM Orders;

SELECT 
    COUNT(o.Freight) AS "Total No. of Orders from USA and UK" 
FROM Orders o
WHERE o.Freight > 100.00
AND o.ShipCountry IN ('USA', 'UK'); 



-- 1.8	Write an SQL Statement to identify the Order Number of the Order with the highest amount of discount applied to that order.
SELECT * FROM [Order Details];


SELECT TOP 1 
od.orderID AS "Order Number with largest discount", 
ROUND(SUM(od.unitPrice * od.Quantity * od.Discount),2) AS "Discount Applied"
FROM [Order Details] od
GROUP BY od.OrderID
ORDER BY [Discount Applied] DESC; 

-- Exercise 2 – Create Spartans Table (20 marks – 10 each)

-- 2.1 Write the correct SQL statement to create the following table:
-- Spartans Table – include details about all the Spartans on this course. Separate Title, First Name and Last Name into separate columns, and include University attended, course taken and mark achieved. Add any other columns you feel would be appropriate. 
-- IMPORTANT NOTE: For data protection reasons do NOT include date of birth in this exercise.

DROP DATABASE sql_at

CREATE DATABASE sql_at

USE sql_at

DROP TABLE Sparta_Table

CREATE TABLE Sparta_Table 
(
    Title varchar(50),
    FirstName varchar(50),
    LastName varchar(50),
    University varchar(50),
    Course varchar(50),
    Grade INT,
);

ALTER TABLE Sparta_Table ADD StudentID INT IDENTITY (1011, 1) PRIMARY KEY; 


-- 2.2 Write SQL statements to add the details of the Spartans in your course to the table you have created.
INSERT INTO Sparta_Table
    (Title, FirstName, LastName, University, Course, Grade)
VALUES 
    ('Mr.', 'Rick', 'Lennon', 'UCL', 'Electrical Engineering', 74),
    ('Miss', 'Zara', 'Cavanagh', 'Sheffield', 'English Literature', 65),
    ('Miss', 'Laura', 'Samil', 'Exeter', 'Ancient History', 58),
    ('Miss', 'Mareesha', 'Saddiqi', 'Brunel', 'Computer Science', 70),
    ('Mr.', 'Alan', 'Kane', 'Lancaster', 'Accounting and Finance', 69),
    ('Miss', 'Serena', 'O''Treasaigh', 'Brunel', 'Visual Effect and Motion Graphics', 61),
    ('Mr.', 'James', 'Hovell', 'Portsmouth', 'Biomedical Sciences', 62),
    ('Mr.', 'Steven', 'Chan', 'Hertfordshire', 'Mathematics', 82),
    ('Ms.', 'Adriana', 'Ahmed', 'Edinburgh', 'Modern Languages', 66),
    ('Ms.', 'Amanda', 'Hu', 'Glasgow', 'Architecture', 74),
    ('Mr.', 'Sharma', 'Whittaker', 'LSE', 'Geography and Economics', 68)


SELECT * FROM Sparta_Table;


-- Exercise 3 – Northwind Data Analysis linked to Excel (30 marks)
-- 3.1 List all Employees from the Employees table and who they report to. No Excel required. (5 Marks)
USE Northwind

SELECT * FROM Employees;

SELECT 
    a.EmployeeID AS "Employee ID",
    CONCAT(a.TitleOfCourtesy,' ',a.FirstName,' ',a.LastName) AS "Employee Name",
    a.ReportsTo AS "Supervisor ID",
    CONCAT(b.TitleOfCourtesy, ' ', b.FirstName, ' ', b.LastName) AS "Reports To"
FROM Employees a 
LEFT JOIN Employees b 
    ON a.ReportsTo = b.EmployeeID  
ORDER BY 
    [Supervisor ID]; 


-- 3.2 List all Suppliers with total sales over $10,000 in the Order Details table. Include the Company Name from the Suppliers Table and present as a bar chart as below:
SELECT * FROM Suppliers; 
SELECT * FROM [Order Details];
SELECT * FROM Products; 
SELECT 
    s.SupplierID, 
    s.CompanyName AS "Supplier Name",
    ROUND(SUM(od.UnitPrice*od.Quantity*(1.00-od.Discount)), 2) AS "Net Sales"
FROM Suppliers s 
INNER JOIN Products p 
    ON p.SupplierID = s.SupplierID
INNER JOIN [Order Details] od 
    ON od.ProductID = p.ProductID
GROUP BY s.SupplierID, s.CompanyName
HAVING ROUND(SUM(od.UnitPrice*od.Quantity*(1.00-od.Discount)), 2) > 10000 
ORDER BY "Net Sales";



-- 3.3 List the Top 10 Customers year to date (YTD) for the latest year in the Orders file. 
-- Based on total value of orders shipped. No Excel required. (10 Marks)
SELECT * FROM Orders; 
SELECT * FROM Customers;
SELECT * FROM [Order Details]; 


SELECT TOP 10
    o.customerID AS "Customer ID",
    c.CompanyName AS "Company",
    ROUND(SUM(od.UnitPrice*od.Quantity*(1.00-od.Discount)), 2) AS [Total Value of Orders placed by Customers], 
    MAX(YEAR(o.OrderDate)) AS "Latest Year"
FROM Customers c
INNER JOIN Orders o 
    ON c.CustomerID = o.CustomerID
INNER JOIN [Order Details] od 
    ON od.OrderID = o.OrderID
WHERE YEAR(o.OrderDate) IN 
    (SELECT YEAR(MAX(o.OrderDate)) FROM Orders o)  
AND o.ShippedDate IS NOT NULL
GROUP BY 
    o.CustomerID,
    c.CompanyName
ORDER BY [Total Value of Orders placed by Customers] DESC;


-- 3.4 Plot the Average Ship Time by month for all data in the Orders Table using a line chart as below.

SELECT * FROM Orders;

SELECT * FROM Orders
ORDER BY ShippedDate;

SELECT
    FORMAT(o.OrderDate, 'MMM-yy') AS "Shipping Month", 
    AVG(CAST(DATEDIFF(DAY, o.OrderDate, o.ShippedDate) AS DECIMAL(10,2))) AS "Average Shipping Time"
FROM Orders o  
GROUP BY 
    MONTH(o.OrderDate), 
    YEAR(o.OrderDate),
    FORMAT(o.OrderDate, 'MMM-yy')
ORDER BY 
    YEAR(o.OrderDate), 
    MONTH(o.OrderDate);




    




    