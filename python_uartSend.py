# use computer com3 send a string characters to mcu
# 2022.6.5
import serial
import binascii,time

ser = serial.Serial("COM3",9600,8,"N",timeout=50,stopbits=1)

# data frame
a = '68 AA AA AA AA AA AA 68 11 04 34 37 33 37 B6 16  89 68 12 24 0D 0A'
d = bytes.fromhex(a)

#uart send data
result = ser.write(d)

time.sleep(1)
count=ser.inWaiting()

# data receive
if count > 0:
    data = ser.read(count)
    if data != b'':
        print("reveive",str(binascii.b2a_hex(data))[2:-1])
# close uart
ser.close()
















