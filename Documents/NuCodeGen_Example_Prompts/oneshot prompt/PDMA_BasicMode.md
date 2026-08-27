# PDMA Basic Mode

## Purpose
This example demonstrates the use of PDMA in basic mode for data transfer.
## Configuration
- Used Model: Claude Opus 4.6
- Pin Connect:
  - UART0_RXD(PB.12), UART0_TXD(PB.13)

## Prompt
```
Use PDMA to transfer 128 bytes of data from a source array to a destination array using software trigger, and use UART0 (PB.12, PB.13) to print messages to verify whether the two arrays contain the same data after the PDMA transfer is completed.
Note: The PDMA and UART clocks and their clock sources must be configured.
```