# DAC Timer Trigger

## Purpose
This example demonstrates how to trigger DAC by timer.

## Configuration
- Used Model: Claude Opus 4.5
- Pin Connect: None

## Generation Flow
```mermaid
graph LR
  DAC+TIMER(DAC+TIMER)
  DAC+TIMER --> UART0(UART0)
  UART0 --> Clock(Clock)
  Clock --> MFPs(MFPs)
  MFPs --> GPIO(GPIO)
```

## Prompts
### DAC+TIMER Prompt
```
Generate a sample DAC code for Nuvoton MCU with the following configuration:
- IP: DAC1
- Trigger Source: Timer 0 trigger (10 Hz)
- DAC Conversion Settling Time: 1 us
- Interrupt Configurations: Enable DAC conversion finish interrupt
- IRQn and IRQHandler Configurations: IRQn: DAC01_IRQn
IRQHandler: DAC01_IRQHandler
- Optional: 
    * configure array to store data for DAC conversion.
    * Sweep data from min to max and back with step size 256.
    * get previous DAC data before updating DAC data.
- Purpose: Demonstrate how to trigger DAC by timer.
```

### UART0 Prompt
```
open UART0 to print original and updated DAC data.
```

### Clock Prompt
```
Generate a sample CLK (clock controller) configuration code for Nuvoton MCU with the following configuration:
- Enable Module Clock: UART0, GPIOB, DAC01, TMR0
- Module Clock Source: 
    * UART0: HIRC
    * TMR0: HIRC
- Module Clock Divider: 
    * UART0: 1
- Enable Clock Source: HIRC
- Set PLL Frequency: Source: HIRC, Frequency: 220 MHz, Select: CLK_APLL0_SELECT
```

### MFPs Prompt
```
Generate a sample PIN (MFP) configuration code for Nuvoton MCU with the following configuration:
- Port: PA, Pin: PA.1, Function: UART0_TXD
- Port: PA, Pin: PA.0, Function: UART0_RXD
- Port: PB, Pin: PB.13, Function: DAC1_OUT
```

### GPIO Prompt
```
Generate a sample GPIO code for Nuvoton MCU with the following configuration:
- Port: PB
- Pin Mask: BIT13
- Operation Mode: Output
- Digital Input Path: Disable
- Purpose: Disable digital input path of analog pin DAC1_OUT to prevent leakage
```
