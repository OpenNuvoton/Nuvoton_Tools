## Using Multiple Devices for Download and Debug in VS Code

1. Connect multiple devices to the PC, then select Target Information in the VS Code CMSIS extension as shown below to obtain the UID of each CMSIS-DAP device.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/DebugMultiDevice/GetDeviceUID.png" alt="GetDeviceUID.png" width="900">
     </p>

1. Before loading code to the target, modify the CMSIS Load task in tasks.json by adding the desired device UID after cmsisdap:. Then click the Load Application button, and pyOCD will use the device with that UID to perform the code load to the target.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/DebugMultiDevice/SetDownloadDeviceUID.png" alt="SetDownloadDeviceUID.png" width="500">
     </p>

1. Before entering debug mode, modify launch.json by adding the desired device UID after cmsisdap:. Then click the Debug Application button, and the device with that UID will be used when entering debug mode.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/DebugMultiDevice/SetDebugDeviceUID.png" alt="SetDebugDeviceUID.png" width="500">
     </p>
