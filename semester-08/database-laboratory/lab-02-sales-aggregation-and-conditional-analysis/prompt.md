# Exercise 02 - Sales Aggregation and Conditional Analysis

## Objective

Use the AdventureWorks sample database to write aggregate and conditional T-SQL queries, then create and summarize a small constrained table.

## Query tasks

1. List territories whose total sales are below `10,000,000`. Show the territory name and total sales in descending order, and classify totals above `8,500,000` as `High sales` and the rest as `Low sales`.
2. For every customer, show identifying name information, total order count, and total sales. Customers without orders must show zero for both aggregate values.
3. For every product, compare sales in the first and second six-month periods across 2006 and 2007. Label a falling second-half result as `Decreased`; otherwise label it `Increased`. Include the product ID and product name.
4. Create a table containing a primary-key person ID and an occupation restricted to `Student`, `Teacher`, or `Manager`. Insert sample data and return one row with separate columns containing the count of each occupation.

This file summarizes the original Persian instruction sheet; it is not a replacement for the source handout in `reference-material/`.
