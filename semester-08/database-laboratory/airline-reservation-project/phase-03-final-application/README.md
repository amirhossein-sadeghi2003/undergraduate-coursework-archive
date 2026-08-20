# Phase 3 - Final Airline Application

The final phase combines the airline database with a Python/Tkinter desktop interface.

## Contents

- `application/database.py`: submitted Tkinter GUI and `pyodbc` integration
- `database/create-airline-db.sql`: complete `AirlineDB` creation and sample-data script
- `documentation/er-diagram.pdf`: final relational diagram
- `documentation/final-report-fa.pdf`: submitted Persian report

The original delivery also contained `AirlineDB.bak` and a 10:06 MP4 demonstration. They are intentionally omitted from this public Git archive because the SQL script recreates the database and the video would add approximately 52 MB of binary history.

## Application functions

- Search flights by departure, destination, and date
- Add a ticket while checking flight capacity
- Cancel a reservation
- Display sold-ticket counts, reservation status, and total customer payments
- Display combined ticket information and active reservations

## Running the archived submission

1. Install Microsoft SQL Server and an ODBC driver compatible with `pyodbc`.
2. Run `database/create-airline-db.sql` in SQL Server Management Studio.
3. Install the Python dependency with `python -m pip install -r ../requirements.txt` from this directory, or install `pyodbc` directly.
4. Edit the `server` value in `application/database.py` to match the local SQL Server instance.
5. Run `python application/database.py`.

Tkinter may require a separate operating-system package on some Linux distributions. The submitted connection string targets Windows authentication and the original developer's SQL Server instance.

## Verification and limitations

- `database.py` passes Python syntax compilation.
- The final report and ER diagram render successfully.
- Database operations were not executed during archival review.
- Sample customer records contain plaintext demonstration passwords and must not be treated as a production security design.
