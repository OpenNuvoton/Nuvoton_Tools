
## Nu-Link2-Pro Features

- Supports programming and debugging of all NuMicro® Family
  microcontrollers

- Supports In-Circuit Programming (ICP)


- Selectable SWD output voltage (1.8 V / 2.5 V / 3.3 V / 5.0 V)

- ICP Programming Tool with image file protection

- Drag & drop Flash programming

- USB flash drive, SD card and SPI Flash as image file storage

- Start button

- Automatic IC programming system connector (Control Bus)

- Powered by Micro USB or target-powered via SWD interface


- Support In-System Programming (ISP)


- Via multi-interfaces bridge

- Supports PC control ISP

- Supports ISP Programming Tool


- Supports multi-debug interfaces and tool


- Supports Serial Wire Debug (SWD)

- Supports high speed up to 96 MHz of Embedded Trace Macrocell (ETM)

- Unlimited breakpoint and step execution

- Supports Arm DAPLink

- Supports PyOCD


- Supports multi-interface analyzer


- SPI, I2C, CAN and RS-485 signal monitor


- Supports multiple bridge connections


- Multi-interface bridge for ISP function (I2C, SPI, CAN,
  UART, RS-485, LIN)

- Virtual COM port by USB  




### System Overview

Overview of software tools, Nu-Link2-Pro adapters, and targets:

![debugger](../../media/nu-link2/7380_BM0.PNG)

![bridge](../../media/nu-link2/7380_BM1.PNG)

![monitor](../../media/nu-link2/7380_BM1_MON.PNG)

![isp](../../media/nu-link2/7380_BM2.png)

![bootloader isp](../../media/nu-link2/7443_BM3.png)

### Driver Installation

For Windows operating systems, please download and install the [Nu-Link_USB_Driver](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW1120201207161057)

### Nu-Link2-Pro Firmware

Download the latest firmware from the [Releases page](https://github.com/OpenNuvoton/Nuvoton_Tools/releases).

Users can reprogram Nu-Link2-Pro with another .bin file using the following instructions (Windows OS):

1. Press the button on Nu-Link2-Pro and plug in the USB cable.
2. The "Nu-Link2-Pro" disk will appear. (If you see the disk name as "NuMicro MCU", it will upgrade the target device firmware instead of Nu-Link2-Pro itself.)
3. Drag and drop the Nu-Link2-Pro firmware .bin file into the disk.
4. Re-plug the USB cable and it's done.

### Configuration Options

1. When you upgrade NuLink2FW.bin to a version greater than or equal to v3.09.7380, you will see some options in NU_CFG.TXT:

- Open the NU_CFG.TXT file in the pop-up "NuMicro MCU" disk

    ![NU_CFG.TXT](../../media/NUTXT.png)

2. For the Nu-Link2-Pro, you will see POWER-MODE and BRIDGE-MODE options. You need to re-plug the USB cable to activate the setting.

- Set POWER-MODE for SWD output voltage level (mainly for CMSIS-DAP interface use).

- Set BRIDGE-MODE=0; this is the default setting. It has a WebUSB interface conforming to the CMSIS-DAP protocol, and you can connect to KEIL Studio Desktop/Cloud via this interface. Note that CMSIS-DAP will be disabled in other BRIDGE-MODEs (limited USB endpoints).  

    ![DEV_WEBUSB](../../media/nu-link2/7380_DEV_WEBUSB_2005.PNG)

- Set BRIDGE-MODE=1; the pass-through bridge function of Nu-Link2-Pro will be enabled ("Nu-Link2-Bridge" refers to the pass-through bridge application on the Nu-Link2-Pro adapter). Nu-Link2-Bridge passes data between the VCOM port and I2C/SPI/RS485/CAN interfaces.
    (You will see a "Nu-Link2-Bridge Virtual Com Port" in Device Manager.)  

    ![device VCOM](../../media/nu-link2/device_manager.png)

- Set BRIDGE-MODE=2; a USB HID interface that supports ISPTool will be enabled. This USB HID interface doesn't pass through data; it communicates with ISPTool via HID_ISP and offers I2C/SPI/RS485/CAN interfaces for ISPTool.

- Set BRIDGE-MODE=3; a USB HID interface that supports Boot_Loader_ISPTool will be enabled. This USB HID interface doesn't pass through data; it communicates with Boot_Loader_ISPTool via HID_MKROM_ISP, and offers I2C/SPI/RS485/CAN interfaces for Boot_Loader_ISPTool. (This mode requires firmware v3.10 or later.)
    Only NuMicro chips that support mask ROM Boot Loader (e.g., M460 series) can communicate with [Boot_Loader_ISPTool](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW132022071806572776&currentFolder=/products/microcontrollers/arm-cortex-m4-mcus/m467-ethernet-crypto-series/).

3. If you use Nu-Link2-ME, it doesn't support BRIDGE functions, and you will only see the CMSIS-DAP option.

- Set CMSIS-DAP=1; this is the default setting. It has a WebUSB interface conforming to the CMSIS-DAP protocol, and you can connect to KEIL Studio Cloud via this interface.
- Set CMSIS-DAP=0; this will disable CMSIS-DAP and enable the Nu-Link2 "USB BULK_ICE" interface (it's faster than "USB HID_ICE").


### Other Example Projects for Nu-Link2

- [DAPLink for Nu-Link2 family](https://github.com/OpenNuvoton/DapLink)
- [CMSIS_DAP for Nu-Link2 family](https://github.com/OpenNuvoton/NuLink2_CMSIS_DAP)
- [ICP_Library for Nu-Link2 family](https://github.com/OpenNuvoton/NuLink2_ICP_Library)


### Comparison of Nu-Link2 and DAPLink

Nu-Link2

- Proprietary code
- Supports NuMicro 8051, offline programming, encryption during data transmission, unlimited flash breakpoints, NuMicro chip-specific features (config0/config1 dataflash setting, KPROM, etc.)
- USB interfaces: MSC/VCOM/HID_ICE (proprietary commands) or CMSIS-DAPv2 WinUSB + WebUSB CMSIS-DAP/VCOM_Nu-Link2-Bridge or HID_ISP (defined by BRIDGE-MODE in NU_CFG.TXT)

DAPLink

- Open source: [DAPLink for Nu-Link2 family](https://github.com/OpenNuvoton/DapLink)
- Supports many third-party IDEs
- USB interfaces: MSC/CDC/CMSIS-DAPv2 WinUSB/WebUSB CMSIS-DAP

CMSIS_DAP

- Open source: [CMSIS_DAP for Nu-Link2 family](https://github.com/OpenNuvoton/NuLink2_CMSIS_DAP)
- Supports many third-party IDEs