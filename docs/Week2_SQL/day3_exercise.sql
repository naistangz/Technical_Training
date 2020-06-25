USE NORTHWIND

/*WHERE clause-filter the data*/
SELECT * FROM Customers
WHERE City = 'Paris';

SELECT COUNT(*) AS 'Number of Employees in London' FROM Employees
WHERE City='London';

SELECT COUNT(*) AS 'Number of Employees with Title Doctor' FROM Employees
WHERE TitleOfCourtesy='Dr.'

SELECT * FROM Employees;

SELECT COUNT(*) FROM Products
WHERE Discontinued != 0;

SELECT * FROM products
WHERE Discontinued != 0;

/*Apostrophe*/
'Anais''s'

/*Using table Alias*/
SELECT c.CompanyName, c.City, c.Country, c.Region
FROM Customers c
WHERE c.Region='BC';

/*TOP*/
SELECT TOP 10 CompanyName, City FROM Customers
WHERE Country = 'France';

SELECT COUNT(*) FROM Customers WHERE Country='France';

/*AND/OR*/
/*AND all the criterias need to be fulfilled*/
/*OR - either of the criterias need to be fulfilled*/

SELECT p.ProductName, p.UnitPrice 
FROM Products p
WHERE CategoryID=1 AND Discontinued=0;

/*Using Operators*/
/*Where units in stock are greater than 0 AND greater than 29.99*/
SELECT p.ProductName, p.UnitPrice
FROM Products p
WHERE UnitsInStock > 0 AND UnitPrice > 29.99;

/*Distinct removes duplicates, only unique values*/
SELECT DISTINCT Country FROM Customers
WHERE ContactTitle ='Owner';

SELECT DISTINCT c.country
FROM customers c;

/*Wildcards can be used as a substitute for any other characters in a string when using the LIKE operator*/

/*Begins with U*/
SELECT DISTINCT c.country
FROM customers c WHERE country LiKE 'U%';

/*Begins with BR*/
SELECT DISTINCT c.country
FROM customers c WHERE country LIKE 'BR%';

/*Ends with A*/
SELECT DISTINCT c.country
FROM customers c WHERE country LIKE '%A';

/*Countries starting with U, ending with letter 'A'*/
SELECT DISTINCT c.country
FROM customers c WHERE country LIKE 'U%A';

/*Countries either starting with U or A in descending order*/
SELECT DISTINCT c.country
FROM customers c WHERE country LIKE '[UAM]%'
ORDER BY c.country DESC;

/*Countries not starting with U or A or M*/
SELECT DISTINCT c.country
FROM customers c WHERE country LIKE '[^UAM]%';

/*Countries not ending with A or E*/
SELECT DISTINCT c.country
FROM customers c WHERE country LIKE '%[^AE]';

/*Countries whose 3rd letter is A. '_' substitutes for a single character*/
SELECT DISTINCT c.Country
FROM customers c 
WHERE country LIKE '__A%';

/*Products that begin with Ch*/
SELECT p.ProductName AS 'Product Name'
FROM Products p 
WHERE ProductName LIKE 'Ch%';

/*Select all columns from customer table where regions only contain two characters, end in A or where the second letter is A*/
SELECT * 
FROM Customers
WHERE Region LIKE '_A';

/*IN If we want to find customers in two specific named regions*/
/*IN allows multiple results on subquery, = will generate error if you have more than one result on the subquery*/
SELECT * 
FROM Customers
WHERE Region IN ('WA','SP');

/*Without IN statement using OR operator*/
SELECT * 
FROM Customers
WHERE Region = 'WA'OR Region ='SP';

/*Find Region WA or SP, AND Brazil. Place query in brackets to avoid complications and make it explicit for SQL to process the correct query*/
SELECT * 
FROM Customers
WHERE (Region = 'WA'OR Region ='SP')
AND country ='Brazil'; --Should only return customers from Brazil where region is WA or SP

/*BETWEEN - includes values between and as well as the boundary values*/
SELECT * 
FROM EmployeeTerritories
WHERE TerritoryID BETWEEN 06800 AND 09999;


/*What are names and product IDs of the products with a unit price below 5.00*/

SELECT * FROM Products;

SELECT p.ProductName, p.productID, p.UnitPrice
FROM Products p
WHERE UnitPrice < 5.00;


/*Which categories have a category name with initials beginning with B or S*/
SELECT * FROM Categories;

/*Option 1*/
SELECT c.CategoryName, c.DESCRIPTION
FROM Categories c
WHERE c.CategoryName LIKE 'B%' OR c.CategoryName LIKE 'S%';

/*Option 2*/
SELECT c.CategoryName, c.DESCRIPTION
FROM categories c
WHERE c.CategoryName LIKE '[BS]%';

/*How many orders are there for EmployeeIDs 5 and 7(Total for both)*/
SELECT * FROM Orders;

SELECT COUNT(*) AS 'Number of Orders placed by Employees with Employee ID 5 or 7' 
FROM Orders o
WHERE EmployeeID IN (5, 7)
GROUP BY o.EmployeeId;

