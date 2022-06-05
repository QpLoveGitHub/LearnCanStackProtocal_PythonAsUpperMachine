# python3 使用 tkinter
from tkinter import *
import serial
import binascii,time

def say_hi():
    print("UDS servie ID 0x34,RequsetDownload")

# data frame
a = '68 AA AA AA AA AA AA 68 11 04 34 37 33 37 B6 16  89 68 12 24 0D 0A'
d = bytes.fromhex(a)
result = 0
def switch_sessionMode():
    print("Uds switch session mode")
    ser = serial.Serial("COM3", 9600, 8, "N", timeout=50, stopbits=1)
    result = ser.write(d)




ser = serial.Serial("COM3",9600,8,"N",timeout=50,stopbits=1)
root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
root.title("CanTest")

label = Label(frame1, text="Label", justify=LEFT)
label.pack(side=LEFT)

hi_there = Button(frame2, text="UDS:RequsetDownload~", command=say_hi)
hi_there.pack()

Uds_Switch_SessionMode_there = Button(frame3, text="UDS:switch_sessionMode~", command=switch_sessionMode)
Uds_Switch_SessionMode_there.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=480, pady=240)
frame3.pack(padx=10,pady=10)

# result = ser.write(d)
time.sleep(1)
count = ser.inWaiting()
# data receive
if count > 0:
    data = ser.read(count)
    if data != b'':
        print("reveive", str(binascii.b2a_hex(data))[2:-1])
# close uart
ser.close()
root.mainloop()