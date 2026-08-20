# Phase 2 - Database Design

This phase turns the reduced airline-reservation scope into a Microsoft SQL Server schema. Although the submitted SQL filename still referenced `Ali Baba`, its implemented entities are airline-specific.

## Contents

- `original-submission/airline-schema.sql`: schema, sample data, queries, triggers, views, functions, and stored procedures
- `original-submission/er-diagram.pdf`: submitted SQL Server database diagram

## Technical coverage

- Primary keys, foreign keys, unique constraints, and check constraints
- Airlines, airports, customers, flights, tickets, reservations, payments, and reservation logs
- Sample inserts and join queries
- Triggers for price handling, reservation logging, and inserts through a view
- Scalar functions and stored procedures for common reservation workflows

## Verification notes

The PDF was rendered successfully and the SQL was reviewed statically. The script was not executed against a live Microsoft SQL Server instance during archival review.
