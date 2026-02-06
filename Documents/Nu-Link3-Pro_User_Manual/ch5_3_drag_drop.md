# 5.3 Drag-n-Drop Programming

## Overview

**Drag-n-Drop Programming** is a method for updating a target device's firmware by treating it as a **Mass Storage Device Class (MSC)**, similar to a USB flash drive. You can simply drag and drop a firmware file onto the device's virtual disk. This process also supports copy commands. The system automatically checks the file format and content, and is compatible with **Windows, Mac, and Linux** operating systems.

## 5.3.1 Functions

This programming method serves two main functions:
* Update the **target chip** firmware
* Update the **Nu-Link firmware**

## 5.3.2 Updating the Target Chip

### Settings
Specific Nu-Link models require certain configurations before connecting to a USB port:
* **Nu-Link1-Me**: Connect the corresponding jumper before plugging in the USB cable.
* **Nu-Link2-Me**: Switch **SW4** to the OFF position before plugging in the USB cable.
* **Nu-Link3**: No configuration is needed.

### Pop-up Disk "NuMicro MCU"
When the device is properly connected, a virtual disk named "**NuMicro MCU**" will appear.
* To update the target chip, drag and drop the firmware file into this disk.
* Supported file formats include **.bin** and **.hex**.
* Dragging an **ERASE.ACT** file will perform a "Chip Erase." The system only recognizes the filename, not its content.
* If an error occurs during the process, a **FAIL.TXT** file is generated.

### Process
The update process involves several steps:
* **Detection**: The system connects to the device, reads its ID, and retrieves flash information.
* **Download**: The system checks the file content (incorrect formats will be treated as errors), loads the programming algorithm, and runs it.
* The algorithm handles initialization, erasing, and programming, but **does not perform verification**.

### Operations
* Only general downloads are available.
* **Erase** operations vary depending on the chip's security features:
    * **Chips without Security Extension**: **Chip Erase** is performed.
    * **Chips with Security Extension**: **Chip Erase** is performed for secure-only cases, while **Page Erase** is performed if a non-secure area exists.
* Supported memory regions include **APROM**, **LDROM**, **Data Flash**, and **Non-Secure APROM**.
* The process is designed to **keep CONFIG 0-3 settings intact**.

### Unsupported
The following are not supported by this programming method:
* **Series**: M030G, 8051, ISDx, NM1x, KM1Mx, etc.
* **Regions**: SPROM, OTP, etc.
* **Settings**: XOM, NSCBA, etc.

## 5.3.3 Updating Nu-Link Firmware

### Settings
Similar to updating the target chip, updating the Nu-Link firmware requires specific settings for different models:
* **Nu-Link1-Me**: Connect the corresponding jumper, then plug in the USB cable.
* **Nu-Link2** or **Nu-Link3** : Press the **offline button**, then plug in the USB cable.

### Pop-up Disk "Nu-Link"
A virtual disk named "**Nu-Link**" will appear. To update the Nu-Link firmware, simply drag and drop the new Nu-Link firmware file into this disk.

## 5.3.4 Troubleshooting

Common issues you might encounter include problems with **USB permissions**, **OS compatibility**, or interference from **antivirus software**.