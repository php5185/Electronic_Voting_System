# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
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

##dateVoto1= datetime(2018,11,18,1,41,0)
##dateVoto2=  datetime(2018,11,18,1,50,0)

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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(1280, 740)
        Frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)

        self.lbl_escudo_1 = QtGui.QLabel(Frame)
        self.lbl_escudo_1.setGeometry(QtCore.QRect(30, 20, 61, 61))
        self.lbl_escudo_1.setStyleSheet(_fromUtf8("image: url(:/JCE/EscudoDom.png);"))
        self.lbl_escudo_1.setText(_fromUtf8(""))
        self.lbl_escudo_1.setObjectName(_fromUtf8("lbl_escudo_1"))

        self.lbl_JCE = QtGui.QLabel(Frame)
        self.lbl_JCE.setGeometry(QtCore.QRect(400, 10, 500, 71))
        self.lbl_JCE.setStyleSheet(_fromUtf8("image: url(:/JCE/JCEpag1.jpg);"))
        self.lbl_JCE.setText(_fromUtf8(""))
        self.lbl_JCE.setObjectName(_fromUtf8("lbl_JCE"))

        self.lbl_escudo_3 = QtGui.QLabel(Frame)
        self.lbl_escudo_3.setGeometry(QtCore.QRect(1180, 20, 61, 61))
        self.lbl_escudo_3.setStyleSheet(_fromUtf8("image: url(:/JCE/EscudoDom.png);"))
        self.lbl_escudo_3.setText(_fromUtf8(""))
        self.lbl_escudo_3.setObjectName(_fromUtf8("lbl_escudo_3"))

        self.lbl_info = QtGui.QLabel(Frame)
        self.lbl_info.setGeometry(QtCore.QRect(260, 90, 841, 41))
        self.lbl_info.setObjectName(_fromUtf8("lbl_info"))


        
        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(290, 310, 161, 26))
        self.label.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnColegio = QtGui.QPushButton(Frame)
        self.btnColegio.setGeometry(QtCore.QRect(820, 310, 101, 26))
        self.btnColegio.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btnColegio.setObjectName(_fromUtf8("btnColegio"))
        self.txtColegio = QtGui.QLineEdit(Frame)
        self.txtColegio.setGeometry(QtCore.QRect(550, 310, 201, 26))
        self.txtColegio.setObjectName(_fromUtf8("txtColegio"))
        self.label_2 = QtGui.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(290, 390, 141, 26))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(290, 670, 71, 26))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(290, 460, 161, 26))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(290, 530, 61, 26))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Frame)
        self.label_6.setGeometry(QtCore.QRect(290, 600, 81, 26))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtSetColegio = QtGui.QLineEdit(Frame)
        self.txtSetColegio.setEnabled(False)
        self.txtSetColegio.setGeometry(QtCore.QRect(550, 390, 371, 26))
        self.txtSetColegio.setObjectName(_fromUtf8("txtSetColegio"))
        self.txtNombreCol = QtGui.QLineEdit(Frame)
        self.txtNombreCol.setEnabled(False)
        self.txtNombreCol.setGeometry(QtCore.QRect(550, 460, 371, 26))
        self.txtNombreCol.setObjectName(_fromUtf8("txtNombreCol"))
        self.txtProvincia = QtGui.QLineEdit(Frame)
        self.txtProvincia.setEnabled(False)
        self.txtProvincia.setGeometry(QtCore.QRect(550, 530, 371, 26))
        self.txtProvincia.setObjectName(_fromUtf8("txtProvincia"))
        self.txtMunicipio = QtGui.QLineEdit(Frame)
        self.txtMunicipio.setEnabled(False)
        self.txtMunicipio.setGeometry(QtCore.QRect(550, 600, 371, 26))
        self.txtMunicipio.setObjectName(_fromUtf8("txtMunicipio"))
        self.xtDir = QtGui.QLineEdit(Frame)
        self.xtDir.setEnabled(False)
        self.xtDir.setGeometry(QtCore.QRect(550, 670, 371, 26))
        self.xtDir.setObjectName(_fromUtf8("xtDir"))
        self.label_7 = QtGui.QLabel(Frame)
        self.label_7.setGeometry(QtCore.QRect(0, 140, 1280, 101))
        self.label_7.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 255);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_10 = QtGui.QLabel(Frame)
        self.label_10.setGeometry(QtCore.QRect(270, 30, 121, 51))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))








