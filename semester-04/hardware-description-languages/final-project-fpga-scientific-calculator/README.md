# FPGA Scientific Calculator Prototype

**Course:** Hardware Description Languages and Circuits  
**Semester:** Spring 2023  
**Team:** Seven-member group project  
**Language and tools:** Verilog, Xilinx ISE  
**Target board:** Xilinx XUPV5-LX110T

This project explored the design of a modular scientific calculator in Verilog.
The intended system combined arithmetic, trigonometric, and elementary
mathematical operations behind a shared operation selector.

## Technical scope

The submitted source contains modules for:

- 32-bit floating-point-inspired addition and subtraction;
- 32-bit floating-point-inspired multiplication and division;
- integer exponentiation and logarithm;
- sine and cosine calculation using a CORDIC implementation;
- selection and integration of the calculator operations;
- block-memory input, switch-based operation selection, and LED output; and
- pin constraints for the target FPGA board.

The `simulation` directory contains an earlier simulation-oriented source
snapshot and a testbench that cycles through the eight operation codes. The
`board-source` directory contains the later board-integration snapshot and its
UCF constraints.

## Collaboration

The project was developed collaboratively by all seven team members. The team
shared responsibility for the design, implementation, debugging, and technical
review of the modules; individual ownership was not assigned to specific source
files.

## Implementation status

This repository preserves an incomplete course prototype rather than a finished
hardware product.

- Several arithmetic and CORDIC modules were implemented and exercised through
  a basic simulation testbench.
- The planned serial input/output interface was not completed. The later
  integration attempt used block memory for two operands, switches for operation
  selection, and LEDs for displaying one byte of the result at a time.
- A complete deployment on the target FPGA board was not demonstrated.
- The generated `blkROM` memory core and its initialization file, the complete
  Xilinx ISE project, synthesis reports, and a programmable bitstream were not
  present in the archived submission. Consequently, the board-level top module
  is not self-contained.
- The arithmetic modules do not implement every IEEE 754 special case or the
  verification coverage expected from a production-quality floating-point
  unit.

## Repository contents

```text
original-submission/
├── board-source/   # Later FPGA-integration source snapshot and UCF file
└── simulation/     # Earlier source snapshot and calculator testbench
```

The original submission also contained a presentation, a code-walkthrough
video, and packaged presentation files. These large binary and generated files
are intentionally omitted from the GitHub archive.

## Archival and attribution note

The source is preserved as submitted in 2023. Only filenames and directory
layout were standardized during archival. The original presentation stated
that external explanations, diagrams, and existing code examples were consulted
while the team learned the algorithms, particularly CORDIC and floating-point
arithmetic. Exact source URLs were not retained, so this archive does not claim
that every individual code pattern originated with the team.

See [`prompt.md`](prompt.md) for an English translation of the relevant project
requirements.
