# Lab 08 - Transactions, Isolation, and Deadlocks

This individual lab explores SQL Server transaction control, savepoints, repeatable-read locking, blocking across sessions, and deliberate deadlock creation through conflicting lock order.

## Main topics

- Explicit and named transactions
- Savepoints and partial rollback
- Transaction commit behavior
- `REPEATABLE READ` isolation
- Shared and exclusive lock interaction
- Multi-session blocking
- Deadlock construction with opposite resource order
- Timing coordination with `WAITFOR DELAY`

## Files

- `original-submission/session-1.sql`: transaction, savepoint, locking, and first deadlock-session script
- `original-submission/session-2.sql`: blocking update and second deadlock-session script
- `reference-material/instructions-08-fa.pdf`: original Persian instruction sheet
- `prompt.md`: concise English summary of the exercise

The submitted SQL content is unchanged. Archive directories and filenames containing the student number were normalized for the public repository.

## Submission summary

The two submitted scripts address all three exercises:

- A named transaction updates two people, creates a savepoint, performs additional updates, rolls back to the savepoint, verifies the restored intermediate values, and commits.
- Session 1 sets `REPEATABLE READ`, selects rows for product `950`, and includes a later commit.
- Session 2 updates rows for product `950`, allowing the blocking behavior to be observed when Session 1 remains open.
- The deadlock scripts update the same Product and SalesOrderHeader rows in opposite order, with a delay between updates to make concurrent lock overlap likely.

## Verification status

The scripts were reviewed statically as SQL Server T-SQL. They were not executed concurrently against AdventureWorks, so actual blocking duration, lock state, and deadlock-victim selection were not captured during archival review.

## Known limitations in the historical submission

- The Session 1 isolation script includes `COMMIT` immediately after the `SELECT`. If the entire file is executed as one batch, the transaction may finish before Session 2 can be used to observe blocking. The exercise therefore requires staged or line-by-line execution.
- Session 2 updates every `SalesOrderDetail` row with `ProductID = 950`, while the instruction asks to update or delete one record. This creates broader and persistent sample-data changes than necessary.
- The blocking example does not include a final verification query or a restoration step after Session 2 succeeds.
- `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ` remains active for that connection until changed again; the script does not restore `READ COMMITTED` afterward.
- Question 1 permanently commits the names `John` and `Jane` for business entities 1 and 2, as requested, but does not restore the original AdventureWorks values after demonstrating the savepoint.
- The deadlock scripts depend on both sessions reaching their first update before the delay ends. `WAITFOR` improves the likelihood but still requires manual concurrent execution.
- No `TRY...CATCH` block records which transaction SQL Server selects as the deadlock victim.
- The deadlock tests commit any surviving updates and do not restore the modified Product and SalesOrderHeader values.

Overall, this is a strong database-systems lab. It demonstrates concurrency behavior that cannot be represented by ordinary single-query coursework.
