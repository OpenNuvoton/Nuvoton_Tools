# EADC Average

## Purpose
This example demonstrates how to get average conversion result from the EADC.

## Configuration
- Used Model: Claude Opus 4.5
- Pin Connect:
  - EADC0_CH0 and DAC1_OUT are connected together.
  - UART0_TXD and UART0_RXD are connected with NuLink3 pro for printing the comparison result.

## Generation Flow
```mermaid
graph LR
  DAC(DAC) --> EADC(EADC)
  EADC --> UART0(UART0)
  UART0 --> Clock(Clock)
  Clock --> MFPs(MFPs)
  MFPs --> GPIO(GPIO)
```

## Prompts
### DAC Prompt
```
@nucodegen Generate a sample DAC code for Nuvoton MCU with the following configuration:
- IP: DAC1
- Trigger Source: Software trigger
- DAC Conversion Settling Time: 1 us
- Data Transfer Type: Polling
- Optional: 
    * check conversion finish interrupt after conversion, and then clear it at polling loop.
    * vary the data for conversion in steps of 256.
- Purpose: 
    * For each while loop, vary the data from the minimum value to the maximum value, and then back to the minimum.
```

### EADC Prompt
```
@nucodegen Generate a sample EADC code for Nuvoton MCU with the following configuration:
- IP: EADC0
- Input Mode: Single-end
- Sample Module: 1
- Trigger Source: Software
- Extend Sample Time: 20
- Average Mode: Enabled
- Accumulation: 32 times
- Data Transfer Type: Interrupt
- Interrupts: Enable ADINT0, enable sample module interrupt for module 1 mapped to ADINT0
- IRQn: EADC00_IRQn, IRQHandler: EADC00_IRQHandler
- Optional:
    * Calibration: Enable
    * start conversion after DAC conversion finish
    * add a flag for the loop that waits for the conversion to finish.
    * reading DAC data and displaying the EADC/DAC results in handler
- Purpose: Demonstrate how to get average conversion result by selecting channel 0, performing 32-time accumulation and averaging
```

### UART0 Prompt
```
@nucodegen open UART0 to print conversion results.
```

### Clock Prompt
```
@nucodegen Generate a sample CLK (clock controller) configuration code for Nuvoton MCU with the following configuration:
- Enable Module Clock: UART0_MODULE, GPIOB_MODULE, DAC01_MODULE, EADC0_MODULE
- Module Clock Source: 
    * UART0: HIRC
    * EADC0: APLL0_DIV2
- Module Clock Divider: 
    * UART0: 1
    * EADC0: 2
- Enable Clock Source: HIRC
- Set PLL Frequency: Source: HIRC, Frequency: 220 MHz, Select: CLK_APLL0_SELECT
- Add 50 us clock delay before EADC start conversion.
```

### MFPs Prompt
```
@nucodegen Generate a sample PIN (MFP) configuration code for Nuvoton MCU with the following configuration:
- Port: PA, Pin: PA.1, Function: UART0_TXD
- Port: PA, Pin: PA.0, Function: UART0_RXD
- Port: PB, Pin: PB.13, Function: DAC1_OUT
- Port: PB, Pin: PB.0, Function: EADC0_CH0
```

### GPIO Prompt
```
@nucodegen Generate a sample GPIO code for Nuvoton MCU with the following configuration:
- Port: PB
- Pin Mask: BIT0
- Operation Mode: Input
- Digital Input Path: Disable
- Purpose: Disable digital input path of analog pin EADC0_CH0 to prevent leakage

- Port: PB
- Pin Mask: BIT13
- Operation Mode: Output
- Digital Input Path: Disable
- Purpose: Disable digital input path of analog pin DAC1_OUT to prevent leakage
```
