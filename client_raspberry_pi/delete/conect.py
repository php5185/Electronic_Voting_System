# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conect.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(433, 256)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(25, 70, 91, 33))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(25, 135, 91, 33))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtUser = QtGui.QLineEdit(Dialog)
        self.txtUser.setGeometry(QtCore.QRect(140, 70, 265, 33))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))
        self.textPass = QtGui.QLineEdit(Dialog)
        self.textPass.setGeometry(QtCore.QRect(140, 135, 265, 33))
        self.textPass.setObjectName(_fromUtf8("textPass"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(25, 200, 115, 31))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(156, 200, 115, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(25, 20, 111, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lblestado = QtGui.QLabel(Dialog)
        self.lblestado.setGeometry(QtCore.QRect(140, 20, 141, 21))
        self.lblestado.setText(_fromUtf8(""))
        self.lblestado.setObjectName(_fromUtf8("lblestado"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(289, 200, 115, 31))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Login", None))
        self.label.setText(_translate("Dialog", "SSID:", None))
        self.label_2.setText(_translate("Dialog", "Contraseña:", None))
        self.pushButton.setText(_translate("Dialog", "Conectar", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))
        self.label_3.setText(_translate("Dialog", "Estado Actual:", None))
        self.pushButton_3.setText(_translate("Dialog", "Teclado", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

