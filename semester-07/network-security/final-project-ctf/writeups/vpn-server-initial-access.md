# VPN Server - Initial Access

## Submitted approach

This was the most involved submitted challenge and documents a chained workflow across multiple CTF systems.

The write-up describes:

1. reusing authorized access to the previously compromised mail server;
2. establishing SSH key-based access to simplify repeated lab access;
3. locating a mail-related file containing Base64-encoded data;
4. transferring the encoded file to the local system and decoding it into a password-protected ZIP archive;
5. extracting the ZIP password hash and recovering the password with John the Ripper and a wordlist;
6. extracting an OpenVPN client configuration and certificate material;
7. using that configuration to reach the VPN-side challenge network;
8. exploiting a ShellShock-vulnerable lab service to obtain a reverse shell;
9. reading the challenge flag; and
10. adding authorized-key access inside the CTF environment for continued challenge work.

## Concepts demonstrated

- SSH key authentication
- secure file transfer
- Base64 decoding
- ZIP password-hash extraction
- password cracking with John the Ripper
- OpenVPN configuration
- pivoting into another lab network segment
- ShellShock
- reverse-shell handling

Recovered passwords, exact commands containing lab-specific values, internal addresses, key material, and flags are omitted from the public archive.
