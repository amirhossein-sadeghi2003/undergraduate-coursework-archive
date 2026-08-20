# Database Laboratory

This directory archives eight individual Microsoft SQL Server laboratory exercises completed as undergraduate coursework. The labs use T-SQL and the AdventureWorks sample database to progress from schema design and aggregate queries to stored procedures, triggers, data transfer, transaction isolation, and deadlocks.

## Course scope

- **Work type:** Individual
- **Database platform:** Microsoft SQL Server
- **Primary language:** T-SQL
- **Main sample database:** AdventureWorks / AdventureWorks2012
- **Laboratory count:** 8

## Laboratory index

| Lab | Main focus | Archival assessment |
| --- | --- | --- |
| [Lab 01](lab-01-university-database/) | Schema extension, constraints, prerequisites, joins, and updates | Foundational submission with several schema and query limitations |
| [Lab 02](lab-02-sales-aggregation-and-conditional-analysis/) | Aggregates, `CASE`, outer joins, and conditional sales analysis | Complete question coverage, but customer and product-sales logic contain material errors |
| [Lab 03](lab-03-sql-server-security-and-role-management/) | Logins, users, roles, permissions, views, `GRANT`, and `DENY` | Useful security topic with incomplete permission modeling; public SQL is sanitized |
| [Lab 04](lab-04-window-functions-and-advanced-grouping/) | Running totals, window frames, ranking, and grouping sets | Intermediate analytical SQL; Question 1 is missing and subtotal grouping is incomplete |
| [Lab 05](lab-05-row-number-pivot-and-scalar-function/) | `ROW_NUMBER`, `PIVOT`, scalar functions, and string cleanup | One of the more complete submissions, with mostly minor correctness and performance limitations |
| [Lab 06](lab-06-stored-procedure-and-price-history-trigger/) | Stored procedures, monthly reporting, triggers, and price history | Strong set-based work and one of the best submissions in the course archive |
| [Lab 07](lab-07-bulk-import-bcp-and-xml-export/) | `BULK INSERT`, BCP, `OPENROWSET`, XML, and `xp_cmdshell` | Advanced data-transfer topic, but the submitted script is not a working end-to-end pipeline |
| [Lab 08](lab-08-transactions-isolation-and-deadlocks/) | Savepoints, isolation levels, blocking, and deadlocks | Strong systems-oriented lab that requires staged, concurrent SQL Server sessions |

## Directory convention

Each lab contains:

- `README.md` with the scope, verification status, and known limitations
- `prompt.md` with a concise English summary of the original exercise
- `reference-material/` with the original Persian instruction sheet and any instructor-provided input data
- `original-submission/` with preserved student work, when safe to publish

Lab 03 uses `sanitized-submission/` because the submitted SQL contained a plaintext login password.

## Archival approach

Historical SQL is preserved rather than silently corrected. Public filenames were normalized and student-number identifiers were removed from archive paths. Each lab README documents missing work, incorrect assumptions, portability problems, and unverified behavior.

The SQL was reviewed statically because the archival environment did not contain a configured Microsoft SQL Server instance with AdventureWorks. PDF handouts were rendered and inspected. The Lab 07 sales CSV was also structurally checked: it contains 2,209 five-field rows dated in July 2008.

## Security notes

- The raw Lab 03 archive is excluded because it contains a weak plaintext SQL login password. The published copy changes only the password literal to a clear placeholder.
- Lab 07 enables `xp_cmdshell` because the exercise explicitly requests it. This script should not be run on a production server without strict controls, path review, and cleanup.
- Several historical scripts modify AdventureWorks sample data and do not restore the original values. Review each lab README before execution.

## Portfolio use

This course is best represented as one aggregate database-laboratory entry rather than eight separate projects. Labs 05, 06, and 08 provide the strongest evidence of practical T-SQL work. The remaining labs are retained to preserve the full learning progression and original coursework record.
