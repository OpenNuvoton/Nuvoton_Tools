# SPI+PDMA Loopback

## Purpose
This example demonstrates the use of SPI and PDMA for loopback data testing.

## Configuration
- Used Model: Claude Opus 4.6
- Pin Connect:
  - SPI2_MOSI(PA.8), SPI2_MISO(PA.9)

## Prompt
```
Use SPI2 (PA.8–PA.11) and PDMA to transfer 256-byte from source array to destination array. Use UART0 (PB.12, PB.13) to verify data consistency. The SPI2, PDMA and UART0 clocks and their clock sources must be configured.
```