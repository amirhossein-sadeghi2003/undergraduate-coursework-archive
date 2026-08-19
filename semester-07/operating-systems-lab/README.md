# Operating Systems Laboratory — Coursework Archive

**Course:** Operating Systems Laboratory  
**Institution:** Isfahan University of Technology, Department of Electrical and Computer Engineering  
**Term:** Fall 2024 (1403)  
**Archive status:** historical coursework, organized for GitHub in August 2026

This directory preserves the submitted work from the Operating Systems Laboratory course. The course progressed from Linux command-line and build-system exercises into kernel-space programming, process management, IPC, shared memory, signals, threads, and synchronization.

The original student submissions are preserved separately where available. The browsable `submission/` copies keep the historical code unchanged except that editor-specific clutter is omitted from the Lab 06 browsable copy. Review notes document build/runtime checks performed during archival; they are not claims that every historical requirement was fully satisfied.

## Sessions

| Session | Main topics | Archival review |
|---|---|---|
| 01 | Linux files, permissions, SSH/SCP, processes, grep | Basic; contains historical command/report artifacts |
| 02 | Bash scripting, multi-file C, Makefile | Bash syntax OK; C build needs a one-line include fix on current GCC |
| 03 | File-related system calls, static library, Makefile | Builds; important logic issues documented |
| 04–05 | Linux character device / kernel module | User-space client builds; kernel module not rebuilt in archive environment |
| 06 | Character device with `ioctl`, dynamic kernel buffer | User-space client builds; kernel-safety limitations documented |
| 07 | Custom system call returning process information | User client builds in GNU mode; kernel integration files are incomplete |
| 08 | `fork`, `waitpid`, `exec`, process supervision | Sources build; supervision logic has known limitations |
| 09 | Unnamed pipes, FIFO/named-pipe IPC | Sources build; factorial test for 20 succeeds |
| 10 | `SIGSEGV`, POSIX shared memory, `SIGUSR1`, fork | Shared-memory versions build/run; SIGSEGV source needs a small handler fix |
| 11 | POSIX threads, semaphores, readers–writers | Builds; dot product and short readers–writers runs verified |

## Repository structure

Each lab directory can contain:

- `submission/` — extracted, browsable coursework files.
- `original-submission/` — the original archive submitted for the course.
- `reference-material/` — the assignment PDF when it was available.
- `prompt.md` — concise English summary of the available assignment brief.
- `README.md` — archival review, build status, and known limitations.
- `archival-fixes/` — optional minimal patches kept separate from the historical source.

## Important archival notes

- The assignment brief for Labs 04–05 and Lab 06 was not available during archival; their scope is described only from the submitted code.
- The PDF supplied alongside Lab 07 is internally labeled **Session 8, Fall 1401**, although its custom-system-call content matches the submitted Lab 07 code. It is retained with an explicit provenance warning rather than silently relabeled.
- Kernel modules and custom kernel syscalls are highly kernel-version dependent. They were not loaded or executed during archival.
- Several submissions intentionally remain imperfect. The goal of this repository is to preserve historical coursework faithfully, not to rewrite it into production-quality code.
