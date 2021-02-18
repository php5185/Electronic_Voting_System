# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import time
import _thread
import mysql.connector as mariadb
import subprocess
import sys
import psutil

#import ntplib
#from time import ctime
#from datetime import datetime

#import shlex
#from subprocess import call, PIPE, STDOUT
import shlex
from subprocess import call, PIPE, STDOUT
Nointernet = None
import socket

from PyQt4 import QtCore, QtGui
##from PyQt4.QtGui import *
##from PyQt4.QtCore import *
from PyQt4.QtGui import QDialog, QLineEdit, QApplication, QMessageBox#*
from PyQt4.QtCore import SIGNAL#*



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


class extQLineEdit(QLineEdit):
    def __init__(self,parent):
        QLineEdit.__init__(self,parent)
    def mousePressEvent(self,QMouseEvent):
        self.emit(SIGNAL("clicked()"))

        
class Ui_Dialog(QDialog):
    #def setupUi(self, Dialog):
    def __init__(self):
        QDialog.__init__(self, parent=None)
        
        self.setObjectName(_fromUtf8("QDialog"))
        #self.resize(437, 229)

        self.setFixedSize(1280, 740)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(QtCore.QRect(0,-5,1280,740))
        

        
        self.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(450, 250, 91, 33))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(450, 330, 91, 33))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtUser = QtGui.QLineEdit(self)
        self.txtUser.setGeometry(QtCore.QRect(610, 250, 265, 33))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))


        self.txtUser.setEnabled(False)


        
        self.textPass = extQLineEdit(self) #QtGui.QLineEdit(self)
        self.textPass.setGeometry(QtCore.QRect(610, 330, 265, 33))
        self.textPass.setObjectName(_fromUtf8("textPass"))        
        self.textPass.setEchoMode(QtGui.QLineEdit.Password)
        self.connect(self.textPass,SIGNAL("clicked()"), self.printText)
        
        self.btnlogin = QtGui.QPushButton(self)
        self.btnlogin.setGeometry(QtCore.QRect(515, 395, 140, 31))
        self.btnlogin.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btnlogin.setObjectName(_fromUtf8("btnlogin"))
        self.btncancel = QtGui.QPushButton(self)
        self.btncancel.setGeometry(QtCore.QRect(685, 395, 140, 31))
        self.btncancel.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btncancel.setObjectName(_fromUtf8("btncancel"))




        self.lbl_escudo_1 = QtGui.QLabel(self)
        self.lbl_escudo_1.setGeometry(QtCore.QRect(30, 20, 61, 61))
        self.lbl_escudo_1.setStyleSheet(_fromUtf8("image: url(:/JCE/EscudoDom.png);"))
        self.lbl_escudo_1.setText(_fromUtf8(""))
        self.lbl_escudo_1.setObjectName(_fromUtf8("lbl_escudo_1"))

        self.lbl_JCE = QtGui.QLabel(self)
        self.lbl_JCE.setGeometry(QtCore.QRect(400, 10, 500, 71))
        self.lbl_JCE.setStyleSheet(_fromUtf8("image: url(:/JCE/JCEpag1.jpg);"))
        self.lbl_JCE.setText(_fromUtf8(""))
        self.lbl_JCE.setObjectName(_fromUtf8("lbl_JCE"))

        self.lbl_escudo_3 = QtGui.QLabel(self)
        self.lbl_escudo_3.setGeometry(QtCore.QRect(1180, 20, 61, 61))
        self.lbl_escudo_3.setStyleSheet(_fromUtf8("image: url(:/JCE/EscudoDom.png);"))
        self.lbl_escudo_3.setText(_fromUtf8(""))
        self.lbl_escudo_3.setObjectName(_fromUtf8("lbl_escudo_3"))

        self.lbl_info = QtGui.QLabel(self)
        self.lbl_info.setGeometry(QtCore.QRect(260, 90, 841, 41))
        self.lbl_info.setObjectName(_fromUtf8("lbl_info"))

        
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(0, 150, 1280, 70))
        self.label_7.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 255);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 111, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.lblestado = QtGui.QLabel(self)
        self.lblestado.setGeometry(QtCore.QRect(125, 250, 250, 21))
        self.lblestado.setText(_fromUtf8("Desconectado"))
        self.lblestado.setObjectName(_fromUtf8("lblestado"))
        


        user=str(sys.argv[1])
        self.txtUser.setText(user)


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        _thread.start_new_thread(self.Internet, ())
        self.btncancel.clicked.connect(self.closeE)
        self.btnlogin.clicked.connect(self.login)
        

    def Internet(self):   #un hilo     
        global Nointernet
        if is_network_alive()!=True:            
            try:
                #self.Etiqueta_1_8.SetLabel("Desconectado")
                stat="Desconectado"
                self.lblestado.setText(_fromUtf8("Desconectado"))
                Nointernet =1
                #print ('no hay')
            except:
                pass
                #print ('Error no hay internet ')
        else:
            try:
                #self.Etiqueta_1_8.SetLabel("Conectado")
                command = ("iwgetid -r")

                p = subprocess.Popen(command, universal_newlines=True, 
                shell=True, stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
                text = p.stdout.read()
                retcode = p.wait()
                
                estado="Conectado a la red "+text
                self.lblestado.setText(_fromUtf8(estado))
                Nointernet =0
                #print ('hay')
            except:
                pass
                #print ('Error hay internet')

    def printText(self):
        y=0
        for pid in psutil.pids():
            try:
                p = psutil.Process(pid)
                if p.name() == "florence" and y==0:              
                    #_thread.start_new_thread(self.colegio, ())
                    y=1
                    #break
            except:
                print("se exploto")
        if(y==0):
            _thread.start_new_thread(self.colegio, ())
        #_thread.start_new_thread(self.colegio, ())

    def colegio(self):
        subprocess.check_output(["florence"])
        

    def login(self, event):
        y=0
        for pid in psutil.pids():
            try:
                p = psutil.Process(pid)
                if p.name() == "florence" and y==0:
                    p.terminate()
                    #p.wait()
                    y=1
            except:
                pass

           
        colegios=self.txtUser.text()
        password=self.textPass.text()
        exito=1
        #if ()
        if is_network_alive()==True:
            if(colegios and password):            
                ###########3try-excep de base de datos sin conexion'error al cargar los datos. revise conexion a internet'
                try:
            
                    #datos="SELECT * FROM Colegio_electoral WHERE id_col_elec = '{}' AND pass='{}'".format(colegio, password) #AES_ENCRYPT('0314A001B', UNHEX(SHA2('eleccionesS2020',512)))
                    #datos="SELECT id_col_elec, nombre_col, provincia, municipio, sector, direccion, paraje, seccion, backup, status, AES_DECRYPT(pass, UNHEX(SHA2('elecciones2020',512))) FROM Colegio_electoral WHERE id_col_elec = '{}' AND AES_DECRYPT(pass, UNHEX(SHA2('elecciones2020',512)))='{}'".format(colegio, password) #AES_ENCRYPT('0314A001B', UNHEX(SHA2('eleccionesS2020',512)))
                    datos="SELECT id_col_elec, nombre_col, provincia, municipio, sector, direccion, paraje, seccion, backup, status FROM Colegio_electoral WHERE id_col_elec = '{}' AND AES_DECRYPT(pass, UNHEX(SHA2('elecciones2020',512)))='{}'".format(colegios, password) #AES_ENCRYPT('0314A001B', UNHEX(SHA2('eleccionesS2020',512)))
                    mariadb_connection = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')
                    

                    cursor = mariadb_connection.cursor()
                    cursor.execute(datos)
                    data = cursor.fetchall()

                    if data:

                        #######################actualizar el tiempo
                        try:
                            ntp="SELECT initCabina, finCabina, phone FROM NTP WHERE control = 1"
                            #tp="SELECT initCabina, finCabina FROM NTP WHERE control = 1"
                            mariadb_connectionTime = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')

                            cursortime = mariadb_connectionTime.cursor()
                            cursortime.execute(ntp)
                            timedata = cursortime.fetchall()

                            if timedata:
                                for row in timedata:
                                    dateVoto1=row[0]
                                    dateVoto2=row[1]
                                    phone=row[2]

                                    

                            mariadb_connectionTime.close()


                            datosntp="UPDATE NTP set initCabina='{}', finCabina='{}', phone='{}' WHERE control= 1".format(dateVoto1, dateVoto2, phone) 
                            #datos=dat
                            mariadb_connectionntp = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                            cursorntp = mariadb_connectionntp.cursor()

                            cursorntp.execute(datosntp)
                            mariadb_connectionntp.commit()
                            mariadb_connectionntp.close()            
                            #inter=0
                            #print(2)
                        except:
                            pass

                        ###############################truncate los votos''no

                        #socket para recibir el numero de backup
                        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        soc.settimeout(3)#estaba en 4 
                        #host = "192.168.30.10"#softether
                        host = "192.168.40.2" #pptp
                        port = 5557

                        eid_voto=-1
                       # eid_mesa='0314A'
                        epartido=0
                        epresidente=0
                        evicepresidente=0
                        backu=0


                        try:
                            soc.connect((host, port))
                            message = "{},{},{},{},{},{}".format(eid_voto, colegios, epartido, epresidente, evicepresidente, backu) #input(" -> ")
                            soc.sendall(message.encode("utf8"))#ver como no se quede esperando
                            recibido= soc.recv(5120).decode("utf8")
                            #soc.send(b'--quit--')#cerrar el socket, maybe quitar eso
    ##                    except socket.gaierror:
    ##                        ##poner un msj de error
    ##                        #exito en 0 y un break
    ##                        exito=0
    ##                        pass
    ##
    ##                    except socket.error:
    ##                        exito=0
    ##                        pass
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    ##                    print(22)
    ##                    #actualizar el valor de backup en la base de datos
    ##                    #envolver eso en un try except
    ##                    try:
                            eliminarCol="TRUNCATE TABLE Colegio_electoral" # num en 0
                            eliminarCed="TRUNCATE TABLE Cedula_ciudadano" # num en 0 
                            mariadb_connectionlocal = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                            cursorlocal = mariadb_connectionlocal.cursor()
                            cursorlocal2 = mariadb_connectionlocal.cursor()
                            cursorlocal.execute(eliminarCol)
                            cursorlocal2.execute(eliminarCed)                  

                            ###entrar los datos luego que se tienen todos para que no falten ninguno
                            for row in data:
                                command="INSERT INTO Colegio_electoral (id_col_elec, nombre_col, provincia, municipio, sector, direccion, paraje, seccion, backup, status) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}',{},{})".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                                cursorlocal.execute(command)####da el error aqui, HAY QUE ACTUALIZAR LA BASE DE DATOSS
                                


                            #buscar todos los votantes en la BD remota
                            votantes="SELECT * FROM Cedula_ciudadano WHERE mesa_electoral = '{}'".format(colegios)
                            cursor2 = mariadb_connection.cursor()
                            cursor2.execute(votantes)
                            votan = cursor2.fetchall()

                            for row in votan:
                                #print(row)
                                command="INSERT INTO Cedula_ciudadano VALUES {}".format(row)
                                cursorlocal2.execute(command)

                            

                            mariadb_connectionlocal.commit()
                            mariadb_connectionlocal.close()
                            mariadb_connection.close()




                            
                            rec=recibido.split(",")
                            
                            updat="UPDATE Colegio_electoral set backup={}".format(rec[0])
                            mariadb_connectiontOne = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                            cursortOne = mariadb_connectiontOne.cursor()
                            cursortOne.execute(updat)
                            mariadb_connectiontOne.commit()

                            mariadb_connectiontOne.close()

                           
                            entero=int(rec[1])+1


                            #if(entero!=0):
                            ###hacer aqui el truncate, si se hace
                            modificar="ALTER TABLE Registo_voto AUTO_INCREMENT = {}".format(entero)
                            mariadb_connectiontOne = mariadb.connect(user='prueba', password='hola', database='voto', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                            cursortOne = mariadb_connectiontOne.cursor()
                            cursortOne.execute(modificar)
                            mariadb_connectiontOne.commit()
                            mariadb_connectiontOne.close()
                        
                        except:
                            ###mensaje de error
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)

                            msg.setText("Error al Cargar los Datos. Intente Nuevamente")        
                            msg.setWindowTitle("Elecciones 2020")        
                            msg.setStandardButtons(QMessageBox.Ok)                    
                            retval = msg.exec_()                        
                            exito=0
                            pass
                        #exito=1
                        



                    else:#no hay datos en la base de datos
                        exito=0
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)

                        msg.setText("Verifique el Nombre y Contraseña de la mesa electoral")        
                        msg.setWindowTitle("Elecciones 2020")        
                        msg.setStandardButtons(QMessageBox.Ok)                    
                        retval = msg.exec_()


                        
                except:#mensaje de fallo en la conexion a internet
                    exito=0
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)

                    msg.setText("Verifique el Estado de la Conexión a Internet")        
                    msg.setWindowTitle("Elecciones 2020")        
                    msg.setStandardButtons(QMessageBox.Ok)                    
                    retval = msg.exec_()
                    pass

           
            else:#no entro nada en el txt de passw
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setText("Contraseña Digitada Incorrectamente")        
                msg.setWindowTitle("Elecciones 2020")        
                msg.setStandardButtons(QMessageBox.Ok)                    
                retval = msg.exec_()
                exito=0
        else:
            exito=0
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Verifique el Estado de la Conexión a Internet")        
            msg.setWindowTitle("Elecciones 2020")        
            msg.setStandardButtons(QMessageBox.Ok)                    
            retval = msg.exec_()
            pass

        
        if exito:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Proceso Completado Satisfactoriamente")        
            msg.setWindowTitle("Elecciones 2020")        
            msg.setStandardButtons(QMessageBox.Ok)                    
            retval = msg.exec_()
            sys.exit()
           

    def closeE(self, event):
        y=0
        for pid in psutil.pids():
            try:
                p = psutil.Process(pid)
                if p.name() == "florence" and y==0:
                    p.terminate()
                    #p.wait()
                    y=1
            except:
                pass

        sys.exit()





        

    def retranslateUi(self, QDialog):
        QDialog.setWindowTitle(_translate("QDialog", "Login", None))
        self.label.setText(_translate("QDialog", "Usuario:", None))
        self.label_2.setText(_translate("QDialog", "Contraseña:", None))
        self.label_3.setText(_translate("QDialog", "Internet:", None))
        self.btnlogin.setText(_translate("QDialog", "Iniciar Sesión ", None))
        self.btncancel.setText(_translate("QDialog", "Cancelar", None))
        self.label_7.setText(_translate("QDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Verificación de Credenciales</span></p>", None))#"<p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\"> </span></p></body></html>", None))
        self.lbl_info.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ELECCIONES ORDINARIAS GENERALES DEL 17 DE MAYO DEL 2020 PARA ELEGIR AL PRESIDENTE Y VICEPRESIDENTE DE LA REPÚBLICA</span></p></body></html>", None))

def get_return_code_of_simple_cmd(cmd, stderr=STDOUT):
	"""Execute a simple external command and return its exit status."""
	args = shlex.split(cmd)
	return call(args, stdout=PIPE, stderr=stderr)

def is_network_alive():
	cmd = "ping -c 1 www.google.com"
	return get_return_code_of_simple_cmd(cmd) == 0        

import JCE

if __name__ == "__main__":
    import sys
##    app = QtGui.QApplication(sys.argv)
##    Dialog = QtGui.QDialog()
##    ui = Ui_Dialog()
##    ui.setupUi(Dialog)
##    
##
##    
##    Dialog.setWindowModality(Qt.ApplicationModal)
##    Dialog.show()
##    sys.exit(app.exec_())
    app= QApplication(sys.argv)
    form = Ui_Dialog()
    form.show()
    sys.exit(app.exec_())

