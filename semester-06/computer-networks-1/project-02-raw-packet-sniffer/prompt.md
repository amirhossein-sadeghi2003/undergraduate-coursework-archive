# Assignment Summary — Computer Networks I Project 02

The original Persian assignment is preserved in `reference-material/computer-networks-project-02-fa.pdf`.

## Part 1 — `tcpdump`

Use `tcpdump` to inspect network traffic, construct protocol filters, and answer questions involving non-IP traffic, ARP-table changes, and observations made while connecting through a mobile hotspot.

## Part 2 — Direct packet capture in C

Use Linux packet sockets to receive Ethernet frames directly from the network interface.

### Program 1 — `dllsniffer.c`

Write a C program that:

- receives raw Ethernet packets;
- prints packet contents in hexadecimal; and
- identifies packet type/direction such as incoming, outgoing, broadcast, or multicast.

### Program 2 — `dllsniffer2.c`

Extend the first program so that it also identifies the higher-layer protocol from the Ethernet header, including IPv4 and ARP.

### Program 3 — `dllsniffer_pro.c`

Extend the second program so that, for IPv4 packets, it also prints:

- IPv4 header length;
- total IPv4 packet length; and
- the protocol number carried above IP.

## Written questions

The report also addresses topics including:

- `sockaddr` and `sockaddr_ll`;
- ARP and MAC-address observations;
- network-to-host byte-order conversion;
- upper-layer IP protocol numbers;
- compile-time byte-order handling; and
- C bit fields in the IPv4 header structure.

The required submission consisted of a PDF report plus the three C source files and a Makefile.
