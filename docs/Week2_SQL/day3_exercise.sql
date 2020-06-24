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