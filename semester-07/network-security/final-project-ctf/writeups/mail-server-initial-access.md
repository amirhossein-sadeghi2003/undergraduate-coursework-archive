# Mail Server - Initial Access

## Submitted approach

The write-up identifies the target service as a vulnerable Zimbra deployment in the authorized CTF lab.

The submitted solution:

1. identified the mail service and the relevant Zimbra vulnerability;
2. used a Metasploit module appropriate to the vulnerable lab service;
3. obtained a remote shell in the CTF environment;
4. inspected the server context with standard Linux commands; and
5. located and read the challenge flag file.

## Concepts demonstrated

- service identification
- vulnerability-to-exploit mapping
- Metasploit usage in a controlled lab
- remote shell interaction
- Linux post-access enumeration

Exact module parameters, internal addresses, ports, and flags are intentionally omitted from the public archive.
