# Lab 02 — Shell scripting, C, and Make

## Contents
- `Q1/Q1.sh`: argument-driven Bash file-generation/removal script.
- `Q2/`: multi-file prime checker with header and Makefile.

## Archival review
`bash -n` succeeds for the shell script. The C project does not build with the current GCC because `main.c` calls `atoi()` without including `<stdlib.h>`. A minimal archival patch is provided separately in `archival-fixes/`; the historical source is unchanged.

The submitted Makefile also installs the executable as `my_program`, while the available assignment asks for the installed name `prime`. `clean` uses `rm` without `-f`, and the shell script removes requested indices without first checking whether the generated file exists.
