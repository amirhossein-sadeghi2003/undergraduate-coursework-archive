# Raw Packet Sniffer and Ethernet/IP Header Analysis

Second project for **Computer Networks I**, completed in Spring 2024 at Isfahan University of Technology.

## Overview

This two-person coursework project explores low-level packet capture and protocol-header inspection on Linux. The work begins with `tcpdump` observations and then implements three small C programs that receive raw Ethernet frames directly through Linux packet sockets.

The submitted programs progressively inspect packet direction/type, Ethernet protocol identifiers, and selected IPv4 header fields. The accompanying report answers the assignment questions on ARP observations, socket address structures, byte order, protocol numbers, and C bit fields.

## Implemented in the submitted version

### `dllsniffer.c`

- opens a Linux `PF_PACKET` / `SOCK_RAW` socket
- receives Ethernet frames with `recvfrom()`
- labels packets as incoming, outgoing, broadcast, multicast, or other
- prints captured packet bytes in hexadecimal

### `dllsniffer2.c`

Extends the first program by:

- interpreting the Ethernet header
- identifying IPv4 and ARP frames from the EtherType field
- retaining packet-direction/type reporting
- printing the complete captured frame in hexadecimal

### `dllsniffer_pro.c`

Further extends the packet inspection by:

- parsing the Ethernet header
- recognizing IPv4 and ARP
- parsing an IPv4 header when present
- printing IPv4 header length
- printing total IPv4 packet length
- printing the upper-layer protocol number
- classifying packet direction/type
- printing the raw frame in hexadecimal

## Technologies and concepts

- C
- Linux / Ubuntu
- raw packet sockets
- `PF_PACKET`
- `SOCK_RAW`
- Ethernet frames
- EtherType
- ARP
- IPv4 headers
- `recvfrom()`
- network/host byte order
- `htons()` / `ntohs()`
- `tcpdump`

## Repository structure

```text
.
├── source/
│   ├── dllsniffer.c
│   ├── dllsniffer2.c
│   ├── dllsniffer_pro.c
│   └── Makefile.txt
├── report/
│   └── computer-networks-project-02-report.pdf
├── reference-material/
│   └── computer-networks-project-02-fa.pdf
├── original-submission/
│   └── ComputerNetworks_40011643_Project2.zip
├── prompt.md
├── .gitignore
└── README.md
```

The original course ZIP is preserved unchanged in `original-submission/`. The files under `source/` are copied from that submission for easier browsing.

## Historical build check

During the 2026 archival review, all three C source files compiled individually with the system GCC:

```bash
gcc dllsniffer.c -o dllsniffer
gcc dllsniffer2.c -o dllsniffer2
gcc dllsniffer_pro.c -o dllsniffer_pro
```

`dllsniffer.c` produced a compiler warning because the final `recvfrom()` length argument is stored in an `int` rather than `socklen_t`; the program still compiled successfully. The historical source is preserved unchanged.

The submitted build file is named `Makefile.txt`. Its targets compile the three programs separately, and its historical `clean` target refers to output names that do not match the compiled binaries. It is retained as submitted rather than silently rewritten.

## Running the programs

These programs use Linux raw packet sockets and normally require elevated privileges. Run them only on a system and network where you have authorization to capture traffic.

For example:

```bash
cd source
gcc dllsniffer2.c -o dllsniffer2
sudo ./dllsniffer2
```

The programs continuously capture traffic until interrupted.

## Known limitations

- Linux-specific packet-socket APIs are used.
- The programs capture from the packet socket without a user-facing interface selector.
- No BPF-style capture filter is implemented inside the C programs.
- Captured frames are printed directly to standard output and are not saved to a capture file.
- The programs are educational packet inspectors, not replacements for Wireshark or `tcpdump`.
- The submitted report and code are preserved as historical coursework and were not rewritten into a production packet-analysis tool.

## Team

This was a two-person course project completed by:

- Amirhossein Sadeghi
- Alireza Moghareh Abed

Both members contributed equally and worked across the project rather than owning separate modules.

## Archival note

The project was submitted in 2024 and archived to GitHub in 2026 as part of an undergraduate coursework archive. The goal is to preserve the original learning work while documenting its behavior and limitations clearly.
