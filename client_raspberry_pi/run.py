import sys
import os

import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT) 

port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
 
port.write('AT'+'\r\n') 
time.sleep(1)
        
respuesta = port.read(10)

if "OK" in respuesta:
        pass
	
		
else:
	GPIO.output(26, False) 
	time.sleep(1)
	GPIO.output(26, True) 
	time.sleep(2)
	GPIO.output(26, False) 
	time.sleep(3)

GPIO.cleanup() # this ensures a clean exit


os.system("python3 /home/pi/Desktop/backup/base.py")
