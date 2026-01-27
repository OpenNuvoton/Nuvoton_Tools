from machine import UART
from machine import I2C
from machine import SPI
from machine import RS485
from machine import Timer
from machine import CAN
import gc


def word_to_bytes(num_int):
    return num_int.to_bytes(4, "little", False)


def bytes_to_word(num_bytes):
    return int.from_bytes(
        num_bytes if len(num_bytes) <= 4 else num_bytes[0:4], "little", False
    )


class ISP_Timer:
    timer = None
    tick_count = 0

    def __init__(self):
        if ISP_Timer.timer == None:
            ISP_Timer.timer = Timer(-1)
            ISP_Timer.timer.init(
                mode=Timer.PERIODIC, freq=1, callback=ISP_Timer._timer_callback
            )

    @staticmethod
    def _timer_callback(timer):
        ISP_Timer.tick_count = (ISP_Timer.tick_count + 1) & 0xFFFF

    @staticmethod
    def get_timer_tick():
        return ISP_Timer.tick_count


class ISP_Intr(ISP_Timer):
    def __init__(self):
        super().__init__()
        self._packet_no = 0
        self._packet_len = 64
        self._packet_checksum = 0

    def _write(self, buf, timeout_sec):
        return False

    def _read(self, nbytes, timeout_sec):
        return bytearray()

    def __run_cmd_write(self, cmd, send_data, timeout_sec=5):
        try:
            data_len = self._packet_len - 8

            send_data = bytearray() if send_data == None else bytearray(send_data)
            if len(send_data) > data_len:
                send_data = send_data[0:data_len]
            else:
                for i in range(0, data_len - len(send_data)):
                    send_data.append(0x00)

            if self._packet_no >= 0xFFFF:
                self._packet_no = 1

                if not self._run_cmd(0xA4, word_to_bytes(self._packet_no), None):
                    return False

            if cmd == 0xAE:
                self._packet_no = 1
            else:
                self._packet_no = self._packet_no & 0xFFFF

            send_packet = (
                word_to_bytes(cmd) + word_to_bytes(self._packet_no) + send_data
            )
            self._packet_checksum = sum(send_packet) & 0xFFFF

            self._write(send_packet, timeout_sec)
            self._packet_no += 2

            return True
        except OSError:
            pass

        return False

    def __run_cmd_read(self, recv_data, timeout_sec=5):
        try:
            tick_count = self.get_timer_tick()

            while True:
                recv_packet = self._read(self._packet_len, timeout_sec)

                if not recv_packet or len(recv_packet) != self._packet_len:
                    break

                if bytes_to_word(recv_packet[0:2]) != self._packet_checksum:
                    pass
                elif bytes_to_word(recv_packet[4:8]) != (self._packet_no - 1):
                    pass
                else:
                    if recv_data != None:
                        recv_data.extend(recv_packet[8:])
                    return True

                if (self.get_timer_tick() - tick_count) >= timeout_sec:
                    break

        except OSError:
            pass

        return False

    def _run_cmd(self, cmd, send_data, recv_data):
        if self.__run_cmd_write(cmd, send_data):
            return self.__run_cmd_read(recv_data)

        return False

    def connect(self, timeout_sec=5):
        tick_count = self.get_timer_tick()

        while True:
            if self.__run_cmd_write(0xAE, None):
                for i in range(10):
                    if self.__run_cmd_read(None, 0):
                        return True

            if (self.get_timer_tick() - tick_count) >= timeout_sec:
                break

        return False

    def get_device_id(self):
        recv_data = bytearray()

        if self._run_cmd(0xB1, None, recv_data):
            return bytes_to_word(recv_data[0:4])
        else:
            return 0

    def get_fw_ver(self):
        recv_data = bytearray()

        if self._run_cmd(0xA6, None, recv_data):
            return bytes_to_word(recv_data[0:2])
        else:
            return 0

    def sync_packet_no(self):
        self._packet_no = 0x0018 & 0xFFFF

        return self._run_cmd(0xA4, word_to_bytes(self._packet_no), None)

    def erase_all(self):
        return self._run_cmd(0xA3, None, None)

    def update_config(self, configs=[]):
        configs = configs[0:14] if len(configs) > 14 else configs

        send_data = bytearray([0xFF for i in range(14 * 4)])

        for i in range(len(configs)):
            for j in range(4):
                send_data[i * 4 + j] = configs[i][j]

        return self._run_cmd(0xA1, send_data, None)

    def _update_flash(self, isp_cmd, start_addr, total_len, curr_addr, data):
        if curr_addr == start_addr:
            data = data[0:48] if len(data) > 48 else data

            if self._run_cmd(
                isp_cmd,
                word_to_bytes(start_addr) + word_to_bytes(total_len) + data,
                None,
            ):
                return len(data)
            else:
                return 0
        else:
            data = data[0:56] if len(data) > 56 else data

            if self._run_cmd(0x00, data, None):
                return len(data)
            else:
                return 0

    def update_aprom(self, start_addr, total_len, curr_addr, data):
        return self._update_flash(0xA0, start_addr, total_len, curr_addr, data)

    def update_dataflash(self, start_addr, total_len, curr_addr, data):
        return self._update_flash(0xC3, start_addr, total_len, curr_addr, data)

    def resend(self):
        return self._run_cmd(0xFF, None, None)

    def reset_and_run(self):
        return self.__run_cmd_write(0xAB, None)