##        self.btninit2 = QtGui.QPushButton(Frame)
##        self.btninit2.setGeometry(QtCore.QRect(1090, 310, 151, 30))
##        self.btninit2.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
##        self.btninit2.setObjectName(_fromUtf8("btninit2"))
##        self.btnwifi1 = QtGui.QPushButton(Frame)
##        self.btnwifi1.setGeometry(QtCore.QRect(1090, 390, 41, 28))
##        self.btnwifi1.setStyleSheet(_fromUtf8("border-image: url(:/icon/wifi.jpg);"))
##        self.btnwifi1.setText(_fromUtf8(""))
##        self.btnwifi1.setObjectName(_fromUtf8("btnwifi1"))
##        self.btnteclado1 = QtGui.QPushButton(Frame)
##        self.btnteclado1.setGeometry(QtCore.QRect(1090, 460, 41, 29))
##        self.btnteclado1.setStyleSheet(_fromUtf8("border-image: url(:/icon/teclado.png);"))
##        self.btnteclado1.setText(_fromUtf8(""))
##        self.btnteclado1.setObjectName(_fromUtf8("btnteclado1"))
        self.btnwifi2 = QtGui.QPushButton(Frame)
        self.btnwifi2.setGeometry(QtCore.QRect(1090, 310, 151, 30))
        self.btnwifi2.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btnwifi2.setObjectName(_fromUtf8("btnwifi2"))
        
        self.btnteclado2 = QtGui.QPushButton(Frame)
        self.btnteclado2.setGeometry(QtCore.QRect(1090, 390, 151, 31))
        self.btnteclado2.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btnteclado2.setObjectName(_fromUtf8("btnteclado2"))
