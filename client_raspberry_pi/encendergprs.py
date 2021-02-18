#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT) 

port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
 
port.write('AT'+'\r\n') 
time.sleep(1)
        
respuesta = port.read(10)

if "OK" in respuesta:
	print "El GPRS esta encendido!"
		
else:
	GPIO.output(26, False) 
	time.sleep(1)
	GPIO.output(26, True) 
	time.sleep(2)
	GPIO.output(26, False) 
	time.sleep(3)

GPIO.cleanup() # this ensures a clean exit 



