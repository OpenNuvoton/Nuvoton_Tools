
## Nu-Link2-Pro Operating Current of ICP

When power is supplied via an USB during ICP online programming, the
operating current of Nu-Link2-Pro is shown in the Table: below.

| **SWD I/O Mode Settings** | **5.0 V** | **3.3 V** | **2.5 V** | **1.8 V** |
|---------------------------|:---------:|:---------:|:---------:|:---------:|
| USB Input Voltage (V)     |    5.0    |    5.0    |    5.0    |    5.0    |
| SWD I/O Voltage (V)       |   4.66    |   3.33    |   2.52    |   1.82    |
| USB Input Current (mA)    |    128    |    117    |    115    |    113    |

Table: Nu-Link2-Pro Operating Current (Online Programming)

When power is supplied from a target board (SWD VCC pin) during offline
programming with offline file stored on SPI flash, the operating current of
Nu-Link2-Pro is shown in the Table: below.

| **Power Supplied from a Target Board** | **5.0 V** | **3.3 V** | **2.5 V** | **1.8 V** |
|----|:--:|:--:|:--:|:--:|
| Power Supplied via an USB | Off | Off | Off | Off |
| SWD VCC Input Voltage (V) | 5.01 | 3.33 | 2.51 | 1.82 |
| SWD VCC Input Current (mA) | 77.5 | 127.5 | 155.4 | 167.5 |

Table: Nu-Link2-Pro Operating Current (Offline Programming) of SPI
Flash

When power is supplied from a target board (SWD VCC pin) during offline
programming with offline file stored on USB flash drive, the operating current
of Nu-Link2-Pro is shown in the Table: below.

| **Power Supplied from a Target Board** | **5.0 V** | **3.3 V** | **2.5 V** | **1.8 V** |
|----|:--:|:--:|:--:|:--:|
| Power Supplied via an USB | Off | Off | Off | Off |
| SWD VCC Input Voltage (V) | 5.00 | 3.22 | 2.52 | 1.82 |
| SWD VCC Input Current (mA) | 77.6 | 123.3 | 152.6 | 161.7 |

Table: Nu-Link2-Pro Operating Current (Offline Programming) of USB
Flash

When power is supplied from a target board (SWD VCC pin) during offline
programming with offline file stored on Micro SD card, the operating current of
Nu-Link2-Pro is shown in the Table: below.

| **Power Supplied from a Target Board** | **5.0 V** | **3.3 V** | **2.5 V** | **1.8 V** |
|----|:--:|:--:|:--:|:--:|
| Power Supplied via an USB | Off | Off | Off | Off |
| SWD VCC Input Voltage (V) | 5.01 | 3.28 | 2.53 | 1.81 |
| SWD VCC Input Current (mA) | 77.3 | 125.5 | 154.6 | 165.2 |

Table: Nu-Link2-Pro Operating Current (Offline Programming) of
Micro SD Card

## Nu-Link2-Pro Operating Current of ISP

The operating current of Nu-Link2-Pro during ISP online programming with
power supply via USB is shown in the Table: below.

| **ISP programming Interface** | **I2C** | **SPI** | **RS-485** | **CAN** | **UART** |
|----|:--:|:--:|:--:|:--:|:--:|
| USB VCC Input Current (mA) | 117.1 | 114.3 | 151 | 191 | 114.2 |
| Target board Input Current (mA) | 11.9 | 15.1 | 47.1 | 90.1 | 15 |

Table: Operating Current of ISP Online Programming

## Automatic IC Programming System

The automatic IC programming system through individual slot and the
Control Bus as Figure:.

![](../../media/nu-link2/image82.png)

#### Figure: SWD Connector Pin Diagrams

### Operation Sequence and Waveform

1.  The Nu-Link2-Pro power on. START, BUSY, PASS, and FAIL are set to
    logic high.

2.  To start programming, START needs to be set to logic 0 for
    TSTART,$\ 50ms \leq T_{START} \leq 80ms$

3.  Programming start-up. BUSY is set to logic 0, and might toggle
    during programming.

4.  When finish programming, BUSY is set to logic 1, and PASS or FAIL is
    set to logic 0.

- When BUSY is set to logic 1, and PASS is set to logic 0, means “PASS”.

- When BUSY is set to logic 1, and FAIL is set to logic 0, means “FAIL”.

![](../../media/nu-link2/image83.png)

> Figure: PASS Waveform

![](../../media/nu-link2/image84.png)

> Figure: FAIL Waveform



## Revision History

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 20%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr>
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>2020.03.13</p>
</blockquote></td>
<td><blockquote>
<p>1.00</p>
</blockquote></td>
<td><ol type="1">
<li><p>Initially issued.</p></li>
</ol></td>
</tr>
<tr>
<td><blockquote>
<p>2020.03.24</p>
</blockquote></td>
<td><blockquote>
<p>1.01</p>
</blockquote></td>
<td><ol type="1">
<li><p>Modify some related descriptions in the introduction
section</p></li>
</ol></td>
</tr>
<tr>
<td><blockquote>
<p>2021.09.10</p>
</blockquote></td>
<td><blockquote>
<p>1.02</p>
</blockquote></td>
<td><ol type="1">
<li><p>Update chapter 3.3 and 5.2.6</p></li>
</ol></td>
</tr>
<tr>
<td><blockquote>
<p>2022.05.17</p>
</blockquote></td>
<td><blockquote>
<p>1.03</p>
</blockquote></td>
<td><ol type="1">
<li><p>Update 5.2.6</p></li>
</ol></td>
</tr>
<tr>
<td><blockquote>
<p>2023.11.07</p>
</blockquote></td>
<td><blockquote>
<p>1.04</p>
</blockquote></td>
<td><ol type="1">
<li><p>Update chapter 3.3.9</p></li>
</ol></td>
</tr>
</tbody>
</table>

**Important Notice**

**Nuvoton Products are neither intended nor warranted for usage in
systems or equipment, any malfunction or failure of which may cause loss
of human life, bodily injury or severe property damage. Such
applications are deemed, “Insecure Usage”.**

**Insecure usage includes, but is not limited to: equipment for surgical
implementation, atomic energy control instruments, airplane or spaceship
instruments, the control or operation of dynamic, brake or safety
systems designed for vehicular use, traffic signal instruments, all
types of safety devices, and other applications intended to support or
sustain life.**

**All Insecure Usage shall be made at customer’s risk, and in the event
that third parties lay claims to Nuvoton as a result of customer’s
Insecure Usage, customer shall indemnify the damages and liabilities
thus incurred by Nuvoton.**

<img src="../../media/nu-link2/image90.png" style="width:6.28542in;height:0.37639in"
alt="Description: 描述: 描述: 描述: 描述: logo3" />