SELECT o.orderID, o.EmployeeID
FROM orders o 
WHERE EmployeeID IN (5, 7);

/*CONCATENATION*/
/*In below example, alias 'City' select city and country in one column using concat operator +*/
/*Option 1*/
SELECT c.companyName AS 'Company Name', c.city + ',' + ' '+  Country As 'City'
FROM Customers c;

/*Option 2*/
SELECT c.CompanyName AS 'Company Name',
CONCAT(c.city, ', ',c.country) AS City
FROM Customers c;

/*Write a select using the Employees table and concat First Name and Last Name together. Use column alias to rename the column to Employee Name*/
SELECT * FROM Employees;

SELECT e.EmployeeID as 'Employee Id', CONCAT(e.FirstName,' ', e.LastName) AS 'Employee Name'
FROM Employees e;  -- Should return First Name and Last Name in the same columm called Employee Name

/*IS NULL*/
SELECT c.CompanyName AS 'Company Name', CONCAT(c.City, ' ', c.Country) AS 'City', c.Region
FROM Customers c
WHERE Region IS NULL;

/*IS NOT NULL*/
SELECT c.CompanyName AS 'Company Name', CONCAT(c.City, ' ', c.Country) AS 'City', c.Region
FROM Customers c
WHERE Region IS NOT NULL;

/*Write a SELECT statement to list the six countries that have Region Codes in the Customers Table*/
SELECT * FROM Customers;

SELECT TOP 6 c.Country, c.Region
FROM Customers c
WHERE Region  IS NOT NULL;

/*ARITHMETIC OPERATORS*/
SELECT UnitPrice, Quantity, Discount, UnitPrice * Quantity AS 'Gross Total'
FROM [Order Details];

SELECT * FROM [Order Details];

--Apples--> Price--> 2 Pounds, quantity=10, Discount -25% = (2*10)*0.75
--Gross Total(The cost apple excluding the discount) = £20
--Net Total (The amount I pay the shopkeeper) = £15

/*Add a new column to the SQL below to show the 'Net Total' which has the discount column applied to it.*/
SELECT 
UnitPrice,
Quantity, 
Discount, 
UnitPrice * Quantity AS 'Gross Total', 
ROUND((UnitPrice * Quantity * (1.00-Discount)),2) AS 'Net Total'
FROM [Order Details]
ORDER BY 'Gross Total' DESC;

--Use ORDER BY to identify the highest Net Total in the Order Details table
--What are the two order numbers with the highest total?

SELECT TOP 2
OrderID,
Unitprice AS 'Unit Price',
Quantity,
Discount,
ROUND((UnitPrice * Quantity * (1.00- Discount)),2) AS 'Net Total'
FROM [Order Details]
ORDER BY 'Net Total' DESC;

/*STRING FUNCTIONS*/
USE astha_db
SELECT * FROM film_table

SELECT film_table, CHARINDEX('S', film_name) AS 'Position of Character'
FROM film_table;
--Returns index of character. In SQL index starts at 1 not 0.

SELECT film_name, SUBSTRING(film_name, 1, 3) AS 'Extracted String' FROM film_table
--returns first to third character

SELECT film_name, RIGHT(film_name, 2) AS 'Extracted String' FROM film_table;
-- Extracts last two characters 

SELECT film_name, LEFT(film_name, 2) AS 'Extracted String' FROM film_table;
-- Extracts first two characters

SELECT film_name, RTRIM(film_name) AS 'Trimmed String' FROM film_table;
--Removes white spaces from the end

SELECT film_name, LTRIM(film_name) AS 'Trimmed String' FROM film_table;
--Removes white spaces from the beginning 

SELECT film_name, REPLACE(film_name, ' ', 'A') AS 'Replaced String' FROM film_table;
--Removes the space with the character A

SELECT film_name, LEN(film_name) AS 'Length of String' FROM film_table;
--Calculates length of string, spaces included.

SELECT film_name, 
UPPER(film_name) AS 'Uppercase String', 
LOWER(film_name) AS 'Lower String'
FROM film_table;

/*CHARINDEX PRACTICE*/
USE Northwind

SELECT PostalCode 'Post code', 
LEFT(PostalCode, CHARINDEX(' ', PostalCode)-1) AS 'Post Code Region',
    CHARINDEX(' ',PostalCode) AS 'Space Found', 
Country
FROM Customers 
WHERE country ='UK';

-- Without -1 it will give index 4 
-- -1 will extract the post code region that reaches the first space then eliminate the white space

/*Use CHARINDEX to list only Product Names that contain a single quote*/
/*Note:Column Alias cannot be used in a WHERE*/
/*For single quote use two single quotes to 'escape' it*/

SELECT * FROM  Products;

SELECT p.ProductName "Product Names",
CHARINDEX('''', p.ProductName) AS "Index of Quote"
FROM Products p
WHERE CHARINDEX('''', p.productName) > 0;


-- SELECT * FROM TableName WHERE CHARINDEX('''',ColumnName) > 0 

/*Option 2 with LIKE*/
SELECT p.ProductName AS 'Product Name'
FROM Products p
WHERE p.productName LIKE '%''%';
--Finds single quotes 





