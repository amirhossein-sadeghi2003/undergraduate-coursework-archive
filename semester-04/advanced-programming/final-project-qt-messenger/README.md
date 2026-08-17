# Qt Messenger Client

A graphical messaging client developed for the final project of the Advanced Programming course at Isfahan University of Technology in Spring 2023.

## Academic Context

The course staff provided the server and its HTTP API. Our task was to design and implement the C++ client, including its object-oriented structure, graphical interface, network requests, JSON response handling, and local message storage.

This was a three-member group project. All three members contributed equally throughout the project and worked across the client codebase rather than owning isolated components.

## Implemented Features

- User registration, login, and logout
- Graphical interface created with Qt Widgets and Qt Designer forms
- Retrieval of user, group, and channel lists
- Creation of and joining groups and channels
- Sending and retrieving direct, group, and channel messages
- Parsing JSON responses returned by the course server
- Basic local text-file storage when message histories are retrieved

## Technologies

- C++17
- Qt Widgets
- Qt Network
- Qt JSON classes
- qmake

## Repository Layout

- `original-submission/` contains the student-authored client source, preserved without code modernization.
- `prompt.md` provides an English summary of the assignment requirements.
- `reference-material/` contains the original Persian assignment specification and API request/response reference supplied for the course.

Qt Creator machine-specific `.pro.user*` files were intentionally omitted from the archive.

## Building

Open `original-submission/pastaW/pastaW.pro` in a Qt installation that provides the Widgets and Network modules, or build from a suitable qmake environment:

```bash
cd original-submission/pastaW
qmake pastaW.pro
make
```

The source was archived without modification and was not rebuilt during archival. Runtime messaging depends on the historical course server at `api.barafardayebehtar.ml:8080`, which may no longer be available.

## Archive Notes

This is an early undergraduate submission and should be read in that context. The archived implementation uses manual message retrieval and basic file persistence; it does not implement the assignment's complete background polling, multithreading, categorized offline storage, or URL-encoding requirements. The original client also sends requests over plain HTTP and should not be used with real credentials.
