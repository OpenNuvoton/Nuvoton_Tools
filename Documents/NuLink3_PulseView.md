
# PulseView + Nu-Link3 Bridge

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_0.png" width="400">

# PulseView

* Logic Analyzer
  * Supports multiple protocols:
    * UART, SPI, I2C, SWD, …
  * Open-source software
  * Cross-platform support:
    * Windows, Linux, …

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_1.png" width="400">

# Connecting Devices

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_2.png" width="400">

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_3.png" width="400">

# Nu-Link3-Pro

Bridge Connector

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_4.png" width="400">

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_5.png" width="400">

# LA Trigger Conditions

* Each channel can independently configure trigger conditions.

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_6.png" width="400">

# Data Capture and Protocol Analysis

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_7.png" width="400">

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_8.png" width="400">

# File Output

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_9.png" width="400">

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_10.png" width="400">

# Bridge Resource Conflicts

* Nu-Link3-Pro Bridge
  * Interface priority order:
    * MicroPython
    * NuTool USB to Serial Port
    * ISP Bridge
    * NuLogic (PSIO)

# Performance Test

Maximum sample rate and record length for various channel count combinations:

| Channel Count | Max Sample Rate (MHz) | Buffer Size = 256K bytes, Record Length (ms) |     |     |     |
|:-------------:|:--------------------:|:---------------------------------------------:|:---:|:---:|:---:|
|               |                      | Sample Rate                                   |     |     |     |
|               |                      | **1 MHz** | **4 MHz** | **10 MHz** | **22 MHz** |
| 1             | 22                   | 2030     | 520      | 210       | 95        |
| 2             | 22                   | 1050     | 260      | 105       | 48        |
| 4             | 10                   | 520      | 130      | 52        |           |
| 6             | 4                    | 260      | 65       |           |           |



