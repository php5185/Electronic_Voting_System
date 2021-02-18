import time
#import random
#from pathlib import Path
from SMWinservice import SMWinservice


import socket
import sys
import traceback
from threading import Thread
#import pymysql
import mysql.connector as mariadb


class PythonCornerExample(SMWinservice):
    _svc_name_ = "Votos_Electronicos"
    _svc_display_name_ = "Votos_Electronicos"
    _svc_description_ = "Recibe los votos electronicos de las cabinas"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        #guardar toda la info del colegio electoral

        datos="SELECT id_col_elec, backup, status, AES_DECRYPT(pass, UNHEX(SHA2('elecciones2020',512))) FROM Colegio_electoral" #AES_DECRYPT(pass, UNHEX(SHA2('elecciones2020',512)))
        
        mariadb_connection = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')

        cursor = mariadb_connection.cursor()
        cursor.execute(datos)
        data = cursor.fetchall()
        #print(data)

        mariadb_connection.close()
            
        eliminarCol="TRUNCATE TABLE colegio" # num en 0    
        mariadb_connection = mariadb.connect(user='root', password='microena', database='voto', host='127.0.0.1')#, unix_socket= '/var/run/mysqld/mysqld.sock')
        cursorlocal = mariadb_connection.cursor()
        cursorlocal.execute(eliminarCol)



        for row in data:
            #add=row[1]+","+row[2]+","+row[3]+","+AES_DECRYPT(row[4], UNHEX(SHA2('elecciones2020',512)))
            #print(add)
            command="INSERT INTO colegio (mesa, backup, status, pass) VALUES ('{}',{},{},AES_ENCRYPT('{}', UNHEX(SHA2('elecciones2020',512))))".format(row[0],row[1],row[2],row[3])
            cursorlocal.execute(command)

        mariadb_connection.commit()
        mariadb_connection.close()





        #start_server()
        host = "0.0.0.0"
        port = 5557         # arbitrary non-privileged port

        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
        #print("Socket created")

        try:
            soc.bind((host, port))
        except:
            self.isrunning = False
            #sys.exit()

        soc.listen(10)       # queue up to 5 requests
        #print("Socket now listening")

        # infinite loop- do not reset for every requests
        while self.isrunning:###sincronizar con el servicio de NTP
            try:#este es el try que no estaba
                connection, address = soc.accept()
                ip, port = str(address[0]), str(address[1])
         #       print("Connected with " + ip + ":" + port)

            #try:
                Thread(target=client_thread, args=(connection, ip, port)).start()
            except:
          #      print("Thread did not start.")
                traceback.print_exc()

        soc.close()



def client_thread(connection, ip, port, max_buffer_size = 5120):
    
    #is_active = True
    #cualquiercosa si se sigue explotando sin saber porque, poner que se cierre automatico

   # while is_active:
    client_input = receive_input(connection, max_buffer_size)
    #print(client_input)#here!!!

