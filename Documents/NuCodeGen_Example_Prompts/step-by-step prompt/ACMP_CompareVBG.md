# ACMP Compare VBG

## Purpose
This example demonstrates how ACMP compare VBG output with ACMP1_P0 value.

## Configuration
- Used Model: Claude Opus 4.5
- Pin Connect:
  - ACMP1_P0 and DAC1_OUT are connected together.
  - UART0_TXD and UART0_RXD are connected with NuLink3 pro for printing the comparison result.

## Generation Flow
```mermaid
graph LR
  ACMP(ACMP) --> DAC(DAC)
  DAC --> UART0(UART0)
  UART0 --> Clock(Clock)
  Clock --> MFPs(MFPs)
  MFPs --> GPIO(GPIO)
```

## Prompts
### ACMP Prompt
```
Generate a sample ACMP code for Nuvoton MCU with the following configuration:
- IP: ACMP01, Channel: 1
- Positive Input Pin: P0
- Negative Input Source: VBG
- Hysteresis: Disabled
- Interrupts: Enable
- IRQn: ACMP01_IRQn, IRQHandler: ACMP01_IRQHandler
- Optional: 
    * Get output value, Clear interrupt flag after handling
    * clear interrupt flag before enabling interrupt
- Purpose: Compare ACMP1_P0 voltage with internal band-gap voltage
```

### DAC Prompt
```
Generate a sample DAC code for Nuvoton MCU with the following configuration:
- IP: DAC1
- Trigger Source: Software trigger
- DAC Conversion Settling Time: 1 us
- Data Transfer Type: Polling
- Optional: 
    *  check conversion finish interrupt after conversion, and then clear it at polling loop.
    * Vary the data for conversion in steps of 256.
- Purpose: 
    * The DAC1 output voltage will serve as the positive input of ACMP1.
    * For each while loop, vary the data from the minimum value to the maximum value, and then back to the minimum.
```

### UART0 Prompt
```
open UART0 to print the comparison result between positive input and VBG.
```

### Clock Prompt
```
Generate a sample CLK (clock controller) configuration code for Nuvoton MCU with the following configuration:
- Enable Module Clock: ACMP01_MOUDLE, GPIOA_MODULE, GPIOB_MODULE, GPIOC_MOUDLE, DAC01_MOUDLE, UART0_MODULE
- Module Clock Source: 
    * UART0: CLK_UARTSEL0_UART0SEL_HIRC
- Module Clock Divider: 
    * UART0: CLK_UARTDIV0_UART0DIV(1)
- Enable Clock Source: CLK_SRCCTL_HIRCEN_Msk
- Set PLL Frequency: Source: CLK_APLLCTL_APLLSRC_HIRC, Frequency: 220 MHz, Select: CLK_APLL0_SELECT
```

### MFPs Prompt
```
Generate a sample PIN (MFP) configuration code for Nuvoton MCU with the following configuration:
- Port: PA, Pin: PA.1, Function: UART0_TXD
- Port: PA, Pin: PA.0, Function: UART0_RXD
- Port: PB, Pin: PB.13, Function: DAC1_OUT
- Port: PA, Pin: PA.10, Function: ACMP1_P0
- Port: PC, Pin: PC.0, Function: ACMP1_O
```

### GPIO Prompt
```
Generate a sample GPIO code for Nuvoton MCU with the following configuration:
- Port: PA
- Pin Mask: BIT10
- Operation Mode: Input
- Digital Input Path: Disable
- Purpose: Disable digital input path of analog pin ACMP1_P0 to prevent leakage

- Port: PB
- Pin Mask: BIT13
- Operation Mode: Output
- Digital Input Path: Disable
- Purpose: Disable digital input path of analog pin DAC1_OUT to prevent leakage
```
