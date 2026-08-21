# Lab 02 — Character LCD and Matrix Keypad

This session contains two STM32 HAL examples. The first drives a 16×2 character LCD in four-bit mode and alternates between two team-member placeholders. The second scans the numeric positions of a matrix keypad and displays the detected digit on the LCD.

## Files

- `reviewed-submission/lcd-team-display.c`: LCD initialization and alternating two-line messages.
- `reviewed-submission/matrix-keypad-lcd.c`: GPIO matrix scan and numeric-key display.
- `prompt.md`: reconstructed exercise description.

## Review changes

- Corrected the original `.c.c` and `.c.txt` extensions.
- Replaced names and student numbers shown on the LCD with public-safe placeholders.
- Replaced repetitive keypad branches with a column/row lookup table.
- Used HAL pin-state constants instead of numeric GPIO states.
- Reduced the key-display delay from 500 ms to 200 ms while retaining basic debounce behavior.

## Limitations

The custom `STM_MY_LCD16X2` driver and the rest of the STM32CubeIDE project are missing. The keypad map intentionally covers only digits `0`–`9`; non-numeric keys are ignored. The source was reviewed statically but could not be built or tested on the original hardware.

This was a two-person group exercise. A task-level contribution breakdown was not preserved.
