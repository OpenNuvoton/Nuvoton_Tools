# UART AutoFlow

## Purpose
This example demonstrates the use of UART in AutoFlow mode for transfer data from UART1 to UART2.

## Configuration
- Used Model: Claude Opus 4.5
- Pin Connect:
  - UART1_nCTS and UART2_nRTS are connected together for loopback testing.
  - UART1_TX and UART2_RX are connected together for loopback testing.

## Generation Flow
```mermaid
graph LR
  UART1/2(UART1/2) --> UART0(UART0)
  UART0 --> Clock(Clock)
  Clock --> MFPs(MFPs)
```

## Prompts
### UART1/2 Prompt
```
Generate a sample UART code for Nuvoton MCU with the following configuration:
- IP: UART1, UART2
- Baud Rate: 115200
- Data Width: 8 bits
- Parity: None
- Stop Bits: 1
- RX FIFO Trigger Level: 8 bytes
- RTS Trigger Level: 8 bytes
- Flow Control: Enable Auto Flow Control
- Data Transfer Type: write: polling, read: interrupt
- Mode: UART
- Time Out: 0x3E
- Interrupts: Enable Receive Data Available, RX Time-out
- IRQn: 
    * UART1: UART1_IRQn, IRQHandler: UART1_IRQHandler
    * UART2: UART2_IRQn, IRQHandler: UART2_IRQHandler
- Optional: 
    * Reset TX FIFO before transfer
    * Before read data, check if RX FIFO is empty.
- Purpose: demonstrate TX, RX autoflow functionality:
    * test: UART1 TX totally transfer 256 bytes to UART2 RX and then store received data into array.
```

### UART0 Prompt
```
open UART0 to print comparison results between TX, RX array after transfer is done.
```

### Clock Prompt
```
Generate a sample CLK (clock controller) configuration code for Nuvoton MCU with the following configuration:
- Enable Module Clock: UART0_MODULE, UART1_MODULE, UART2_MODULE
- Module Clock Source: 
    * UART0: CLK_UARTSEL0_UART0SEL_HIRC
    * UART1: CLK_UARTSEL0_UART1SEL_HIRC
    * UART2: CLK_UARTSEL0_UART2SEL_HIRC
- Module Clock Divider: 
    * UART0: CLK_UARTDIV0_UART0DIV(1)
    * UART1: CLK_UARTDIV0_UART1DIV(1)
    * UART2: CLK_UARTDIV0_UART2DIV(1)
- Enable Clock Source: CLK_SRCCTL_HIRCEN_Msk
- Set PLL Frequency: Source: CLK_APLLCTL_APLLSRC_HIRC, Frequency: 220 MHz, Select: CLK_APLL0_SELECT
```

### MFPs Prompt
```
Generate a sample PIN (MFP) configuration code for Nuvoton MCU with the following configuration:
- Port: PB, Pin: PB.12, Function: UART0_RXD
- Port: PB, Pin: PB.13, Function: UART0_TXD
- Port: PA, Pin: PA.1, Function: UART1_nCTS
- Port: PA, Pin: PA.3, Function: UART1_TXD
- Port: PC, Pin: PC.3, Function: UART2_nRTS
- Port: PC, Pin: PC.0, Function: UART2_RXD
```
