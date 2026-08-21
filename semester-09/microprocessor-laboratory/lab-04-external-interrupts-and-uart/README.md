# Lab 04 — External Interrupts and UART

This session configures rising-edge external interrupts on `PA1` and `PA2`. When either input is triggered, the HAL EXTI callback starts a corresponding serial message on `USART1` at 115200 baud. The main loop remains empty because the behavior is event-driven.

## Review changes

- Renamed the submitted text file to `main.c`.
- Replaced personal names with event-oriented messages.
- Removed unused formatting code.
- Transmitted only the meaningful bytes in each message.
- Changed UART output to interrupt mode so the EXTI callback does not wait for a blocking serial transfer.

## Limitations

The complete CubeIDE project is unavailable. In particular, the MSP and IRQ-handler sources needed for the GPIO and UART interrupts were not preserved. Rapid repeated button events may be ignored while a previous UART transfer is busy. Hardware debounce is also outside the surviving code.

This was a two-person group exercise. A task-level contribution breakdown was not preserved.
