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

partidos =''
nombre=''



class PythonCornerExample(SMWinservice):
    _svc_name_ = "Votos_Fisicos"
    _svc_display_name_ = "Votos_Fisicos"
    _svc_description_ = "Recibe el conteo de votos físicos de mesas electorales"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
##        i = 0
##        while self.isrunning:
##            random.seed()
##            x = random.randint(1, 1000000)
##            Path(f'c:\\{x}.txt').touch()
##            time.sleep(5)
        
        datos="SELECT sigla_partido, nombre_partido FROM candidatos"
        mariadb_connection = mariadb.connect(user='root', password='microena', database='voto', host='127.0.0.1')

        cursor = mariadb_connection.cursor()
        cursor.execute(datos)
        data = cursor.fetchall()

      
                    #back='-1-1-1'
        partid=''
        nom=''
        for row in data:
            back=row[0]+','
            backj=row[1]+','
            partid+=back
            nom+=backj

       
        global partidos
        partidos=partid
        global nombre
        nombre=nom

##        prueba="UPDATE colegio SET status=5 WHERE mesa='0314A'"
##        cursor.execute(prueba)
##        mariadb_connection.commit()
        
        mariadb_connection.close()








        #start_server()
        host = "0.0.0.0"
        port = 5556         # arbitrary non-privileged port

        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
        #print("Socket created")

        try:
            soc.bind((host, port))
        except:
         #   print("Bind failed. Error : " + str(sys.exc_info()))
            self.isrunning = False
            sys.exit()###############################

        soc.listen(10)       # queue up to 5 requests
        #print("Socket now listening")

        
        
        #mariadb_connection.close()

        y=0
        #x=0

        # infinite loop- do not reset for every requests
        while self.isrunning:#True:###sincronizar con el servicio de NTP
                        
            try:
                connection, address = soc.accept()
                ip, port = str(address[0]), str(address[1])
                 
            except:
                if y==0:
                    y=1
               #pass
                    
         #   print("Connected with " + ip + ":" + port)
         

            try:
                Thread(target=client_thread, args=(connection, ip, port)).start()
            except:
          #      print("Thread did not start.")
                traceback.print_exc()

        soc.close()












def client_thread(connection, ip, port, max_buffer_size = 5120):
    
   ## is_active = True
    #cualquiercosa si se sigue explotando sin saber porque, poner que se cierre automatico

    #while is_active:
    client_input = receive_input(connection, max_buffer_size)
    #print(client_input)#here!!!
    mensaje=client_input.split(",")
    id_voto=mensaje[1]
   # print(id_voto)

    if id_voto=="1":#login del programa
        
        id_mesa=mensaje[2]
        passw=mensaje[3]
        #compare= hashlib.md5(passw).digest()

        #datos="SELECT pass FROM colegio WHERE mesa='{}'".format(id_mesa)
        #datos="SELECT AES_DECRYPT(pass, UNHEX(SHA2('elecciones2020',512))) FROM colegio WHERE mesa='{}'".format(id_mesa)
        datos="select AES_DECRYPT(pass, UNHEX(SHA2('elecciones2020',512))) from colegio where mesa='{}'".format(id_mesa);
        #datos="SELECT pass FROM colegio WHERE mesa='{}'".format(id_mesa)

        
        mariadb_connection = mariadb.connect(user='root', password='microena', database='voto', host='127.0.0.1')#, host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')

        cursor = mariadb_connection.cursor()
        cursor.execute(datos)
        data = cursor.fetchall()

        back='-1-1-1'
        for row in data:
            back=row[0]

        contrase=0
        
        if back==passw:
            contrase=1
        datos="SELECT recibido, observado, reobservado FROM votos_fisicos WHERE id_mesa_elec='{}'".format(id_mesa)
        cursor = mariadb_connection.cursor()
        cursor.execute(datos)
        data = cursor.fetchall()

        rec=0
        obs=0
        reob=0
        for row in data:
            rec=int(row[0])
            obs=int(row[1])
            reob=int(row[2])
            
        
        mariadb_connection.close()
##        sending = "0,{}".format(contrase)
        sending = "{},{},{},{}".format(contrase,rec,obs,reob)
        #print(sending)
        connection.send(sending.encode("utf8"))#########
        connection.close()

    if(id_voto=="2"):#cargar los partidos
        envio=partidos+'0'+nombre
       # print(envio)
        connection.send(envio.encode("utf8"))#########
        #connection.send(partidos.encode("utf8"))#########
        #connection.send(nombre.encode("utf8"))#########
        connection.close()

    if(id_voto=="3"):#envio de los resultados
        #datos="INSERT INTO registro_voto values ({},'{}',AES_ENCRYPT('{}', UNHEX(SHA2('elecciones2020',512))), AES_ENCRYPT('{}', UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT('{}', UNHEX(SHA2('elecciones2020',512))))".format(id_voto, id_mesa, part, presi, vice)

        datos="INSERT INTO votos_fisicos values ('{}',{},{},{},AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),AES_ENCRYPT({}, UNHEX(SHA2('elecciones2020',512))),{},{})".format(mensaje[2], mensaje[3], mensaje[4], mensaje[5], mensaje[6], mensaje[7], mensaje[8], mensaje[9], mensaje[10], mensaje[11], mensaje[12], mensaje[13], mensaje[14], mensaje[15], mensaje[16], mensaje[17], mensaje[18], mensaje[19], mensaje[20], mensaje[21], mensaje[22], mensaje[23], mensaje[24],mensaje[25])
        #datos="INSERT INTO votos_fisicos values ('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(mensaje[2], mensaje[3], mensaje[4], mensaje[5], mensaje[6], mensaje[7], mensaje[8], mensaje[9], mensaje[10], mensaje[11], mensaje[12], mensaje[13], mensaje[14], mensaje[15], mensaje[16], mensaje[17], mensaje[18], mensaje[19], mensaje[20], mensaje[21], mensaje[22], mensaje[23], mensaje[24],mensaje[25])
        
        #datos="INSERT INTO registro_voto values (6,'02222','PRD','Danilo Medina',AES_ENCRYPT('Estoy ', UNHEX(SHA2('hola',512))))"
        mariadb_connection = mariadb.connect(user='root', password='microena', database='voto', host='127.0.0.1')#, unix_socket= '/var/run/mysqld/mysqld.sock')
        cursor = mariadb_connection.cursor()
        cursor.execute(datos)
        mariadb_connection.commit()
        

        recib="1"
        connection.send(recib.encode("utf8"))#########
        connection.close()

        #conteo=0
        if (mensaje[4]=='0'):
            conteo=1
            upda="UPDATE colegio SET conteo={} WHERE mesa='{}'".format(conteo,mensaje[2])
            cursor.execute(upda)
        elif (mensaje[4]=='1' and mensaje[5]=='1'):
            conteo=2
            upda="UPDATE colegio SET conteo={} WHERE mesa='{}'".format(conteo,mensaje[2])
            cursor.execute(upda)


        
        
        mariadb_connection.commit()
        





        
def receive_input(connection, max_buffer_size):## esta funcion tambien se puede eliminar
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
       # print("The input size is greater than expected {}".format(client_input_size))
       pass

    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    #result = process_input(decoded_input)
    result= str(decoded_input)

    return result   
        

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()
