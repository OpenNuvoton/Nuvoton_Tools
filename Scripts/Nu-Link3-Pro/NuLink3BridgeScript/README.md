# Nu-Link3-Pro Bridge Scripts

## Overview
This collection of Python scripts provides bridge functionality for Nuvoton's Nu-Link3-Pro debugger/programmer. The scripts run on the PC side and communicate with target devices through the Nu-Link3-Pro hardware bridge. They enable communication with target devices via I2C, SPI, and CAN interfaces.

## Scripts Included
- **i2c_master.py**: I2C master mode operations.
- **spi_master.py**: SPI master mode operations.
- **can_normal.py**: CAN normal mode operations.
- **can_monitor.py**: CAN bus monitoring.

**Note**: Compared to Nu-Link2-Pro, Nu-Link3-Pro bridge do not include dedicated I2C and SPI monitor modes. Nu-Link3-Pro use [PulseView](../../../Documents/Nu-Link3-Pro_User_Manual/ch6_1_pulseview.md) for I2C and SPI signal monitoring and protocol analyzing instead.

## Features
- **Host Mode**: Act as a host to transparently communicate with target chips via Nu-Link3-Pro.
- **Monitor Mode**: Detect and capture data transmitted on the bus lines via Nu-Link3-Pro.
- Support for I2C, SPI, and CAN interfaces in master, slave, monitor, and normal modes.
- Real-time bus monitoring and data logging/display.

## Requirements
- Nu-Link3-Pro hardware configured in bridge mode.
- Python 3.x with `pyserial` library (`pip install pyserial`).
- Serial port connection (e.g., COM11 on Windows).
- Target device connected to Nu-Link3-Pro bridge pins.

## Installation
1. Ensure Nu-Link3-Pro is connected and in bridge mode (refer to Nu-Link3-Pro documentation).
2. Install dependencies:
   ```
   pip install pyserial
   ```
3. Clone or download the scripts to your local machine.

## Usage
1. Connect the target device to the appropriate Nu-Link3-Pro bridge pins (I2C: SDA/SCL, SPI: MOSI/MISO/SCK, CAN: CANH/CANL).
2. Run the desired script:
   ```
   python i2c_master.py
   ```
   - Modify the serial port in the script if necessary (default: COM11).
   - Adjust parameters like baud rate or clock speed as needed.

## Configuration
- **Serial Port**: Update `serial.Serial("COM11", ...)` to match your system's port.
- **Baud Rate/Clock**: Adjust `i2c_clock` or similar variables for your interface speed.


## Troubleshooting
- **Serial Port Error**: Ensure Nu-Link3-Pro is connected and the port is correct.
- **No Data**: Check bridge mode configuration and target device connections.
- **Permission Issues**: Run as administrator or adjust serial port permissions.

## References
- [Nu-Link3-Pro Documentation](../../../Documents/Nu-Link3-Pro_User_Manual/Nu-Link3-Pro_User_Manual.md)