class ISP_UART(ISP_Intr):
    def __init__(self):
        super().__init__()
        self._intf = UART(0, 115200, bits=8, parity=None, stop=1)

    def _write(self, buf, timeout_sec):
        self._intf.write(buf)
        return True

    def _read(self, nbytes, timeout_sec):
        send_data = bytearray()
        tick_count = self.get_timer_tick()

        while len(send_data) < nbytes:
            if self._intf.any() > 0:
                send_data.extend(self._intf.read(nbytes - len(send_data)))

            if (self.get_timer_tick() - tick_count) >= timeout_sec:
                break

        return send_data


class ISP_I2C(ISP_Intr):
    def __init__(self):
        super().__init__()
        self._intf = I2C(0, I2C.MASTER)
        self._address = 0x60

    def _write(self, buf, timeout_sec):
        self._intf.send(buf, self._address, timeout=timeout_sec * 1000)
        return True

    def _read(self, nbytes, timeout_sec):
        buf = bytearray(nbytes)
        self._intf.recv(buf, self._address, timeout=timeout_sec * 1000)
        return buf


class ISP_SPI(ISP_Intr):
    def __init__(self):
        super().__init__()
        self._intf = SPI(0, SPI.MASTER, baudrate=1000000, bits=32)

    def _write(self, buf, timeout_sec):
        if len(buf) >= 4:
            self._intf.write(bytearray([buf[0], 0x49, 0x50, 0x53]) + buf[4:])
            return True

        return False

    def _read(self, nbytes, timeout_sec):
        if nbytes >= 4:
            buf = bytearray(nbytes)
            self._intf.readinto(buf)
            return buf[4:] + bytearray([0x00, 0x00, 0x00, 0x00])

        return bytearray()


class ISP_RS485(ISP_Intr):
    def __init__(self):
        super().__init__()
        self._intf = RS485(0, 115200, bits=8, parity=None, stop=1)

    def _write(self, buf, timeout_sec):
        self._intf.write(buf)
        return True

    def _read(self, nbytes, timeout_sec):
        send_data = bytearray()
        tick_count = self.get_timer_tick()

        while len(send_data) < nbytes:
            if self._intf.any() > 0:
                send_data.extend(self._intf.read(nbytes - len(send_data)))

            if (self.get_timer_tick() - tick_count) >= timeout_sec:
                break

        return send_data


