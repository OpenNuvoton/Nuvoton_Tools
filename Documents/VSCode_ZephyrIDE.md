## Outline
- [Zephyr Project Setup Guide for Nuvoton NuMicro Cortex-M](#zephyr-project-setup-guide-for-nuvoton-numicro-cortex-m)
- [Trouble Shooting](#trouble-shooting)

## Zephyr Project Setup Guide for Nuvoton NuMicro Cortex-M

1. Install Required Extension Packs

    Install the following extension packs:

    - **Nuvoton NuMicro Cortex-M Pack**
    - **Zephyr IDE Extension Pack**

     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_Nuvoton_Pack.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_Nuvoton_Pack.png" alt="install_Nuvoton_Pack.png" width="800">
         </a>
     </p>
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_Zephyr_Pack.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_Zephyr_Pack.png" alt="install_Zephyr_Pack.png" width="800">
         </a>
     </p>
1. Click the Host Tools option to install the environment.
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/setup_configuration2.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/setup_configuration2.png" alt="setup_configuration2.png" width="1200">
         </a>
     </p>
1. Download and install the SDK version that matches your Zephyr version.
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_sdk.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_sdk.png" alt="install_sdk.png" width="900">
         </a>
     </p>

1. Select initialize current directory -> Full Zephyr.
After that, wait for a while as the Zephyr Project files and configurations are downloaded and the workspace is created.
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/workspace_setup2.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/workspace_setup2.png" alt="workspace_setup2.png" width="900">
         </a>
     </p>
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/full_zephyr.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/full_zephyr.png" alt="full_zephyr.png" width="300">
         </a>
     </p>
1. Creating a Zephyr Project from Sample Code

    Create a new project using sample code.
    Choose a project template provided by the Zephyr IDE.
   <p>
       <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_template2.png" target="_blank">
           <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_template2.png" alt="select_template2.png" width="1200">
       </a>
   </p>

1. Add a build configuration and choose your target board, e.g., `NuMaker-PFM-M467`.
   <p>
       <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_board.png" target="_blank">
           <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_board.png" alt="select_board.png" width="600">
       </a>
   </p>

1. Add Runner Profiles
  Configure the project runner to use PYOCD.
   <p>
       <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/add_runner_profiles.png" target="_blank">
           <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/add_runner_profiles.png" alt="add_runner_profiles.png" width="1200">
       </a>
   </p>
   
1. Build Project and Flash to Target and Debug Target
  Use the build button to build and flash the firmware to your target board and debug your target.

   <p>
       <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/build_flash2.png" target="_blank">
           <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/build_flash2.png" alt="build_flash2.png" width="1200">
       </a>
   </p>

## Trouble Shooting

1. Problem with winget tool installation.

   From this webpage (https://github.com/microsoft/winget-cli/releases), download the two files shown in the red box. Please download the appropriate winget version according to your operating system version.
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/download_winget.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/download_winget.png" alt="download_winget.png" width="600">
         </a>
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
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_tool_message.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_tool_message.png" alt="install_tool_message.png" width="900">
         </a>
     </p>
   If installing gperf and wget results in error messages, you can manually install them from the terminal by adjusting the parameters:

    ```
    winget install --accept-package-agreements --accept-source-agreements gperf --source winget
    winget install --accept-package-agreements --accept-source-agreements wget --source winget
    ```