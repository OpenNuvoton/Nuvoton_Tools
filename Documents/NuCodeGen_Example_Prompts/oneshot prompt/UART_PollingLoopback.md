# UART Polling Loopback

## Purpose
This example demonstrates the use of UART for loopback data testing.

## Configuration
- Used Model: Claude Opus 4.6
- Pin Connect:
  - UART1_RXD(PA.8) and UART1_TXD(PA.9) are connected together for loopback testing.

## Prompt
```
Use UART1 (PA.8, PA.9) to perform a loopback test by writing and reading 1 byte for 256 iterations. Use UART0 (PB.12, PB.13) to verify data consistency. The UART1 and UART0 clocks and their clock sources must be configured.
```