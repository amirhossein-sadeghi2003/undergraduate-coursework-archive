# Assignment Summary — Computer Networks I Project 01

The original Persian assignment is preserved in `reference-material/computer-networks-project-01-fa.pdf`.

## Part 1 — Network programming

Implement a simple reverse-shell-style client/server exercise in **C** on **Ubuntu** using **TCP sockets**.

The server should:

- listen on a port supplied by the user;
- accept a client connection;
- send shell commands to the connected client;
- receive and display the command output;
- correctly handle output that may be larger than a single socket buffer; and
- pay attention to the return values of socket send/receive operations.

The client should:

- know the server address and port;
- connect to the server;
- receive shell commands;
- execute them locally;
- return their output to the server; and
- support outputs whose size is not known in advance.

The assignment also requested a short discussion of concurrency models. A multi-client concurrent server and a `sendall` command were optional bonus features.

A Makefile was required for compilation.

## Part 2 — HTTP analysis with Wireshark

Capture and analyze HTTP traffic for several scenarios, including:

- a basic HTTP request and response;
- comparison with a request sent using `curl`;
- transfer of a larger HTML document and its use of multiple TCP segments; and
- HTTP authentication, including examination of the `Authorization` header.

The submission was expected to include answers to the questions, screenshots from Wireshark, the C source files, and the Makefile.
