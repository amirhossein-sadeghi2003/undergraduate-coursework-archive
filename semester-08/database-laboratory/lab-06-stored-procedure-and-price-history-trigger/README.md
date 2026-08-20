# Lab 06 - Stored Procedure and Price History Trigger

This individual lab uses AdventureWorks to build a parameterized monthly customer-purchase report and a trigger-driven product-price history table.

## Main topics

- Parameterized stored procedures
- Multi-stage reporting with common table expressions
- Monthly customer aggregation
- Window functions for per-group selection
- DML triggers and `inserted`/`deleted` pseudo-tables
- Set-based handling of multi-row updates
- Current-record flags and effective date ranges
- Basic price-history modeling

## Files

- `original-submission/lab-06.sql`: original SQL content extracted from the submitted RAR archive
- `reference-material/instructions-06-fa.pdf`: original Persian instruction sheet
- `prompt.md`: concise English summary of the exercise

The SQL content is unchanged. Its filename was normalized for the public archive.

## Submission summary

The submitted script addresses both tasks:

- `customerpurchasereport` accepts a year and returns monthly customer order counts, total spending, largest order, and a selected favorite product.
- `product_price_history` is populated from `Production.Product` with initial effective dates and current-row flags.
- `trg_update_product_price` closes current history rows and inserts new rows whenever `ListPrice` changes.
- The trigger uses the `inserted` and `deleted` tables and can process multiple changed products in one statement.
- Two sample product-price updates and history queries are included.

## Verification status

The script was reviewed statically as T-SQL for AdventureWorks. It was not executed against a Microsoft SQL Server instance during archival review.

## Known limitations in the historical submission

- The report uses an inner join from `Sales.Customer` to `Person.Person`. Customers represented by stores rather than people are excluded even though the exercise asks for all customers who purchased during the selected year.
- The favorite-product query counts the number of distinct orders containing each product. If the intended definition is the greatest number of units purchased, it should aggregate `SalesOrderDetail.OrderQty` instead.
- The favorite-product tie is resolved arbitrarily by `ROW_NUMBER()`. This is permitted by the exercise, but the selection is not deterministic without a secondary ordering key.
- Filtering with `YEAR(OrderDate) = @year` is clear but non-sargable and can prevent efficient use of an index on `OrderDate`. A bounded date range would scale better.
- The history table has no primary key, foreign key, or uniqueness constraint ensuring at most one current row per product.
- `current_flag` is stored as an unrestricted integer rather than a `bit` or a checked `0`/`1` value.
- The included verification statements directly modify products `1` and `938` in the sample database and do not roll those changes back.
- The history mechanism responds only to list-price updates. Product deletion and standalone name changes are outside its scope.

Overall, this is one of the strongest database-lab submissions in the archive. It demonstrates stored procedures, reporting queries, and a correctly set-based update trigger.
