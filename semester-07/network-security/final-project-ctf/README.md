# Network Security CTF Coursework

Individual **Network Security** final project completed at Isfahan University of Technology in the 2024-2025 academic year.

## Overview

This project was an **authorized university Capture The Flag (CTF)** exercise hosted on the MAZAPA training infrastructure.

The assignment provided several security challenges covering initial access, lateral movement, and privilege escalation. Full credit required solving the mandatory Sanity Check plus four of the six main challenges and submitting short write-ups describing the solution process.

The submitted coursework contains write-ups for:

- Sanity Check
- Website - Initial Access
- Mail Server - Initial Access
- VPN Server - Initial Access
- PC3 - Lateral Movement

The public GitHub archive intentionally summarizes the work instead of publishing the original write-up PDFs verbatim, because those files contain CTF flags, internal lab IP addresses, challenge-specific credentials, and other environment-specific details.

## Practical work represented in the submission

Across the completed challenges, the coursework documents hands-on use of:

- Linux command-line tooling
- HTTP request inspection and manipulation
- hidden-path and application-file discovery
- SQLite inspection
- PHP type-juggling behavior
- Zimbra service identification
- Metasploit in an authorized lab
- remote shell access in the CTF environment
- SSH key-based access
- Base64 decoding and file transfer
- password-hash extraction
- John the Ripper
- OpenVPN configuration and access
- ShellShock exploitation in the lab
- reverse shells
- lateral movement between CTF hosts
- service restart / application behavior analysis

## Challenge summaries

Public, sanitized summaries of the submitted work are available under `writeups/`:

```text
writeups/
├── sanity-check.md
├── website-initial-access.md
├── mail-server-initial-access.md
├── vpn-server-initial-access.md
└── pc3-lateral-movement.md
```

These summaries remove flags, exact internal addresses, recovered passwords, public-key material, and challenge-specific secrets while preserving the technical learning path.

## Repository structure

```text
.
├── writeups/
│   ├── sanity-check.md
│   ├── website-initial-access.md
│   ├── mail-server-initial-access.md
│   ├── vpn-server-initial-access.md
│   └── pc3-lateral-movement.md
├── reference-material/
│   └── network-security-ctf-project-fa.pdf
├── original-submission/
│   └── README.md
├── prompt.md
├── .gitignore
└── README.md
```

## Security and archival note

This repository documents historical coursework performed in an **authorized CTF environment**. It is not a claim of testing real third-party systems.

The private historical submission consisted of five PDF write-ups. Those PDFs are not published here because they contain:

- valid challenge flags from the course environment;
- internal CTF IP addresses and ports;
- recovered challenge passwords and hashes;
- challenge-specific shell payloads and access details.

The original support package also contained a course-provided instructional video, which is omitted from Git history because it is large and was not authored by the student.

## Authorship

This was an **individual course project** completed by Amirhossein Sadeghi.

## Archival note

The coursework was completed during the 2024-2025 academic year and archived to GitHub in 2026 as part of an undergraduate coursework archive. The public version preserves the scope and technical work while removing challenge secrets and infrastructure-specific details.
