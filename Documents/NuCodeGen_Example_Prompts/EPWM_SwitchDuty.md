# EPWM Switch Duty

## Purpose
This example demonstrates how to change the duty cycle of the output waveform by configuring the period.

## Configuration
- Used Model: Claude Opus 4.5
- Pin Connect:
  - EPWM0_CH0 are connected to Nulink 3 pro PSIO_CH0 for waveform observation using [PulseView](https://github.com/OpenNuvoton/Nuvoton_Tools/blob/master/Documents/Nu-Link3-Pro_User_Manual/ch6_1_pulseview.md).


## Generation Flow
```mermaid
graph LR
  EPWM(EPWM) --> UART0(UART0)
  UART0 --> Clock(Clock)
  Clock --> MFPs(MFPs)
```

## Prompts
### EPWM Prompt
```
@nucodegen Generate a sample EPWM code for Nuvoton MCU with the following configuration:
- IP: EPWM0
- Channel(s): 0
- Mode: Output
- Frequency: 1800 Hz
- Duty Cycle: 50% (initial), dynamically switch to:
    * 1: 100%
    * 2: 75%
    * 3: 50%
    * 4: 25%
    * 5:  0%
- Output Enable: Channel 0
- Function: CMP = duty cycle * (CNR + 1) / 100
- Purpose: Change duty cycle of output waveform by configured period based on the number entered by the user
```

### UART0 Prompt
```
@nucodegen Open UART0, print the duty-cycle options, and get a character from user to determine which duty cycle to be used.
Print and read input in the main loop to allow the user to switch the duty cycle.
```

### Clock Prompt
```
@nucodegen Generate a sample CLK (clock controller) configuration code for Nuvoton MCU with the following configuration:
- Enable Module Clock: UART0, EPWM0
- Module Clock Source: 
    * UART0: HIRC
    * EPWM0: PCLK
- Module Clock Divider: 
    * UART0: 1
- Enable Clock Source: HIRC
- Set PLL Frequency: Source: HIRC, Frequency: 220 MHz, Select: CLK_APLL0_SELECT
```

### MFPs Prompt
```
@nucodegen Generate a sample PIN (MFP) configuration code for Nuvoton MCU with the following configuration:
- Port: PB, Pin: PB.12, Function: UART0_RXD
- Port: PB, Pin: PB.13, Function: UART0_TXD
- Port: PE, Pin: PE.7, Function: EPWM0_CH0
```

