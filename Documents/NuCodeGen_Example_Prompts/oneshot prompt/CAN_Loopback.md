# CAN Loopback

## Purpose
This example demonstrates the use of CANFD in CAN mode for a loopback transfer of 8 bytes, testing both standard and extended IDs.

## Configuration
- Used Model: Claude Opus 4.6
- Pin Connect:
  - UART0_RXD(PB.12), UART0_TXD(PB.13)

## Prompt
```
Use CANFD in CAN mode to demonstrate a loopback transfer of 8 bytes. Each ID must be tested:
1. Standard ID: 0x110–0x112
2. Extended ID: 0x33333–0x33335
Use UART0 (PB.12, PB.13) to print whether each test result is correct.
The clocks and clock sources for UART0 and CANFD must be configured.
```