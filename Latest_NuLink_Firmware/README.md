NuLinkFW revision history:

# v3.13.7537r
# v3.12.7513r
# v3.11.7470r
# v3.10.7443r
# v3.09.7380r
If you upgrade Nu-Link2 firmware from old version to later than v3.09.7380r. 
1. Be sure to install USB driver in the final step of the tool installation.
2. If you are using Nu-Link2-Pro bridge function, see how to configure new defined BRIDGE_MODE on https://github.com/OpenNuvoton/Nuvoton_Tools
3. If you are using Nu-Link2-Pro bridge, there is new USB PIDs for each bridge mode. please update your "NuMicro_ISP_Programming_Tool" later than v4.08 and "USB to Serial Port tool" later than v1.02.  
USB to Serial Port Tool: https://www.nuvoton.com/tool-and-software/software-tool/general/nutool/  
NuMicro_ISP_Programming_Tool: https://www.nuvoton.com/tool-and-software/software-tool/programmer-tool/  
Or just patch new USB PID to your source code to recognize new defines   
   https://github.com/OpenNuvoton/ISPTool/commit/b1d1894d31721d86a56b0c0927da71ebffc117e0  
   https://github.com/OpenNuvoton/NuTool-USB-to-Serial-Port/commit/9b2404b25f55e533dfb8b30377843b25f0da5a0b  
       
