# Lab 05 — PWM Motor Control with Interrupts

This exercise configures `TIM3` channel 1 for PWM with a period of 999 counts. Three rising-edge inputs on `PC1`–`PC3` change the two direction-control outputs or select a lower or higher PWM compare value.

The two output pins, `PA11` and `PA12`, are initialized to complementary states and toggled together to reverse the assumed motor direction. The PWM compare values are 500, 800, and 900 counts.

## Review changes

- Renamed the submitted text file to `main.c`.
- Added named constants for the PWM compare values.
- Moved PWM startup and initial output configuration before the main loop.
- Removed a redundant timer-base start.
- Replaced ineffective instantaneous `for` loops with a bounded compare-update helper. One original loop used `i > 900` while starting from 500 and therefore never executed.
- Checked the PWM startup result and routed failures to `Error_Handler`.

## Limitations

The hardware schematic and original task sheet are unavailable, so the motor-driver interpretation is inferred from the complementary direction pins and PWM output. The full CubeIDE project and timer post-initialization source are missing. No ramp timing or switch debounce is implemented, and the reviewed source was not tested on hardware.

This was a two-person group exercise. A task-level contribution breakdown was not preserved.
