## Using Multiple Devices for Download and Debug in VS Code

1. Connect multiple devices to the PC, then select Target Information in the VS Code CMSIS extension as shown below to obtain the UID of each CMSIS-DAP device.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/DebugMultiDevice/GetDeviceUID.png" alt="GetDeviceUID.png" width="900">
     </p>

1. Before loading code to the target, modify the CMSIS Load task in tasks.json by adding the desired device UID after cmsisdap:. Then click the Load Application button, and pyOCD will use the device with that UID to perform the code load to the target.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/DebugMultiDevice/SetDownloadDeviceUID.png" alt="SetDownloadDeviceUID.png" width="500">
     </p>

### Debug Configuration Guide: Specifying Device UID

Specify the unique ID (UID) of the target device in your `launch.json` file to ensure the debugger connects to the correct hardware.

---

#### 1. Using pyOCD
To target a specific device using **pyOCD**, you need to modify the device connection string.

* **Instruction:** Locate the device field and append the UID immediately after the `cmsis-dap:` prefix.
* **Format:** `cmsis-dap:<YOUR_DEVICE_UID>`
* **Next Step:** Save the file and click the **Debug Application** button.

     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/DebugMultiDevice/SetDebugDeviceUID.png" alt="SetDebugDeviceUID.png" width="500">
     </p>

#### 2. Using OpenOCD
To target a specific device using **OpenOCD**, you must pass the serial number as a server argument.

* **Instruction:** Add the `serverArgs` property to your configuration and use the `adapter serial` command.
* **Configuration Snippet:**
    ```json
    "serverArgs": [
        "-c", "adapter serial 13150000000A25020450395D00000F80"
    ]
    ```
* **Next Step:** Once added, click the **Debug Application** button to initiate the session.

     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/DebugMultiDevice/SetDebugDeviceUID_OpenOCD.png" alt="SetDebugDeviceUID_OpenOCD.png" width="500">
     </p>

---