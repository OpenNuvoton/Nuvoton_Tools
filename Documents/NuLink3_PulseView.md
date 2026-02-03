
# PulseView and Nu-Link3-Pro Integration

This document details the integration between the **Nu-Link3-Pro** debugging adapter and **PulseView**, the popular GUI for the sigrok logic analyzer software suite. By leveraging the specific hardware capabilities of the Nu-Link3-Pro. This integration provides a seamless workflow for visualizing digital signals, decoding protocols, and troubleshooting embedded systems directly on the PC.

You can download the PulseView software from [here](https://github.com/OpenNuvoton/pulseview/Releases).

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_0.png" width="400">

Figure: System block diagram

# PulseView Logic Analysis

PulseView provides a rich set of features for analyzing digital logic signals captured by the Nu-Link3-Pro:

- **Comprehensive Protocol Support**: Native support for decoding a wide variety of standard communication protocols including UART, SPI, I2C, I2S, CAN, and SWD. This allows developers to see high-level data packets alongside raw signal waveforms.
- **Cross-Platform Compatibility**: The software is designed to run efficiently on major operating systems, fully supporting both Windows and Linux environments.

  <img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_1.png" width="400">  

  Figure: Nu-Link3-Pro logic analyzer monitoring signals via PulseView

# Device Connectivity

The Nu-Link3-Pro device establishes a connection with external hardware through a dedicated bridge connector.

- **Hardware Interface**: The device utilizes the dedicated bridge connector (CON.6) to interface with external circuits.
- **Signal Integrity**: This connection is optimized to maintain signal integrity during high-speed sampling, ensuring that the captured data accurately reflects the state of the target system.

  <img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_3.png" width="400">

  Figure: illustrates the process of opening the ‘Connect to Device’ dialog, which is the initial step for establishing connectivity.

Once the dialog is open, users should select the ‘Nuvoton Nu-Link3-Pro with 6 channels’ option to proceed with the connection. This selection specifies the exact device configuration used for logic analysis and protocol testing.

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_2.png" width="400">

Figure: demonstrates how to select the appropriate device from the available options within the interface.

The subsequent figure involves identifying the PSIO (Programmable Serial Input/Output) pins utilized during operation. The reference diagram provides a visual representation of the bridge pins (CON.6) that are used to facilitate connections to external circuits.

Bridge connector pins (CON.6)

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_5.png" width="400">

Figure: shows the layout and assignment of the bridge pins, offering clarity for hardware integration and signal routing.

# LA Trigger Conditions

Each logic analyzer channel allows independent configuration of trigger conditions, enhancing flexibility during signal monitoring and analysis.

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_6.png" width="400">

Figure: Select trigger type for channels

# Data Capture and Protocol Analysis

PulseView offers functionality to add protocol decoders, which interpret the captured data according to specific communication standards. Below figure illustrates the process of adding a protocol decoder in the PulseView interface.


<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_7.png" width="400">

Figure: Add protocol decoder of PulseView

For example, when analyzing UART communication, a UART protocol decoder can be added to PulseView. 

Below figure demonstrates the addition of this decoder, enabling the software to interpret and display UART data streams in a human-readable format.

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_8.png" width="400">

Figure: Add protocol decoder of PulseView (UART)

Captured data can be exported to files, providing flexibility for storing and reviewing results later. This feature ensures that critical information is not lost and can be referenced for further analysis or reporting purposes.

PulseView includes an option to export annotations related to protocol analysis. These annotations include details such as decoded data values, timing information, and other relevant metadata. 

<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_10.png" width="300">
<img src="../img/NL3_PulseView/NL3_PulseView_NuLogic_9.png" width="100">

Figure: The process of exporting these annotations for documentation or further examination.



# Performance Test

Maximum sample rate and record length for various channel count combinations:

| Channel Count | Max Sample Rate (MHz) | Buffer Size = 1M bytes, Record Length (ms) |     |     |     |
|:-------------:|:--------------------:|:---------------------------------------------:|:---:|:---:|:---:|
|               |                      | Sample Rate                                   |     |     |     |
|               |                      | **1 MHz** | **4 MHz** | **10 MHz** | **22 MHz** |
| 1             | 22                   | 8120     | 2080      | 840       | 380        |
| 2             | 22                   | 4200     | 1040      | 420       | 192        |
| 4             | 10                   | 2080      | 520      | 208        |           |
| 6             | 4                    | 1040      | 260       |           |           |



