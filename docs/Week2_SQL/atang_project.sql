-- SQL Project 

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
-- Returns 8 rows 


-- 1.2	List all products stored in bottles.
SELECT * FROM Products;

SELECT 
    p.productID,
    p.productName AS "Product Name",
    p.QuantityPerUnit AS "Products Stored in Bottles"  -- Changed name of column to specify the type of packaging used to store the product
FROM Products p
WHERE p.QuantityPerUnit LIKE '%bottle%';  -- Used singular form of bottle NOT plural
-- Returns 12 products stored in bottles 

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

SELECT * FROM Categories; -- Categories has eight rows, therefore OUTPUT table should reflect same number of rows

SELECT 
    c.CategoryName AS "Category Name", 
    COUNT(c.CategoryID) "Number of Products in Each Category" -- Used COUNT to determine how many products match with the same category
FROM Categories c
INNER JOIN Products p 
    ON p.CategoryID = c.CategoryID 
GROUP BY c.CategoryName, c.CategoryID
ORDER BY COUNT(c.CategoryID) DESC; -- ORDER BY DESC to get the highest number first 


-- 1.5	List all UK employees using concatenation to join their title of courtesy, first name and last name together. Also include their city of residence.
SELECT * FROM Employees;

SELECT 
    CONCAT(e.TitleOfCourtesy, ' ',e.Firstname,' ',e.LastName) AS "Employee Name",
    e.City, -- Included city of residence 
    e.Country
FROM Employees e
WHERE e.Country = 'UK'; 
-- Returns 4 records 

-- 1.6	List Sales Totals for all Sales Regions (via the Territories table using 4 joins) with a Sales Total greater than 1,000,000. Use rounding or FORMAT to present the numbers. 
SELECT * FROM Territories;
SELECT DISTINCT RegionID FROM Territories;
SELECT * FROM Orders; -- via EmployeeID from Employees, via CustomerID from Customers
SELECT * FROM Region; -- via TerritoryID from Territories 
SELECT * FROM Customers; -- via CustomerID from Orders
SELECT * FROM Employees; --via EmployeeID from orders
SELECT * FROM EmployeeTerritories; --via EmployeeID from Employees, via TerritoryID from Territories
SELECT * FROM [Order Details]; --via OrderID, CustomerID, EmployeeID from Orders

SELECT 
    r.RegionDescription AS "Region", 
    t.RegionID, 
    ROUND(SUM(od.UnitPrice * od.Quantity * (1.00-od.Discount)),2) AS "Net Sales" -- Total Sales after discount has been applied
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
    ROUND(SUM(od.UnitPrice * od.Quantity),2) > 1000000 -- Excludes regions where total sales fall below 1,000,000
ORDER BY [Net Sales] DESC;
-- To note: I calculated Net Sales which includes sales with discount 


-- 1.7	Count how many Orders have a Freight amount greater than 100.00 and either USA or UK as Ship Country.
SELECT * FROM Orders;

SELECT 
    COUNT(o.Freight) AS "Total No. of Orders from USA and UK" 
FROM Orders o
WHERE o.Freight > 100.00
AND o.ShipCountry IN ('USA', 'UK'); 
-- Result should be 49 total orders


-- 1.8	Write an SQL Statement to identify the Order Number of the Order with the highest amount of discount applied to that order.
SELECT * FROM [Order Details];


SELECT TOP 1 
od.orderID AS "Order Number with largest discount", 
ROUND(SUM(od.unitPrice * od.Quantity * od.Discount),2) AS "Discount Applied"
FROM [Order Details] od
GROUP BY od.OrderID
ORDER BY [Discount Applied] DESC; 

SELECT * FROM [Order Details]
WHERE orderID IN (11030);
-- To note: OrderID's are not unique, OrderID can link to multiple productIDs, therefore SUM is required to add ALL products for the same OrderID
-- Lists all products with OrderID 11030. When adding all values for discount applied, answer should reflect same answer previous query.
-- Discount applied should add up to 3706.85 




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
    Title varchar(50), -- Using varchar to store variable-length character strings, requires less storage space than fixed-length (CHAR())
    FirstName varchar(50),
    LastName varchar(50),
    University varchar(50),
    Course varchar(50),
    Grade INT,
);

ALTER TABLE Sparta_Table ADD StudentID INT IDENTITY (1011, 1) PRIMARY KEY; 
-- PRIMARY KEY constraint indicates unique values 
-- Starting value 1011, increment by 1. IDENTITY keyword peforms auto-increment feature

