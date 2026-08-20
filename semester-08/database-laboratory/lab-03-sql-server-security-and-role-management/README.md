# Lab 03 - SQL Server Security and Role Management

This individual lab explores SQL Server authentication and authorization using server logins, database users, custom roles, schema and object permissions, views, and permission testing in AdventureWorks2012.

## Main topics

- SQL Server logins and database users
- Role creation and membership
- Object-level and schema-level permissions
- `GRANT` and `DENY`
- View-based access without direct table access
- Permission delegation and least-privilege design
- SQL Server Management Studio security configuration

## Files

- `sanitized-submission/lab-03.sql`: submitted T-SQL with the embedded plaintext password replaced by a public placeholder
- `reference-material/instructions-03-fa.pdf`: original Persian instruction sheet
- `prompt.md`: concise English summary of the exercise

## Public-archive sanitization

The submitted RAR archive is not included because its SQL file contains a plaintext login password. The published SQL changes only that password literal to `REPLACE_WITH_STRONG_PASSWORD`; the remaining historical content is preserved. The original file also had a `.txt` extension and was renamed to `.sql` for clarity.

## Submission summary

The script attempts to:

- Create a SQL Server login and corresponding AdventureWorks2012 user.
- Create `role3`, grant selected read and write permissions, and add the user to the role.
- Create a table in the `Sales` schema.
- Create `role4` and grant access to selected views while denying access to an underlying table.
- Add a second user to `role4` and extend the role with access to another table.

## Verification status

The submission was reviewed statically as SQL Server T-SQL. It was not executed because it requires a configured SQL Server instance, AdventureWorks2012, administrative privileges, and separate login sessions for permission verification.

## Known limitations in the historical submission

- The original login uses a very weak plaintext password, disables password policy and expiration checks, and therefore does not represent a strong production security configuration.
- `role3` receives `SELECT` on only five Production objects rather than read access to all AdventureWorks2012 tables as requested.
- The script repeats several `GRANT` statements and attempts to create `role4` three times. Running the file from top to bottom would fail after the first successful `CREATE ROLE [role4]`.
- Creating a table in the `Sales` schema normally requires database-level `CREATE TABLE` plus suitable permission on that schema. The script grants `CREATE TABLE` but does not grant `ALTER` on `SCHEMA::Sales`.
- The script creates `Sales.test` with a single `char` column but does not insert the requested sample records.
- An unrelated `ALTER` permission is granted on `Production.ProductModel`.
- `role4` is supposed to be able to grant selected view permissions to other users, but the script does not use `WITH GRANT OPTION`.
- The script grants view access and denies one underlying table, but it does not include the requested explicit test showing that direct table access fails while view access succeeds.
- `sadeghi2` is added to `role4` without a corresponding `CREATE LOGIN` or `CREATE USER` statement in the submitted file.
- The final extra table permission targets `Person.PhoneNumberType`, not a SalesOrder-related table as suggested in the exercise.
- The second user and the updated role permissions are not fully verified.

Despite these limitations, the lab introduces useful database-security concepts and is a stronger coursework topic than a basic query exercise.