##    if "--quit--" in client_input:
##        print("Client is requesting to quit")
##        connection.close()
##        print("Connection " + ip + ":" + port + " closed")
##        is_active = False
##        
##    else:
    mensaje=client_input.split(",")
    #print("mensaje en si: "+ mensaje)
    id_voto=mensaje[0]
    #print(mensaje[1])
    id_mesa =mensaje[1]
    part=mensaje[2]
    presi=mensaje[3]
    vice=mensaje[4]
    backup=int(mensaje[5])
    #print("Processed result: {}".format(mensaje))
    #convertir el backup siempre a int

    if(id_voto=='-2'):
        mariadb_connection = mariadb.connect(user='root', password='microena', database='voto', host='127.0.0.1')#, host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')

        cursor = mariadb_connection.cursor()

        upda="UPDATE colegio set status=2 WHERE mesa='{}'".format(id_mesa)
        cursor.execute(upda)
        mariadb_connection.commit()
        sending = "1"#.format(backup,fff)#enviar el numero de voto que va
        connection.send(sending.encode("utf8"))#########

    elif(id_voto=='-1'):#para iniciar una cabina//
       # print("-1")
        datos="SELECT backup FROM colegio WHERE mesa='{}'".format(id_mesa) 
        mariadb_connection = mariadb.connect(user='root', password='microena', database='voto', host='127.0.0.1')#, host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')

        cursor = mariadb_connection.cursor()
        cursor.execute(datos)
        data = cursor.fetchall()

        #tomar el numero y sumarle 1, enviarlo sumado y darle un update
        #enviar el numero de voto siguiente
        for row in data:
            back=int(row[0])
            
        backup=back+1
       # print (backup)

        upda="UPDATE colegio set backup={} WHERE mesa='{}'".format(backup, id_mesa)
        cursor.execute(upda)
        mariadb_connection.commit()

       

        try:

            numero="SELECT MAX(id_voto) FROM Registro_voto WHERE id_mesa_elec='{}'".format(id_mesa)
            cursor.execute(numero)
            fetchs = cursor.fetchall()

            #if fetchs:
            for row in fetchs:
                fff=int(row[0])
               # print(fff)
        except:
            fff=0
            pass
            
        mariadb_connection.close()

       # print(fff)

        #el envio por el socket

        sending = "{},{}".format(backup,fff)#enviar el numero de voto que va
        connection.send(sending.encode("utf8"))#########
        #print("el nuemro de backup y el numero de voto son "+sending)
        

    else:
                        
        datos="INSERT INTO registro_voto values ({},'{}',AES_ENCRYPT('{}', UNHEX(SHA2('elecciones2020',512))), AES_ENCRYPT('{}', UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT('{}', UNHEX(SHA2('elecciones2020',512))))".format(id_voto, id_mesa, part, presi, vice)
        #datos="INSERT INTO registro_voto values ({},'{}',AES_ENCRYPT('{}', UNHEX('elecciones2020')), AES_ENCRYPT('{}', UNHEX('elecciones2020')),AES_ENCRYPT('{}', 'elecciones2020'))".format(id_voto, id_mesa, part, presi, vice)
        #datos="INSERT INTO registro_voto values ({},'{}','{}','{}','{}')".format(id_voto, id_mesa, part, presi, vice)
        sele="SELECT backup FROM colegio WHERE mesa='{}'".format(id_mesa)

        #datos="INSERT INTO registro_voto values (6,'02222','PRD','Danilo Medina',AES_ENCRYPT('Estoy ', UNHEX(SHA2('hola',512))))"
        mariadb_connection = mariadb.connect(user='root', password='microena', database='voto', host='127.0.0.1')#, unix_socket= '/var/run/mysqld/mysqld.sock')


        #print(1)
        cursor = mariadb_connection.cursor()
        cursor.execute(sele)
        fetchs = cursor.fetchall()

        for row in fetchs:
            fff=int(row[0])

        if (fff==backup):                  
           # print(datos)
            try:
                cursor.execute(datos)
                #print(3)
                mariadb_connection.commit()
            except:
                pass
                #print(4)
                #print('ya esta este voto')                  
            sending = "{},{}".format(id_voto, id_mesa)#puede que halla que poner eso dentro de otro if
            connection.send(sending.encode("utf8"))#########
        #poner otro sending
        else:
           # print("no se guardó porque la cabina no es valida")
            sending = "{},{}".format(0, id_mesa)#puede que halla que poner eso dentro de otro if
            connection.send(sending.encode("utf8"))#########

        #print(5)
        mariadb_connection.close()
        
        #connection.sendall("-".encode("utf8"))#########
        #print(234)

    connection.close()

def receive_input(connection, max_buffer_size):## esta funcion tambien se puede eliminar
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
        #print("The input size is greater than expected {}".format(client_input_size))
        pass

    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    #result = process_input(decoded_input)
    result= str(decoded_input)

    return result

           

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()
