import serial   
import os, time
import sys
##import mysql.connector as mariadb
##
##
##mariadb_connectionlocal = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
##cursor2 = mariadb_connectionlocal.cursor()
##
##
##votantes="SELECT phone FROM NTP"
###cursor2 = mariadb_connection.cursor()
##cursor2.execute(votantes)
##votan = cursor2.fetchall()
##
##for row in votan:
##    phone= row[0]
##    #print(row)
##    #command="INSERT INTO Cedula_ciudadano VALUES {}".format(row)
##    #cursorlocal2.execute(command)
##
##
###mariadb_connectionlocal.commit()
##mariadb_connectionlocal.close()
##
##print(phone)
##work = 'AT+CMGS="+8296458623"\r'
##paola = 'AT+CMGS="+'+phone+'"\r'
##print(work)
##print(paola)

# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
#port = serial.Serial("/dev/ttyserial0", baudrate=9600, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
mensaje=str(sys.argv[1])
tel=str(sys.argv[2])
#print(mensaje)
#print(tel)
paola = 'AT+CMGS="+'+tel+'"\r'
port.write(paola)
#port.write('AT+CMGS="+8296458623"\r')
time.sleep(2)
port.write(mensaje)     #'"'+ mensaje+'"')
#port.write("hola")
time.sleep(1)
port.write('\032')
#port.write('\x1A')
rcv = port.read(50)
#print (rcv)

#atd 8296458623;
#at+cmgs="+8296458623"
#at+cmgs="+8296458623"
