# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msj1.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        #Form.resize(1280, 740)
        Form.setFixedSize(1280, 740)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setGeometry(QtCore.QRect(0,-5,1280,740))


        
        Form.setStyleSheet(_fromUtf8("image: url(:/newPrefix/force.png);"))
        self.btnOK = QtGui.QPushButton(Form)
        self.btnOK.setGeometry(QtCore.QRect(770, 407, 90, 31))
        self.btnOK.setObjectName(_fromUtf8("btnOK"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btnOK.clicked.connect(self.close)

    def close(self, event):
        sys.exit()
        
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnOK.setText(_translate("Form", "OK", None))

import pic_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

