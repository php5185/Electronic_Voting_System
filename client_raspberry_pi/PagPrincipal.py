# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PagPrincipal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
#!/usr/bin/python3

import hashlib
import time
import _thread
import sys
from pyfingerprint.pyfingerprint import PyFingerprint
import mysql.connector as mariadb
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox, QScrollArea

import subprocess
import shlex
from subprocess import call, PIPE, STDOUT
import socket

import ntplib
import time
from time import ctime
from datetime import datetime

#from conect import Ui_Dialog1
#dateVoto2=  datetime(2018,11,18,1,50,0)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def get_return_code_of_simple_cmd(cmd, stderr=STDOUT):
    args = shlex.split(cmd)
    return call(args, stdout=PIPE, stderr=stderr)
        
class Ui_Dialog(object):
##    def mensaje (self):
##        window =QtGui.QDialog()
##        uio = Ui_Dialog1()
##        uio.setupUi(window)
##        window.show()

        
    def setupUi1(self, Dialog):#, ddate
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setFixedSize(1280, 740)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setGeometry(QtCore.QRect(0,-5,1280,740))


        
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lbl_2 = QtGui.QLabel(Dialog)
        self.lbl_2.setGeometry(QtCore.QRect(-10, 0, 1281, 111))
        self.lbl_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lbl_2.setObjectName(_fromUtf8("lbl_2"))
        self.lbl_escudo_1 = QtGui.QLabel(Dialog)
        self.lbl_escudo_1.setGeometry(QtCore.QRect(30, 20, 61, 61))
        self.lbl_escudo_1.setStyleSheet(_fromUtf8("image: url(:/JCE/EscudoDom.png);"))
        self.lbl_escudo_1.setText(_fromUtf8(""))
        self.lbl_escudo_1.setObjectName(_fromUtf8("lbl_escudo_1"))
        self.lbl_pasos = QtGui.QLabel(Dialog)
        self.lbl_pasos.setGeometry(QtCore.QRect(0, 130, 1281, 71))
        self.lbl_pasos.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 255);"))
        self.lbl_pasos.setObjectName(_fromUtf8("lbl_pasos"))
        self.lbl_paso1 = QtGui.QLabel(Dialog)
        self.lbl_paso1.setGeometry(QtCore.QRect(0, 250, 1281, 71))
        self.lbl_paso1.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 127);"))
        self.lbl_paso1.setObjectName(_fromUtf8("lbl_paso1"))
        self.lbl_paso2 = QtGui.QLabel(Dialog)
        self.lbl_paso2.setGeometry(QtCore.QRect(0, 370, 1281, 71))
        self.lbl_paso2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 127);"))
        self.lbl_paso2.setObjectName(_fromUtf8("lbl_paso2"))
        self.lbl_paso3 = QtGui.QLabel(Dialog)
        self.lbl_paso3.setGeometry(QtCore.QRect(0, 490, 1281, 71))
        self.lbl_paso3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 127);"))
        self.lbl_paso3.setObjectName(_fromUtf8("lbl_paso3"))
        self.lbl_paso4 = QtGui.QLabel(Dialog)
        self.lbl_paso4.setGeometry(QtCore.QRect(0, 610, 1281, 71))
        self.lbl_paso4.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 127);"))
        self.lbl_paso4.setObjectName(_fromUtf8("lbl_paso4"))
        self.lbl_JCE = QtGui.QLabel(Dialog)
        self.lbl_JCE.setGeometry(QtCore.QRect(400, 10, 500, 71))
        self.lbl_JCE.setStyleSheet(_fromUtf8("image: url(:/JCE/JCEpag1.jpg);"))
        self.lbl_JCE.setText(_fromUtf8(""))
        self.lbl_JCE.setObjectName(_fromUtf8("lbl_JCE"))
        self.lbl_info = QtGui.QLabel(Dialog)
        self.lbl_info.setGeometry(QtCore.QRect(260, 80, 841, 41))
        self.lbl_info.setObjectName(_fromUtf8("lbl_info"))
        self.lbl_escudo_3 = QtGui.QLabel(Dialog)
        self.lbl_escudo_3.setGeometry(QtCore.QRect(1180, 20, 61, 61))
        self.lbl_escudo_3.setStyleSheet(_fromUtf8("image: url(:/JCE/EscudoDom.png);"))
        self.lbl_escudo_3.setText(_fromUtf8(""))
        self.lbl_escudo_3.setObjectName(_fromUtf8("lbl_escudo_3"))
