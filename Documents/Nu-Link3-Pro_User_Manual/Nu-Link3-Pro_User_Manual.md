# Nu-Link3-Pro User Manual

**Professional Debugger and Programmer for Nuvoton Microcontrollers**

---

## Table of Contents

### [Chapter 1: Overview](ch1_overview.md)
- [1.1 Introduction](ch1_overview.md#11-introduction)
- [1.2 Nu-Link3-Pro Features](ch1_overview.md#12-nu-link3-pro-features)
  - [1.2.1 Programming and Debugging Support](ch1_overview.md#121-programming-and-debugging-support)
  - [1.2.2 Advanced Debugging and Analysis](ch1_overview.md#122-advanced-debugging-and-analysis)

### [Chapter 2: Getting Started](ch2_getting_started.md)
- [2.1 Kit Contents](ch2_getting_started.md#21-nu-link3-pro-kit-contents)
- [2.2 Nu-Link3-Pro PCBA Views](ch2_getting_started.md#22-nu-link3-pro-pcba)
- [2.3 Connector Overview](ch2_getting_started.md#23-nu-link3-pro-overview)
- [2.4 LED Status Indicators](ch2_getting_started.md#24-status-leds)
- [2.5 Firmware Update](ch2_getting_started.md#25-nu-link3-adapter-firmware-update)
- [2.6 Configuration Options](ch2_getting_started.md#26-configuration-options)

### [Chapter 3: Connecting to Target Chip](ch3_connecting.md)
- [3.1 Pin Definitions](ch3_connecting.md#31-nu-link3-pro-compatible-extension-connectors)
  - [3.1.1 SWD Connector Pin Definition](ch3_connecting.md#32-swd-interface-pin-definition-and-function-connection)
  - [3.1.2 Bridge Connector Pin Definition](ch3_connecting.md#33-bridge-interface-pin-definition-and-function-connection)
  - [3.1.3 ETM Connector Pin Definition](ch3_connecting.md#34-etm-interface-pin-definition-and-function-connection)
- [3.2 SWD Port Wiring Diagrams](ch3_connecting.md#321-ice-programming-connection)
  - [3.2.1 ICE Programming Connection](ch3_connecting.md#321-ice-programming-connection)
  - [3.2.2 Virtual COM Connection](ch3_connecting.md#322-virtual-com-connection)
  - [3.2.3 Automatic IC Programming Connection](ch3_connecting.md#323-automatic-ic-programming-connection)
  - [3.2.4 SWO Debug Connection](ch3_connecting.md#324-swo-debug-connection)
- [3.3 Bridge Port Wiring Diagrams](ch3_connecting.md#33-bridge-interface-pin-definition-and-function-connection)
  - [3.3.1 UART Connection](ch3_connecting.md#331-uart-connection)
  - [3.3.2 I2C/I3C Connection](ch3_connecting.md#332-i2ci3c-connection)
  - [3.3.3 SPI Connection](ch3_connecting.md#333-spi-connection)
  - [3.3.4 RS-485 Connection](ch3_connecting.md#334-rs-485-connection)
  - [3.3.5 CAN BUS Connection](ch3_connecting.md#335-can-bus-connection)
  - [3.3.6 PWM and Capture](ch3_connecting.md#336-pwm-and-capture)
  - [3.3.7 ADC Connection](ch3_connecting.md#337-adc-connection)
  - [3.3.8 GPIO Connection](ch3_connecting.md#338-gpio-connection)
- [3.4 ETM Port Wiring Diagrams](ch3_connecting.md#341-swd-and-etm-connection)

### [Chapter 4: Debugging](ch4_debugging.md)
- [4.1 Keil MDK](ch4_1_keil_mdk.md)
  - [4.1.1 Debugger Settings](ch4_1_keil_mdk.md#411-debugger-settings)
  - [4.1.2 Programmer Settings](ch4_1_keil_mdk.md#412-programmer-settings)
  - [4.1.3 ETM Trace Settings](ch4_1_keil_mdk.md#413-etm-trace-settings)
  - [4.1.4 Debug Mode](ch4_1_keil_mdk.md#414-debug-mode)
- [4.2 IAR EWARM](ch4_2_iar_ewarm.md)
  - [4.2.1 Project Settings](ch4_2_iar_ewarm.md#421-project-settings)
  - [4.2.2 Debugger and Programmer Settings](ch4_2_iar_ewarm.md#422-debugger-and-programmer-settings)
  - [4.2.3 Driver Plugin File Settings](ch4_2_iar_ewarm.md#423-driver-plugin-file-settings)
  - [4.2.4 Compile and Debug](ch4_2_iar_ewarm.md#424-compile-and-debug)
- [4.3 Visual Studio Code](ch4_3_vscode.md)

### [Chapter 5: Programming](ch5_programming.md)
- [5.1 ICP Programming Tool](ch5_1_icp_tool.md)
  - [5.1.1 Online ICP Programming](ch5_1_1_online_icp.md)
  - [5.1.2 Offline ICP Programming](ch5_1_2_offline_icp.md)
- [5.2 ISP Programming Tool](ch5_2_isp_tool.md)
  - [5.2.1 Online ISP Programming](ch5_2_1_online_isp.md)
  - [5.2.2 Offline ISP Programming](ch5_2_2_offline_isp.md)
- [5.3 Drag-n-Drop Programming](ch5_3_drag_drop.md)
  - [5.3.1 Functions](ch5_3_drag_drop.md#531-functions)
  - [5.3.2 Updating the Target Chip](ch5_3_drag_drop.md#532-updating-the-target-chip)
  - [5.3.3 Updating Nu-Link Firmware](ch5_3_drag_drop.md#533-updating-nu-link-firmware)
  - [5.3.4 Troubleshooting](ch5_3_drag_drop.md#534-troubleshooting)

### [Chapter 6: Additional Features](ch6_additional_features.md)
- [6.1 PulseView Logic Analyzer](ch6_1_pulseview.md)
- [6.2 MicroPython Support](ch6_2_micropython.md)

### [Chapter 7: Appendix](ch7_appendix.md)
- [7.1 Nu-Link3-Pro Operating Current of ICP](ch7_appendix.md#71-nu-link3-pro-operating-current-of-icp)
- [7.2 Nu-Link3-Pro Operating Current of ISP](ch7_appendix.md#72-nu-link3-pro-operating-current-of-isp)
- [7.3 Automatic IC Programming System](ch7_appendix.md#73-automatic-ic-programming-system)
- [7.4 Nu-Link Debugger and Programmer Comparison](ch7_appendix.md#74-nu-link-debugger-and-programmer-comparison)

---

## Quick Links

| Resource | Description |
|----------|-------------|
| [Nuvoton Website](https://www.nuvoton.com) | Official Nuvoton homepage |
| [NuMicro Software](https://www.nuvoton.com/tool-and-software/software-tool/) | Development tools and software |
| [BSP Downloads](https://github.com/OpenNuvoton) | Board Support Packages on GitHub |

---

## Document Information

- **Document:** UM_Nu-Link3-Pro_EN
- **Revision:** 1.00
- **Date:** 2026.01.20

**Copyright © Nuvoton Technology Corporation. All rights reserved.**
