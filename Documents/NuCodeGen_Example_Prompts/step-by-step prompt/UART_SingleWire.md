# UART SingleWire

## Purpose
This example demonstrates the use of UART in SingleWire mode for loopback data testing.

## Configuration
- Used Model: Claude Opus 4.5
- Pin Connect:
  - UART1_RXD and UART2_RXD are connected together for loopback testing.

## Generation Flow
```mermaid
graph LR
  UART1/2(UART1/2) --> UART0(UART0)
  UART0 --> Clock(Clock)
  Clock --> MFPs(MFPs)
  MFPs --> GPIO(GPIO)
```

## Prompts
### UART1/2 Prompt
```
Generate a sample UART code for Nuvoton MCU with the following configuration:
- IP: UART1, UART2
- Baud Rate: 115200
- Line Mode: Single Wire
- Interrupts: Enable RX Ready, Single-wire Bit Error Detection, RX Timeout
- IRQn:
    * UART1: UART1_IRQn, IRQHandler: UART1_IRQHandler
    * UART2: UART2_IRQn, IRQHandler: UART2_IRQHandler
- Optional: add a flag for the loop to wait until the transfer is complete.
- Purpose: Two test:
    1. UART1 totally write 128 bytes data to UART2, and UART2 repeatedly read byte.
    2. UART2 totally write 128 bytes data to UART1, and UART1 repeatedly read byte.
```

### UART0 Prompt
```
open UART0 to print comparison results between TX and RX array
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
- Port: PA, Pin: PA.2, Function: UART1_RXD
- Port: PB, Pin: PB.0, Function: UART2_RXD
```

### GPIO Prompt
```
Generate a sample GPIO code for Nuvoton MCU with the following configuration:
- Port: PB
- Pin Mask: BIT0
- Pull Control: Pull-up
- Purpose: for UART2 single-wire demo

- Port: PA
- Pin Mask: BIT2
- Pull Control: Pull-up
- Purpose: for UART1 single-wire demo
```
