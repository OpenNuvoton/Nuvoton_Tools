import serial
from time import sleep
import sys

COM_PORT = 'COM7'  # <-- CAN Bridge
BAUD_RATES = 9600  # dont care
ser = serial.Serial(COM_PORT, BAUD_RATES)
 
print("connected to: " + ser.portstr)

can_mode = [
    0x43, 0x41, 0x4E, 0x43,  # CAN Command: 'C', 'A', 'N', 'C'
    0x01, 0x00, 0x00, 0x00,  # CONSTANT
    0x20, 0xA1, 0x07, 0x00,  # CAN Baudrate: 500K
    0x01, 0x00, 0x00, 0x00,  # CAN Mode. 0: Normal, 1: Silent
    0xFF, 0xFF, 0xFF, 0xFF,  # CAN STD_ID for Normal Only
    0xFF, 0xFF, 0xFF, 0xFF,  # CAN STD_ID for Normal Only
    0xFF, 0xFF, 0xFF, 0xFF,  # CAN EXT_ID for Normal Only
    0xFF, 0xFF, 0xFF, 0xFF,  # CAN EXT_ID for Normal Only
]

Setting = bytearray(can_mode)

ser.write(Setting)

try:
    while True:
        data = ser.read(24)
        print(data)
            
except KeyboardInterrupt:
    ser.close()
    print('Bye !!!')
