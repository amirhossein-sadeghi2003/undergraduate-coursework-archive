# Microprocessor Laboratory

Selected STM32 laboratory exercises completed during Semester 09. The available material covers sessions 02 through 06 and was produced collaboratively by a two-person team.

## Available sessions

| Session | Topic | Main peripherals |
| --- | --- | --- |
| 02 | Character LCD and numeric matrix-keypad scanning | GPIO, LCD1602 |
| 03 | Polling an analog input and reporting it over serial | ADC1, USART1 |
| 04 | Sending serial messages from external-interrupt events | EXTI, USART1 |
| 05 | Interrupt-based PWM motor control | TIM3 PWM, EXTI, GPIO |
| 06 | Interrupt-driven ADC-to-UART pipeline | ADC1, USART1 |

Session 01 is not included because its submission is no longer available.

## Repository status

Only individual `main.c` snapshots survived. The STM32CubeIDE projects, `main.h`, HAL support files, startup code, linker scripts, and board configuration files were not preserved. Session 02 also depends on an unavailable `STM_MY_LCD16X2` driver. Consequently, these files document the application logic but are not standalone buildable projects.

The raw uploads used inconsistent extensions and contained a few clear implementation defects. This public archive therefore contains reviewed copies rather than unedited submissions. The review was deliberately limited to:

- normalizing filenames and line endings;
- removing student identifiers and anonymizing the second team member;
- replacing fixed-size UART transmissions with actual message lengths;
- simplifying repetitive keypad scanning;
- correcting the ineffective PWM update logic; and
- making the interrupt-driven ADC/UART flow deterministic.

No hardware-in-the-loop validation was possible, so the archive does not claim that the reviewed sources can be flashed without reconstructing their original CubeMX configuration.

## Collaboration

All included sessions were completed by Amir Hossein Sadeghi and one laboratory partner. A reliable task-by-task contribution record is unavailable, so no individual ownership is claimed for specific portions of the code.
