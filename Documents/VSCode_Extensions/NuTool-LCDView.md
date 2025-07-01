# 🔧 LCDView Environment Setup Guide

This guide walks you through setting up a LCDView project.

---

## ✅ Step 1: Install Required Extension Packs

Install the following extension packs:
- **Nuvoton NuMicro Cortex-M Pack**
- **NuTool-LCDView**

---

## ✅ Step 2: Prepare your NuMicro BSP project.
You can choose from the following options
- Go to [Nuvoton Technology Corp](https://github.com/opennuvoton), and download the project which you need.

---

## ✅ Step 3: Launch Visual Studio Code, choose "Open Folder...", and select VSCode folder in your project.

## ✅ Step 4: Open `launch.json` file, click `Add Configuration...` button, and type `Nuvoton Debug` to insert the configuration as below.
    {
        "name": "Nuvoton Debug",
        "type": "cortex-debug-nuvoton",
        "request": "launch",
        "cwd": "${workspaceFolder}",
        "executable": "${command:embedded-debug.getApplicationFile}",
        "servertype": "openocd",
        "serverpath": "${command:openocd-helper.getOpenOcdPath}",
        "svdFile": "${command:openocd-helper.getSvdPath}",
        "configFiles": [
            "interface/cmsis-dap.cfg",
            "${command:openocd-helper.getOpenOcdConfigPath}"
        ],
        "runToEntryPoint": "main"
    },

---

## ✅ Step 5: Click `CMSIS`, then execute `Build solution` and `Run`

<img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/LCDView/step3.jpg" width="300"  />

---



## ✅ Step 6: Click `Run and Debug` and select `Nuvoton Debug`

## ✅ Step 7: Set breakpoints and then click `Start Debugging`

## ✅ Step 8: Open LCDView to observe LCD view
- Load project, please select M258KG6AE.nvt
- Switch to Emulator Mode
![](../../img/LCDView/step7.jpg)

---