# Website - Initial Access

## Submitted approach

The write-up documents a multi-step web challenge in the authorized university CTF environment:

1. The initial page indicated that the request needed to appear as if it had been referred by Google.
2. The HTTP request was adjusted with the expected headers to pass that restriction.
3. A hidden server path was discovered, exposing a downloadable SQLite database file.
4. The database was inspected locally and an administrative account record and password hash were identified.
5. The hash format and application behavior led to a PHP type-juggling / loose-comparison weakness.
6. A specially chosen numeric password value was used to satisfy the vulnerable comparison and access the protected application.
7. The challenge flag was then recovered.

## Concepts demonstrated

- HTTP header manipulation
- web-content discovery
- SQLite database inspection
- password-hash analysis
- PHP loose comparison / type juggling
- authentication-logic weaknesses

Exact lab addresses, hashes, credentials, and flags are omitted from this public summary.