-- SET IDENTITY_INSERT Sparta_Table ON; 
--This feature allows explicit values to be inserted manually into the identity column instead of performing auto-increment

-- 2.2 Write SQL statements to add the details of the Spartans in your course to the table you have created.
INSERT INTO Sparta_Table
    (Title, FirstName, LastName, University, Course, Grade)
VALUES 
    ('Mr.', 'Rick', 'Lennon', 'UCL', 'Electrical Engineering', 74),
    ('Miss', 'Zara', 'Cavanagh', 'Sheffield', 'English Literature', 65),
    ('Miss', 'Laura', 'Samil', 'Exeter', 'Ancient History', 58),
    ('Miss', 'Mareesha', 'Saddiqi', 'Brunel', 'Computer Science', 70),
    ('Mr.', 'Alan', 'Kane', 'Lancaster', 'Accounting and Finance', 69),
    ('Miss', 'Serena', 'O''Treasaigh', 'Brunel', 'Visual Effect and Motion Graphics', 61), -- Use of escape single character
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
    CONCAT(b.TitleOfCourtesy, ' ', b.FirstName, ' ', b.LastName) AS "Reports To" -- Including a column to clarify who the Employee will be reporting to
FROM Employees a -- Left Table
LEFT JOIN Employees b -- Join on same table, using aliasing to differentiante the two tables. Use of left join returns all records from Employee a (left table) and matched records on emloyee b (right table)
    ON a.ReportsTo = b.EmployeeID  -- Linking Supervisor ID according to the corresponding Employee ID 
ORDER BY 
    [Supervisor ID]; 


-- 3.2 List all Suppliers with total sales over $10,000 in the Order Details table. Include the Company Name from the Suppliers Table and present as a bar chart as below:
SELECT * FROM Suppliers; --supplierID
SELECT * FROM [Order Details];--ProductID
SELECT * FROM Products; --productID, --supplierID 

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
HAVING ROUND(SUM(od.UnitPrice*od.Quantity*(1.00-od.Discount)), 2) > 10000 -- Amount including discount with value over 10,000
ORDER BY "Net Sales";



-- 3.3 List the Top 10 Customers year to date (YTD) for the latest year in the Orders file. 
-- Based on total value of orders shipped. No Excel required. (10 Marks)
SELECT * FROM Orders; --via OrderID, CustomerID
SELECT * FROM Customers; --via CustomerID
SELECT * FROM [Order Details]; --via OrderID


SELECT TOP 10
    o.customerID AS "Customer ID",
    c.ContactName AS "Customer Name",
    ROUND(SUM(od.UnitPrice*od.Quantity*(1.00-od.Discount)), 2) AS [Total Value of Orders placed by Customers], -- Calculation for sales after discount is applied, rounded to two decimal places
    MAX(YEAR(o.ShippedDate)) AS "Latest Year" -- MAX(year) selects the latest year. Result should expect the same value in every row.
FROM Orders o
INNER JOIN Customers c
    ON c.CustomerID = o.CustomerID
INNER JOIN [Order Details] od 
    ON od.OrderID = o.OrderID
GROUP BY 
    o.CustomerID,
    c.ContactName,
    o.ShippedDate
HAVING YEAR(o.ShippedDate) IN 
    (SELECT YEAR(MAX(o.ShippedDate)) FROM Orders o) -- This subquery selects top 10 Order amount 'only' in the latest year which is 1998
ORDER BY [Total Value of Orders placed by Customers] DESC;


-- 3.4 Plot the Average Ship Time by month for all data in the Orders Table using a line chart as below.

-- Find every shipping month 
-- Find average number of days it takes to ship an order by finding the difference between order date and shipping date 
-- Above query will return the difference for every row (every OrderID), so group by month, year

SELECT * FROM Orders;

SELECT * FROM Orders
ORDER BY ShippedDate;

SELECT
    FORMAT(o.OrderDate, 'MMM-yy') AS "Shipping Month", -- Format to get Shipping Month and Year in text format
    AVG(DATEDIFF(DAY, o.OrderDate, o.ShippedDate)) AS "Average Shipping Time" -- Get average shipping time in days from when the order was placed and when it was shipped
FROM Orders o
GROUP BY 
    MONTH(o.OrderDate), -- Group by each month to each year as data spans across multiple years.
    YEAR(o.OrderDate),
    FORMAT(o.OrderDate, 'MMM-yy')
ORDER BY 
    YEAR(o.OrderDate), -- To ensure that dates are ordered in chronological order 
    MONTH(o.OrderDate);







    




    