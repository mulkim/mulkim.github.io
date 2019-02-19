import serial
portName = '/dev/cu.usbmodem14201'

ser = serial.Serial(portName, 9600)

while True:
	print(ser.readline())