##        self.lbl_check1 = QtGui.QLabel(Dialog)
##        self.lbl_check1.setGeometry(QtCore.QRect(1180, 255, 61, 61))
##        self.lbl_check1.setStyleSheet(_fromUtf8("image: url(:/JCE/check.png);"))
##        self.lbl_check1.setText(_fromUtf8(""))
##        self.lbl_check1.setObjectName(_fromUtf8("lbl_check1"))
##
##        self.lbl_check1.setVisible(False)
##        
##        self.lbl_check2 = QtGui.QLabel(Dialog)
##        self.lbl_check2.setGeometry(QtCore.QRect(1180, 375, 61, 61))
##        self.lbl_check2.setStyleSheet(_fromUtf8("image: url(:/JCE/check.png);"))
##        self.lbl_check2.setText(_fromUtf8(""))
##        self.lbl_check2.setObjectName(_fromUtf8("lbl_check2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #subprocess.check_output(["python3", "base.py"])


        ntp="SELECT finCabina FROM NTP WHERE control = 1"
        mariadb_connectionTime = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')

        cursor = mariadb_connectionTime.cursor()
        cursor.execute(ntp)
        timedata = cursor.fetchall()

        if timedata:
            for row in timedata:
                dateV=row[0]

        mariadb_connectionTime.close()

        global dateVoto2
        dateVoto2=dateV
       
        
        _thread.start_new_thread(self.autentificacion, ())
        _thread.start_new_thread(self.conexion, ())


    

        
    def autentificacion(self): #quizas si se pasa el dialog aqui es mas facil poner y quitar el label
        
        while(dateVoto2 > datetime.now()):
            
            finger = str(fingerprint())

            #finger="-1"
            #time.sleep(2)
            #finger ='b64e862b5f2f5a912d7a0fba9f435240c20309fb8008d1bbbe2223923b9878db'
            #finger='f9f39084e33bc308b05cb8813ac043c9146242d6a71bb1e4d910ee28fd299d8f'
            #finger = '1906b20f6dd04b387bbf5cb2a3d020e0e11a438c6517bfd9557d246aaf0eb3df'
            if finger =='-1':
                subprocess.check_output(["python3", "/home/pi/Desktop/backup/msj1.py"])
                #print(11)
                #self.mensaje()                
                #subprocess.check_output(["python3", "modal.py"])
                
                #kk = showdialog()
                #kk.show()
                #showdialog()
                #msj()
##
#                letreto = QtGui.QMessageBox.question(Dialog, "Elecciones 2020",
#                                            "Usted no Tiene Permitido Votar en Esta Mesa Electoral")

