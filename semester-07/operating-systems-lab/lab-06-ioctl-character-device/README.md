# Lab 06 — `ioctl` character device

## Contents
The submission extends a character device with `ioctl` operations for mute, unmute, set volume, and get volume. It also uses `kmalloc` for read buffers and includes a user-space exercise plus build/teardown scripts.

## Archival review
`user.c` compiles with the current GCC. The kernel module was not rebuilt because matching kernel headers are unavailable in the archival environment. Editor-specific `.vscode` files are omitted from the browsable copy but remain inside the preserved original ZIP.

Known issues include an unchecked write length into the 1024-byte kernel buffer, no guaranteed NUL terminator before printing the buffer with `%s`, and user-space printing random read bytes as C strings without guaranteed termination.
