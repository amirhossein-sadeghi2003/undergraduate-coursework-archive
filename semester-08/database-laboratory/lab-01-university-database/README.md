# Lab 01 - University Database Schema and Prerequisite Queries

This lab extends a small university database in Microsoft SQL Server. It adds course offerings, completed courses, and prerequisite relationships, then uses the resulting schema for several update and retrieval queries.

**Work type:** Individual

## Main topics

- T-SQL data definition and data manipulation
- Primary keys, foreign keys, defaults, and `CHECK` constraints
- Multi-row inserts
- Joins and correlated subqueries
- Self-joins for two-level prerequisite relationships
- Conditional `UPDATE` statements

## Files

- `original-submission/lab-01.sql`: original submitted SQL script
- `reference-material/exercise-01-fa.pdf`: original Persian exercise sheet
- `prompt.md`: concise English summary of the exercise

## Submission summary

The submitted script:

- Recreates the university tables and their relationships.
- Adds a passed-credit field to the student table.
- Inserts sample departments, teachers, students, courses, offerings, completed courses, and prerequisites.
- Finds two-level prerequisite relationships.
- Lists courses associated with a selected teacher.
- Increases grades for students associated with that teacher's courses.
- Attempts to identify students who completed a course without completing its prerequisite.

## Verification status

The script was reviewed statically as T-SQL. It was not executed against a Microsoft SQL Server instance during archival review.

## Known limitations in the historical submission

The original submission is preserved without modification. The following limitations were found during archival review:

- The table name `prerequistes` is misspelled consistently.
- `available_courses` omits the `ID` field shown in the exercise and defines no primary key.
- `students.advisor_id` references `departments(id)` rather than a teacher or advisor record.
- The exercise specifies teacher ID `36745`, while the sample data and queries use teacher ID `1`.
- The grade update matches only `course_id`. It does not also match the semester and year of the teacher's offering, so it can update unrelated instances of the same course.
- The prerequisite-violation query does not check whether either course was passed according to a grade threshold and can return duplicate student numbers.
- `pass_credit` is stored manually and is not calculated or kept synchronized with passed courses.
- The sample data records course `3` as taken in fall 1400, although its only available offering is inserted for fall 1404.
- Several useful domain constraints are absent, including valid grade and non-negative credit ranges.

These issues make the lab most useful as evidence of early database coursework and learning progression rather than as a standalone portfolio project.
