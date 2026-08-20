# Lab 07 - Bulk Import, BCP, and XML Export

This individual lab explores external data movement in SQL Server using `BULK INSERT`, BCP, `OPENROWSET`, `xp_cmdshell`, and XML-formatted aggregate reporting with AdventureWorks2012.

## Main topics

- CSV import with `BULK INSERT`
- Duplicate prevention with `NOT EXISTS`
- BCP query export
- Bulk file access with `OPENROWSET`
- Server configuration for external access
- XML construction with `FOR XML PATH`
- Command execution through `xp_cmdshell`

## Files

- `original-submission/lab-07.sql`: original submitted SQL content
- `original-submission/my_csv.csv`: submitted sales export
- `original-submission/love.text`: submitted but empty text-export file
- `reference-material/instructions-07-fa.pdf`: original Persian instruction sheet
- `reference-material/NewProductData.csv`: instructor-provided product input data
- `prompt.md`: concise English summary of the exercise

The SQL and submitted output files are preserved without modification. Generic archive and folder names were not retained.

## Submission summary

The submission attempts all three tasks:

- It defines temporary and destination product tables, imports the provided product CSV, and uses `NOT EXISTS` for duplicate filtering.
- It selects July 2008 sales rows, invokes BCP through `xp_cmdshell`, and attempts to import the resulting file with `OPENROWSET`.
- It builds XML containing order count, first order date, and total sales for each product, then attempts to export the result through BCP and `xp_cmdshell`.

The submitted `my_csv.csv` contains 2,209 rows. Every row has five semicolon-separated fields, and every recorded date is in July 2008. The submitted `love.text` file is empty.

## Verification status

The SQL was reviewed statically. The provided CSV files were structurally inspected, but the script was not executed because it depends on SQL Server configuration, AdventureWorks2012, BCP, filesystem permissions, and machine-specific Windows paths.

## Known limitations in the historical submission

- Both product-table definitions contain a trailing comma before the closing parenthesis, which is invalid T-SQL syntax.
- `temp_products` is dropped immediately after it is created and before `BULK INSERT`, so the import cannot succeed as written.
- `new_products` is dropped without checking whether it exists, which can stop a first run.
- `new_products` is recreated empty immediately before the `NOT EXISTS` insert. As a result, every imported row is inserted and the duplicate-prevention logic is not meaningfully tested.
- The product tables have no primary key or uniqueness constraint on `ProductID`.
- All import and export paths are hard-coded to one laboratory Windows desktop and are not portable.
- The BCP command specifies a comma field terminator, while the submitted `my_csv.csv` is semicolon-delimited.
- `OPENROWSET(..., SINGLE_CLOB)` loads the complete CSV as one text value. It does not parse five relational columns or create the requested `TempSalesData` rows.
- The imported table is named `sales_temp`, not `TempSalesData`, and `SELECT INTO` will fail on a repeated run if the table already exists.
- The standalone XML query counts order-detail rows rather than distinct sales orders.
- The reported sales expression multiplies quantity by unit price but ignores `UnitPriceDiscount`; `LineTotal` would better represent the recorded line sale.
- The BCP query for Question 3 selects `kh.Name`, but its product table is aliased as `p`. This undefined alias prevents the export query from running.
- The submitted `love.text` file is zero bytes, consistent with the failed Question 3 export.
- The script enables `xp_cmdshell` and leaves it enabled. Although the exercise explicitly requests it, this expands the SQL Server attack surface and would require careful restriction and cleanup outside a laboratory environment.
- Some server-configuration statements are duplicated, and the `sp_configure 'Advanced'` statement is not a valid replacement for `show advanced options`.

This lab introduces valuable data-import and export concepts, but its historical script should be treated as an incomplete laboratory attempt rather than a working end-to-end pipeline.
