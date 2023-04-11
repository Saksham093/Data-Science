# **Part 10 Between Operator**

Purpose is to filter records based on some `Range`.
  
Practical Demonstrations: Try at [W3School](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

`BETWEEN`

```sql
Select * from Products;
-- 
Select * from Products where Price Between 10 And 20;
-- 
Select * from Products where Price>=10 And Price<=20;
-- 
Select * from Products where Price NOT Between 10 And 20;
-- 
Select * from Products where Price<10 OR Price>20;
```
