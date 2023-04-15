# **Part 13 - In Operator**

Simplifies providing multiple values in Where Clause, when all the values are from the same column
  
Practical Demonstrations: Try at [W3School](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

```sql
Select * from Products;
-- 
Select * from Products where Price=18 OR Price=30 OR Price=10;
-- 
Select * from Products where Price in (18,30,10);
-- 
Select * from Customers;
-- 
Select * from Customers where Country='USA' OR Country='Canada' OR Country='UK';
-- 
Select * from Customers where Country in ('USA','Canada','UK');
```
