# Archival fix

`sigsegv-handler-current-gcc.patch` adjusts the `sa_sigaction` callback signature and enables `SA_SIGINFO` so the historical exercise compiles with the current GCC. The original source in `submission/` remains unchanged.
