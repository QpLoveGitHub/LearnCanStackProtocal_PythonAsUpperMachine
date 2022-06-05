# -*- coding: utf-8 -*-
import serial


t = serial.Serial('com3',9600)
n = t.write('you are my world:'.encode())
print (t.portstr)
print (n)
str = t.read(n)
print (str)