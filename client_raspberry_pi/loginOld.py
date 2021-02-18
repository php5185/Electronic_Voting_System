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

import ntplib
from time import ctime
from datetime import datetime

import shlex
from subprocess import call, PIPE, STDOUT
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
        Dialog.resize(414, 226)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(35, 25, 91, 33))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(35, 105, 91, 33))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtUser = QtGui.QLineEdit(Dialog)
        self.txtUser.setGeometry(QtCore.QRect(170, 25, 211, 33))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))
        self.textPass = QtGui.QLineEdit(Dialog)
        self.textPass.setGeometry(QtCore.QRect(170, 105, 211, 33))
        self.textPass.setObjectName(_fromUtf8("textPass"))
        self.textPass.setEchoMode(QtGui.QLineEdit.Password)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 165, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 170, 165, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_2.clicked.connect(self.closeE)
        self.pushButton.clicked.connect(self.login)








    def login(self, event):
        colegio=self.txtUser.text()
        password=self.textPass.text()
        if(colegio and password):
            print(self.textPass.text())
            ###########3try-excep de base de datos sin conexion'error al cargar los datos. revise conexion a internet'
        
            datos="SELECT * FROM Colegio_electoral WHERE id_col_elec = '{}' AND pass='{}'".format(colegio, password) 
            mariadb_connection = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')

            cursor = mariadb_connection.cursor()
            cursor.execute(datos)
            data = cursor.fetchall()

            if data:
                
                eliminarCol="TRUNCATE TABLE Colegio_electoral" # num en 0
                eliminarCed="TRUNCATE TABLE Cedula_ciudadano" # num en 0 
                mariadb_connectionlocal = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                cursorlocal = mariadb_connectionlocal.cursor()
                cursorlocal2 = mariadb_connectionlocal.cursor()
                cursorlocal.execute(eliminarCol)
                cursorlocal2.execute(eliminarCed)                  

                
                for row in data:
                    command="INSERT INTO Colegio_electoral VALUES {}".format(row)
                    cursorlocal.execute(command)####da el error aqui, HAY QUE ACTUALIZAR LA BASE DE DATOSS
                    
##                    mesaelectoral=''
##                    for row in data:
##                        self.txtSetColegio.setText(row[0])
##                        mesaelectoral=row[0]
##                        self.txtNombreCol.setText(row[1])
##                        self.txtProvincia.setText(row[2])
##                        self.txtMunicipio.setText(row[3])
##                        self.xtDir.setText(row[5])

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

                ###############################truncate los votos''no




                #socket para recibir el numero de backup
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                soc.settimeout(4) 
                #host = "192.168.30.10"#softether
                host = "192.168.40.2" #pptp
                port = 5557

                eid_voto=-1
               # eid_mesa='0314A'
                epartido=0
                epresidente=0
                evicepresidente=0
                backu=0

                ###########poner aqui el mensaje de exito
                #subprocess.check_output(["python3", "subp.py","7"])#mensaje de exito

##                msg = QMessageBox()
##               # msg.setIcon(QMessageBox.Information)
##                msg.setText("Proceso Completado Satisfactoriamente")
##                #msg.setInformativeText("This is additional information")
##                msg.setWindowTitle("MessageBox demo")

##                d = QDialog()
##                b1 = QPushButton("ok",d)
##                b1.move(50,50)
##                b1.clicked.connect(hhh)
##                d.setWindowTitle("Dialog")
##                d.setWindowModality(Qt.ApplicationModal)
##                d.exec_()

                try:
                    soc.connect((host, port))
                    message = "{},{},{},{},{},{}".format(eid_voto, colegio, epartido, epresidente, evicepresidente, backu) #input(" -> ")
                    soc.sendall(message.encode("utf8"))#ver como no se quede esperando
                    recibido= soc.recv(5120).decode("utf8")
                    soc.send(b'--quit--')#cerrar el socket, maybe quitar eso
                except socket.gaierror:
                    pass

                except socket.error:
                    pass


                #actualizar el valor de backup en la base de datos
                #envolver eso en un try except
                try:
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
                    #print("backup not updated")
                    pass

                sys.exit()
                def hhh():
                    sys.exit()

                
##                mesaelectoral=''
##                for row in data:
##                    self.txtSetColegio.setText(row[0])
##                    mesaelectoral=row[0]
##                    self.txtNombreCol.setText(row[1])
##                    self.txtProvincia.setText(row[2])
##                    self.txtMunicipio.setText(row[3])
##                    self.xtDir.setText(row[5])



            else:
                subprocess.check_output(["python3", "subp.py","3"])#no existe esa mesa

        
        else:
            subprocess.check_output(["python3", "subp.py","5"])#contraseña incorrecta

    def closeE(self, event):
        subprocess.check_output(["python3", "subp.py","7"])#mensaje de exito
        sys.exit()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Login", None))
        self.label.setText(_translate("Dialog", "Usuario:", None))
        self.label_2.setText(_translate("Dialog", "Contraseña:", None))
        self.pushButton.setText(_translate("Dialog", "Iniciar Sesión ", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

