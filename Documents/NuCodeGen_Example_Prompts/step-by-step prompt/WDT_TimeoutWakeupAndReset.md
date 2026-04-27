# WDT Timeout Wakeup and Reset

## Purpose
This example implements WDT0 time-out interrupt event to wake up system and generate time-out reset system event while WDT time-out reset delay period expired.

## Configuration
- Used Model: Claude Opus 4.5
- Pin Connect:
  - PA.0 are connected to Nulink 3 pro PSIO_CH0 for waveform observation using [PulseView](https://github.com/OpenNuvoton/Nuvoton_Tools/blob/master/Documents/Nu-Link3-Pro_User_Manual/docs/06_additional_features/02_pulseview.md).


## Generation Flow
```mermaid
graph LR
  PMC(PMC) --> WDT(WDT)
  WDT --> GPIO(GPIO)
  GPIO --> UART0(UART0)
  UART0 --> Clock(Clock)
  Clock --> MFPs(MFPs)
```

## Prompts
### PMC Prompt
```
Generate a sample PMC configuration code for Nuvoton MCU with the following configuration:
- IP: PMC
- Power-down Mode: NPD0, Power Level: PL1
- Enter Mode: Power-down
- Optional: 
    * repeatedly enter power-down node in main loop.
- Purpose: Enter power-down mode for demonstration.
```

### WDT Prompt
```
Generate a sample WDT code for Nuvoton MCU with the following configuration:
- IP: WDT0
- Timeout Interval: WDT_TIMEOUT_2POW14
- Reset Delay: WDT_RESET_DELAY_130CLK
- Enable Timeout Reset: TRUE
- Enable Timeout Wakeup: TRUE
- Interrupts: Enable Timeout Interrupt
- IRQn: WDT0_IRQn, IRQHandler: WDT0_IRQHandler
- Optional: 
    * Check if the system recently reset due to WDT before re-initializing.
	* If so, clear reset flag, enter an infinite loop.
    * Reset WDT counter (if timeout interrupt counts < 10) in handler
    * Add a flag to indicate when the timeout-wakeup flag is triggered.
    * Loop and wait after entering power-down mode until the wakeup flag is set in the main loop.
- Purpose: Implement WDT0 time-out interrupt event to wake up system and generate time-out reset system event while WDT time-out reset delay period expired.
```

### GPIO Prompt
```
Generate a sample GPIO code for Nuvoton MCU with the following configuration:
- Port: PA
- Pin Mask: BIT0
- Pin Mode: Output
- Optional: 
    * Set the initial state to low
	* Change the state every time a wakeup occurs.
```

### UART0 Prompt
```
open UART0 to get a character from user to start WDT demonstration before WDT configuration
and print
1. already reset one time when the system recently reset due to WDT before re-initializing
2. ready to enter power-down mode (waiting TX empty before entering power-down mode)
3. the WDT interrupt count after wakeup flag is set.
4. a message to prompt the user to press any key.
```

### Clock Prompt
```
Generate a sample CLK (clock controller) configuration code for Nuvoton MCU with the following configuration:
- Enable Module Clock: UART0, GPIOA, WDT0
- Module Clock Source: 
    * UART0: HIRC
    * WDT0: LIRC
- Module Clock Divider: 
    * UART0: 1
- Enable Clock Source: HIRC, LIRC
- Set PLL Frequency: Source: HIRC, Frequency: 220 MHz, Select: CLK_APLL0_SELECT
```

### MFPs Prompt
```
Generate a sample PIN (MFP) configuration code for Nuvoton MCU with the following configuration:
- Port: PB, Pin: PB.12, Function: UART0_RXD
- Port: PB, Pin: PB.13, Function: UART0_TXD
- Port: PA, Pin: PA.0, Function: GPIO
```

