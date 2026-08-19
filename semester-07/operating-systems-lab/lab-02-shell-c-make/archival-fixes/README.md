# Archival fix

`current-gcc-build.patch` only adds the missing `<stdlib.h>` include required for the submitted `atoi()` call to compile on the current GCC. It intentionally does not change the historical Makefile semantics or assignment behavior.
