# Assignment summary

The lab focuses on process creation and supervision. It asks students to distribute simulated tasks among child processes using `fork`, inspect child state with `waitpid`/`WNOHANG`, replace completed workers in a fixed-size process pool, and stop on a terminating signal. A second exercise runs another executable from a child with `exec` and measures/logs its execution time; a repeating version is bonus work.

The original Persian assignment PDF is preserved in `reference-material/`.
