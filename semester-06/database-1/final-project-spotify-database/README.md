# Spotify-Like Relational Database Application

Final project for **Database I**, completed in Spring 2024 at Isfahan University of Technology.

## Overview

This three-person coursework project models a simplified Spotify-like platform using PostgreSQL and a Python/Tkinter desktop interface. The submitted work combines a relational schema, an ER diagram, and a single Python application that directly issues SQL queries through `psycopg2`.

The project is preserved as historical coursework. It should not be interpreted as a production-ready Spotify clone or as a complete implementation of every requirement in the assignment brief.

## Technologies

- PostgreSQL
- SQL
- Python
- Tkinter
- `psycopg2`

## Contents

```text
.
├── app/
│   └── spotify.py
├── database/
│   └── schema/
│       └── *.sql
├── documentation/
│   └── ER-diagram.pdf
├── original-submission/
│   └── README.md
├── reference-material/
│   └── database-final-project-fa.pdf
├── .env.example
├── .gitignore
├── prompt.md
└── README.md
```

## Implemented in the submitted project

The Python application contains interfaces and database operations for a substantial subset of the requested platform, including:

- User and singer sign-up/login
- Separate user and singer dashboards
- Adding songs and albums
- Viewing song lyrics and comments
- Liking songs, albums, and playlists
- Playlist creation and song management
- Friend requests with accepted/rejected states
- Direct messages
- Following users and singers
- Wallet balance handling
- Subscription purchase flow
- Creating concerts
- Purchasing concert tickets
- Viewing purchased tickets
- Basic recommendation logic based on liked songs/related attributes

The SQL directory contains schema definitions for users, singers, songs, albums, playlists, likes, follows, friend requests, messages, comments, wallets, concerts, and tickets.

## Known limitations of the archived submission

This archive intentionally documents the state of the course submission rather than silently rewriting it into a finished system.

- The SQL schema files were submitted as separate scripts rather than a single ordered setup/migration script.
- At least one schema file (`comment.sql`) contains spelling errors in `FOREIGN KEY` / `REFERENCES` syntax in the historical submission.
- Singer identifiers are referenced inconsistently in parts of the schema (`singer.id` versus `singer.user_id`).
- The historical project has not been revalidated end-to-end against a fresh PostgreSQL installation.
- Some assignment requirements do not appear to be fully implemented in the submitted Python application, including concert cancellation with automatic ticket refunds and complete platform-wide song/album deletion behavior.
- The application stores user account passwords as ordinary database values and is educational coursework, not a secure authentication implementation.

## Security-related archival edit

The original submitted `spotify.py` contained a hard-coded password for a local PostgreSQL instance. That credential is **not published** in this repository.

For the browsable archive, the database connection block was changed only to read connection values from environment variables:

```text
SPOTIFY_DB_USER
SPOTIFY_DB_PASSWORD
SPOTIFY_DB_HOST
SPOTIFY_DB_PORT
SPOTIFY_DB_NAME
```

An example file is provided as `.env.example`. The original private course ZIP is intentionally excluded from the public repository because it contains the embedded credential; see `original-submission/README.md`.

## Historical run notes

A compatible PostgreSQL database named `spotify` and the required tables are needed before launching the application. The schema files reflect the historical submission and may require manual corrections/order resolution before they can initialize a fresh database.

Set the database connection variables in your shell, for example:

```bash
export SPOTIFY_DB_USER=postgres
export SPOTIFY_DB_PASSWORD='your-local-password'
export SPOTIFY_DB_HOST=127.0.0.1
export SPOTIFY_DB_PORT=5432
export SPOTIFY_DB_NAME=spotify
```

Then run the Python application in an environment with Tkinter and `psycopg2` available:

```bash
python spotify.py
```

No claim is made that the historical application has been fully re-tested on current PostgreSQL or Python versions.

## Team

This was a three-person course project completed by:

- Amirhossein Sadeghi
- Arian Madani
- Amir Hasan Taban

All three members contributed approximately equally and worked across the overall project rather than owning isolated modules.

## Archival note

The project was submitted in 2024 and archived to GitHub in 2026 as part of an undergraduate coursework archive. The browsable copy preserves the historical structure and behavior as closely as practical while removing the embedded local database credential from the public version.
