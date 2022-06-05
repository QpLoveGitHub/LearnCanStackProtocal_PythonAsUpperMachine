# receive a string data from mcu
# MCU uart 3n
# -*- coding: utf-8 -*-
import serial  #导入串口模块
import time    #导入时间模块，时间模块是Python自带模块，无需安装
try:
    #打开串口，并且获得串口对象
    SCI1 = serial.Serial("com3",9600,timeout=50)
    #判断是否打开成功
    if (SCI1.isOpen()==True):
        print("串口已经打开！")
except Exception as exc:
    print("串口打开异常:",exc)
while True:
    commandFromECU = input("请输入控制命令，c-向ECU发送命令；r-从ECU中读取数据。")  #从键盘上输入一个命令
    SCI1.write(str(commandFromECU).encode("utf-8"))  #将键盘输入的控制命令发送给ECU上的单片机
    if commandFromECU == 'c':
        time.sleep(1)
        print("send c");
    if commandFromECU == 'r':          #如果是读取数据，则从串口中接收数据。
        time.sleep(1)                  #等待1秒,等待接收ECU上单片机返回的数据. ECU会依次发送0x30-0x39等10个数据
        bufferSize = SCI1.in_waiting   #接收ECU上单片机发过来的数据，并且返回数据的大小
        print("接收到",str(bufferSize),'个数据') #打印缓冲区中接收到数据的个数
        data = SCI1.read_all().hex()           #将接收缓冲区中数据读取到data中
        print(data)                    #将接收到的数据按照16进制打印出来
    time.sleep(1)                      #等待1秒
    if(input("如果退出，请输入n，如果继续发送命令，请按其他键 ") == 'n'):
        break
SCI1.close()    #关闭端口
