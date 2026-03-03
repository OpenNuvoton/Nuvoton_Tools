# I2C Master and Slave

## Purpose
This example demonstrates how to use I2C in Master and Slave mode for loopback data testing.

## Configuration
- Used Model: Claude Opus 4.5
- Pin Connect:
  - I2C0_SCL and I2C1_SCL are connected together for loopback testing.
  - I2C0_SDA and I2C1_SDA are connected together for loopback testing.

## Generation Flow
```mermaid
graph LR
  I2C0/1(I2C0/1) --> UART0(UART0)
  UART0 --> Clock(Clock)
  Clock --> MFPs(MFPs)
```

## Prompts
### I2C0/1 Prompt
```
@nucodegen Generate a sample I2C code for Nuvoton MCU with the following configuration:
- IP: I2C0, I2C1
- Bus Clock: 100 kHz
- Mode: I2C0: Master, I2C1: Slave
- Slave Address: 0x16
- Data Transfer Type: Interrupt
- Interrupts: Enable I2C interrupt
- IRQn: I2C0_IRQn, IRQHandler: I2C0_IRQHandler
- IRQn: I2C1_IRQn, IRQHandler: I2C1_IRQHandler
- Optional: 
   * add a flag for the loop to wait transfer is done.
   * Master send W(write) or R(read)  based on test type
- Purpose: 
    * test 1：write 128 bytes from master to slave address 0x16
    * test 2：read 128 bytes from slave to master
```

### UART0 Prompt
```
@nucodegen open UART0 to print comparison results between arrays.
```

### Clock Prompt
```
@nucodegen Generate a sample CLK (clock controller) configuration code for Nuvoton MCU with the following configuration:
- Enable Module Clock: UART0_MODULE, I2C0_MODULE, I2C1_MODULE
- Module Clock Source: 
    * UART0: CLK_UARTSEL0_UART0SEL_HIRC
- Module Clock Divider: 
    * UART0: CLK_UARTDIV0_UART0DIV(1)
- Enable Clock Source: CLK_SRCCTL_HIRCEN_Msk
- Set PLL Frequency: Source: CLK_APLLCTL_APLLSRC_HIRC, Frequency: 220 MHz, Select: CLK_APLL0_SELECT
```

### MFPs Prompt
```
@nucodegen Generate a sample PIN (MFP) configuration code for Nuvoton MCU with the following configuration:
- Port: PB, Pin: PB.12, Function: UART0_RXD
- Port: PB, Pin: PB.13, Function: UART0_TXD
- Port: PG, Pin: PG.0, Function: I2C0_SCL
- Port: PG, Pin: PG.1, Function: I2C0_SDA
- Port: PG, Pin: PG.2, Function: I2C1_SCL
- Port: PG, Pin: PG.3, Function: I2C1_SDA
```
