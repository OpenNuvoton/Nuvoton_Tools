## Debug Options

Add or edit `pyocdOptions` in the **CMSIS_DAP@pyOCD (launch)** configuration in `.vscode/launch.json`:

```jsonc
{
    "name": "CMSIS_DAP@pyOCD (launch)",
    ...
    "pyocdOptions": {
        "probe_uid": "",
        "frequency": 1000000,
        "boot_from_ldrom": false
    }
}
```

| Option | Description |
|---|---|
| `probe_uid` | ID of the probe to use. Required only when several probes are connected. |
| `frequency` | SWD clock in Hz, for example `1000000`. Lower it if the connection is unstable. |
| `boot_from_ldrom` | `true`: run from LDROM after reset. `false` (default): run from APROM. |
| `connect_mode` | `attach` (default), `halt`, `pre-reset` or `under-reset`. |
| `rtos.name` | Shows RTOS threads in the **RTOS** view, for example `"FreeRTOS"`. |

Your `pyocdOptions` are kept when the extension updates `launch.json`.
