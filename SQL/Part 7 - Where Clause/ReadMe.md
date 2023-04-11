# **Part 7 - Where Clause**

1. Purpose is to filter records based on some `condition`.
2. Practice Where Clause: Try at [W3School](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

```sql
Select * from Customers where City='London'; 
-- or
Select * from Customers where CustomerID=9; 
-- or
Select CustomerName,Country,City where City='London';
```

We have used Where Clause with only Select statements, using Where Clause with other statements like Update, Delete etc. will be explained
