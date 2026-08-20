# Airline Reservation Database Project

This three-person Database Laboratory project implements an airline-reservation system with Microsoft SQL Server and a Python/Tkinter desktop interface. It was developed in three phases during the Spring 1403-1404 academic term.

## Scope evolution

Phase 1 proposed an Alibaba-like travel platform covering airline tickets, train tickets, and hotels. The instructor later asked the team to reduce the project scope. From Phase 2 onward, the design focuses only on airline reservations. This explains why early material uses the `Ali Baba` label while the implemented database and application use `AirlineDB`.

## Phase index

| Phase | Deliverables | Outcome |
| --- | --- | --- |
| [Phase 1 - Proposal](phase-01-proposal/) | Assignment brief and public proposal summary | Broad travel-booking concept with flights, trains, hotels, reservations, and payments |
| [Phase 2 - Database Design](phase-02-database-design/) | T-SQL schema and ER diagram | Reduced airline-only schema with sample data and SQL Server programmability objects |
| [Phase 3 - Final Application](phase-03-final-application/) | Final SQL script, Python GUI, ER diagram, and Persian report | Runnable desktop front end for flight search, ticket creation, reservation cancellation, and reporting |

## Implemented components

- 8 tables: airlines, airports, customers, flights, tickets, reservations, payments, and reservation logs
- 4 views for flight tickets, ticket details, flight availability, and active reservations
- 3 scalar functions for ticket counts, reservation status, and customer payments
- 3 stored procedures for flight search, ticket creation, and reservation cancellation
- 3 triggers for ticket-price validation, reservation logging, and controlled view insertion
- Tkinter interface connected to SQL Server through `pyodbc`

## Team attribution

- **Work type:** Collaborative, three-person project
- **Original group label:** MSS
- **Individual contribution:** Not documented in the supplied deliverables

This archive therefore presents the work as a team project and does not imply sole authorship.

## Public archive decisions

- The Phase 1 report named all group members. Its technical content is summarized in Markdown instead of republishing teammates' names.
- The final `AirlineDB.bak` file is omitted because the database can be recreated from the SQL script.
- The original 10:06 demonstration video is omitted to avoid adding approximately 52 MB of binary history to the Git repository.
- Historical source files are otherwise retained without silently correcting their logic.

## Verification

- The Python source passes `python -m py_compile`.
- All included PDFs were rendered and visually inspected.
- ZIP archives and source files were inspected statically.
- SQL Server execution was not available in the archival environment, so the T-SQL behavior was not tested against a live server.

## Main limitations

- The application hardcodes the original Windows SQL Server instance name and uses a trusted connection; this must be changed for another computer.
- Customer passwords and contact details are demonstration data stored as plaintext. The design is educational and not suitable for production use.
- The GUI performs database operations synchronously and has no automated tests.
- Several T-SQL objects assume simple single-row workflows rather than production-grade concurrency and validation.
