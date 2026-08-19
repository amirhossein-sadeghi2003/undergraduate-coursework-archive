# Lab 03 — File system calls and a static library

## Contents
A command-line C program links against a student-created static library implementing file creation, access checks, metadata display, and indexed file creation.

## Archival review
The submitted Makefile builds successfully with the current GCC. Important historical logic issues remain: `showFileInfo()` reads an uninitialized `struct stat` because `stat()` is never called; `checkFile()` has a non-void return type but no return statement; and file creation does not use `O_TRUNC`, so an existing file is not fully replaced as requested.

The original source is intentionally preserved unchanged.
