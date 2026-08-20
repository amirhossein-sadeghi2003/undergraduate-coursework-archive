# Lab 05 - Row Number, Pivot, and Scalar Function

This individual lab uses AdventureWorks to practice row numbering, pivoted yearly sales, scalar user-defined functions, and string normalization in T-SQL.

## Main topics

- `ROW_NUMBER()` with partitioning
- Common table expressions
- Static `PIVOT`
- Scalar user-defined functions
- Customer and person joins
- Case conversion and whitespace trimming
- `COALESCE` fallback values
- Digit removal with `PATINDEX`, `SUBSTRING`, and `REPLACE`

## Files

- `original-submission/lab-05.sql`: original SQL content extracted from the submitted RAR archive
- `reference-material/instructions-05-fa.pdf`: original Persian instruction sheet
- `prompt.md`: concise English summary of the exercise

The SQL content is unchanged. Its filename was normalized for the public archive so that the student number from the submitted archive name is not exposed unnecessarily.

## Submission summary

The submitted script addresses all three tasks:

- It returns the fifth chronologically recorded order for each non-null salesperson using `ROW_NUMBER()`.
- It pivots salesperson sales totals into columns for 2006, 2007, and 2008.
- It creates `dbo.FormatCustomerName`, which looks up a person customer, normalizes name casing and whitespace, adds a prefix, supplies an `unknown` fallback, and removes digits.
- It tests the function with fixed customer IDs and then applies it to customers whose formatted first names begin with `MA`.

## Verification status

The script was reviewed statically as T-SQL for AdventureWorks. It was not executed against a Microsoft SQL Server instance during archival review.

## Known limitations in the historical submission

- Question 1 orders rows only by `OrderDate`. If a salesperson has multiple orders on the same date, the selected fifth row is not deterministic. Adding `SalesOrderID` as a secondary ordering key would resolve the tie.
- Question 2 leaves a yearly value as `NULL` when a salesperson has no sales in that year. The exercise does not explicitly require zero, but a reporting query might normally wrap the pivoted columns with `COALESCE`.
- The function uses an inner join to `Person.Person`. Store customers and nonexistent customer IDs therefore produce the same `Client: unknown` result.
- The fixed customer-ID tests do not explain which ID is expected to exist and which is expected to be absent, so their intent is not self-documenting without the original database contents.
- The final query calls the scalar function once in the result list and again in the `WHERE` clause for each customer. This is correct but can be inefficient on larger datasets.
- `TRIM` requires a sufficiently recent SQL Server engine even though the sample database is named AdventureWorks2012.

Overall, this is one of the more complete database-lab submissions in the archive and demonstrates several useful intermediate T-SQL techniques.
