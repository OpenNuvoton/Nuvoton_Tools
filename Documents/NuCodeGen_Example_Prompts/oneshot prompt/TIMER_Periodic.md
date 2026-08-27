# TIMER Periodic

## Purpose
This example demonstrates the use of TIMER to periodically trigger an interrupt and print a message using UART.

## Configuration
- Used Model: Claude Opus 4.6
- Pin Connect:
  - UART0(PB.12, PB.13) is used for printing messages.

## Prompt
```
Use TIMER0 to demonstrate periodically triggering an interrupt every 1 second and use UART0(PB.12, PB.13) to print "Interrupt has occurred". The TIMER0 and UART0 clocks and their clock sources must be configured.
```