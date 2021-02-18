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

#import ntplib
#from time import ctime
#from datetime import datetime

#import shlex
#from subprocess import call, PIPE, STDOUT
import socket

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *



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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(437, 229)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 25, 91, 33))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 105, 91, 33))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtUser = QtGui.QLineEdit(Dialog)
        self.txtUser.setGeometry(QtCore.QRect(130, 25, 265, 33))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))


        self.txtUser.setEnabled(False)


        
        self.textPass = QtGui.QLineEdit(Dialog)
        self.textPass.setGeometry(QtCore.QRect(130, 105, 265, 33))
        self.textPass.setObjectName(_fromUtf8("textPass"))
        self.textPass.setEchoMode(QtGui.QLineEdit.Password)
        self.btnlogin = QtGui.QPushButton(Dialog)
        self.btnlogin.setGeometry(QtCore.QRect(15, 170, 115, 31))
        self.btnlogin.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btnlogin.setObjectName(_fromUtf8("btnlogin"))
        self.btncancel = QtGui.QPushButton(Dialog)
        self.btncancel.setGeometry(QtCore.QRect(148, 170, 115, 31))
        self.btncancel.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btncancel.setObjectName(_fromUtf8("btncancel"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 170, 115, 31))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))


        user=str(sys.argv[1])
        print(user)
        self.txtUser.setText(user)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.btncancel.clicked.connect(self.closeE)
        self.btnlogin.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.teclado)



    
    def teclado(self, event):
        _thread.start_new_thread(self.florence, ())

    def florence(self):
        subprocess.check_output(["florence"])



    def login(self, event):
        colegio=self.txtUser.text()
        password=self.textPass.text()
        exito=1
        
        if(colegio and password):            
            ###########3try-excep de base de datos sin conexion'error al cargar los datos. revise conexion a internet'
            try:
        
                datos="SELECT * FROM Colegio_electoral WHERE id_col_elec = '{}' AND pass='{}'".format(colegio, password) 
                mariadb_connection = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')

                cursor = mariadb_connection.cursor()
                cursor.execute(datos)
                data = cursor.fetchall()

                if data:
                    
##                    eliminarCol="TRUNCATE TABLE Colegio_electoral" # num en 0
##                    eliminarCed="TRUNCATE TABLE Cedula_ciudadano" # num en 0 
##                    mariadb_connectionlocal = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
##                    cursorlocal = mariadb_connectionlocal.cursor()
##                    cursorlocal2 = mariadb_connectionlocal.cursor()
##                    cursorlocal.execute(eliminarCol)
##                    cursorlocal2.execute(eliminarCed)                  
##
##                    ###entrar los datos luego que se tienen todos para que no falten ninguno                    
##                    for row in data:
##                        command="INSERT INTO Colegio_electoral VALUES {}".format(row)
##                        cursorlocal.execute(command)####da el error aqui, HAY QUE ACTUALIZAR LA BASE DE DATOSS
##                        
##
##
##                    #buscar todos los votantes en la BD remota
##                    votantes="SELECT * FROM Cedula_ciudadano WHERE mesa_electoral = '{}'".format(colegio)
##                    cursor2 = mariadb_connection.cursor()
##                    cursor2.execute(votantes)
##                    votan = cursor2.fetchall()
##
##                    for row in votan:
##                        #print(row)
##                        command="INSERT INTO Cedula_ciudadano VALUES {}".format(row)
##                        cursorlocal2.execute(command)
##                    
##
##                    mariadb_connectionlocal.commit()
##                    mariadb_connectionlocal.close()
##                    mariadb_connection.close()

                    print(11)
            

                    ###############################truncate los votos''no




                    #socket para recibir el numero de backup
                    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    soc.settimeout(2)#estaba en 4 
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
                        message = "{},{},{},{},{},{}".format(eid_voto, colegio, epartido, epresidente, evicepresidente, backu) #input(" -> ")
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
                            command="INSERT INTO Colegio_electoral VALUES {}".format(row)
                            cursorlocal.execute(command)####da el error aqui, HAY QUE ACTUALIZAR LA BASE DE DATOSS
                            


                        #buscar todos los votantes en la BD remota
                        votantes="SELECT * FROM Cedula_ciudadano WHERE mesa_electoral = '{}'".format(colegio)
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

        if exito:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Proceso Completado Satisfactoriamente")        
            msg.setWindowTitle("Elecciones 2020")        
            msg.setStandardButtons(QMessageBox.Ok)                    
            retval = msg.exec_()
            sys.exit()
           

    def closeE(self, event):
        #subprocess.check_output(["python3", "subp.py","7"])#mensaje de exito
        sys.exit()






        

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Login", None))
        self.label.setText(_translate("Dialog", "Usuario:", None))
        self.label_2.setText(_translate("Dialog", "Contraseña:", None))
        self.btnlogin.setText(_translate("Dialog", "Iniciar Sesión ", None))
        self.btncancel.setText(_translate("Dialog", "Cancelar", None))
        self.pushButton_3.setText(_translate("Dialog", "Teclado", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    

    
    Dialog.setWindowModality(Qt.ApplicationModal)
    Dialog.show()
    sys.exit(app.exec_())

