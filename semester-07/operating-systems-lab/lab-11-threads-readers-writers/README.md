# Lab 11 — Threads and readers–writers synchronization

## Contents
- Question 1 computes an array dot product with POSIX threads and protects the shared accumulator with a semaphore.
- Question 2 implements a readers-preference readers–writers scheme using processes, anonymous shared memory, and process-shared semaphores. Student report/screenshots are retained in the submission.

## Archival review
Question 1 compiles with `-pthread`; a test with `[1,2,3,4,5] · [5,4,3,2,1]` produced 35. Question 2 compiles in GNU C mode and a short run with two readers and one writer showed shared-state updates and concurrent reads.

Known limitations include hard-coded four threads, GNU `void *` pointer arithmetic in the shared-memory layout, no graceful shutdown for the infinite readers/writers loops, overlapping numeric IDs for reader/writer roles, and unreachable cleanup after the parent waits forever.
