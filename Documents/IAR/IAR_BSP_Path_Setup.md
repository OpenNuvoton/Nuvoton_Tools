# Nu-Link Debugger Driver Setup Guide for IAR EWARM 9.6+

If you are using **IAR EWARM version 9.60 or later** (e.g., 9.60, 9.70+), please follow the steps below to configure the Nu-Link third-party debugger driver path.

---

## Configuration Steps

### Step 1: Open Project Options
1. Open your project in **IAR Embedded Workbench**.
2. In the **Workspace** panel, right-click the project root node.
3. Select **Options...** (or press `Alt + F7`).

---

### Step 2: Navigate to Third-Party Driver
1. In the **Category** list on the left, select **Debugger**.
2. Click on **Third-Party Driver**.

---

### Step 3: Update Driver Plugin Path
Set the **IAR debugger driver plugin** field to the absolute path of the Nu-Link DLL:

```text
C:\Program Files\Nuvoton Tools\Nu-Link_IAR\Nu-Link_IAR.dll
```

Note: Alternatively, you can click the ... button on the right to browse and select Nu-Link_IAR.dll manually.

### Step 4: Save Settings
Click OK at the bottom right to apply the changes. You are now ready to flash and debug your target board.