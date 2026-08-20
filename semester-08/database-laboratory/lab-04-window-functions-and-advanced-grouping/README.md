# Lab 04 - Window Functions and Advanced Grouping

This individual lab uses AdventureWorks sales data to practice analytical T-SQL, including window functions, running totals, ranking, percentage rank, and grouping sets.

## Main topics

- Common table expressions
- Aggregate window functions
- `PARTITION BY` and ordered window frames
- `ROWS` compared with `RANGE`
- `DENSE_RANK` and `PERCENT_RANK`
- `GROUPING SETS`
- Aggregate filtering with `HAVING`

## Files

- `original-submission/lab-04.sql`: original SQL content extracted from the submitted RAR archive
- `reference-material/instructions-04-fa.pdf`: original Persian instruction sheet
- `prompt.md`: concise English summary of the exercise

The SQL content is unchanged. Its filename was normalized for the public archive so that the student number from the submitted archive name is not exposed unnecessarily.

## Submission summary

The submitted script contains responses for Questions 2 through 5:

- A CTE and windowed average used to filter sales orders.
- Two running-total queries comparing `ROWS` and `RANGE` frames.
- Product price ranking and percentage rank within each subcategory.
- Two approaches to sales summaries using `GROUPING SETS` and `UNION`.

Question 1, which requests product-subcategory sales and contribution percentages within product categories, is absent from the submitted file.

## Verification status

The script was reviewed statically as T-SQL for AdventureWorks. It was not executed against a Microsoft SQL Server instance during archival review.

## Known limitations in the historical submission

- Question 1 is missing entirely.
- Question 2 labels its windowed value as an average per salesperson, but partitions only by `TerritoryID`. It therefore computes the average order total for the territory rather than for each salesperson within that territory.
- Question 2 does not return or use `SalesPersonID`, even though the requested comparison refers to each salesperson.
- The upper bound in Question 2 uses the maximum individual `TotalDue` across all orders. Every order is necessarily less than or equal to that global maximum, so this condition does not further restrict the result.
- Question 3 groups all rows with a `NULL` `SalesPersonID` into one running-total partition even though those rows are not associated with a salesperson.
- The `ROWS` and `RANGE` versions in Question 3 order by the unique `SalesOrderID`. Because there are no peer rows for that ordering key, the two methods normally produce identical results and do not demonstrate their practical difference.
- Question 4 uses `DENSE_RANK()` instead of the explicitly requested `RANK()`. These functions behave differently when multiple products have the same list price.
- Question 5 uses `GROUPING SETS (TerritoryID, SalesPersonID)`, which produces separate territory and salesperson subtotals but omits the required detailed grouping by the pair `(TerritoryID, SalesPersonID)`.
- The manual `UNION` version in Question 5 has the same omission and also uses `UNION` rather than `UNION ALL`, allowing accidental removal of equal aggregate rows.
- The `HAVING` condition in Question 5 is applied independently to salesperson totals as well as territory totals. It does not consistently enforce the requirement that the containing territory's total sales be below `1,000,000`.

The lab covers useful intermediate analytical-SQL concepts, but the incomplete first question and grouping errors should remain visible in the archive.
