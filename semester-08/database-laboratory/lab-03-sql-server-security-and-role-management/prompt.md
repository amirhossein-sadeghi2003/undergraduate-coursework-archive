# Exercise 03 - SQL Server Security and Role Management

## Objective

Configure and test SQL Server security in AdventureWorks2012 using both SQL Server Management Studio and equivalent T-SQL commands.

## Part 1 - Login and Role 3

1. Create a new SQL Server login.
2. Create `Role3` with read access to all AdventureWorks2012 tables and write access to a selected schema such as `Sales`.
3. Create or map the corresponding database user and assign `Role3`.
4. Connect with the new login, create a table in the `Sales` schema, and insert several rows.

## Part 2 - Role 4 and controlled view access

1. Create another database user and assign `Role4`.
2. Configure `Role4` so it has no direct table access but can grant `SELECT` on selected views to other users and can query a predefined view without direct access to its underlying table.
3. Verify that the user can query the selected Customer-related view but cannot query the Customer table directly.
4. Extend the role with `SELECT` access to an additional table such as a SalesOrder table.
5. Create another user and verify the updated role membership and permissions.

This file summarizes the original Persian instruction sheet; it is not a replacement for the source handout in `reference-material/`.