##        self.btninit1 = QtGui.QPushButton(Frame)
##        self.btninit1.setGeometry(QtCore.QRect(1090, 310, 41, 28))
##        self.btninit1.setStyleSheet(_fromUtf8("border-image: url(:/icon/iniciar.png);"))
##        self.btninit1.setText(_fromUtf8(""))
##        self.btninit1.setObjectName(_fromUtf8("btninit1"))
        self.btnteclado2.raise_()
        self.btnwifi2.raise_()
        #self.btninit2.raise_()
        #self.btnwifi1.raise_()
        #self.btnteclado1.raise_()
        #self.btninit1.raise_()



        

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        _thread.start_new_thread(self.colegioss, ())
        self.btnColegio.clicked.connect(self.verificacion)
        self.btnteclado2.clicked.connect(self.teclado)


        
        #crear un nuevo hilo para verificar el tiempo y cerrar base
        _thread.start_new_thread(self.habilitar, ())

    def teclado(self, event):
        _thread.start_new_thread(self.florence, ())

    def florence(self):
        subprocess.check_output(["florence"])

        
    def verificacion(self, event):

        veri = self.txtSetColegio.text()

        if veri:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Esta Mesa Electoral Ya Tiene La Información Necesaria Cargada")        
            msg.setWindowTitle("Elecciones 2020")        
            msg.setStandardButtons(QMessageBox.Ok)                    
            retval = msg.exec_()
            #subprocess.check_output(["python3", "subp.py","4"])

        else: 
            colegio = self.txtColegio.text()
            #print(colegio)

            if colegio:#buscar en la bd del backup

                subprocess.check_output(["python3", "login.py", colegio])
                _thread.start_new_thread(self.colegioss, ())
                
                

            else:
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setText("Verifique el Nombre de la mesa electoral")        
                msg.setWindowTitle("Elecciones 2020")        
                msg.setStandardButtons(QMessageBox.Ok)                    
                retval = msg.exec_()
                #subprocess.check_output(["python3", "subp.py","6"])

    def colegioss(self):
        
        datos="SELECT id_col_elec, nombre_col, provincia, municipio, direccion FROM Colegio_electoral" # num en 0        
        mariadb_connectionlocal = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
        
        cursor = mariadb_connectionlocal.cursor()

        
        cursor.execute(datos)
        data = cursor.fetchall()

        if data:
            for row in data:
                self.txtSetColegio.setText(row[0])
                self.txtNombreCol.setText(row[1])
                self.txtProvincia.setText(row[2])
                self.txtMunicipio.setText(row[3])
                self.xtDir.setText(row[4])
                #print(row[0])
                
            #print ("Cedula Votante: %s " % data)          

        
        mariadb_connectionlocal.close()




    def habilitar(self):
        #buscar el tiempo agrege eso
        ntp="SELECT initCabina, finCabina FROM NTP WHERE control = 1"
        mariadb_connectionTime = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')

        cursor = mariadb_connectionTime.cursor()
        cursor.execute(ntp)
        timedata = cursor.fetchall()

        if timedata:
            for row in timedata:
                dateVoto1=row[0]
                dateVoto2=row[1]

        mariadb_connectionTime.close()
        print(dateVoto1)
        print(dateVoto2)


        
        datos="UPDATE NTP set initCabina='{}', finCabina='{}' WHERE control= 1".format(dateVoto1, dateVoto2) 
        #datos=dat
        mariadb_connection = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
        cursor = mariadb_connection.cursor()

        cursor.execute(datos)
        mariadb_connection.commit()

        mariadb_connection.close()



        






        
        while(1):
            #print(55)
            veri = self.txtSetColegio.text()
            if (veri and dateVoto1 < datetime.now() and dateVoto2 > datetime.now()):
                
                time.sleep(2)#quitar ese sleep
                subprocess.check_output(["python3", "PagPrincipal.py"])
                

            if (dateVoto2 < datetime.now()):
                
                #revisar conexion y enviar datos que falten

                cmd = "ping -c 1 8.8.8.8"
                datos="SELECT * FROM Registo_voto WHERE recibido=0"
                #datos=dat
                mariadb_connection = mariadb.connect(user='prueba', password='hola', database='voto', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                cursor = mariadb_connection.cursor()

                cursor.execute(datos)

                # Fetch a single row using fetchone() method.
                data = cursor.fetchall()
                mariadb_connection.close()

                if data:
                    while(1):
                        if (get_return_code_of_simple_cmd(cmd) == 0):
                            llego="Se reestablecio la conexion en la mesa electoral "+self.txtSetColegio.text()
                            #subprocess.check_output(["python", "gsm1.py", llego])

                            datos3="SELECT cedula FROM Cedula_ciudadano WHERE voto=1 AND actualizar=0"    #0

                            mariadb_connectionOne = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                            #funciona tanto si el host es 127.0.1.1 como 127.0.0.1
                            cursorOne = mariadb_connectionOne.cursor()
                            cursorOne.execute(datos3)
                            data3 = cursorOne.fetchall()


                            mariadb_connectionRemota = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com', connect_timeout=2)
                            cursorRemota = mariadb_connectionRemota.cursor()

                            if data3: #atualizar update en local y voto en remota
                                for row in data3:
                                    votoUpdate="UPDATE Cedula_ciudadano set voto=1, actualizar =1 WHERE cedula= '{}'".format(row[0])    
                                    cursorRemota.execute(votoUpdate)
                                    mariadb_connectionRemota.commit()
                                    upda="UPDATE Cedula_ciudadano set actualizar=1 WHERE cedula= '{}'".format(row[0])
                                    cursorOne.execute(upda)
                                    mariadb_connectionOne.commit()
                                                                        
                                    
                            mariadb_connectionOne.close()
                            mariadb_connectionRemota.close()

                            #buscar el valor del backup

                            mariadb_connection = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                            cursor = mariadb_connection.cursor()

                            get="SELECT backup FROM Colegio_electoral" #buscar aqui el backup
                            cursor.execute(get)
                            colegio= cursor.fetchall()
                            global backup
                            for row in colegio:
                                backup=row[0]
                            mariadb_connection.close()
                            #print(backup)
                            

                            for row in data:
                                    eid_voto = row[0]
                                    eid_mesa = row[1]
                                    epartido = row[2]
                                    epresidente = row[3]
                                    evicepresidente = row[4]
                                    message = "{},{},{},{},{},{}".format(eid_voto, eid_mesa, epartido, epresidente, evicepresidente, backup) #input(" -> ")
                                    #print(message)
                                    time.sleep(2)

                                    try:
                                        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        soc.settimeout(3) 
                                        #host = "192.168.30.10"#softether
                                        host = "192.168.40.2" #pptp
                                        port = 5557
                                        
                                        soc.connect((host, port))
                                        #print(99)
                                        
                                        
                                        soc.sendall(message.encode("utf8"))#ver como no se quede esperando
                                        #print("here")
                                        recibido= soc.recv(5120).decode("utf8")
                                        time.sleep(1)
                                        #soc.send(b'--quit--')#cerrar el socket
                                        #time.sleep(3)###quite eso

                                        rec=recibido.split(",")

                                        datosupdate= "UPDATE Registo_voto SET recibido=1 WHERE id_voto={} and id_mesa_elec='{}'".format(rec[0],rec[1])##############3                      
                                        cursor.execute(datosupdate)                        
                                        mariadb_connection.commit()                       
                                    except socket.gaierror:
                                        pass

                                    except socket.error:
                                        pass

                            mariadb_connection.close()
                            break

###talves deberia apagar la maquina
                
                #print("ya no se habilita mas")
                break
            
                 


    def cerrar(self, event):
        sys.exit(app.exec_())
        #sys.exit()

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">No. Colegio Electoral:</span></p></body></html>", None))
        self.btnColegio.setText(_translate("Frame", "Cargar Datos", None))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">No. Colegio Electoral:</span></p></body></html>", None))
        self.label_3.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Dirección:</span></p></body></html>", None))
        self.label_4.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Nombre Colegio Electoral:</span></p></body></html>", None))
        self.label_5.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Provincia:</span></p></body></html>", None))
        self.label_6.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Municipio:</span></p></body></html>", None))
        self.label_7.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">El Programa de Votación estará Disponible el día 17 de Mayo del 2020</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">en Horario de 6:00 AM a 6:00 PM</span></p></body></html>", None))
        self.lbl_info.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ELECCIONES ORDINARIAS GENERALES DEL 17 DE MAYO DEL 2020 PARA ELEGIR AL PRESIDENTE Y VICEPRESIDENTE DE LA REPÚBLICA</span></p></body></html>", None))
       # self.btninit2.setText(_translate("Frame", "Iniciar", None))
        self.btnwifi2.setText(_translate("Frame", "Wifi", None))
        self.btnteclado2.setText(_translate("Frame", "Teclado", None))

def get_return_code_of_simple_cmd(cmd, stderr=STDOUT):
    args = shlex.split(cmd)
    return call(args, stdout=PIPE, stderr=stderr)

#import icon
import JCE

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

