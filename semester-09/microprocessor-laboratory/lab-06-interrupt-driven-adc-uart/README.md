# Lab 06 — Interrupt-Driven ADC and UART

This session combines ADC conversion-complete and UART transmission-complete callbacks. `ADC1` channel 0 produces a 12-bit sample, the main loop formats the completed value, and `USART1` transmits it at 115200 baud. Completion of the UART transfer starts the next ADC conversion.

## Review changes

- Renamed the submitted text file to `main.c`.
- Replaced the shared uninitialized 50-byte character array with a bounded serial buffer.
- Added peripheral-instance checks to both HAL callbacks.
- Changed the ADC to single-conversion mode so each conversion has one clear start and completion event.
- Moved string formatting out of the ADC interrupt callback.
- Transmitted only the formatted length and added a serial line terminator.
- Removed repeated ADC starts from the main loop and callback.
- Added failure paths that restart acquisition if a UART transfer cannot be started.

## Limitations

Only `main.c` survived. Correct operation also depends on the missing CubeMX-generated ADC, UART, GPIO, MSP, and NVIC configuration. The reviewed event flow was checked statically but not tested on the original board.

This was a two-person group exercise. A task-level contribution breakdown was not preserved.