##                msg = QMessageBox()
##                msg.setIcon(QMessageBox.Information)
##
##                msg.setText("Usted no Tiene Permitido Votar en Esta Mesa Electoral")        
##                msg.setWindowTitle("Elecciones 2020")        
##                msg.setStandardButtons(QMessageBox.Ok)                
##                retval = msg.exec_()

               # subprocess.check_output(["python3", "subp.py","1"])
                #print("Usted no tiene permitido emitir el voto en esta mesa electoral")

            else:
                dat="SELECT cedula, primer_nombre, primer_apellido FROM Cedula_ciudadano WHERE huella_pulg_der= '{}' AND voto={}".format(finger, 0)# num en 0
                datos=dat
                mariadb_connection = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                #funciona tanto si el host es 127.0.1.1 como 127.0.0.1
                cursor = mariadb_connection.cursor()

                
                cursor.execute(datos)

                # Fetch a single row using fetchone() method.
                data = cursor.fetchall()

                idc=""
                for row in data:
    ##                print ("Cedula: "+ row[0])
    ##                print("Nombre: "+row[1])
    ##                print("Apellido: "+row[2])
                    idc=row[0]
                    #print ("Cedula: %s  Nombre: %s  Apellido: %s" %row[0] %row[1] %row[2])
                    #print(row[1])
                #print ("Cedula Votante: %s " % data)
                    


                if data:
                    #print ("hay datos "+idc)
                    #self.lbl_check1.setVisible(True)
                    time.sleep(1)
                    #print(id_col)
                    subprocess.check_output(["python3", "/home/pi/Desktop/backup/boletae.py", idc, id_col, backup])
                    time.sleep(1)
                    #self.lbl_check1.setVisible(False)                

                else:
##                    msg = QMessageBox()
##                    msg.setIcon(QMessageBox.Information)
##
##                    msg.setText("Usted Ya Emitió Su Voto Exitosamente")        
##                    msg.setWindowTitle("Elecciones 2020")        
##                    msg.setStandardButtons(QMessageBox.Ok)                    
##                    retval = msg.exec_()
                    #subprocess.check_output(["python3", "subp.py","2"])
                    subprocess.check_output(["python3", "/home/pi/Desktop/backup/msj2.py"])

                mariadb_connection.close()##agrege eso
                    
        subprocess.check_output(["python3", "/home/pi/Desktop/backup/base.py"])
        


