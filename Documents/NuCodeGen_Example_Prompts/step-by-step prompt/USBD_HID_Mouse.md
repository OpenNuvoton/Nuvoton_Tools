# USBD HID Mouse

## Purpose
Show how to implement a USB mouse device. The mouse cursor will move automatically when this mouse device connecting to PC by USB.

## Configuration
- Used Model: Claude Sonnet 4.6
- Pin Connect: connect to PC by USB

## Generation Flow
```mermaid
graph LR
  Clock(Clock) --> MFPs(MFPs)
  MFPs --> USBD(USBD + descriptors)
  USBD --> PMC(PMC)
  PMC --> UART0(UART0)
```

## Prompts
### Clock Prompt
```
Generate a sample CLK configuration code for Nuvoton M55M1 MCU with the following configuration:
- Clock Sources: Enable HXT (external crystal oscillator)
- SCLK (System Clock) Source: APLL0 (220 MHz)

- APLL1 Configuration:
  - APLL1 Source: HXT
  - APLL1 Frequency: 192 MHz

- Module Clock Configuration:
  - UART0: Enable, Clock Source = HXT, Clock Divider = 1
  - USBD: Enable, Clock Source = APLL1_DIV2, Clock Divider = 2
```

### MFPs Prompt
```
Generate a sample PIN (Multi-Function Pin) configuration code for Nuvoton MCU M55M1 with the following configuration:
- Port: PB, Pin: PB.12, Function: UART0_RXD
- Port: PB, Pin: PB.13, Function: UART0_TXD
- PA.12 - PA.15: USBD
```

### USBD + descriptors
```
Generate a sample USBD code for Nuvoton M55M1 MCU with the following configuration and create a file for current project:
- IP: USBD
- USB Controller: Enabled
- USB PHY: Enabled
- Endpoints:
  - Endpoint 0: In endpoint, control, Buffer size 8 bytes, Buffer offset: step up buffer size, endpoint number = 0
  - Endpoint 1: Out endpoint, control, Buffer size 8 bytes, Buffer offset EP0 buffer base+EP0 buffer size, endpoint number = 0
  - Endpoint 2: In endpoint, Interrupt, Buffer size 8 bytes, Buffer offset EP1 buffer base+EP1 buffer size, endpoint number = 1
- Interrupts: Enable USBD_INT_USB, USBD_INT_BUS, USBD_INT_FLDET, USBD_INT_WAKEUP
- IRQn: USBD_IRQn, IRQHandler: USBD_IRQHandler
- Optional:
    * Add a flag to record whether USBD is suspended.
    * Generate descriptors for a mouse with 3 buttons + X/Y/wheel
- Purpose: Initialize USB mouse device controller to communicate with USB host, send/receive data via endpoints, and handle USB mouse control transfers to automatically move along a square path.
```

### PMC
```
Generate a sample PMC (Power Management Controller) code for Nuvoton MCU with the following configuration:
- IP: PMC
- Purpose: In the main loop, enter power-down mode if the USBD suspend flag is triggered.
```

### UART0
```
Open UART0 to print some debug messages.
```
