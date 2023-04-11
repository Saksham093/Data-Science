# **Part 11 - Order By Clause [ASC, DESC]**

Purpose is to order the retrieved records in `Ascending (ASC)` or `Descending order (DESC)` and by-default Ascending order is applyied.
  
Practical Demonstrations: Try at [W3School](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

`ASC / DESC`

```sql
SELECT * FROM Customers;
-- 
SELECT * FROM Customers Order By Country;
-- 
SELECT * FROM Customers Order By Country ASC;
-- 
SELECT * FROM Customers Order By Country DESC;
-- 
SELECT * FROM Customers Order By Country ASC,City ASC;
-- 
SELECT * FROM Customers Order By Country DESC,City DESC;
-- 
SELECT * FROM Products Order By Price;
-- 
SELECT * FROM Products Order By Price ASC;
-- 
SELECT * FROM Products Order By Price DESC;
```
