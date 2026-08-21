# Lab 03 — ADC Polling and UART

This exercise samples `ADC1` channel 2 at 12-bit resolution and sends each reading through `USART1` at 115200 baud. A new reading is produced approximately every 500 ms.

## Review changes

- Renamed the submitted text file to `main.c`.
- Added an explicit `HAL_ADC_PollForConversion` step before reading the ADC result.
- Replaced `sprintf` with bounded `snprintf`.
- Added a line terminator to each serial reading.
- Transmitted only the formatted message length instead of the entire 50-byte buffer.
- Stopped each polling conversion cleanly before the next sample.

## Limitations

Only `main.c` survived. The related CubeMX pin configuration, MSP source, interrupt source, startup code, and project metadata are unavailable. This reviewed source was not tested on the original board.

This was a two-person group exercise. A task-level contribution breakdown was not preserved.
