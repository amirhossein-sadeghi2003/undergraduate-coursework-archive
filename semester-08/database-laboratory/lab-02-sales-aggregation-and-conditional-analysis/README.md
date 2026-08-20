# Lab 02 - Sales Aggregation and Conditional Analysis

This individual lab uses the Microsoft AdventureWorks sample database to analyze territory, customer, and product sales. It also creates a small constrained table and summarizes its records with conditional aggregation.

## Main topics

- T-SQL aggregate functions
- `GROUP BY`, `HAVING`, and ordering aggregated results
- Conditional output with `CASE`
- Outer joins and zero-value handling
- Date filtering and conditional aggregation
- Table creation, primary keys, and `CHECK` constraints
- Conditional counting

## Files

- `original-submission/lab-02.sql`: original SQL content extracted from the submitted RAR archive
- `reference-material/instructions-02-fa.pdf`: original Persian instruction sheet
- `prompt.md`: concise English summary of the exercise

The extracted SQL content is unchanged. Its filename was normalized for the public archive so that the student number from the submitted archive name is not exposed unnecessarily.

## Submission summary

The submitted script contains all four requested sections:

- Territory sales totals below a specified limit, sorted in descending order and classified as high or low sales.
- Customer order counts and sales totals, including customers without orders.
- A product sales-trend query based on the first and second halves of 2006 and 2007.
- A constrained occupation table and a one-row summary of teacher, manager, and student counts.

## Verification status

The script was reviewed statically as T-SQL for the AdventureWorks schema. It was not executed against Microsoft SQL Server with an AdventureWorks database during archival review.

## Known limitations in the historical submission

The original SQL is preserved without modification. The following issues were found during archival review:

- Query 1 classifies a total of exactly `8,500,000` as `High sales`, while the instruction says the total must be greater than that threshold.
- Query 2 joins `Sales.Customer.CustomerID` directly to `Person.Person.BusinessEntityID`. In AdventureWorks, person customers should normally be joined through `Sales.Customer.PersonID`, so customer names can be incorrect or missing.
- Query 3 treats months 1 through 5 as the first half and months 6 through 12 as the second half. A six-month split should use months 1 through 6 and 7 through 12.
- Query 3 sums `SalesOrderHeader.TotalDue` after joining to order details. This repeats an entire order total for every detail row and does not measure each product's own line sales.
- Query 3 evaluates 2006 and 2007 in sequential `WHEN` branches, so an increase in either branch can determine one combined label rather than performing a consistent comparison across the requested period.
- Query 3 does not convert missing half-year totals to zero, which can cause `NULL` comparisons to fall into the `decreased` result.
- The occupation column in Query 4 is nullable. SQL Server `CHECK` constraints do not reject `NULL`, so `NOT NULL` would be needed to enforce exactly the three stated occupations.

This lab is useful as an early example of aggregate queries and analytical SQL, but its historical limitations should remain visible in the archive.
