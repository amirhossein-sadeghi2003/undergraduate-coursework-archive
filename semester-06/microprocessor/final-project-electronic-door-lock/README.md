# AVR Electronic Door-Lock Simulation

Final project for the **Microprocessor** course, completed in Spring 2024 at Isfahan University of Technology.

## Overview

This coursework project explored an electronic door-lock concept using AVR microcontrollers and a Proteus simulation. The submitted design used two ATmega32 microcontrollers, alphanumeric LCDs, a matrix keypad, status/alarm outputs, and C firmware generated and developed with CodeVisionAVR.

The first microcontroller implements the password-entry and password-management logic. The second microcontroller displays the two group members' names and student IDs on its LCD.

## Implemented in the submitted version

- Four-digit default password (`0000`)
- Matrix-keypad scanning by polling
- Masked password entry on a 16x2 LCD
- Password verification
- Addition of up to two extra passwords in RAM
- Changing an existing password
- Failed-attempt counter
- LED/alarm output after three consecutive incorrect passwords
- Separate success and failure indicator outputs
- Second ATmega32 and LCD for displaying group-member information
- Proteus project and compiled HEX images for simulation

## Assignment requirements vs. submitted implementation

The original assignment requested a broader design, including USART communication between the two microcontrollers, ADC-based alarm-volume control, and non-volatile password storage. These parts are **not fully implemented in the submitted firmware**:

- USART is disabled in both microcontroller configurations.
- ADC is disabled; no ADC-based volume-control logic is present in the firmware.
- Added/changed passwords are stored in RAM rather than EEPROM, so they do not persist after power loss.
- Keypad input is implemented with polling rather than the optional interrupt-based method.
- The second microcontroller only cycles through group-member information; it does not implement the requested password-reception/door-control communication path.

This repository preserves the project as coursework rather than presenting it as a complete production security system.

## Repository structure

```text
.
├── firmware/
│   ├── avr1/Fp.hex
│   └── avr2/Fp2.hex
├── original-submission/
│   └── MicroProject_9933133_40011643.rar
├── reference-material/
│   └── microprocessor-final-project-fa.pdf
├── simulation/
│   └── electronic-door-lock.pdsprj
└── source/
    ├── avr1/
    │   ├── Fp.c
    │   ├── Fp.cwp
    │   └── Fp.prj
    └── avr2/
        ├── FP2.c
        ├── Fp2.cwp
        └── Fp2.prj
```

The original submitted RAR is kept unchanged under `original-submission/`. The other directories are a curated copy for easier browsing; CodeVisionAVR build artifacts, Proteus autosaves/backups, and personal workspace files were intentionally omitted from the curated copy.

## Tools

- C
- ATmega32
- CodeVisionAVR
- Proteus
- 16x2 alphanumeric LCD
- Matrix keypad

## Running the historical simulation

Open `simulation/electronic-door-lock.pdsprj` in a compatible Proteus version. The historical project may still contain machine-specific or old relative firmware paths. If Proteus cannot locate the program images, relink the two ATmega32 components to:

```text
firmware/avr1/Fp.hex
firmware/avr2/Fp2.hex
```

No claim is made that the historical simulation has been revalidated on current Proteus or CodeVisionAVR versions.

## Team

This was a two-person course project completed by:

- Amirhossein Sadeghi
- Amir Hasan Taban

Both members contributed equally and worked across the project rather than owning separate modules.

## Archival note

The project was submitted in 2024 and archived to GitHub in 2026 as part of an undergraduate coursework archive. The original submission is preserved unchanged, while the browsable copy removes generated and user-specific files.