#enviar sms y reenviar datos guardados no enviados


    def conexion(self):
        up=1#va en 1
        #buscar el Numero telefonico en la base de datos
        
        
        #llego="Se reestablecio la conexion en la mesa electoral "+id_col #poner eso de la bd
        fue="Se perdio la conexion en la mesa electoral "+id_col
        while(dateVoto2 > datetime.now()):#tiempo de la pi
            
            #up=1
            cmd = "ping -c 1 8.8.8.8"
            if (get_return_code_of_simple_cmd(cmd) == 0):

                ###########marcar usuarios que votaron en amazon

                datosss="SELECT cedula FROM Cedula_ciudadano WHERE voto=1 AND actualizar=0"    #0
                mariadb_connection = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                #funciona tanto si el host es 127.0.1.1 como 127.0.0.1
                cursor = mariadb_connection.cursor()
                cursor.execute(datosss)
                data = cursor.fetchall()


                mariadb_connectionRemota = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')
                cursorRemota = mariadb_connectionRemota.cursor()

                if data: #atualizar update en local y voto en remota
                    for row in data:
                        votoUpdate="UPDATE Cedula_ciudadano set voto=1, actualizar =1 WHERE cedula= '{}'".format(row[0])    
                        cursorRemota.execute(votoUpdate)
                        mariadb_connectionRemota.commit()
                        upda="UPDATE Cedula_ciudadano set actualizar=1 WHERE cedula= '{}'".format(row[0])
                        cursor.execute(upda)
                        mariadb_connection.commit()
                        
                        
                mariadb_connection.close()
                mariadb_connectionRemota.close()



                #agregado hasta el if
                datos="SELECT * FROM Registo_voto WHERE recibido=0"
                mariadb_connection = mariadb.connect(user='prueba', password='hola', database='voto', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                cursor = mariadb_connection.cursor()

                cursor.execute(datos)

                
                data = cursor.fetchall()            

                if data:
                    
                    for row in data:
                        
                        eid_voto = row[0]
                        eid_mesa = row[1]
                        epartido = row[2]
                        epresidente = row[3]
                        evicepresidente = row[4]
                        message = "{},{},{},{},{},{}".format(eid_voto, eid_mesa, epartido, epresidente, evicepresidente, backup) #input(" -> ")
                        time.sleep(5)
                        
                        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        soc.settimeout(3) 
                        #host = "192.168.30.10"#softether
                        host = "192.168.40.2" #pptp
                        port = 5557

                        try:
                             
                            
                            soc.connect((host, port))                           
                            
                            soc.sendall(message.encode("utf8"))#ver como no se quede esperando
                            recibido= soc.recv(5120).decode("utf8")
                            #time.sleep(1)
                            #soc.send(b'--quit--')#cerrar el socket
                            time.sleep(3)

                            rec=recibido.split(",")

                            datosupdate= "UPDATE Registo_voto SET recibido=1 WHERE id_voto={} and id_mesa_elec='{}'".format(rec[0],rec[1])##############3                      
                            cursor.execute(datosupdate)                        
                            mariadb_connection.commit()                       
                        except socket.gaierror:
                            pass

                        except socket.error:
                            pass

                mariadb_connection.close()
                
                if(up==0):#esto va en 0
                    mariadb_connectionlocal = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                    cursor2 = mariadb_connectionlocal.cursor()

                    votantes="SELECT phone FROM NTP"
                    cursor2.execute(votantes)
                    votan = cursor2.fetchall()

                    for row in votan:
                        phone= row[0]
                        
                    mariadb_connectionlocal.close()
                    
                    
                    try:
                        print(1)
                        llego="Se reestablecio la conexion en la mesa electoral "+id_col #poner eso de la bd
                        subprocess.check_output(["python", "gsm1.py", llego, phone])
                    except:
                        print(9)
                        pass


##                    datos="SELECT * FROM Registo_voto WHERE recibido=0"
##                    mariadb_connection = mariadb.connect(user='prueba', password='hola', database='voto', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
##                    cursor = mariadb_connection.cursor()
##
##                    cursor.execute(datos)
##
##                    # Fetch a single row using fetchone() method.
##                    data = cursor.fetchall()            
##
##                    if data:
##                        
##                        for row in data:
##                            
##                            eid_voto = row[0]
##                            eid_mesa = row[1]
##                            epartido = row[2]
##                            epresidente = row[3]
##                            evicepresidente = row[4]
##                            message = "{},{},{},{},{},{}".format(eid_voto, eid_mesa, epartido, epresidente, evicepresidente, backup) #input(" -> ")
##                            time.sleep(5)
##
##                            try:
##                                
##                                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##                                soc.settimeout(3) 
##                                #host = "192.168.30.10"#softether
##                                host = "192.168.40.2" #pptp
##                                port = 5557
##                                
##                                soc.connect((host, port))
##                                
##                                
##                                soc.sendall(message.encode("utf8"))#ver como no se quede esperando
##                                recibido= soc.recv(5120).decode("utf8")
##                                time.sleep(1)
##                                #soc.send(b'--quit--')#cerrar el socket
##                                time.sleep(3)
##
##                                rec=recibido.split(",")
##
##                                datosupdate= "UPDATE Registo_voto SET recibido=1 WHERE id_voto={} and id_mesa_elec='{}'".format(rec[0],rec[1])##############3                      
##                                cursor.execute(datosupdate)                        
##                                mariadb_connection.commit()                       
##                            except socket.gaierror:
##                                pass
##
##                            except socket.error:
##                                pass
##
##                    mariadb_connection.close()

               
                up=1
                time.sleep(100)# en 300
            else:                
                if (up==1):
                    mariadb_connectionlocal = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                    cursor2 = mariadb_connectionlocal.cursor()

                    votantes="SELECT phone FROM NTP"
                    cursor2.execute(votantes)
                    votan = cursor2.fetchall()

                    for row in votan:
                        phone= row[0]
                        
                    mariadb_connectionlocal.close()
                    
                    try:
                        print(123)
                        subprocess.check_output(["python", "gsm1.py", fue, phone])
                    except:
                        print(10)
                        pass
                    time.sleep(100)# en 300
                up=0
                
  
             
        
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lbl_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.lbl_pasos.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Pasos Para Votar:</span></p></body></html>", None))
        self.lbl_paso1.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">1- Coloque su Pulgar Derecho en el Lector de Huella </span></p></body></html>", None))
        self.lbl_paso2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">2- Seleccione al Candidato o Partido de su Preferencia</span></p></body></html>", None))
        self.lbl_paso3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">3- Presione el Botón &quot;Votar&quot;</span></p></body></html>", None))
        self.lbl_paso4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">4- Deposite el Comprobante de Votación Físico en la Urna</span></p></body></html>", None))
        self.lbl_info.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ELECCIONES ORDINARIAS GENERALES DEL 17 DE MAYO DEL 2020 PARA ELEGIR AL PRESIDENTE Y VICEPRESIDENTE DE LA REPÚBLICA</span></p></body></html>", None))

