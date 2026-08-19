# Assignment summary

1. Handle `SIGSEGV`, report the faulting address, and deliberately trigger a segmentation fault without calling `kill`.
2. Exchange structured player-score data through POSIX shared memory. The exercise progresses from a basic updater/viewer pair to periodic updates signaled with `SIGUSR1`, and finally to a multi-process updater that distributes array elements among children before notifying the viewer.

The original Persian assignment PDF is preserved in `reference-material/`.
