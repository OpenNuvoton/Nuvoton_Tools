## Zephyr Projects

Use **Zephyr IDE** together with the **Nuvoton NuMicro Cortex-M Pack** to set up, build, flash and debug a Zephyr project for NuMicro devices.

### Setup Guide

1. Install the required extension packs:
   - **Nuvoton NuMicro Cortex-M Pack**
   - **Zephyr IDE Extension Pack**

   <img src="../../media/install_Nuvoton_Pack.png" alt="Install Nuvoton Pack" width="734">
   <img src="../../media/install_Zephyr_Pack.png" alt="Install Zephyr Pack" width="737">

2. Select **Host Tools** and install the required development tools:

   1. Under **Package Manager Status**, check that **winget** shows **Available**. If it does not, see
      [Problems Installing the winget Tool](#problems-installing-the-winget-tool).

      <img src="../../media/setup_configuration2.png" alt="Host Tools" width="1236">

   2. Click **Install All Missing Packages**, then click **Refresh Status** and check that all packages show
      **Installed**. Restart VS Code if a tool is still not found.

      <img src="../../media/setup_configuration3.png" alt="Required packages" width="854">

   If a package fails to install, see [Problems Installing Related Packages](#problems-installing-related-packages).

3. Select **Zephyr SDK** and click **Install / Update**.

   <img src="../../media/install_sdk.png" alt="Install SDK" width="1207">

   Select the SDK version that matches the Zephyr version you will use in step 4, for example **1.0.1** for
   Zephyr 4.4.0.

   <img src="../../media/zephyr_sdk_version.png" alt="Zephyr SDK version" width="294">

   Select **Select Specific Toolchains**, then select **arm-zephyr-eabi**. This is the only toolchain needed for
   NuMicro Cortex-M devices, so you do not need to install all toolchains.

   <img src="../../media/install_toolchain.png" alt="Install toolchain" width="466">

4. Under **West Workspaces**, click **+** (**Create New West Workspace**).

   <img src="../../media/workspace_setup2.png" alt="Workspace setup" width="778">

   Select **Full Zephyr** as the workspace template.

   <img src="../../media/full_zephyr.png" alt="Full Zephyr" width="317">

   Select the Zephyr version, for example **v4.4.0**. It must match the SDK version installed in step 3. Wait while
   the Zephyr project files and configuration are downloaded and the workspace is created.

5. Create a Zephyr project from sample code by selecting a project template provided by the Zephyr IDE.

   <img src="../../media/select_template2.png" alt="Select template" width="1201">

6. Add a build configuration and select your target board, for example `NuMaker-PFM-M467`.

   <img src="../../media/select_board.png" alt="Select board" width="769">

7. Add runner profiles and configure the project runner to use pyOCD.

   <img src="../../media/add_runner_profiles.png" alt="Add runner profiles" width="1200">

8. Click the build button to build and flash the firmware to your target board, then start a debug session.

   <img src="../../media/build_flash2.png" alt="Build and flash" width="1158">

### Troubleshooting

#### Problems Installing the winget Tool

1. From the [winget-cli releases page](https://github.com/microsoft/winget-cli/releases), download:
   - `DesktopAppInstaller_Dependencies.zip`
   - `Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle`

   <img src="../../media/download_winget.png" alt="Download winget" width="800">

2. Unzip `DesktopAppInstaller_Dependencies.zip`, open PowerShell in its `x64` folder and install the dependencies
   for the winget version you downloaded:

   winget v1.12:
   ```powershell
   Add-AppPackage -Path .\Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64.appx
   Add-AppPackage -Path .\Microsoft.VCLibs.140.00_14.0.33519.0_x64.appx
   Add-AppPackage -Path .\Microsoft.WindowsAppRuntime.1.8_8000.616.304.0_x64.appx
   ```

   winget v1.11:
   ```powershell
   Add-AppPackage -Path .\Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64.appx
   Add-AppPackage -Path .\Microsoft.UI.Xaml.2.8_8.2310.30001.0_x64.appx
   ```

3. Install winget from the folder that contains the `.msixbundle` file:

   ```powershell
   Add-AppPackage -Path .\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
   ```

4. Restart VS Code and check that **winget** shows **Available** in **Host Tools**.

#### Problems Installing Related Packages

If installation fails with a red error, open the **OUTPUT** panel and select **Zephyr IDE**.

<img src="../../media/install_tool_message.png" alt="Install tool message" width="1000">

If `gperf` or `wget` fails to install, install it manually from the terminal (replace the package name for other tools
that fail):
```powershell
winget install --accept-package-agreements --accept-source-agreements gperf --source winget
winget install --accept-package-agreements --accept-source-agreements wget --source winget
```

After installing, click **Refresh Status** in **Host Tools**.
