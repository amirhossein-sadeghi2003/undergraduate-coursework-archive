# Lab 08 — Process management and `exec`

## Contents
Three C sources cover child task creation, polling with `waitpid`, a worker-replacement experiment, and repeated execution/timing of an external `./app`.

## Archival review
All three sources compile with the current GCC. The step-1/2 program calls non-blocking `waitpid` only once per child and can exit before all children are reaped. The step-3 version puts each child in an infinite busy loop, then uses blocking `wait`, so its intended replacement logic does not operate as described. No clean signal-based shutdown is implemented.

`question2.c` expects an external executable named `./app`, which was not included in the submitted ZIP; therefore that exercise is not self-contained.
