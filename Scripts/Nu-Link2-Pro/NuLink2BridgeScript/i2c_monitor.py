import serial
from time import sleep
import sys


i2c_clock = 100000
i2c_monitor = serial.STOPBITS_ONE
i2c_master = serial.STOPBITS_TWO

try:
    serialPort = serial.Serial("COM7",\
                               i2c_clock
                               serial.EIGHTBITS,\
                               serial.PARITY_NONE,
                               i2c_monitor);
except:
    print("Couldn't open serial port");
    exit();
 
print("connected to: " + serialPort.portstr)

try:
    while True:
        data = serialPort.read()
        print(data)
            
except KeyboardInterrupt:
    serialPort.close()
    print('Bye !!!')
