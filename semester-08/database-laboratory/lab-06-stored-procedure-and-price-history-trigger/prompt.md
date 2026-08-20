# Exercise 06 - Stored Procedure and Price History Trigger

## Part 1 - Monthly customer purchase report

Create a stored procedure for AdventureWorks that:

1. Accepts a year such as `2008`.
2. Returns every customer who purchased during that year, including the customer's first and last name and one row per month containing orders.
3. Reports the monthly order count, total spending, largest order, and favorite product for each customer.
4. May choose any tied product when several products are equally favored.
5. Sorts the final output by month number and customer ID.

## Part 2 - Product price history

1. Create a `ProductsPriceHistory` table containing product ID, name, list price, start date, end date, and a current-row flag.
2. Initially copy every product from `Production.Product`, using `ModifiedDate` as the start date, leaving the end date empty, and setting the current flag to `1`.
3. Create a trigger that reacts to product-price changes.
4. When a price changes, close the previous history row with an end date and current flag `0`, then insert a new current row containing the updated price.

This file summarizes the original Persian instruction sheet; it is not a replacement for the source handout in `reference-material/`.
