# **Part 9 - Using Logical Operators [AND, OR, NOT]**

* What is the purpose of Logical Operators: `To filter the records based on Multiple Conditions`
* Different Logical Operators we can use in Where Clause Condition
  * `AND`
  * `OR`
  * `NOT`
  
* Practical Demonstrations: Try at [W3School](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

`AND`

```sql
Select * from Customers;
-- 
Select * from Customers where Country='Mexico'; 
-- 
Select * from Customers where Country='Mexico' AND CustomerID>3;
-- 
Select * from Customers where Country='Mexico' AND CustomerID>3 AND ContactName<>'Francisco Chang';
```

`OR`

```sql
Select * from Customers;
-- 
Select * from Customers where Country='Germany';
-- 
Select * from Customers where Country='Germany' OR City='London';
-- 
Select * from Customers where Country='Germany' OR City='London' OR CustomerID>90;
```

`NOT`

```sql
Select * from Customers;
-- 
Select * from Customers where Country='Germany';
-- 
Select * from Customers where NOT Country='Germany';
-- 
Select * from Customers where NOT Country='Germany' AND City='London';
```
