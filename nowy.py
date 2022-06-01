import serial


ser = serial.Serial('COM4', 9600)

data = ser.readline()
print (data)
data = ser.readline()
print (data)
data = ser.readline()
print (data)
data = ser.readline()
print (data)
data = ser.readline()
print (data)
data = ser.readline()
print (data)



