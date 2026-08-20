# Exercise 08 - Transactions, Isolation, and Deadlocks

## Part 1 - Transaction management

1. Begin a transaction on `Person.Person`.
2. Change the first names for business entities 1 and 2 to `John` and `Jane`.
3. Create a savepoint.
4. Change the same names to `Michael` and `Emily`.
5. Roll back to the savepoint and verify that `John` and `Jane` are restored.
6. Commit the transaction.

## Part 2 - Isolation and locks

1. Set Session 1 to `REPEATABLE READ`.
2. Begin a transaction and select every `Sales.SalesOrderDetail` row with product ID 950, leaving the transaction open.
3. In Session 2, attempt to update or delete a matching record and observe blocking.
4. Commit Session 1 and retry or complete the Session 2 operation.

## Part 3 - Deadlock

1. In Transaction 1, update Product 1 and then SalesOrderHeader 43659.
2. In Transaction 2, update SalesOrderHeader 43659 and then Product 1.
3. Run both transactions concurrently so that they acquire the resources in opposite order and create a deadlock.

This file summarizes the original Persian instruction sheet; it is not a replacement for the source handout in `reference-material/`.
