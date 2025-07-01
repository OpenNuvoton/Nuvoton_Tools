# Zephyr IDE Environment Setup Guide (Nuvoton NuMicro Cortex-M)

This guide walks you through setting up a Zephyr project.

---

## Step 1: Install Required Extension Packs

Install the following extension packs:
- **Nuvoton NuMicro Cortex-M Pack**
- **Zephyr IDE Extension Pack**

![](../../img/ZephyrIDE/install_Nuvoton_Pack.png)
![](../../img/ZephyrIDE/install_Zephyr_Pack.png)

---

Use the Zephyr IDE buttons in the following steps to create the environment.

![](../../img/ZephyrIDE/environment_setup.png)

## Step 2: Creating a Zephyr Project from Sample Code

Create a new project using sample code.
Choose a project template provided by the Zephyr IDE.
![](../../img/ZephyrIDE/select_template.png)

---

## Step 3: Add Build Option and Select Board

Add a build configuration and choose your target board, e.g., `NuMaker-PFM-M467`.

![](../../img/ZephyrIDE/select_board.png)

---

## Step 4: Add Runner Configuration (OpenOCD)

Configure the project runner to use OpenOCD.

![](../../img/ZephyrIDE/add_runner.png)
![](../../img/ZephyrIDE/configuration_complete.png)

---

## Step 5: Update Zephyr Project Runner Settings

Go to `View → Command Palette` and run `Update Zephyr Project Runner`. Select the project to update the runner settings.

![](../../img/ZephyrIDE/update_setting.png)
![](../../img/ZephyrIDE/select_project.png)
![](../../img/ZephyrIDE/update_complete.png)

---

## Step 6: Build Project and Flash to Target

Use the build button to build and flash the firmware to your target board.

![](../../img/ZephyrIDE/build_flash.png)

---

## Step 7: Create launch.json

Create the `launch.json` file used for debugging.

![](../../img/ZephyrIDE/create_launch.json.png)

---

## Step 8: Select Debug Settings

Select `Nuvoton Debug Zephyr`.

![](../../img/ZephyrIDE/select_debug_setting.png)

---

## Step 9: Enter Debug Mode and Start Monitor for Output

Launch the debugger and open the monitor or terminal to view runtime output.

![](../../img/ZephyrIDE/debug_and_monitor.png)
