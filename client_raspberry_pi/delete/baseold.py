# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

#!/usr/bin/python3


import time
import _thread
import mysql.connector as mariadb
import subprocess

from PyQt4 import QtCore, QtGui

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
        Frame.resize(490, 520)
        Frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(20, 35, 161, 23))
        self.label.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnColegio = QtGui.QPushButton(Frame)
        self.btnColegio.setGeometry(QtCore.QRect(370, 33, 101, 25))
        self.btnColegio.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 255);"))
        self.btnColegio.setObjectName(_fromUtf8("btnColegio"))
        self.txtColegio = QtGui.QLineEdit(Frame)
        self.txtColegio.setGeometry(QtCore.QRect(200, 35, 141, 23))
        self.txtColegio.setObjectName(_fromUtf8("txtColegio"))
        self.label_2 = QtGui.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 141, 23))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 71, 23))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 161, 23))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 61, 23))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Frame)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 81, 23))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtSetColegio = QtGui.QLineEdit(Frame)
        self.txtSetColegio.setEnabled(False)
        self.txtSetColegio.setGeometry(QtCore.QRect(200, 90, 271, 23))
        self.txtSetColegio.setObjectName(_fromUtf8("txtSetColegio"))
        self.txtNombreCol = QtGui.QLineEdit(Frame)
        self.txtNombreCol.setEnabled(False)
        self.txtNombreCol.setGeometry(QtCore.QRect(200, 130, 271, 23))
        self.txtNombreCol.setObjectName(_fromUtf8("txtNombreCol"))
        self.txtProvincia = QtGui.QLineEdit(Frame)
        self.txtProvincia.setEnabled(False)
        self.txtProvincia.setGeometry(QtCore.QRect(200, 170, 271, 23))
        self.txtProvincia.setObjectName(_fromUtf8("txtProvincia"))
        self.txtMunicipio = QtGui.QLineEdit(Frame)
        self.txtMunicipio.setEnabled(False)
        self.txtMunicipio.setGeometry(QtCore.QRect(200, 210, 271, 23))
        self.txtMunicipio.setObjectName(_fromUtf8("txtMunicipio"))
        self.xtDir = QtGui.QLineEdit(Frame)
        self.xtDir.setEnabled(False)
        self.xtDir.setGeometry(QtCore.QRect(200, 250, 271, 23))
        self.xtDir.setObjectName(_fromUtf8("xtDir"))
        self.label_7 = QtGui.QLabel(Frame)
        self.label_7.setGeometry(QtCore.QRect(10, 300, 471, 71))
        self.label_7.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 255);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Frame)
        self.label_8.setGeometry(QtCore.QRect(20, 440, 81, 23))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Frame)
        self.label_9.setGeometry(QtCore.QRect(20, 400, 91, 23))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.txtFecha = QtGui.QLineEdit(Frame)
        self.txtFecha.setEnabled(False)
        self.txtFecha.setGeometry(QtCore.QRect(200, 400, 271, 23))
        self.txtFecha.setObjectName(_fromUtf8("txtFecha"))
        self.txtHora = QtGui.QLineEdit(Frame)
        self.txtHora.setEnabled(False)
        self.txtHora.setGeometry(QtCore.QRect(200, 440, 271, 23))
        self.txtHora.setObjectName(_fromUtf8("txtHora"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        self.btnColegio.clicked.connect(self.verificacion)


        _thread.start_new_thread(self.colegio, ())

    def verificacion(self, event):

        veri = self.txtSetColegio.text()

        if veri:
            subprocess.check_output(["python3", "subp.py","4"])

        else: 
            colegio = self.txtColegio.text()
            #print(colegio)

            if colegio:

                datos="SELECT * FROM Colegio_electoral WHERE id_col_elec = '{}'".format(colegio) 
                mariadb_connection = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com')
                ##
                ##
                ###funciona tanto si el host es 127.0.1.1 como 127.0.0.1
                cursor = mariadb_connection.cursor()
                ##
                ### execute SQL query using execute() method.
                ###cursor.execute("SELECT cedula FROM Cedula_ciudadano WHERE huella_pulg_der= '%s' ", finger)
                ###cursor.execute("SELECT cedula FROM Cedula_ciudadano WHERE huella_pulg_der='b64e862b5f2f5a912d7a0fba9f435240c20309fb8008d1bbbe'")
                ###cursor.execute("SELECT huella_pulg_der FROM Cedula_ciudadano")
                cursor.execute(datos)
                ##
                ### Fetch a single row using fetchone() method.
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
                        cursorlocal.execute(command)

                    for row in data:
                        self.txtSetColegio.setText(row[0])
                        self.txtNombreCol.setText(row[1])
                        self.txtProvincia.setText(row[2])
                        self.txtMunicipio.setText(row[3])
                        self.xtDir.setText(row[5])

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

                else:
                    subprocess.check_output(["python3", "subp.py","3"])


            else:
                subprocess.check_output(["python3", "subp.py","3"])

    def colegio(self):
        
        datos="SELECT id_col_elec, nombre_col, provincia, municipio, direccion FROM Colegio_electoral" # num en 0        
        mariadb_connectionlocal = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
        #funciona tanto si el host es 127.0.1.1 como 127.0.0.1
        cursor = mariadb_connectionlocal.cursor()

        
        cursor.execute(datos)

        # Fetch a single row using fetchone() method.
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








        
    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">No. Colegio Electoral:</span></p></body></html>", None))
        self.btnColegio.setText(_translate("Frame", "Cargar Datos", None))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">No. Colegio Electoral:</span></p></body></html>", None))
        self.label_3.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Dirección:</span></p></body></html>", None))
        self.label_4.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Nombre Colegio Electoral:</span></p></body></html>", None))
        self.label_5.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Provincia:</span></p></body></html>", None))
        self.label_6.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Municipio:</span></p></body></html>", None))
        self.label_7.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">El Programa de Votación Estará Disponible el día 15 de Mayo del 2018</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">en Horario de 6:00 AM a 6:00 PM</span></p></body></html>", None))
        self.label_8.setText(_translate("Frame", "Hora Actual:", None))
        self.label_9.setText(_translate("Frame", "Fecha Actual:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

