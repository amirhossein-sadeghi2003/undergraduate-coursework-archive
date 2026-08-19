# Lab 07 — Custom process-information system call

## Contents
- `sadeghi.c`: custom syscall implementation using `task_struct`, `find_vpid`, `pid_task`, `get_task_comm`, and `copy_to_user`.
- `init.c`: user-space caller using hard-coded syscall number 548.

## Archival review
The user-space source compiles with the current GCC in its default GNU mode. The custom syscall cannot be tested without the corresponding modified kernel and syscall-table integration files, which are not present in the submission.

The caller does not check the syscall return value, so an invalid PID can lead to printing uninitialized data. State classification is simplified to running/sleeping/unknown, and syscall number 548 is kernel-specific.

The supplied assignment PDF has an internal session/year mismatch; see `prompt.md`.
