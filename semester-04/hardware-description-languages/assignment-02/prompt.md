# Assignment 02 — Timing, Adders, Tasks, and Functions

This document is an English translation of the original Persian assignment
handout.

## Problem 1 — Ripple-Carry Adder

Implement an eight-bit ripple-carry adder hierarchically at the gate level. Use
the following propagation delays:

| Two-input gate | 0-to-1 delay | 1-to-0 delay |
|---|---:|---:|
| AND | 5 ns | 3 ns |
| OR | 6 ns | 3 ns |
| XOR | 8 ns | 4 ns |

Test the adder for its worst-case propagation delay. Determine and demonstrate
the minimum amount of time for which the inputs must remain stable before the
final output becomes valid.

## Problem 2 — Carry-Lookahead Adder

Research the structure of a carry-lookahead adder and implement it using
behavioral modeling while accounting for the propagation delays specified in
Problem 1.

If a gate has more than two inputs, add 1 ns to that gate's delay for every
additional input beyond two.

Test the adder for its worst-case propagation delay. Determine and demonstrate
the minimum amount of time for which the inputs must remain stable before the
final output becomes valid.

## Problem 3 — Integer Logarithm Task

Write a Verilog task that calculates the integer part of the logarithm of a
16-bit first input using a three-bit second input as the base, and returns the
result through an output argument. Also write an appropriate test module that
calls the task and checks its result for five different cases.

## Problem 4 — Factorial Function

Write a Verilog function that calculates the factorial of a four-bit input and
returns the result. Also write an appropriate test module that calls the
function and checks its result for three different cases.
