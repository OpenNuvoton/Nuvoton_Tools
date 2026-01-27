import serial
from time import sleep
import sys


i2c_clock = 100000
i2c_monitor = serial.STOPBITS_ONE
i2c_master = serial.STOPBITS_TWO

serialPort = serial.Serial() # omit port to avoid auto-open
serialPort.port = 'COM11'
serialPort.baudrate = i2c_clock
serialPort.stopbits = i2c_master
serialPort.setDTR(True)
serialPort.setRTS(False)

try:
    serialPort.open()
except:
    print("Couldn't open serial port");
    exit();
 
print("connected to: " + serialPort.portstr)


i2c_write = [
    0x60, 0x00, # [Bit0~Bit6] 7-Bit I2C Address: 0x60, Bit7 = 0 for I2C Write
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # Write Data
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
]

i2c_read = [
    0xE0, 0x00, # [Bit0~Bit6] 7-Bit I2C Address: 0x60, Bit7 = 1 for I2C Read
    0x40, 0x00, # Read Length
]

print('Sending CMD_CONNECT(0xAE) !!!')

i2c_write[2] = 0xAE;
IspCmd = bytearray(i2c_write)
serialPort.setRTS(True)
serialPort.write(IspCmd)
serialPort.setRTS(False)
BrgAck = serialPort.read(2)
print(BrgAck)

sleep(.1)

print('Waiting for response of CMD_CONNECT(0xAE) !!!')


IspAck = bytearray(i2c_read)
serialPort.setRTS(True)
sleep(.1)
serialPort.write(IspAck)
serialPort.setRTS(False)
BrgAck = serialPort.read(64)
print(BrgAck)


print('Sending CMD_GET_DEVICEID (0xB1) !!!')

i2c_write[2] = 0xB1;
IspCmd = bytearray(i2c_write)
serialPort.setRTS(True)
sleep(.1)
serialPort.write(IspCmd)
serialPort.setRTS(False)
BrgAck = serialPort.read(2)
print(BrgAck)

sleep(.1)

print('Waiting for response of CMD_GET_DEVICEID(0xB1) !!!')

IspAck = bytearray(i2c_read)
serialPort.setRTS(True)
sleep(.1)
serialPort.write(IspAck)
serialPort.setRTS(False)
BrgAck = serialPort.read(64)
print(BrgAck)

print('Bye !!!')
exit();


