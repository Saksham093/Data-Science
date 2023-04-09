# **Part 4 - Distinct Keyword**

1. For `unique values` to be retrieved, we have to use `distinct` keyword with Select command.
2. Without distinct: Try at [W3School](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

```sql
Select Country from Customers;
```

3. With distinct:

```sql
Select distinct Country from Customers;
```

`Example :`

```sql
Select distinct country, postalcode from customers; --Combination of --country and postalcode should be unique.
```
