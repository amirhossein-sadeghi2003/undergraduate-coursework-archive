# TCP Reverse-Shell and HTTP Analysis Coursework

Individual **Computer Networks I** coursework completed in Spring 2024 at Isfahan University of Technology.

## Overview

This project had two parts:

1. a small TCP client/server program in C, designed as a classroom reverse-shell exercise on Ubuntu; and
2. an HTTP traffic analysis exercise using Wireshark.

The repository preserves the submitted coursework as an educational networking exercise. It is not presented as production remote-administration software or as a complete security tool.

## Implemented in the submitted version

### TCP client/server

- IPv4 TCP sockets in C
- A listening server and one connected client at a time
- Command transmission from server to client
- Command execution on the client with `popen()`
- Sending command output back to the server
- Small fixed-size buffers to exercise multi-chunk output handling
- A simple `*` end-of-output marker and `+` continuation signal
- Makefile-based compilation

### HTTP/Wireshark analysis

The submitted report and screenshots cover coursework observations related to:

- basic HTTP request/response traffic
- HTTP status and header fields
- comparison of browser and `curl` traffic
- transfer of a larger HTTP document across multiple TCP segments
- HTTP Basic Authentication and the `Authorization` header
- brief discussion of concurrency models

## Repository structure

```text
.
├── source/
│   ├── client.c
│   ├── server.c
│   └── Makefile
├── report/
│   └── questions.pdf
├── wireshark-screenshots/
│   └── *.png
├── reference-material/
│   └── computer-networks-project-01-fa.pdf
├── original-submission/
│   └── ComputerNetworks_40011643_Project1.tar.gz
├── archival-build-fix.patch
├── prompt.md
└── README.md
```

The original submitted archive is preserved unchanged under `original-submission/`. The other folders provide a browsable copy of the same coursework materials.

## Historical implementation notes

The submitted code reflects the state of the 2024 coursework and has several limitations:

- The assignment specified taking the server port from the command line, while the submitted source hard-codes port `8080`.
- The client hard-codes the server address as `127.0.0.1`, so the submitted version is configured for local testing.
- The implementation accepts one client at a time; the multi-client concurrent server was an optional bonus task and is not included.
- The simple `*` / `+` framing scheme is coursework-level and is not a robust general-purpose application protocol.
- The continuation logic for large command output is not claimed to be fully reliable for arbitrary command output.
- Shell commands are executed through `popen()`, so this code should only be run in a controlled environment that you own and understand.

## Archival build fix

On a current Linux/GCC environment, the historical `server.c` requires the declaration for `inet_ntop()`. The submitted source is preserved unchanged, and the one-line compatibility fix is stored separately in `archival-build-fix.patch`.

From the project directory:

```bash
patch -p1 < archival-build-fix.patch
cd source
make
```

After applying that patch, both programs compiled successfully with the system GCC used during the 2026 archival review.

## Running the historical exercise

After building, start the server and client in separate terminals on a controlled local machine:

```bash
cd source
./server8080
```

and:

```bash
cd source
./client
```

The archived client is configured for `127.0.0.1:8080`.

## Tools and concepts

- C
- Linux / Ubuntu
- TCP sockets
- IPv4
- `popen()`
- Make
- Wireshark
- HTTP
- TCP segmentation and buffering

## Authorship

This was an **individual course project** completed by Amirhossein Sadeghi.

## Archival note

The project was submitted in 2024 and archived to GitHub in 2026 as part of an undergraduate coursework archive. The goal is to preserve the original learning work and document its limitations rather than rewrite it into a modern networking or security tool.
