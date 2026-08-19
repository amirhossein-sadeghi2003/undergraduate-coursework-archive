# Lab 10 — Signals and shared memory

## Contents
The submission progresses from a `SIGSEGV` handler to POSIX shared-memory score updater/viewer pairs. Versions 2 and 3 add `SIGUSR1`; version 3 additionally forks child processes and splits player updates among them.

## Archival review
With default GCC, all shared-memory updater/viewer sources compile. Version 1 was run successfully, and short version-2/version-3 tests showed repeated updater → `SIGUSR1` → viewer refresh cycles.

`question1.c` does not compile as submitted because the `sa_sigaction` handler has the wrong function signature and `SA_SIGINFO` is not enabled. A minimal archival patch is included separately. Even with that patch, doing `printf`/`exit` directly inside a signal handler is not production-quality signal handling. Versions 2/3 similarly perform non-async-signal-safe work inside the `SIGUSR1` handler.
