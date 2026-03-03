# CAN Loopback

## Purpose
This example demonstrates the use of CAN in Loopback mode for self-test.

## Configuration
- Used Model: Claude Opus 4.5
- Pin Connect: None


## Generation Flow
```mermaid
graph LR
  CANFD(CANFD) --> UART0(UART0)
  UART0 --> Clock(Clock)
  Clock --> MFPs(MFPs)
```

## Prompts
### CANFD Prompt
```
@nucodegen Generate a sample CANFD code for Nuvoton MCU with the following configuration:
- IP: CANFD0
- Operation Mode: CAN Mode
- Nominal Bit Rate: 1000000 bps
- Data Bit Rate: 0 bps
- Number of Tx Buffers, Rx Buffers, Rx FIFO0/1 Elements, Tx Event FIFO Elements: use default value
- Loopback Enable: Enable
- Global Filter: Reject non-matching standard frames to Rx FIFO0, reject remote frames
- Standard ID Filter: Classic, 2 elements, 
    * Filter Value: 0x110, Mask: 0x7F0
    * Filter Value: 0x220, Mask: 0x7FF
- Extended ID Filter: Classic, 2 elements, 
    * Filter Value: 0x33333, Mask: 0x1FFFFFF0
    * Filter Value: 0x44444, Mask: 0x1FFFFFFF
- Rx Buffer Type: RX_FIFO_0
- Frame Type: Data Frame
- Interrupts: Enable RX FIFO 0 New Message, Timeout Occurred
- IRQn: CANFD00_IRQn, IRQHandler: CANFD00_IRQHandler
- Optional: 
    * wait in a loop until RX is completed after TX transmits data.
- Purpose: For each ID, transmit and then receive CAN frames with 8 bytes using different standard ID and extended ID.
    * standard ID 0x110 to 0x115, 0x220.
    * extended ID 0x33333 t0 0x33337, 0x44444.
```

### UART0 Prompt
```
@nucodegen open UART to print comparsion result between TX and RX data for each ID.
```

### Clock Prompt
```
@nucodegen Generate a sample CLK (clock controller) configuration code for Nuvoton MCU with the following configuration:
- Enable Module Clock: UART0, CANFD0
- Module Clock Source: 
    * UART0: HIRC
    * CANFD0: APLL0_DIV2
- Module Clock Divider: 
    * UART0: 1
    * CANFD0: 1
- Enable Clock Source: HIRC
- Set PLL Frequency: Source: HIRC, Frequency: 220 MHz, Select: CLK_APLL0_SELECT
```

### MFPs Prompt
```
@nucodegen Generate a sample PIN (MFP) configuration code for Nuvoton MCU with the following configuration:
- Port: PB, Pin: PB.12, Function: UART0_RXD
- Port: PB, Pin: PB.13, Function: UART0_TXD
```

