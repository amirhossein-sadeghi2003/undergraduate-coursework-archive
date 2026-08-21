# Lab 06 - Secure Switching, DHCP, and Spoofing Analysis

This lab combined secure Layer 2/Layer 3 configuration with DHCP service, SSH management restrictions, and controlled analysis of common network attacks.

## Included artifacts

- `sanitized-submission/report-fa.pdf`: Persian lab report with the student ID removed.
- `sanitized-submission/session-06.pkt`: Packet Tracer topology.
- `reference-material/`: original Persian instruction and pre-lab PDFs.

## Review notes

The Packet Tracer portion covers VLANs, EtherChannel, unused-port isolation, inter-VLAN routing, DHCP pools, SSH, and VTY access control. DHCP starvation was intentionally not executed on a live network because no isolated interface was available. The report instead records the safety assessment. A limited ICMP source-spoofing demonstration was captured with `hping3` and `tcpdump`.

