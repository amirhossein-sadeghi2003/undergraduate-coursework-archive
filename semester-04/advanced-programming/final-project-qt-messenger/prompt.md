# Assignment Summary

The original assignment was to build a graphical messaging client in C++ using Qt and object-oriented programming. The messaging server and its HTTP API were provided by the course staff; students were responsible for the client application.

## Core Scenario

1. Allow a user to register and log in.
2. Store the authentication token returned by the server and include it in authenticated requests.
3. Let users create and join groups and channels.
4. Display user, group, and channel lists.
5. Send and retrieve direct, group, and channel messages.
6. Log out and invalidate the active session.

## Provided API Operations

- `signup`, `login`, and `logout`
- `creategroup` and `createchannel`
- `joingroup` and `joinchannel`
- `getuserlist`, `getgrouplist`, and `getchannellist`
- `sendmessageuser`, `sendmessagegroup`, and `sendmessagechannel`
- `getuserchats`, `getgroupchats`, and `getchannelchats`

Server responses used JSON objects containing a status code, a message, and operation-specific data such as an authentication token or numbered result blocks.

## Technical Requirements

- Use suitable C++ classes, headers, source files, attributes, and methods.
- Implement the graphical interface with Qt.
- Use files to retain previously retrieved conversations for offline access.
- Organize saved histories into user, group, and channel categories.
- Retrieve new messages automatically while connected, using multithreading appropriately.
- Keep CPU and memory usage reasonable.
- Develop collaboratively in a shared GitHub repository with meaningful commits and contributions from every member.

The original Persian specification and the supplied API request/response table are preserved in `reference-material/`.
