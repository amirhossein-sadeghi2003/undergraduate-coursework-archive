# Lab 09 — Pipes and IPC

## Contents
- `factorial.c`: five child processes compute partial products and send them through one unnamed pipe.
- `my_server.c` / `my_client.c`: temperature IPC over one named FIFO.

## Archival review
All three sources compile with the current GCC. A test with input 20 produced `2432902008176640000`, the correct value for 20!. The repeated input prompt seen when stdout is piped is a classic pre-`fork()` stdio-buffer duplication effect.

The factorial parent does not explicitly `wait` for/reap the children. The FIFO design uses the same stream in both directions and every participant opens it `O_RDWR`; with multiple clients this can race or route a response to the wrong reader. The client also sleeps one second before reading and three seconds after reading, so its full cycle exceeds the requested three-second update interval.
