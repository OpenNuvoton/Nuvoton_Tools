## Long-Duration Capture with sigrok-cli

PulseView is a GUI application that buffers all captured samples in system memory (DDR/RAM). Because the buffer size is limited, the maximum record length is constrained, especially at high sample rates or with many channels (see the Performance Specifications table in the [PulseView](02_pulseview.md) section).

For long-duration acquisitions, use **sigrok-cli**, the command-line front-end of the sigrok logic analyzer software suite. Instead of holding samples in RAM, sigrok-cli streams the captured data directly to a file on disk (SSD/HDD). This removes the memory limitation and lets you record much larger data sets, bounded only by available storage.

You can download the Nu-Link3-Pro build of sigrok-cli from [here](https://github.com/OpenNuvoton/sigrok-cli/releases).

### Advantages over the GUI Buffer

- **Disk-based storage**: Samples are written to an output file on SSD/HDD rather than buffered in DDR, so capture length is limited by disk space instead of RAM.
- **Extended record length**: Suitable for long-running tests, intermittent-event capture, and unattended logging.
- **Scriptable and automatable**: Captures can be launched from scripts or batch jobs, making it ideal for regression testing and CI workflows.

### Typical Usage

- List the connected device and its supported channels:

  ```
  sigrok-cli --driver nuvoton-nulink3-pro --scan
  ```

- Capture 6 channels at 4 MHz for a fixed number of samples and save the result to a sigrok session file (`.sr`) on disk:

  ```
  sigrok-cli --driver nuvoton-nulink3-pro --config samplerate=4m -C 0-5 --samples 100M -o capture.sr
  ```

- Capture continuously until interrupted (Ctrl+C) and write to disk:

  ```
  sigrok-cli --driver nuvoton-nulink3-pro --config samplerate=4m --continuous -o capture.sr
  ```

The saved `.sr` file can later be opened in PulseView for offline viewing, protocol decoding, and annotation export.

### Performance Specifications

Because sigrok-cli streams the captured samples directly to disk, the record length is not limited by memory. The maximum sustainable sample rate, however, depends on the selected output format, since each format requires a different amount of processing and disk throughput.

> **Note:** Since sigrok-cli writes the captured data to disk in real time, the achievable sample rate is bounded by how fast the PC can process and store the incoming stream. If the PC side cannot keep up (due to CPU load, disk throughput, output format overhead, or channel count), samples may be dropped. In that case, lower the configured sample rate (`--config samplerate=...`) until the capture runs without loss.

The following example commands show continuous captures for each output format:

#### Output format `sr` (signal recording file; the default format for PulseView)

```
sigrok-cli --driver nuvoton-nulink3-pro --config samplerate=4m --continuous -C 0-5 -o capture.sr
```

#### Output format `hex` (hexadecimal digits logic data)

```
sigrok-cli --driver nuvoton-nulink3-pro --config samplerate=2m --continuous -C 0-5 -O hex -o capture.txt
```

#### Output format `binary` (raw binary logic data)

```
sigrok-cli --driver nuvoton-nulink3-pro --config samplerate=4m --continuous -C 0-5 -O binary -o capture.bin
```


