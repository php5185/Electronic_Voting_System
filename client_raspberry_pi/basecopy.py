# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(1280, 740)
        Frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(290, 310, 161, 26))
        self.label.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnColegio = QtGui.QPushButton(Frame)
        self.btnColegio.setGeometry(QtCore.QRect(820, 310, 101, 30))
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
        self.btninit2 = QtGui.QPushButton(Frame)
        self.btninit2.setGeometry(QtCore.QRect(1050, 310, 101, 30))
        self.btninit2.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btninit2.setObjectName(_fromUtf8("btninit2"))
        self.btnwifi2 = QtGui.QPushButton(Frame)
        self.btnwifi2.setGeometry(QtCore.QRect(1050, 390, 101, 31))
        self.btnwifi2.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btnwifi2.setObjectName(_fromUtf8("btnwifi2"))
        self.btnteclado2 = QtGui.QPushButton(Frame)
        self.btnteclado2.setGeometry(QtCore.QRect(1050, 460, 101, 31))
        self.btnteclado2.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.btnteclado2.setObjectName(_fromUtf8("btnteclado2"))
        self.btnteclado2.raise_()
        self.btnwifi2.raise_()
        self.label.raise_()
        self.btnColegio.raise_()
        self.txtColegio.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.txtSetColegio.raise_()
        self.txtNombreCol.raise_()
        self.txtProvincia.raise_()
        self.txtMunicipio.raise_()
        self.xtDir.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.btninit2.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">No. Colegio Electoral:</span></p></body></html>", None))
        self.btnColegio.setText(_translate("Frame", "Cargar Datos", None))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">No. Colegio Electoral:</span></p></body></html>", None))
        self.label_3.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Dirección:</span></p></body></html>", None))
        self.label_4.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Nombre Colegio Electoral:</span></p></body></html>", None))
        self.label_5.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Provincia:</span></p></body></html>", None))
        self.label_6.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Municipio:</span></p></body></html>", None))
        self.label_7.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">El Programa de Votación estará Disponible el día 15 de Mayo del 2018</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">en Horario de 6:00 AM a 6:00 PM</span></p></body></html>", None))
        self.btninit2.setText(_translate("Frame", "Iniciar", None))
        self.btnwifi2.setText(_translate("Frame", "Internet", None))
        self.btnteclado2.setText(_translate("Frame", "Teclado", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

