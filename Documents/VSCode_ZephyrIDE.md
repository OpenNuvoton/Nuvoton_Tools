## Outline
- [Zephyr Project Setup Guide for Nuvoton NuMicro Cortex-M](#zephyr-project-setup-guide-for-nuvoton-numicro-cortex-m)
- [Troubleshooting](#troubleshooting)

## Zephyr Project Setup Guide for Nuvoton NuMicro Cortex-M

1. Install the required extension packs.

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
1. Select **Host Tools** to install the required environment.
    Install `winget` first. If you encounter any problems, see item 1 in the Troubleshooting section.
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/setup_configuration2.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/setup_configuration2.png" alt="setup_configuration2.png" width="1200">
         </a>
     </p>
    If you encounter any problems while installing the required development tools, see item 2 in the Troubleshooting section.
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/setup_configuration3.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/setup_configuration3.png" alt="setup_configuration3.png" width="1200">
         </a>
     </p>
1. Download and install the SDK version that matches your Zephyr version.
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_sdk.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_sdk.png" alt="install_sdk.png" width="900">
         </a>
     </p>

1. Select **Initialize Current Directory** > **Full Zephyr**.
    Wait while the Zephyr Project files and configuration are downloaded and the workspace is created.
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
1. Create a Zephyr project from sample code.

    Create a new project from sample code by selecting a project template provided by the Zephyr IDE.
   <p>
       <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_template2.png" target="_blank">
           <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_template2.png" alt="select_template2.png" width="1200">
       </a>
   </p>

1. Add a build configuration and select your target board, for example, `NuMaker-PFM-M467`.
   <p>
       <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_board.png" target="_blank">
           <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/select_board.png" alt="select_board.png" width="600">
       </a>
   </p>

1. Add runner profiles.
    Configure the project runner to use PyOCD.
   <p>
       <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/add_runner_profiles.png" target="_blank">
           <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/add_runner_profiles.png" alt="add_runner_profiles.png" width="1200">
       </a>
   </p>
   
1. Build, flash, and debug the target.
    Select the build button to build and flash the firmware to your target board, and then start a debug session.

   <p>
       <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/build_flash2.png" target="_blank">
           <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/build_flash2.png" alt="build_flash2.png" width="1200">
       </a>
   </p>

## Troubleshooting

1. Problems installing the winget tool.

    From the [winget-cli releases page](https://github.com/microsoft/winget-cli/releases), download the two files shown in the red box. Select the winget version that matches your operating system.
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/download_winget.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/download_winget.png" alt="download_winget.png" width="600">
         </a>
     </p>
    First, unzip the ZIP file, open PowerShell in the `x64` folder, and run the commands below to install the dependency files:

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
    
1. Problems installing related packages.

    If the installation fails and an error appears in red, open the OUTPUT panel in the terminal and select **Zephyr IDE**.
     <p>
         <a href="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_tool_message.png" target="_blank">
             <img src="https://raw.githubusercontent.com/OpenNuvoton/Nuvoton_Tools/master/img/ZephyrIDE/install_tool_message.png" alt="install_tool_message.png" width="900">
         </a>
     </p>
    If installing `gperf` or `wget` results in an error, install the package manually from the terminal. The same procedure applies to other development tools: replace the package name in the command with the name of the tool that failed to install.

    ```
    winget install --accept-package-agreements --accept-source-agreements gperf --source winget
    winget install --accept-package-agreements --accept-source-agreements wget --source winget
    ```