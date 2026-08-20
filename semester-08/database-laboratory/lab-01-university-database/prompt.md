# Exercise 01 - University Database Extension

## Objective

Extend an existing university database and write queries over course offerings, completed courses, and prerequisite relationships.

## Schema tasks

1. Add a field to `Students` for the number of credits completed by each student.
2. Add the following entities and select appropriate primary keys, foreign keys, and other constraints:
   - `Courses`
   - `Available_Courses`
   - `Taken_Courses`
   - `Prerequisites`
3. Restrict `Available_Courses.Semester` to `spring` or `fall`.
4. Insert sample records into every table.

## Query tasks

1. Return the student numbers of students who completed a course without completing its prerequisite.
2. Return prerequisite relationships separated by two levels. For example, if `x` is a prerequisite of `y` and `y` is a prerequisite of `z`, return `x` and `z`.
3. Add one point to the relevant course grade for every student who completed a course taught by teacher `36745`.
4. List all courses taught by teacher `36745`.

This file summarizes the original Persian exercise sheet; it is not a replacement for the source handout in `reference-material/`.
