# **Part 3 - Select Command**

1. The purpose this SQL command is to retrieve the data from the tables
2. Retrieving all the data from Customers table

`Syntax :`

```sql
SELECT* from <Table_Name>; 
```

`Example :`

```sql
Select * from Customers;
```

3. Retrieving specific column data from Customers table

```sql
-- single column
Select CustomerName from Customers;

-- Multi Columns
SELECT CustomerName, Country, City, PostalCode from Customers;
```
