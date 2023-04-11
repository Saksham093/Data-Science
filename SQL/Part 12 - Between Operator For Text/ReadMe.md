# **Part 12 - Between Operator with Text**

In [Part - 10](https://github.com/Saksham093/Data-Science/SQL/Part 10 - Between Operator For Num/ReadMe.md), Explained how to use Between operator with Numbers.
  
Practical Demonstrations: Try at [W3School](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

```sql
Select * from Customers;
-- 
Select * from Customers Order By Country;
-- 
Select * from Customers where Country Between 'Canada' And 'Finland' Order By Country;
-- 
Select * from Customers where Country NOT Between 'Canada' And 'Finland' Order By Country;
```
