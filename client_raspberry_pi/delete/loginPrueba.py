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
import os
#import Gtk

import ntplib
from time import ctime
from datetime import datetime

import shlex
from subprocess import call, PIPE, STDOUT
import socket

import PyQt4
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog, QLineEdit, QApplication#*
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

##class Ui_Dialog(object):
###class Ui_Dialog(Dialog):
##    def __init__(self):
##    #def setupUi(self, Dialog):
##        Dialog.__init__(self, parent=None)
##        Dialog.setObjectName(_fromUtf8("Dialog"))
##        Dialog.resize(414, 226)

class Form(QDialog):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.resize(414,226)

       
##        self.setFixedSize(1280, 740)
##        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
##        self.setGeometry(QtCore.QRect(0,-5,1280,740))

        
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(35, 25, 91, 33))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(35, 105, 91, 33))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtUser = QtGui.QLineEdit(self)
        self.txtUser.setGeometry(QtCore.QRect(170, 25, 211, 33))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))


        self.lineEdit=extQLineEdit(self)
        self.lineEdit.move(170,105)
        self.connect(self.lineEdit,SIGNAL("clicked()"), self.printText)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)

        
##        self.textPass = extQlineEdit(self)#QtGui.QLineEdit(Dialog)
##        self.textPass.setGeometry(QtCore.QRect(170, 105, 211, 33))
##        self.textPass.setObjectName(_fromUtf8("textPass"))
##        self.textPass.setEchoMode(QtGui.QLineEdit.Password)
##        self.connect(self.lineEdit,SIGNAL("clicked()"), self.printText)


        
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 165, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 170, 165, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        

        self.pushButton_2.clicked.connect(self.closeE)
        self.pushButton.clicked.connect(self.login)
        #_thread.start_new_thread(self.colegio, ())
        
            

    def login(self, event):
        _thread.start_new_thread(self.colegio, ())

     
    def closeE(self, event):
        sys.exit()

        
    def colegio(self):
        subprocess.check_output(["florence"])
                #break
        
    def printText(self):
        print("klk menor")
    def retranslateUi(self, QDialog):
        QDialog.setWindowTitle(_translate("QDialog", "Login", None))
        self.label.setText(_translate("QDialog", "Usuario:", None))
        self.label_2.setText(_translate("QDialog", "Contraseña:", None))
        self.pushButton.setText(_translate("QDialog", "Iniciar Sesión ", None))
        self.pushButton_2.setText(_translate("QDialog", "Cancelar", None))



if __name__ == "__main__":
    import sys
##    app = QtGui.QApplication(sys.argv)
##
##    form=Ui_Dialog()
##    form.show()
##
####    Dialog = QtGui.QDialog()
####    ui = Ui_Dialog()
####    ui.setupUi(Dialog)
####    Dialog.show()
##    sys.exit(app.exec_())

    app = QApplication(sys.argv)
    form =Form()
    form.show()

    sys.exit(app.exec_())