class ISP_CAN(ISP_Timer):
    def __init__(self, config_offset, df_base_addr):
        super().__init__()
        self._packet_cmd = 0
        self._packet_len = 8
        self._master_id = 0x487
        self._device_id = 0x784

        self._config_offset = config_offset
        self._df_base_addr = df_base_addr

        self._intf = CAN(0, mode=CAN.NORMAL, extframe=False, baudrate=500000)
        self._intf.setfilter(id=self._device_id, mask=0x7FF)

        self._recv_buf = bytearray(8)
        self._recv_list = [0, 0, 0, memoryview(self._recv_buf)]
        self._recv_event = False
        self._intf.rxcallback(self._rxcallback)

    def _rxcallback(self, can, reason, fifo_num):
        if reason == CAN.CB_REASON_RX:
            can.recv(self._recv_list)
            self._recv_event = True

    def __run_cmd_write(self, cmd, send_data, timeout_sec=5):
        try:
            data_len = self._packet_len - 4

            cmd = bytearray(cmd)
            if len(cmd) > 4:
                cmd = cmd[0:4]
            else:
                for i in range(0, 4 - len(cmd)):
                    cmd.append(0x00)

            send_data = bytearray() if send_data == None else bytearray(send_data)
            if len(send_data) > data_len:
                send_data = send_data[0:4]
            else:
                for i in range(0, data_len - len(send_data)):
                    send_data.append(0x00)

            self._packet_cmd = cmd
            self._recv_event = False
            self._intf.send(
                data=cmd + send_data, id=self._master_id, timeout=timeout_sec * 1000
            )

            return True
        except OSError:
            pass

        return False

    def __run_cmd_read(self, recv_data, timeout_sec=5):
        tick_count = self.get_timer_tick()
        while not self._recv_event:
            if (self.get_timer_tick() - tick_count) > timeout_sec:
                break

        if self._recv_event:
            if self._packet_cmd == self._recv_buf[0:4]:
                if recv_data != None:
                    recv_data.extend(self._recv_buf[4:8])
                return True

        return False

    def _run_cmd(self, cmd, send_data, recv_data):
        if self.__run_cmd_write(cmd, send_data):
            return self.__run_cmd_read(recv_data)

        return False

    def connect(self, timeout_sec=5):
        tick_count = self.get_timer_tick()

        while True:
            if self.__run_cmd_write([0x00, 0x00, 0x00, 0xB1], None):
                for i in range(10):
                    if self.__run_cmd_read(None, 0):
                        return True

            if (self.get_timer_tick() - tick_count) >= timeout_sec:
                break

        return False

    def get_device_id(self):
        recv_data = bytearray()

        if self._run_cmd([0x00, 0x00, 0x00, 0xB1], None, recv_data):
            return bytes_to_word(recv_data)
        else:
            return 0

    def get_fw_ver(self):
        return 0  # Not supported

    def sync_packet_no(self):
        return True  # Not supported

    def erase_all(self):
        return True  # Not supported

    def update_config(self, configs=[]):
        configs = configs[0:14] if len(configs) > 14 else configs

        for i in range(len(configs)):
            if not self._run_cmd(
                word_to_bytes(self._config_offset + 0x00300000 + (4 * i)),
                configs[i],
                None,
            ):
                return False

        return True

    def _update_flash(self, start_addr, total_len, curr_addr, data):
        update_len = len(data) & ~0x3

        for i in range(0, update_len, 4):
            if not self._run_cmd(word_to_bytes(curr_addr + i), data[i : i + 4], None):
                return 0

        return update_len

    def update_aprom(self, start_addr, total_len, curr_addr, data):
        return self._update_flash(start_addr, total_len, curr_addr, data)

    def update_dataflash(self, start_addr, total_len, curr_addr, data):
        return self._update_flash(
            self._df_base_addr + start_addr,
            total_len,
            self._df_base_addr + curr_addr,
            data,
        )

    def resend(self):
        return False  # Not supported

    def reset_and_run(self):
        return self.__run_cmd_write([0x00, 0x00, 0x00, 0xAB], None)


