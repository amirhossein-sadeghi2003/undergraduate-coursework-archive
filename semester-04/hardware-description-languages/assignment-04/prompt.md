# Assignment 04 — Finite-State Machines

This document is an English translation of the original Persian assignment
handout.

## Problem 1 — Consecutive-One Detector

Using a complete finite-state-machine design method, describe a circuit that
examines a serial input stream, receiving one bit on each clock pulse. When it
detects exactly two consecutive `1` bits, but not more than two, the circuit
must assert its first output for one clock pulse.

In addition, assert the second output while the number of consecutive `1` bits
is less than four.

## Problem 2 — Six-Bit Pattern Search

Using an appropriate state-machine design, create a circuit that receives a
six-bit pattern through its first input and searches for that pattern within a
serial stream received through its second input, one bit per clock pulse. When
a match is found, assert the output for one clock pulse.

## Problem 3 — Traffic-Light Controller

Implement a traffic-light control circuit with the following behavior:

- By default, the highway light is green.
- When a vehicle is detected on the side road, the highway light first remains
  yellow for `y1` clock cycles and then turns red. When the highway light turns
  red, the side-road light turns green.
- After the side road has cleared, its light remains yellow for `y2` clock
  cycles and then turns red. When the side-road light turns red, the highway
  light turns green.
- The values of `y1` and `y2` must be configurable through a higher-level
  module.
- Use one-hot encoding for the output/state representation.

## Problem 4 — Washing-Machine Controller

Consider a washing machine and its different components. First describe its
operating sequence using Persian sentences and a flowchart. Then implement the
state machine that controls the machine in Verilog.

At minimum, account for the following components:

- water-inlet valve;
- drain valve;
- motor;
- heater; and
- user control panel.

Including additional components and modeling behavior closer to a real washing
machine will receive additional credit.
