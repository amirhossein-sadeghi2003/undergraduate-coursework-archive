# Exercise 05 - Row Number, Pivot, and Scalar Function

## Objective

Use AdventureWorks to practice row-number windowing, pivoted yearly aggregates, and a scalar customer-name formatting function.

## Query tasks

1. For each salesperson, return the fifth order by `OrderDate` from `Sales.SalesOrderHeader`. Exclude rows with a null salesperson ID and return the salesperson ID, sales order ID, order date, and `TotalDue`.
2. Return one row per salesperson with the salesperson ID followed by separate sales-total columns for 2006, 2007, and 2008.

## Function task

Create a SQL Server function that:

1. Accepts a customer ID.
2. Retrieves the customer's first and last names.
3. Converts the first name to uppercase and the last name to lowercase.
4. Trims surrounding whitespace and separates the names with one space.
5. Returns a suitable fallback such as `unknown` when no name exists.
6. Prefixes the formatted result with `Client: `.
7. Removes digits from the first or last name.
8. Is tested with an existing customer, a missing customer, and all customers whose first names begin with `ma`.

This file summarizes the original Persian instruction sheet; it is not a replacement for the source handout in `reference-material/`.