class ISP_Config:
    def __init__(self):
        self._config_items = {
            "Connection Interface": {"Bridge": (1, lambda value: int(value))},
            "Files": {
                "APROM": ("aprom.bin", lambda value: str(value)),
                "DataFlash": ("dataflash.bin", lambda value: str(value)),
            },
            "Config Bits": {
                # Config0-13
            },
            "Programming Options": {
                "APROM": (1, lambda value: int(value)),
                "DataFlash": (0, lambda value: int(value)),
                "Config": (0, lambda value: int(value)),
                "ResetAndRun": (0, lambda value: int(value)),
                "EraseAll": (1, lambda value: int(value)),
            },
            "ISP CAN": {
                "DataFlashBaseAddress": (
                    self._hex_str_to_bytes("0xFFFFFFFF"),
                    self._hex_str_to_bytes,
                ),
                "ConfigBaseSel": (0, lambda value: int(value)),
            },
        }

        for i in range(14):
            self._config_items["Config Bits"]["Config" + str(i)] = (
                self._hex_str_to_bytes("0xFFFFFFFF"),
                self._hex_str_to_bytes,
            )

    def _hex_str_to_bytes(self, value):
        if value.startswith("0x") or value.startswith("0X"):
            value = value[2:]
        value = ("00000000" + value)[-8:]
        return bytes([int(value[i : i + 2], 16) for i in range(6, -1, -2)])

    def _default_config(self):
        config = {}
        for section, item in self._config_items.items():
            for key, value in item.items():
                if not (section in config):
                    config[section] = {}
                config[section][key] = value[0]
        return config

    def parse_ini(self, file_name):
        config = self._default_config()
        section = None

        try:
            with open(file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith("#") or line.startswith(";"):
                        continue
                    if line.startswith("[") and line.endswith("]"):
                        section = line[1:-1]
                        if not (section in config):
                            config[section] = {}
                    elif "=" in line:
                        if section is None:
                            continue
                        key, value = line.split("=", 1)
                        key = key.strip()
                        value = value.strip()
                        if (section in self._config_items) and (
                            key in self._config_items[section]
                        ):
                            config[section][key] = (
                                self._config_items[section][key][1]
                            )(value)
                        else:
                            config[section][key] = value
        except OSError:
            return (False, {})

        return (True, config)


def main():
    result, user_config = ISP_Config().parse_ini("config.ini")

    if (not result) or (len(user_config) == 0):
        raise RuntimeError("Read config.ini failed")

    isp_bridge = {
        0: ISP_UART(),
        1: ISP_SPI(),
        2: ISP_I2C(),
        3: ISP_RS485(),
        4: ISP_CAN(
            0x0F000000 if (user_config["ISP CAN"]["ConfigBaseSel"] == 1) else 0x00000000,
            user_config["ISP CAN"]["DataFlashBaseAddress"],
        ),
    }

    index = user_config["Connection Interface"]["Bridge"]
    if index in isp_bridge:
        intf = isp_bridge[index]
    else:
        raise RuntimeError("Unsupported Interface")

    if not intf.connect(timeout_sec=5):
        raise RuntimeError("Connection failed")

    if not intf.sync_packet_no():
        raise RuntimeError("Sync Packet failed")

    if intf.get_device_id() == 0:
        raise RuntimeError("Get Device ID failed")

    if user_config["Programming Options"]["EraseAll"] > 0:
        if not intf.erase_all():
            raise RuntimeError("Erase All failed")

    if user_config["Programming Options"]["Config"] > 0:
        configs = []
        for i in range(14):
            key = "Config" + str(i)
            if key in user_config["Config Bits"]:
                configs.append(user_config["Config Bits"][key])
            else:
                configs.append(bytes([0xFF, 0xFF, 0xFF, 0xFF]))

        if not intf.update_config(configs):
            raise RuntimeError("Update Config failed")

    def _update_flash(file_name, start_addr, intf_update_flash):
        with open(file_name, "rb") as file:
            file.seek(0, 2)
            total_len = file.tell()

            curr_addr = start_addr
            while curr_addr < total_len:
                file.seek(curr_addr, 0)
                file_bytes = file.read(56)

                retry_count = 5
                while True:
                    update_len = intf_update_flash(
                        start_addr, total_len, curr_addr, file_bytes
                    )

                    if update_len > 0:
                        curr_addr = curr_addr + update_len
                        break
                    elif retry_count > 0:
                        retry_count -= 1
                        if not intf.resend():
                            return False
                    else:
                        return False

                gc.collect()

            return True

        return False

    if user_config["Programming Options"]["APROM"] > 0:
        if not _update_flash(user_config["Files"]["APROM"], 0x00000000, intf.update_aprom):
            raise RuntimeError("Update APROM failed")

    if user_config["Programming Options"]["DataFlash"] > 0:
        if not _update_flash(user_config["Files"]["DataFlash"], 0x00000000, intf.update_dataflash):
            raise RuntimeError("Update DataFlash failed")

    if user_config["Programming Options"]["ResetAndRun"] > 0:
        intf.reset_and_run()


if __name__ == "__main__":
    main()
