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
    0x00, 0x00, 0x00, 0x00,  # CAN Mode. 0: Normal, 1: Silent
    0x87, 0x04, 0x00, 0x00,  # CAN STD_ID for ISP_Bridge
    0x84, 0x07, 0x00, 0x00,  # CAN STD_ID for ISP_Can
    0xFF, 0xFF, 0xFF, 0xFF,  # CAN EXT_ID for Normal Only
    0xFF, 0xFF, 0xFF, 0xFF,  # CAN EXT_ID for Normal Only
]

Setting = bytearray(can_mode)

ser.write(Setting)

# M480BSP/Library/StdDriver/inc/can.h
# typedef struct
# {
#     uint32_t  IdType;       /*!< ID type */
#     uint32_t  FrameType;    /*!< Frame type */
#     uint32_t  Id;           /*!< Message ID */
#     uint8_t   DLC;          /*!< Data length */
#     uint8_t   Data[8];      /*!< Data */
# } STR_CANMSG_T;

can_data = [
    0x43, 0x41, 0x4E, 0x44,  # CAN Command: 'C', 'A', 'N', 'D'
    # STR_CANMSG_T
    0x00, 0x00, 0x00, 0x00,  # 0: CAN_STD_ID, 1: CAN_EXT_ID   
    0x01, 0x00, 0x00, 0x00,  # 0: CAN_REMOTE_FRAME, 1: CAN_DATA_FRAME
    0x87, 0x04, 0x00, 0x00,  # ID used by ISP_Bridge
    0x08,                    # DLC = 8
    0x00, 0x00, 0x00, 0xB1,  # Data[0] ~ Data[3]
    0x00, 0x00, 0x00, 0x00,  # Data[4] ~ Data[7]
]

print("Sending ISP Command to query PDID")

IspCmd = bytearray(can_data)

ser.write(IspCmd)
IspAck = ser.read(24)
print(IspAck)

try:
    while True:
        data = ser.read(24)
        print(data)
            
except KeyboardInterrupt:
    ser.close()
    print('Bye !!!')
