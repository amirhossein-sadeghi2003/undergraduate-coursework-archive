# Labs 04–05 — Character device driver

## Contents
A Linux character-device module registers a dynamic major number and implements `open`, `release`, `read`, and `write`; shell scripts build/load the module and create `/dev/module`; `user.c` exercises the device.

## Archival review
The user-space client compiles with the current GCC. The kernel module was not rebuilt because matching kernel headers are unavailable in the archival environment.

The historical code has important safety/logic issues: the read path writes up to the requested `len` into a 20-byte stack buffer; the write path can copy more than the 100-byte global buffer; and the user program opens the device `O_RDONLY` before attempting a write. Do not load this historical module on a production system without review.
