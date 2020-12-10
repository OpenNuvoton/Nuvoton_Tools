# NuMicro software development tools  
[Nuvoton tools official website](https://www.nuvoton.com/tool-and-software/software-development-tool/driver/)  
<br>
IDE and Debugger
- [KEIL Nu-Link debugger driver installer](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW1120200221180521)
- [IAR Nu-Link debugger driver installer](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW1120200221180914)
- [NuEclipse installer](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW1120200401182901)
- [PinView installer](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW1320200221181935)  
- [Customized pyOCD source code](https://github.com/OpenNuvoton/pyOCD) (using adapter firmware "NuLink2_DAPLink.bin")
- [Customized openOCD source code](https://github.com/OpenNuvoton/OpenOCD-Nuvoton)  (using adapter firmware "NuLink2FW.bin")

Programmer  
- [ICPTool installer](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW1720200221181328)  
- [ISPTool installer](https://www.nuvoton.com/opencms/resource-download.jsp?tp_GUID=SW0320101221101703)  
- [ISPTool source code](https://github.com/OpenNuvoton/ISPTool)    
- [ISPTool command set document](./doc/NuMicro_ISP_Flow_And_Command_Set.pdf)    
- [NuLink command tool installer](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW1720200221181644)  

Coding assistant  
- [NuTool-PinConfigure](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW1320200319135912)
- [NuTool-ClockConfigure](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW1320200930114649)

Signal pass-through/monitor (I2C/SPI/CAN of Nu-Link2-Pro): 
- [NuTool-USB_to_Serial_Port](https://www.nuvoton.com/resource-download.jsp?tp_GUID=SW1320201210175128) 

<br>
<br>

# Nu-Link2-Pro debugging and programming adapter
When using software development tools above, you may need an USB adapter. 
We introduce you a new feature-rich Nu-Link2-Pro adapter here.   
- [Where to buy](https://direct.nuvoton.com/tw/Nu-Link2-pro)   
- [User manual](https://www.nuvoton.com/resource-download.jsp?tp_GUID=UG1320200319174043)  

An overview picture of software tools, adapter and targets  
![](img/nulink2-1.PNG)
![](img/nulink2-2.PNG)
![](img/nulink2-3.PNG)

### The firmware of Nu-Link2-Pro adapter
All Nu-Link2-Pro firmware binary files can be found [here](./Latest_NuLink_Firmware)  
User can re-program Nu-Link2-Pro to another .bin file by the following instructions (Windows OS)  
1. Press the button on Nu-Link2-Pro and plug in USB cable.
2. A "Nu-Link2-Pro" disk will show.  (If you see disk name is "NuMicro MCU", it will upgrade target device firmware instead of Nu-Link2-Pro itself) 
3. Drag and drop Nu-Link2-Pro firmware .bin file into the disk.
4. Re-plug the USB cable and it's done.  

More options for NuLink2FW (configuration file NU_CFG.TXT)
1. When you upgrade the NuLink2FW.bin larger than version v7143, open NU_CFG.TXT file in pop-up "NuMicro MCU" disk, you will see some options in NU_CFG.TXT.  
![](img/NUTXT.png)
2. For example, you can see BRIDGE_MODE and CMSIS-DAP options.
* Set BRIDGE_MODE=1 then re-plug in USB cable, the pass-through bridge function of Nu-Link2-Pro will be enabled (The word Nu-Link2-Bridge will be used to represent the pass-through bridge application on Nu-Link2-Pro adapter). Nu-Link2-Bridge pass-through the data between VCOM port and I2C/SPI/RS485/CAN interfaces.  
(You will see an "Nu-Link2-Bridge Virtual Com Port" in device manager.)  
![](img/device_manager.png)
* Set BRIDGE_MODE=0 then re-plug in USB cable, an USB HID interface supports ISP Tool will be enabled. This USB HID interface doesn't pass through data, it communicates with ISPTool via HID_ISP, and offers I2C/SPI/RS485/CAN interfaces for ISPTool.  
(You will see an USB HID interface [HID_ISP][VID:0x0416, PID:0x520*, interface:05] in device manager.)  
* Set CMSIS-DAP=1 then re-plug in USB cable, it presents one more interface HID_CMSIS-DAP, this is handy if you want to use CMSIS-DAP protocol.
(You will see an USB HID interface [HID_CMSIS-DAP][VID:0x0416, PID:0x520*, interface:06] in device manager.)

### Comparison of NuLink2FW.bin and NuLink2_DAPLink.bin  
#### [NuLink2FW.bin](./Latest_NuLink_Firmware)
- Proprietary code 
- Support NuMicro 8051, offline programming, user code read-out protection, unlimited flash break points, NuMicro chips specific features (config0/config1 dataflash setting, KPROM, etc.)
- USB interfaces: HID_ICE(proprietary commands)/MSC/VCOM/HID_CMSIS-DAP/HID_ISP or VCOM_Nu-Link2-Bridge (set in NU_CFG.TXT)

#### [NuLink2_DAPLink.bin](./Latest_NuLink_Firmware)
- Open source: [DAPLink on Nu-Link2-Pro](https://github.com/OpenNuvoton/DapLink)  
- Support many third party IDE
- USB interfaces: HID(CMSIS-DAP commands)/MSC/VCOM 

### Some other example projects for NuLink2  
- [Nu-Link2-Pro_Offline_ISP](https://github.com/OpenNuvoton/Nu-Link2-Pro_Offline_ISP)
- [NuLink2_ICP_Library](https://github.com/OpenNuvoton/NuLink2_ICP_Library)
            
<br>
<br>


