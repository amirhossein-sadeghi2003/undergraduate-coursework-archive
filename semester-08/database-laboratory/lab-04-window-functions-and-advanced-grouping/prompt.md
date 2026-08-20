# Exercise 04 - Window Functions and Advanced Grouping

## Objective

Use AdventureWorks sales data to solve analytical queries with aggregates, window functions, ranking, running totals, and subtotal grouping.

## Query tasks

1. Calculate total sales for each product subcategory and its percentage contribution to the corresponding product-category sales. Include only categories and subcategories whose sales exceed `100,000`.
2. Find sales orders whose total is greater than the average order total for the relevant salesperson in the same sales territory and less than or equal to the maximum order total across all territories.
3. For every sales order, calculate the running total of `TotalDue` for orders recorded by the same salesperson. Use different window-frame methods and compare their results.
4. Rank each product by `ListPrice` within its product subcategory and calculate its percentage rank in the same subcategory using windowing and partitioning.
5. Group sales totals by `TerritoryID` and `SalesPersonID`, include the corresponding subtotals, and filter results associated with territories whose total sales are below `1,000,000`.

This file summarizes the original Persian instruction sheet; it is not a replacement for the source handout in `reference-material/`.