import JCE



def msj():
    letreto = QtGui.QMessageBox.question(Dialog, "Elecciones 2020",
                                            "Usted no Tiene Permitido Votar en Esta Mesa Electoral")

##    msg = QMessageBox()
##    msg.setIcon(QMessageBox.Information)
##
##    msg.setText("Esta Mesa Electoral Ya Tiene La Información Necesaria Cargada")        
##    msg.setWindowTitle("Elecciones 2020")        
##    msg.setStandardButtons(QMessageBox.Ok)                    
##    retval = msg.exec_()

#class showdialog(QtGui.QDialog):
class extQLineEdit(QScrollArea):
    def __init__(self,parent):        
        d = QtGui.QScrollArea()
        b1 = QtGui.QPushButton("ok",d)
        b1.move(50,50)
        d.setWindowTitle("Dialog")
   #d.setWindowModality(QtGui.ApplicationModal)
   #d.show() 
   
def fingerprint():
    
        try:
            f = PyFingerprint('/dev/ttyUSBPort1', 57600, 0xFFFFFFFF, 0x00000000)

            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

        ## Gets some sensor information
        #print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

        ## Tries to search the finger and calculate hash
        try:
            #print('Waiting for finger...')

            ## Wait that finger is read
            while ( f.readImage() == False): #poner condicion del tiempo
                if ( dateVoto2 < datetime.now()):
                    subprocess.check_output(["python3", "/home/pi/Desktop/backup/base.py"])
                pass

            ## Converts read image to characteristics and stores it in charbuffer 1
            f.convertImage(0x01)
            
            ## Searchs template
            result = f.searchTemplate()

            positionNumber = result[0]
            accuracyScore = result[1]

            if ( positionNumber == -1 ): #poner condicion de retorno si se acaba el tiempo, y arriba poner if para llamar a base si return -2
                #print('No match found!')                                     
                return -1
                #exit(0)
            #else:
                #print('Found template at position #' + str(positionNumber))
                #print('The accuracy score is: ' + str(accuracyScore))

            ## OPTIONAL stuff
            ##

            ## Loads the found template to charbuffer 1
            f.loadTemplate(positionNumber, 0x01)

            ## Downloads the characteristics of template loaded in charbuffer 1
            characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

            ## Hashes characteristics of template
            #print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())
            return hashlib.sha256(characterics).hexdigest()

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            exit(1)



if __name__ == "__main__":

    mariadb_connection = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
    #funciona tanto si el host es 127.0.1.1 como 127.0.0.1
    cursor = mariadb_connection.cursor()

    get="SELECT id_col_elec, backup FROM Colegio_electoral" #buscar aqui el backup
    cursor.execute(get)
    colegio= cursor.fetchall()
    global id_col
    global backup
    for row in colegio:
        id_col=row[0]
        backup=str(row[1])
    mariadb_connection.close()
    
   
    app = QtGui.QApplication(sys.argv)

    
    
    Dialog = QtGui.QDialog()
    #Dialog = QtGui.QScrollArea()
    ui1 = Ui_Dialog()
    ui1.setupUi1(Dialog)    #, ddate
    Dialog.show()   
    sys.exit(app.exec_())

