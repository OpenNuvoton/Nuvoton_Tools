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
serialPort.stopbits = spi_master
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


spi_write = [
    0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88,
    0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99,
    0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA,
    0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB,
    0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC,
    0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD,
    0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE,
    0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF,
]

print('Sending 16 Words to SPI_SlaveFIFOMode !!!')

data = bytearray(spi_write)
serialPort.setRTS(True)
sleep(.1)
serialPort.write(data)
serialPort.setRTS(False)

print('Getting 16 Words to SPI_SlaveFIFOMode !!!')

data = serialPort.read(64)
print(data)

print('Bye !!!')
exit();


