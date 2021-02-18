# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conect.ui'
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

from random import randint
import os
import shlex
from subprocess import call, PIPE, STDOUT
Nointernet = None

from PyQt4 import QtCore, QtGui
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

        
##class Ui_Dialog1(object):
##    
##    def setupUi(self, Dialog):
class Ui_Dialog(QDialog):
    #def setupUi(self, Dialog):
    def __init__(self):
        QDialog.__init__(self, parent=None)
        
        self.setObjectName(_fromUtf8("Dialog"))
        #self.resize(1280, 740)
        self.setFixedSize(1280, 740)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(QtCore.QRect(0,-5,1280,740))

        
        self.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(450, 295, 91, 33))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(450, 375, 91, 33))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.txtUser = extQLineEdit(self)
        self.txtUser.setGeometry(QtCore.QRect(610, 295, 265, 33))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))
        self.connect(self.txtUser,SIGNAL("clicked()"), self.printText)
        
        self.textPass = extQLineEdit(self) #QtGui.QLineEdit(self)
        self.textPass.setGeometry(QtCore.QRect(610, 375, 265, 33))
        self.textPass.setObjectName(_fromUtf8("textPass"))        
        self.textPass.setEchoMode(QtGui.QLineEdit.Password)
        self.connect(self.textPass,SIGNAL("clicked()"), self.printText)

        
        self.btnlogin = QtGui.QPushButton(self)
        self.btnlogin.setGeometry(QtCore.QRect(515, 440, 140, 31))
        self.btnlogin.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btnlogin.setObjectName(_fromUtf8("btnlogin"))
        self.btncancel = QtGui.QPushButton(self)
        self.btncancel.setGeometry(QtCore.QRect(685, 440, 140, 31))
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
        self.label_3.setGeometry(QtCore.QRect(450, 230, 111, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lblestado = QtGui.QLabel(self)
        self.lblestado.setGeometry(QtCore.QRect(610, 230, 250, 21))
        self.lblestado.setText(_fromUtf8("Desconectado"))
        self.lblestado.setObjectName(_fromUtf8("lblestado"))

        self.label_13 = QtGui.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(900, 440, 411, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        

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
        
    def printText(self):
        y=0
        for pid in psutil.pids():
            try:
                p = psutil.Process(pid)
                if p.name() == "florence" and y==0:              
                    #_thread.start_new_thread(self.colegio, ())
                    y=1
            except:
                pass
        if(y==0):
            _thread.start_new_thread(self.colegio, ())

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

        
        if self.txtUser.text() and self.textPass.text():            
            
            ssid=self.txtUser.text()
            clave = self.textPass.text()
            
            f=open("wpa_supplicant.conf","w")
            f.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n"+
                    "update_config=1\n"+
                    "country=GB\n"+
                    "\n"+
                    "network={\n" +
                            "ssid="+ "\""+ssid +"\""+"\n"+
                            "psk="+ "\""+clave +"\""+"\n"+                            
                            "key_mgmt=WPA-PSK\n"+
                            "}")
            f.close()
            os.system('sudo rm /etc/wpa_supplicant/wpa_supplicant.conf')
            os.system('sudo mv wpa_supplicant.conf /etc/wpa_supplicant/')
            #print(111)
            os.system('sudo service mysql stop')
            time.sleep(1)
            #print(123)
            os.system('sudo reboot')
            

        else:
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("SSID o Contraseña Incorrecto")        
            msg.setWindowTitle("Elecciones 2020")        
            msg.setStandardButtons(QMessageBox.Ok)                    
            retval = msg.exec_()
            
            
            
    def retranslateUi(self, QDialog):
        QDialog.setWindowTitle(_translate("QDialog", "Login", None))
        self.label.setText(_translate("QDialog", "SSID:", None))
        self.label_2.setText(_translate("QDialog", "Contraseña:", None))
        self.label_13.setText(_translate("QDialog", "*Los Cambios Toman Efecto Después de Reiniciar", None))
        self.btnlogin.setText(_translate("QDialog", "Conectar*", None))
        self.btncancel.setText(_translate("QDialog", "Cancelar", None))
        self.label_3.setText(_translate("QDialog", "Estado Actual:", None))
        self.label_7.setText(_translate("QDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Conexión a Internet</span></p>", None))#"<p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\"> </span></p></body></html>", None))
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
##    ui = Ui_Dialog1()
##    ui.setupUi(Dialog)
##    Dialog.show()
##    sys.exit(app.exec_())

    app= QApplication(sys.argv)
    form = Ui_Dialog()
    form.show()
    sys.exit(app.exec_())

