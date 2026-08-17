# Assignment 01 — Verilog Fundamentals

This document is an English translation of the original Persian assignment
handout.

## Problem 1 — Logic Gates Using NOR

Using only two-input NOR gates, implement each of the following circuits and
provide an appropriate test module for each implementation:

1. a NOT gate;
2. a two-input AND gate; and
3. a two-input XOR gate.

For the second and third parts, you may instantiate modules developed in the
preceding parts.

## Problem 2 — JK Flip-Flop

Implement a JK flip-flop by instantiating logic gates and provide an appropriate
test module. Use hierarchical design as extensively as practical.

## Problem 3 — Hierarchical Comparator

At the register-transfer level, describe a comparator for two unsigned four-bit
numbers. The module must have three outputs:

- `X`: the first input is greater than the second input;
- `Y`: the second input is greater than the first input; and
- `Z`: the two inputs are equal.

Instantiate this module as needed in a higher-level module to create a 16-bit
comparator. Demonstrate the correct operation of the higher-level module using
three different pairs of 16-bit values.

## Problem 4 — Four-Function ALU

Using behavioral modeling, define a four-function arithmetic logic unit. The
unit has two five-bit inputs, `a` and `b`, and produces a six-bit output, `out`,
according to the two-bit `select` input:

| `select` | `out` |
|---|---|
| `00` | `a` |
| `01` | `a + b` |
| `10` | `a - b` |
| `11` | `a + 1` |

## Problem 5 — Eight-Bit Shift Register

Using behavioral modeling, describe an eight-bit shift register with inputs
`Clk`, `Load`, `Data`, `Clear`, `Shift`, and `Dir`, and output `Out`, subject to
the following requirements:

- When `Load` is active, load the value of `Data` into the register.
- When `Clear` is active, load zero into the register.
- When `Shift` is active, shift the register by one bit in the direction
  selected by `Dir`. A value of `1` selects a right shift and `0` selects a left
  shift.
- Do not use Verilog's left- or right-shift operators. Implement the shift using
  a loop.
- Perform all operations on the falling edge of `Clk`.

After implementing the circuit, use a test module and appropriate stimulus
vectors to demonstrate correct operation.

## Problem 6 — Loop-Based Divider

Using loops, implement a module that calculates the integer quotient and
remainder when an eight-bit input value is divided by a specified divisor. Show
the quotient and remainder on two separate output ports.

Observe the following constraints:

- The `/` and `%` operators are not permitted.
- For simplicity, the divisor may be any selected value from 1 through 8.
- If the divisor falls outside this range, display an appropriate simulation
  message.
