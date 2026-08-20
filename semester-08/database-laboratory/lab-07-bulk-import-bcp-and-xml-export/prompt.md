# Exercise 07 - Bulk Import, BCP, and XML Export

## Part 1 - Import new products

1. Create a `TempProducts` table with product ID, name, product number, and list price.
2. Import `NewProductData.csv` into the table with `BULK INSERT`.
3. Create a similar `NewProducts` table.
4. Transfer only imported products that do not already exist in `NewProducts`.

## Part 2 - Export and re-import monthly sales

1. Use BCP to export product ID, sales order ID, order quantity, unit price, and order date for a selected month such as July 2008.
2. Save the result as a CSV file.
3. Import the extracted data into `TempSalesData` using `OPENROWSET`.
4. Ensure the resulting table contains only records from the selected month.

## Part 3 - XML-formatted product report

1. Return every product name together with order count, first order date, and total sales.
2. Format the three aggregate fields as XML while leaving the product name as a normal column.
3. Use `xp_cmdshell` to save the query result to a text file.

This file summarizes the original Persian instruction sheet; it is not a replacement for the source handout and input CSV in `reference-material/`.
