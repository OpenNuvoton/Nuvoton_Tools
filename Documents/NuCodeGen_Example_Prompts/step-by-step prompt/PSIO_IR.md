# PSIO NEC IR

## Purpose
Demonstrate how to implement NEC IR protocol by PSIO.

## Configuration
- Used Model: Claude Opus 4.8
- Pin Connect:
  - PE.14 is connected to NuLink3 Pro to display the output waveform in PulseView.

## Generation Flow
```mermaid
graph LR
  Clock(Clock) --> MFPs(MFPs)
  MFPs --> PSIO(PSIO)
  PSIO --> UART0(UART0)
```

## Prompts
### Clock+MFPs Prompt
```
Generate a sample CLK configuration, PIN (Multi-Function Pin) code for Nuvoton M55M1 MCU with the following configuration:
- Clock Sources: Enable HIRC, LIRC
- SCLK (System Clock) Source: APLL0 (220 MHz)
- HCLK2 DIV: 2
- PCLKx DIV: 2
- Module Clock Configuration:
  - UART0: Enable, Clock Source = HIRC, Clock Divider = 1
  - PSIO: Enable, Clock Source = LIRC, Clock Divider = 2
  - GPIOE: Enable
- Port: PB, Pin: PB.12, Function: UART0_RXD
- Port: PB, Pin: PB.13, Function: UART0_TXD
- Port: PE, Pin: PE.14, Function: PSIO0_CH0
```

### PSIO Prompt
```
Generate a sample PSIO code for Nuvoton MCU implementing the NEC IR transmitter protocol with the following configuration:

- IP: PSIO
- Slot Controller: SC0
- Repeat Mode: Disabled
- Pin: PIN0
- Pin Enable: Enabled
- Slot Controller for Pin Check Point: SC0
- I/O Mode: Output Mode
- Pin Initial Output State: Low Level
- Pin Interval Output State: Low Level
- Output Data Width: 8 bits
- Input Data Width: 0 bits
- Data Order: LSB first
- Output Data Depth: DEPTH4
- Trigger Source: Software Trigger
- IRQn: PSIO_IRQn
- Interrupts: Configurable Interrupt 0 enabled
- IRQHandler: PSIO_IRQHandler
- IRQHandler behavior:
  - Check Output Empty flag for the TX pin; if empty and transfer not done, write next 32-bit encoded word to PIN0 OUTDAT register
- Purpose: Transmit full NEC IR protocol frames through a single PSIO output pin.
  - Send 0x1(Address), 0x2(Command) -> Send repeat signal
```

### UART0
```
open UART0 to print debug messages before starting test.
```
