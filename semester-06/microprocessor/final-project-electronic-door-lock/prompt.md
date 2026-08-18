# Final Project Prompt - Microprocessor

This file is an English summary of the original Persian assignment. The original PDF is preserved in `reference-material/`.

## Project

Design and simulate an electronic door-lock security system in Proteus using AVR microcontrollers and supporting components.

## Core requirements

- Use two microcontrollers, each with its own LCD.
- Connect a keypad to the user-facing microcontroller for password entry.
- Use USART as part of the communication between the two-microcontroller design.
- Use ADC in the system.
- Preserve passwords when the system is powered off.
- Start with one default password: `0000`.
- Allow the user to add a new password or change an existing password.
- When a correct password is entered, represent the electronic door as opened through the second-microcontroller side of the design and display a message containing the password.
- After three consecutive incorrect password attempts, flash an LED for a short period.
- Sound an alarm during the repeated-wrong-password warning.
- Add a potentiometer so the alarm volume can be changed.
- Display the group members' names and student IDs on the LCD during execution.

## Bonus requirements

- Display the group-member information as readable scrolling text.
- Read keypad input using interrupts instead of polling.
- Allow deletion of the last character while entering a password.

## Submission notes

The assignment required submission of both source code and simulation files. It was followed by an oral presentation in which both group members were expected to attend and understand the project.
