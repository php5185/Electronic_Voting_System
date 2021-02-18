import serial   
import os, time
import sys

# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
#port = serial.Serial("/dev/ttyserial0", baudrate=9600, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
mensaje=str(sys.argv[1])
print(mensaje)
port.write('AT+CMGS="+8296458623"\r')
time.sleep(2)
port.write(mensaje)     #'"'+ mensaje+'"')
#port.write("hola")
time.sleep(1)
port.write('\032')
#port.write('\x1A')
rcv = port.read(50)
print (rcv)

#atd 8296458623;
#at+cmgs="+8296458623"
#at+cmgs="+8296458623"
