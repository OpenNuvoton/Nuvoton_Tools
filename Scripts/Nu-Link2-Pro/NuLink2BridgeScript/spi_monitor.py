import serial
from time import sleep
import sys


spi_clock = 1000000
spi_monitor = serial.STOPBITS_ONE
spi_master = serial.STOPBITS_TWO

spi_type0 = serial.PARITY_NONE
spi_type1 = serial.PARITY_ODD
spi_type2 = serial.PARITY_EVEN
spi_type3 = serial.PARITY_MARK

# BIT0: 0(MSB First), 1(LSB First)
# BIT1: 0(Low), 1(High)
# MSB first, low level active (Defualt SPI settings for BSP sample)
spi_misc = serial.EIGHTBITS


serialPort = serial.Serial() # omit port to avoid auto-open
serialPort.port = 'COM11'
serialPort.baudrate = spi_clock
serialPort.stopbits = spi_monitor
serialPort.parity  = spi_type0
serialPort.bytesize  = spi_misc
serialPort.setDTR(True)
serialPort.setRTS(False)

try:
    serialPort.open()
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

