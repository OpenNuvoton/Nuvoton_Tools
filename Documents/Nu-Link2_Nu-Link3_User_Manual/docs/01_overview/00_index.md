# Overview

## Introduction

The Nuvoton Nu-Link family is a series of powerful debuggers and programmers for Nuvoton
NuMicro® Family microcontrollers. The usage of Nu-Link
can vary from software and hardware development to mass production.

The Nu-Link Debugger and Programmer provides SWD debugging and emulation for NuMicro® Family microcontrollers. It integrates with major IDEs, including Keil MDK, IAR EWARM, and VS Code, allowing developers to program and debug directly within their preferred environment with full access and deep visibility into the microcontroller. Additionally, the Nu-Link features a virtual COM port (VCOM), enabling users to easily print diagnostic messages to a PC.

The Nu-Link can be used as a mass production programmer for
NuMicro® Family microcontrollers. The
Nu-Link can work with the Nuvoton NuMicro® ICP Programming
Tool or serve as a stand-alone ICP programmer. It also provides a
control bus interface that can connect to an automated IC programming
system. The programming process can be triggered by the ICP Programming
tool, a physical button, or an automated IC programming system.

Nu-Link devices also function as In-System Programming (ISP) programmers, supporting firmware upgrades after field deployment.


## Nu-Link Family Comparison

The tables below compare the Nu-Link family of devices.

### Debug

| Function | Nu-Link3-Pro | Nu-Link2-Pro | Nu-Link2 | Nu-Link2-Me | Nu-Link-Me |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Debug via SWD | ✔ | ✔ | ✔ | ✔ | ✔ |
| ETM | ✔ | ✔ | - | - | - |
| pyOCD | ✔ | ✔ | ✔ | ✔ | - |

### Program

| Function | Nu-Link3-Pro | Nu-Link2-Pro | Nu-Link2 | Nu-Link2-Me | Nu-Link-Me |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Online ICP Programming | ✔ | ✔ | ✔ | ✔ | ✔ |
| Offline ICP Programming | ✔ | ✔ | ✔ | ✔ | - |
| Offline ICP-Control Bus | ✔ | ✔ | ✔ | ✔ | - |
| Drag-and-drop flash programming | ✔ | ✔ | ✔ | ✔ | - |
| SWD I/O Voltage Support | 1.8V, 2.5V, 3.3V, 5.0V | 1.8V, 2.5V, 3.3V, 5.0V | 1.8V, 2.5V, 3.3V, 5.0V | 1.8V, 3.3V, 5.0V [^2] | 3.3V, 5.0V [^3] |

### Upgrade

| Function | Nu-Link3-Pro | Nu-Link2-Pro | Nu-Link2 | Nu-Link2-Me | Nu-Link-Me |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Online ISP | ✔ | ✔ | ✔ [^1] | ✔ [^1] | - |
| Offline ISP | ✔ | ✔ | ✔ [^1] | ✔ [^1] | - |

### Storage

| Function | Nu-Link3-Pro | Nu-Link2-Pro | Nu-Link2 | Nu-Link2-Me | Nu-Link-Me |
| :--- | :---: | :---: | :---: | :---: | :---: |
| SPI Flash | ✔ | ✔ | ✔ | ✔ | - |
| SD Card | ✔ | ✔ | - | - | - |
| USB Flash Drive | ✔ | ✔ | - | - | - |

### Bridge

| Function | Nu-Link3-Pro | Nu-Link2-Pro | Nu-Link2 | Nu-Link2-Me | Nu-Link-Me |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Virtual COM | ✔ | ✔ | ✔ | ✔ | ✔ |
| I2C Bridge | ✔ | ✔ | - | - | - |
| I3C Bridge | ✔ | - | - | - | - |
| SPI Bridge | ✔ | ✔ | - | - | - |
| RS-485 Bridge | ✔ | ✔ | - | - | - |
| CAN 2.0 Bridge | ✔ | ✔ | - | - | - |
| CAN FD Bridge | ✔ | - | - | - | - |

### Bus Monitor

| Function | Nu-Link3-Pro | Nu-Link2-Pro | Nu-Link2 | Nu-Link2-Me | Nu-Link-Me |
| :--- | :---: | :---: | :---: | :---: | :---: |
| I2C Bus Monitor | ✔ | ✔ | - | - | - |
| I3C Bus Monitor | ✔ | - | - | - | - |
| SPI Bus Monitor | ✔ | ✔ | - | - | - |
| CAN 2.0 Bus Monitor | ✔ | ✔ | - | - | - |
| CAN FD Bus Monitor | ✔ | - | - | - | - |
| RS-485 Bus Monitor | ✔ | ✔ | - | - | - |

## Additional Features

| Function | Nu-Link3-Pro | Nu-Link2-Pro | Nu-Link2 | Nu-Link2-Me | Nu-Link-Me |
| :--- | :---: | :---: | :---: | :---: | :---: |
| PulseView | ✔ | - | - | - | - |
| MicroPython | ✔ | - | - | - | - |

Table: Nu-Link Family Comparison




## Abbreviations

For simplicity and clarity, some specific terms in this user manual
are contracted or abbreviated, as listed in Table: Nu-Link Debugger/Programmer Technical Abbreviations.

| **Short Name** | **Full Name** |
| --- | --- |
| Nu-Link | Nuvoton Nu-Link Family (Nu-Link standalone unit, Nu-Link-ME, Nu-Link-Pro, Nu-Link2 standalone unit, Nu-Link2-ME, Nu-Link2-Pro, Nu-Link3-Pro, etc.) |
| Nu-Link1 family | Nu-Link standalone unit, Nu-Link-ME, Nu-Link-Pro |
| Nu-Link2 family | Nu-Link2 standalone unit, Nu-Link2-ME, Nu-Link2-Pro |
| Nu-Link3 family | Nu-Link3-Pro |
| ICP Tool | Nuvoton NuMicro® ICP Programming Tool |
| Keil MDK | Keil ARM Microcontroller Development Kit (MDK-ARM®) |
| IAR EWARM | IAR Embedded Workbench for ARM |
| VS Code | Visual Studio Code |
| NuEclipse | NuEclipse Integrated Development Environment |
| SWD | Serial Wire Debug |
| ICP | In-Circuit Programming |
| ISP | In-System Programming |
| ETM | Embedded Trace Macrocell |

Table: Nu-Link Debugger/ Programmer Technical Abbreviations


[^1]: Only supports the UART interface for ISP updates.<br>
[^2]: Voltage is adjusted by resistor ICEJPR1.<br>
[^3]: Voltage is adjusted by resistor JPR1.
