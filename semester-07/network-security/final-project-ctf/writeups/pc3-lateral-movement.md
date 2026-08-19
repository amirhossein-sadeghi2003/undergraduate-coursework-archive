# PC3 - Lateral Movement

## Submitted approach

The write-up starts from the previously obtained mail-server access and uses it as a pivot point for lateral movement inside the authorized CTF environment.

The documented workflow:

1. connected back to the mail server using the previously configured SSH key;
2. inspected a stored mail message and decoded its Base64 content;
3. identified behavior in which message content would later be processed on another system;
4. replaced the relevant message payload with a lab reverse-shell command;
5. copied the modified message back to the mail-server storage location;
6. started a local listener;
7. restarted the relevant mail service so the modified content would be processed;
8. received a shell on the next CTF host; and
9. recovered the PC3 challenge flag.

## Concepts demonstrated

- lateral movement
- SSH-based pivot access
- Base64 inspection
- application/workflow abuse
- controlled payload delivery in a CTF
- service lifecycle interaction
- reverse-shell handling

Internal paths, IP addresses, payload values, and flags are omitted from the public summary.
