# IAR EWARM

**Prerequisites:**

- Install **IAR EWARM**.
- Download and install [Nu-Link_IAR_Driver](https://www.nuvoton.com/tool-and-software/ide-and-compiler/) for IAR EWARM before configuring the Nu-Link3-Pro.

---

## Project Settings

1. Open IAR EWARM, and open the project to be configured.

2. In the **Target** tab of the **General Options** page (through invoking **Project → Options**), click the button to the right of the **Device** option and select your target chip.

   ![IAR EWARM Target Chip Selection](../../media/nu-link3/image64.png)
   
   *Figure: IAR EWARM Target Chip Selection*

---

## Debugger and Programmer Settings

3. In the **Setup** tab of the **Debugger** page, select **Third-Party Driver** as the driver.

   ![Set IAR EWARM as Third-Party Driver for Debugger & Programmer](../../media/nu-link3/image65.png)
   
   *Figure: Set IAR EWARM as Third-Party Driver for Debugger & Programmer*

4. In the **Download** tab of the **Debugger** page, make sure that the **Use flash loader(s)** option is selected.

   ![IAR EWARM Programming Settings](../../media/nu-link3/image66.png)
   
   *Figure: IAR EWARM Programming Settings*

5. In the **Download** tab, select the **Override default .board file** option if you want the firmware to be downloaded to APROM or LDROM, and then specify the appropriate .board file.

   ![Select .board File for IAR EWARM](../../media/nu-link3/image67.png)
   
   *Figure: Select .board File for IAR EWARM*

---

## Driver Plugin File Settings

6. In the **Third-Party Driver** page, specify the path of the IAR debugger driver plugin `C:\Program Files\Nuvoton Tools\Nu-Link_IAR\Nu-Link_IAR.dll`.

   ![Set the Path of the IAR EWARM Debugger Driver Plugin](../../media/nu-link3/image68.png)
   
   *Figure: Set the Path of the IAR EWARM Debugger Driver Plugin*

7. Click **OK** to save the settings and return to the IAR EWARM main window.

8. Invoke **Nu-Link3-Pro** to open the Nu-Link form, select **SWD** as the Port, and specify the **Nu-Link3-Pro I/O Voltage** in the **Target power control** section.

   ![Specify the Port and Target I/O Voltage](../../media/nu-link3/image69.png)
   
   *Figure: Specify the Port and Target I/O Voltage*

---

## Compile and Debug

9. After successfully compiling the project, download code to the flash memory and enter debug mode.

   ![Compile and Download the Project](../../media/nu-link3/image70.png)
   
   *Figure: Compile and Download the Project*

10. Click "Go" and the debug message will be printed out. Users can debug the project under debug mode by checking source code, assembly language, peripherals' registers, and setting breakpoint, step run, value monitor, etc.

    ![IAR EWARM Debug Mode](../../media/nu-link3/image71.png)
    
    *Figure: IAR EWARM Debug Mode*
