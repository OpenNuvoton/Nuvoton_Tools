## Outline
- [Zephyr Project Setup Guide for Nuvoton NuMicro Cortex-M](#zephyr-project-setup-guide-for-nuvoton-numicro-cortex-m)
- [Trouble Shooting](#trouble-shooting)

## Zephyr Project Setup Guide for Nuvoton NuMicro Cortex-M

1. Install Required Extension Packs

    Install the following extension packs:

    - **Nuvoton NuMicro Cortex-M Pack**
    - **Zephyr IDE Extension Pack**

     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_Nuvoton_Pack.png" alt="install_Nuvoton_Pack.png" width="600">
     </p>
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_Zephyr_Pack.png" alt="install_Zephyr_Pack.png" width="600">
     </p>
1. Click the Zephyr IDE Configuration option, then click Host Tools to install the environment.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/setup_configuration.png" alt="setup_configuration.png" width="900">
     </p>
1. Need to manually install the winget tool first.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_manager.png" alt="install_manager.png" width="900">
     </p>
1. Install the related packages by clicking "install" button according to the status detected by the Zephyr IDE extension.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/required_development_tools.png" alt="required_development_tools.png" width="900">
     </p>

1. Select initialize current directory -> create new west.yml -> Full Zephyr.
After that, wait for a while as the Zephyr Project files and configurations are downloaded and the workspace is created.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/workspace_setup.png" alt="workspace_setup.png" width="900">
     </p>
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/create_west_yml.png" alt="create_west_yml.png" width="600">
     </p>
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/full_zephyr.png" alt="full_zephyr.png" width="300">
     </p>
1. Creating a Zephyr Project from Sample Code

    Create a new project using sample code.
    Choose a project template provided by the Zephyr IDE.
   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_template.png" alt="select_template.png" width="600">
   </p>

1. Add a build configuration and choose your target board, e.g., `NuMaker-PFM-M467`.
   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_board.png" alt="select_board.png" width="600">
   </p>

1. Add Runner Configuration (OpenOCD)
  Configure the project runner to use OpenOCD.
   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/configuration_complete.png" alt="configuration_complete.png" width="600">
   </p>

1. Update Zephyr Project Runner Settings

    Go to `View → Command Palette` and run `Update Zephyr Project Runner`. Select the project to update the runner settings and refresh the settings.

   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/update_setting.png" alt="update_setting.png" width="300">
   </p>
   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_project.png" alt="select_project.png" width="300">
   </p>
   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/update_complete.png" alt="update_complete.png" width="600">
   </p>
   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/refresh_settings.png" alt="refresh_settings.png" width="600">
   </p>

1. Set the target type
  Please choose the target type for debugging according to the project.
   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_target_type.png" alt="select_target_type.png" width="600">
   </p>
   
1. Build Project and Flash to Target
  Use the build button to build and flash the firmware to your target board.

   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/build_flash.png" alt="build_flash.png" width="300">
   </p>

1. Create launch.json
  Create the launch.json file used for debugging.

   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/create_launch.json.png" alt="create_launch.json.png" width="600">
   </p>

1. Set the runToEntryPoint (optional)
  If you don’t want execution to stop at the main function when running in debug mode, set the runToEntryPoint parameter and specify the symbol function where you want it to stop (for example, Zephyr’s execution entry point z_arm_reset; for Nuvoton BSP projects, the entry point is Reset_Handler).

   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/entrypoint_setting.png" alt="entrypoint_setting.png" width="600">
   </p>


1. Select Debug Settings
  Select Nuvoton Debug Zephyr.

   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_debug_setting.png" alt="select_debug_setting.png" width="600">
   </p>

1. Enter Debug Mode and Start Monitor for Output
  Launch the debugger and open the monitor or terminal to view runtime output.

   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/add_runner.png" alt="add_runner.png" width="600">
   </p>
   <p>
       <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/debug_and_monitor.png" alt="debug_and_monitor.png" width="600">
   </p>

## Trouble Shooting

1. Problem with winget tool installation.

   From this webpage (https://github.com/microsoft/winget-cli/releases), download the two files shown in the red box. Please download the appropriate winget version according to your operating system version.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/download_winget.png" alt="download_winget.png" width="900">
     </p>
   First, unzip the ZIP file, go into the x64 folder, open PowerShell, and enter the commands below in order to install the three dependency files:

    winget v1.12
    ```
    Add-AppPackage -Path .\Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64.appx
    Add-AppPackage -Path .\Microsoft.VCLibs.140.00_14.0.33519.0_x64.appx
    Add-AppPackage -Path .\Microsoft.WindowsAppRuntime.1.8_8000.616.304.0_x64.appx
    ```

    winget v1.11
    ```
    Add-AppPackage -Path .\Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64.appx
    Add-AppPackage -Path .\Microsoft.UI.Xaml.2.8_8.2310.30001.0_x64.appx
    ```

    Then enter the following command to install the winget tool:

    ```
    Add-AppPackage -Path .\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
    ```
    
1. Problem with related packages installation.

   If the installation fails, as shown in the red text in the image, you can open the OUTPUT panel in the terminal and select the Zephyr IDE option.
     <p>
         <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_tool_message.png" alt="install_tool_message.png" width="900">
     </p>
   If installing gperf and wget results in error messages, you can manually install them from the terminal by adjusting the parameters:

    ```
    winget install --accept-package-agreements --accept-source-agreements gperf --source winget
    winget install --accept-package-agreements --accept-source-agreements wget --source winget
    ```