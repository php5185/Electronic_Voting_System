# -*- coding: utf-8 -*-
#!/usr/bin/python3

# Form implementation generated from reading ui file 'boletaA.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import mysql.connector as mariadb
from PyQt4 import QtCore, QtGui
import socket
import sys
import time
import _thread
import os


import shlex
from subprocess import call, PIPE, STDOUT


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

class Ui_ScrollArea(object):
    def setupUi(self, ScrollArea, ced, id_col, back):
        
        global cedula
        cedula =ced
        global colegio
        colegio= id_col        
        global backup
        backup=back
        
        ScrollArea.setObjectName(_fromUtf8("ScrollArea"))
        ScrollArea.setEnabled(True)
        #ScrollArea.resize(1276, 688)

        ScrollArea.setFixedSize(1280, 740)
        ScrollArea.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ScrollArea.setGeometry(QtCore.QRect(0,-5,1280,740))


        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScrollArea.sizePolicy().hasHeightForWidth())
        ScrollArea.setSizePolicy(sizePolicy)
        ScrollArea.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1274, 686))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.lbl_1 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_1.setGeometry(QtCore.QRect(0, 46, 1271, 41))
        self.lbl_1.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 127);"))
        self.lbl_1.setObjectName(_fromUtf8("lbl_1"))
        self.lbl_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_2.setGeometry(QtCore.QRect(0, 0, 1271, 46))
        self.lbl_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lbl_2.setObjectName(_fromUtf8("lbl_2"))
        self.btn_PRD_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PRD_1.setEnabled(True)
        self.btn_PRD_1.setGeometry(QtCore.QRect(10, 95, 375, 71))
        self.btn_PRD_1.setWhatsThis(_fromUtf8(""))
        self.btn_PRD_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PRD_1.setText(_fromUtf8(""))
        self.btn_PRD_1.setObjectName(_fromUtf8("btn_PRD_1"))
        self.lbl_JCE = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_JCE.setGeometry(QtCore.QRect(530, 0, 224, 46))
        self.lbl_JCE.setStyleSheet(_fromUtf8("image: url(:/JCE/JCE.png);"))
        self.lbl_JCE.setText(_fromUtf8(""))
        self.lbl_JCE.setObjectName(_fromUtf8("lbl_JCE"))
        self.lbl_escudo_1 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_escudo_1.setGeometry(QtCore.QRect(9, 5, 41, 41))
        self.lbl_escudo_1.setStyleSheet(_fromUtf8("image: url(:/JCE/EscudoDom.png);"))
        self.lbl_escudo_1.setText(_fromUtf8(""))
        self.lbl_escudo_1.setObjectName(_fromUtf8("lbl_escudo_1"))
        self.lbl_escudo_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_escudo_2.setGeometry(QtCore.QRect(1210, 5, 41, 41))
        self.lbl_escudo_2.setStyleSheet(_fromUtf8("image: url(:/JCE/EscudoDom.png);"))
        self.lbl_escudo_2.setText(_fromUtf8(""))
        self.lbl_escudo_2.setObjectName(_fromUtf8("lbl_escudo_2"))
        self.btn_PLD_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PLD_1.setEnabled(True)
        self.btn_PLD_1.setGeometry(QtCore.QRect(445, 95, 375, 71))
        self.btn_PLD_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PLD_1.setText(_fromUtf8(""))
        self.btn_PLD_1.setObjectName(_fromUtf8("btn_PLD_1"))
        self.btn_PRSC_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PRSC_1.setEnabled(True)
        self.btn_PRSC_1.setGeometry(QtCore.QRect(880, 95, 375, 71))
        self.btn_PRSC_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PRSC_1.setText(_fromUtf8(""))
        self.btn_PRSC_1.setObjectName(_fromUtf8("btn_PRSC_1"))
        self.btn_MODA_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_MODA_1.setEnabled(True)
        self.btn_MODA_1.setGeometry(QtCore.QRect(10, 180, 375, 71))
        self.btn_MODA_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_MODA_1.setText(_fromUtf8(""))
        self.btn_MODA_1.setObjectName(_fromUtf8("btn_MODA_1"))
        self.btn_PQDC_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PQDC_1.setEnabled(True)
        self.btn_PQDC_1.setGeometry(QtCore.QRect(10, 265, 375, 71))
        self.btn_PQDC_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PQDC_1.setText(_fromUtf8(""))
        self.btn_PQDC_1.setObjectName(_fromUtf8("btn_PQDC_1"))
        self.btn_FNP_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_FNP_1.setEnabled(True)
        self.btn_FNP_1.setGeometry(QtCore.QRect(10, 350, 375, 71))
        self.btn_FNP_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_FNP_1.setText(_fromUtf8(""))
        self.btn_FNP_1.setObjectName(_fromUtf8("btn_FNP_1"))
        self.btn_BIS_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_BIS_1.setEnabled(True)
        self.btn_BIS_1.setGeometry(QtCore.QRect(445, 180, 375, 71))
        self.btn_BIS_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_BIS_1.setText(_fromUtf8(""))
        self.btn_BIS_1.setObjectName(_fromUtf8("btn_BIS_1"))
        self.btn_UDC_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_UDC_1.setEnabled(True)
        self.btn_UDC_1.setGeometry(QtCore.QRect(445, 265, 375, 71))
        self.btn_UDC_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_UDC_1.setText(_fromUtf8(""))
        self.btn_UDC_1.setObjectName(_fromUtf8("btn_UDC_1"))
        self.btn_PTD_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PTD_1.setEnabled(True)
        self.btn_PTD_1.setGeometry(QtCore.QRect(445, 350, 375, 71))
        self.btn_PTD_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PTD_1.setText(_fromUtf8(""))
        self.btn_PTD_1.setObjectName(_fromUtf8("btn_PTD_1"))
        self.btn_PRSD_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PRSD_1.setEnabled(True)
        self.btn_PRSD_1.setGeometry(QtCore.QRect(880, 180, 375, 71))
        self.btn_PRSD_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PRSD_1.setText(_fromUtf8(""))
        self.btn_PRSD_1.setObjectName(_fromUtf8("btn_PRSD_1"))
        self.btn_PHD_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PHD_1.setEnabled(True)
        self.btn_PHD_1.setGeometry(QtCore.QRect(880, 265, 375, 71))
        self.btn_PHD_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PHD_1.setText(_fromUtf8(""))
        self.btn_PHD_1.setObjectName(_fromUtf8("btn_PHD_1"))
        self.btn_PAL_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PAL_1.setEnabled(True)
        self.btn_PAL_1.setGeometry(QtCore.QRect(880, 350, 375, 71))
        self.btn_PAL_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PAL_1.setText(_fromUtf8(""))
        self.btn_PAL_1.setObjectName(_fromUtf8("btn_PAL_1"))
        self.btn_votar = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_votar.setEnabled(True)
        self.btn_votar.setGeometry(QtCore.QRect(1086, 625, 170, 60))
        self.btn_votar.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 255);"))
        self.btn_votar.setText(_fromUtf8(""))
        self.btn_votar.setObjectName(_fromUtf8("btn_votar"))

        self.btn_votar.setVisible(False)



        self.cancel = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.cancel.setEnabled(True)
        self.cancel.setGeometry(QtCore.QRect(10, 625, 170, 60))
        self.cancel.setStyleSheet(_fromUtf8("background-color: rgb(177, 0, 0);"))
        self.cancel.setText(_fromUtf8(""))
        self.cancel.setObjectName(_fromUtf8("cancel"))

        
       
        self.btn_PRD_2 = QtGui.QToolButton(self.scrollAreaWidgetContents)
        self.btn_PRD_2.setGeometry(QtCore.QRect(350, 100, 25, 25))
        self.btn_PRD_2.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);"))
        self.btn_PRD_2.setObjectName(_fromUtf8("btn_PRD_2"))
        self.btn_PRM_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PRM_1.setEnabled(True)
        self.btn_PRM_1.setGeometry(QtCore.QRect(10, 435, 375, 71))
        self.btn_PRM_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PRM_1.setText(_fromUtf8(""))
        self.btn_PRM_1.setObjectName(_fromUtf8("btn_PRM_1"))
        self.btn_APD_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_APD_1.setEnabled(True)
        self.btn_APD_1.setGeometry(QtCore.QRect(10, 520, 375, 71))
        self.btn_APD_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_APD_1.setText(_fromUtf8(""))
        self.btn_APD_1.setObjectName(_fromUtf8("btn_APD_1"))
        self.btn_PUN_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PUN_1.setEnabled(True)
        self.btn_PUN_1.setGeometry(QtCore.QRect(445, 435, 375, 71))
        self.btn_PUN_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PUN_1.setText(_fromUtf8(""))
        self.btn_PUN_1.setObjectName(_fromUtf8("btn_PUN_1"))
        self.btn_PR1_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PR1_1.setEnabled(True)
        self.btn_PR1_1.setGeometry(QtCore.QRect(445, 520, 375, 71))
        self.btn_PR1_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_PR1_1.setText(_fromUtf8(""))
        self.btn_PR1_1.setObjectName(_fromUtf8("btn_PR1_1"))
        self.btn_FRENTE_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_FRENTE_1.setEnabled(True)
        self.btn_FRENTE_1.setGeometry(QtCore.QRect(880, 435, 375, 71))
        self.btn_FRENTE_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_FRENTE_1.setText(_fromUtf8(""))
        self.btn_FRENTE_1.setObjectName(_fromUtf8("btn_FRENTE_1"))
        self.btn_ALIANZA_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_ALIANZA_1.setEnabled(True)
        self.btn_ALIANZA_1.setGeometry(QtCore.QRect(880, 520, 375, 71))
        self.btn_ALIANZA_1.setStyleSheet(_fromUtf8("background-color: rgb(173, 173, 130);"))
        self.btn_ALIANZA_1.setText(_fromUtf8(""))
        self.btn_ALIANZA_1.setObjectName(_fromUtf8("btn_ALIANZA_1"))
        self.lbl_PRD_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRD_PR.setGeometry(QtCore.QRect(170, 100, 141, 16))
        self.lbl_PRD_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PRD_PR.setObjectName(_fromUtf8("lbl_PRD_PR"))
        self.lbl_PRD_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRD_vc.setGeometry(QtCore.QRect(170, 120, 161, 16))
        self.lbl_PRD_vc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PRD_vc.setObjectName(_fromUtf8("lbl_PRD_vc"))
        self.lbl_PRD_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRD_part.setGeometry(QtCore.QRect(170, 140, 71, 16))
        self.lbl_PRD_part.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PRD_part.setObjectName(_fromUtf8("lbl_PRD_part"))
        self.lbl_APD_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_APD_cand.setGeometry(QtCore.QRect(10, 520, 81, 68))
        self.lbl_APD_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/MinouTavarez_foto.jpg);"))
        self.lbl_APD_cand.setText(_fromUtf8(""))
        self.lbl_APD_cand.setObjectName(_fromUtf8("lbl_APD_cand"))
        self.lbl_ALIANZA_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_ALIANZA_logo.setGeometry(QtCore.QRect(961, 520, 61, 68))
        self.lbl_ALIANZA_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/AlianzaPais_logo.jpg);"))
        self.lbl_ALIANZA_logo.setText(_fromUtf8(""))
        self.lbl_ALIANZA_logo.setObjectName(_fromUtf8("lbl_ALIANZA_logo"))
        self.lbl_PRD_can = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRD_can.setGeometry(QtCore.QRect(10, 95, 81, 68))
        self.lbl_PRD_can.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/Danilo_foto.jpg);"))
        self.lbl_PRD_can.setText(_fromUtf8(""))
        self.lbl_PRD_can.setObjectName(_fromUtf8("lbl_PRD_can"))
        self.lbl_PRD_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRD_logo.setGeometry(QtCore.QRect(90, 95, 61, 68))
        self.lbl_PRD_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PRD_logo.png);"))
        self.lbl_PRD_logo.setText(_fromUtf8(""))
        self.lbl_PRD_logo.setObjectName(_fromUtf8("lbl_PRD_logo"))
        self.lbl_PLD_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PLD_cand.setGeometry(QtCore.QRect(445, 95, 81, 68))
        self.lbl_PLD_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/Danilo_foto.jpg);"))
        self.lbl_PLD_cand.setText(_fromUtf8(""))
        self.lbl_PLD_cand.setObjectName(_fromUtf8("lbl_PLD_cand"))
        self.lbl_MODA_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_MODA_cand.setGeometry(QtCore.QRect(10, 180, 81, 68))
        self.lbl_MODA_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/Danilo_foto.jpg);"))
        self.lbl_MODA_cand.setText(_fromUtf8(""))
        self.lbl_MODA_cand.setObjectName(_fromUtf8("lbl_MODA_cand"))
        self.lbl_BIS_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_BIS_cand.setGeometry(QtCore.QRect(445, 180, 81, 68))
        self.lbl_BIS_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/Danilo_foto.jpg);"))
        self.lbl_BIS_cand.setText(_fromUtf8(""))
        self.lbl_BIS_cand.setObjectName(_fromUtf8("lbl_BIS_cand"))
        self.lbl_UDC_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_UDC_cand.setGeometry(QtCore.QRect(445, 265, 81, 68))
        self.lbl_UDC_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/Danilo_foto.jpg);"))
        self.lbl_UDC_cand.setText(_fromUtf8(""))
        self.lbl_UDC_cand.setObjectName(_fromUtf8("lbl_UDC_cand"))
        self.lbl_PTD_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PTD_cand.setGeometry(QtCore.QRect(445, 350, 81, 68))
        self.lbl_PTD_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/Danilo_foto.jpg);"))
        self.lbl_PTD_cand.setText(_fromUtf8(""))
        self.lbl_PTD_cand.setObjectName(_fromUtf8("lbl_PTD_cand"))
        self.lbl_PAL_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PAL_cand.setGeometry(QtCore.QRect(880, 350, 81, 68))
        self.lbl_PAL_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/Danilo_foto.jpg);"))
        self.lbl_PAL_cand.setText(_fromUtf8(""))
        self.lbl_PAL_cand.setObjectName(_fromUtf8("lbl_PAL_cand"))
        self.lbl_PRI_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRI_cand.setGeometry(QtCore.QRect(445, 520, 81, 68))
        self.lbl_PRI_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/Danilo_foto.jpg);"))
        self.lbl_PRI_cand.setText(_fromUtf8(""))
        self.lbl_PRI_cand.setObjectName(_fromUtf8("lbl_PRI_cand"))
        self.lbl_PRSC_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRSC_cand.setGeometry(QtCore.QRect(880, 95, 81, 68))
        self.lbl_PRSC_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/LuisAbinader_foto.jpg);"))
        self.lbl_PRSC_cand.setText(_fromUtf8(""))
        self.lbl_PRSC_cand.setObjectName(_fromUtf8("lbl_PRSC_cand"))
        self.lbl_PRSD_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRSD_cand.setGeometry(QtCore.QRect(880, 180, 81, 68))
        self.lbl_PRSD_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/HatueydeCamps_foto.jpg);"))
        self.lbl_PRSD_cand.setText(_fromUtf8(""))
        self.lbl_PRSD_cand.setObjectName(_fromUtf8("lbl_PRSD_cand"))
        self.lbl_FRENTE_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_FRENTE_cand.setGeometry(QtCore.QRect(880, 435, 81, 68))
        self.lbl_FRENTE_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/LuisAbinader_foto.jpg);"))
        self.lbl_FRENTE_cand.setText(_fromUtf8(""))
        self.lbl_FRENTE_cand.setObjectName(_fromUtf8("lbl_FRENTE_cand"))
        self.lbl_PRM_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRM_cand.setGeometry(QtCore.QRect(10, 435, 81, 68))
        self.lbl_PRM_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/LuisAbinader_foto.jpg);"))
        self.lbl_PRM_cand.setText(_fromUtf8(""))
        self.lbl_PRM_cand.setObjectName(_fromUtf8("lbl_PRM_cand"))
        self.lbl_PQDC_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PQDC_cand.setGeometry(QtCore.QRect(10, 265, 81, 68))
        self.lbl_PQDC_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/EliasWessin_foto.jpg);"))
        self.lbl_PQDC_cand.setText(_fromUtf8(""))
        self.lbl_PQDC_cand.setObjectName(_fromUtf8("lbl_PQDC_cand"))
        self.lbl_FNP_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_FNP_cand.setGeometry(QtCore.QRect(10, 350, 81, 68))
        self.lbl_FNP_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PelegrinCastillo_foto.jpg);"))
        self.lbl_FNP_cand.setText(_fromUtf8(""))
        self.lbl_FNP_cand.setObjectName(_fromUtf8("lbl_FNP_cand"))
        self.lbl_PUN_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PUN_cand.setGeometry(QtCore.QRect(445, 435, 81, 68))
        self.lbl_PUN_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/SorayaAquino_foto.jpg);"))
        self.lbl_PUN_cand.setText(_fromUtf8(""))
        self.lbl_PUN_cand.setObjectName(_fromUtf8("lbl_PUN_cand"))
        self.lbl_PHD_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PHD_cand.setGeometry(QtCore.QRect(880, 265, 81, 68))
        self.lbl_PHD_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/LuisAbinader_foto.jpg);"))
        self.lbl_PHD_cand.setText(_fromUtf8(""))
        self.lbl_PHD_cand.setObjectName(_fromUtf8("lbl_PHD_cand"))
        self.lbl_ALIANZA_cand = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_ALIANZA_cand.setGeometry(QtCore.QRect(880, 520, 81, 68))
        self.lbl_ALIANZA_cand.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/guillermoMoreno_foto.jpg);"))
        self.lbl_ALIANZA_cand.setText(_fromUtf8(""))
        self.lbl_ALIANZA_cand.setObjectName(_fromUtf8("lbl_ALIANZA_cand"))
        self.lbl_PRI_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRI_logo.setGeometry(QtCore.QRect(526, 520, 61, 68))
        self.lbl_PRI_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PRI_logo.jpg);"))
        self.lbl_PRI_logo.setText(_fromUtf8(""))
        self.lbl_PRI_logo.setObjectName(_fromUtf8("lbl_PRI_logo"))
        self.lbl_PRSC_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRSC_logo.setGeometry(QtCore.QRect(961, 95, 61, 68))
        self.lbl_PRSC_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PRSC_logo.jpg);"))
        self.lbl_PRSC_logo.setText(_fromUtf8(""))
        self.lbl_PRSC_logo.setObjectName(_fromUtf8("lbl_PRSC_logo"))
        self.lbl_PLD_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PLD_logo.setGeometry(QtCore.QRect(526, 95, 61, 68))
        self.lbl_PLD_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PLD_logo.png);"))
        self.lbl_PLD_logo.setText(_fromUtf8(""))
        self.lbl_PLD_logo.setObjectName(_fromUtf8("lbl_PLD_logo"))
        self.lbl_PRSD_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRSD_logo.setGeometry(QtCore.QRect(961, 180, 61, 68))
        self.lbl_PRSD_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PRSD_logo.jpg);"))
        self.lbl_PRSD_logo.setText(_fromUtf8(""))
        self.lbl_PRSD_logo.setObjectName(_fromUtf8("lbl_PRSD_logo"))
        self.lbl_BIS_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_BIS_logo.setGeometry(QtCore.QRect(526, 180, 61, 68))
        self.lbl_BIS_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/BIS_logo.jpg);"))
        self.lbl_BIS_logo.setText(_fromUtf8(""))
        self.lbl_BIS_logo.setObjectName(_fromUtf8("lbl_BIS_logo"))
        self.lbl_MODA_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_MODA_logo.setGeometry(QtCore.QRect(90, 180, 61, 68))
        self.lbl_MODA_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/MODA_logo.jpg);"))
        self.lbl_MODA_logo.setText(_fromUtf8(""))
        self.lbl_MODA_logo.setObjectName(_fromUtf8("lbl_MODA_logo"))
        self.lbl_PTD_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PTD_logo.setGeometry(QtCore.QRect(526, 350, 61, 68))
        self.lbl_PTD_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PTD_logo.jpg);"))
        self.lbl_PTD_logo.setText(_fromUtf8(""))
        self.lbl_PTD_logo.setObjectName(_fromUtf8("lbl_PTD_logo"))
        self.lbl_FNP_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_FNP_logo.setGeometry(QtCore.QRect(90, 350, 61, 68))
        self.lbl_FNP_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/FNP_logo.png);"))
        self.lbl_FNP_logo.setText(_fromUtf8(""))
        self.lbl_FNP_logo.setObjectName(_fromUtf8("lbl_FNP_logo"))
        self.lbl_PHD_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PHD_logo.setGeometry(QtCore.QRect(961, 265, 61, 68))
        self.lbl_PHD_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PHD_logo.jpg);"))
        self.lbl_PHD_logo.setText(_fromUtf8(""))
        self.lbl_PHD_logo.setObjectName(_fromUtf8("lbl_PHD_logo"))
        self.lbl_UDC_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_UDC_logo.setGeometry(QtCore.QRect(526, 265, 61, 68))
        self.lbl_UDC_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/UDC_logo.jpg);"))
        self.lbl_UDC_logo.setText(_fromUtf8(""))
        self.lbl_UDC_logo.setObjectName(_fromUtf8("lbl_UDC_logo"))
        self.lbl_PQDC_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PQDC_logo.setGeometry(QtCore.QRect(90, 265, 61, 68))
        self.lbl_PQDC_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PQDC_logo.jpg);"))
        self.lbl_PQDC_logo.setText(_fromUtf8(""))
        self.lbl_PQDC_logo.setObjectName(_fromUtf8("lbl_PQDC_logo"))
        self.lbl_APD_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_APD_logo.setGeometry(QtCore.QRect(90, 520, 61, 68))
        self.lbl_APD_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/APD_logo.jpg);"))
        self.lbl_APD_logo.setText(_fromUtf8(""))
        self.lbl_APD_logo.setObjectName(_fromUtf8("lbl_APD_logo"))
        self.lbl_PUN_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PUN_logo.setGeometry(QtCore.QRect(526, 435, 61, 68))
        self.lbl_PUN_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PUN_logo.jpg);"))
        self.lbl_PUN_logo.setText(_fromUtf8(""))
        self.lbl_PUN_logo.setObjectName(_fromUtf8("lbl_PUN_logo"))
        self.lbl_PRM_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRM_logo.setGeometry(QtCore.QRect(90, 435, 61, 68))
        self.lbl_PRM_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PRM_logo.jpg);"))
        self.lbl_PRM_logo.setText(_fromUtf8(""))
        self.lbl_PRM_logo.setObjectName(_fromUtf8("lbl_PRM_logo"))
        self.lbl_PAL_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PAL_logo.setGeometry(QtCore.QRect(961, 350, 61, 68))
        self.lbl_PAL_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/PAL_logo.png);"))
        self.lbl_PAL_logo.setText(_fromUtf8(""))
        self.lbl_PAL_logo.setObjectName(_fromUtf8("lbl_PAL_logo"))
        self.lbl_FRENTE_logo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_FRENTE_logo.setGeometry(QtCore.QRect(961, 435, 61, 68))
        self.lbl_FRENTE_logo.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"image: url(:/JCE/FreteAmplio_logo.jpg);"))
        self.lbl_FRENTE_logo.setText(_fromUtf8(""))
        self.lbl_FRENTE_logo.setObjectName(_fromUtf8("lbl_FRENTE_logo"))
        self.lbl_MODA_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_MODA_PR.setGeometry(QtCore.QRect(170, 185, 151, 16))
        self.lbl_MODA_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_MODA_PR.setObjectName(_fromUtf8("lbl_MODA_PR"))
        self.lbl_MODA_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_MODA_vc.setGeometry(QtCore.QRect(170, 205, 171, 16))
        self.lbl_MODA_vc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_MODA_vc.setObjectName(_fromUtf8("lbl_MODA_vc"))
        self.lbl_MODA_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_MODA_part.setGeometry(QtCore.QRect(170, 225, 71, 16))
        self.lbl_MODA_part.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_MODA_part.setObjectName(_fromUtf8("lbl_MODA_part"))
        self.lbl_PLD_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PLD_PR.setGeometry(QtCore.QRect(605, 100, 131, 16))
        self.lbl_PLD_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PLD_PR.setObjectName(_fromUtf8("lbl_PLD_PR"))
        self.lbl_BIS_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_BIS_PR.setGeometry(QtCore.QRect(605, 185, 141, 16))
        self.lbl_BIS_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_BIS_PR.setObjectName(_fromUtf8("lbl_BIS_PR"))
        self.lbl_UDC_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_UDC_PR.setGeometry(QtCore.QRect(605, 270, 151, 16))
        self.lbl_UDC_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_UDC_PR.setObjectName(_fromUtf8("lbl_UDC_PR"))
        self.lbl_PTD_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PTD_PR.setGeometry(QtCore.QRect(605, 355, 161, 16))
        self.lbl_PTD_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PTD_PR.setObjectName(_fromUtf8("lbl_PTD_PR"))
        self.lbl_PAL_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PAL_PR.setGeometry(QtCore.QRect(1040, 355, 141, 16))
        self.lbl_PAL_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PAL_PR.setObjectName(_fromUtf8("lbl_PAL_PR"))
        self.lbl_PRI_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRI_PR.setGeometry(QtCore.QRect(605, 525, 151, 16))
        self.lbl_PRI_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PRI_PR.setObjectName(_fromUtf8("lbl_PRI_PR"))
        self.lbl_PLD_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PLD_vc.setGeometry(QtCore.QRect(605, 120, 161, 16))
        self.lbl_PLD_vc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PLD_vc.setObjectName(_fromUtf8("lbl_PLD_vc"))
        self.lbl_BIS_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_BIS_vc.setGeometry(QtCore.QRect(605, 205, 161, 16))
        self.lbl_BIS_vc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_BIS_vc.setObjectName(_fromUtf8("lbl_BIS_vc"))
        self.lbl_UDC_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_UDC_vc.setGeometry(QtCore.QRect(605, 290, 161, 16))
        self.lbl_UDC_vc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_UDC_vc.setObjectName(_fromUtf8("lbl_UDC_vc"))
        self.lbl_PTD_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PTD_vc.setGeometry(QtCore.QRect(605, 375, 161, 16))
        self.lbl_PTD_vc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PTD_vc.setObjectName(_fromUtf8("lbl_PTD_vc"))
        self.lbl_PAL_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PAL_vc.setGeometry(QtCore.QRect(1040, 375, 171, 16))
        self.lbl_PAL_vc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PAL_vc.setObjectName(_fromUtf8("lbl_PAL_vc"))
        self.lbl_PRI_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRI_vc.setGeometry(QtCore.QRect(605, 545, 161, 16))
        self.lbl_PRI_vc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PRI_vc.setObjectName(_fromUtf8("lbl_PRI_vc"))
        self.lbl_PLD_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PLD_part.setGeometry(QtCore.QRect(605, 140, 51, 16))
        self.lbl_PLD_part.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PLD_part.setObjectName(_fromUtf8("lbl_PLD_part"))
        self.lbl_BIS_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_BIS_part.setGeometry(QtCore.QRect(605, 225, 46, 16))
        self.lbl_BIS_part.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_BIS_part.setObjectName(_fromUtf8("lbl_BIS_part"))
        self.lbl_UDC_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_UDC_part.setGeometry(QtCore.QRect(605, 310, 61, 16))
        self.lbl_UDC_part.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_UDC_part.setObjectName(_fromUtf8("lbl_UDC_part"))
        self.lbl_PTD_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PTD_part.setGeometry(QtCore.QRect(605, 395, 121, 16))
        self.lbl_PTD_part.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PTD_part.setObjectName(_fromUtf8("lbl_PTD_part"))
        self.lbl_PAL_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PAL_part.setGeometry(QtCore.QRect(1040, 395, 61, 16))
        self.lbl_PAL_part.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PAL_part.setObjectName(_fromUtf8("lbl_PAL_part"))
        self.lbl_PRI_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRI_part.setGeometry(QtCore.QRect(605, 565, 71, 16))
        self.lbl_PRI_part.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PRI_part.setObjectName(_fromUtf8("lbl_PRI_part"))
        self.lbl_PRSC_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRSC_PR.setGeometry(QtCore.QRect(1040, 100, 141, 16))
        self.lbl_PRSC_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PRSC_PR.setObjectName(_fromUtf8("lbl_PRSC_PR"))
        self.lbl_PRSC_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRSC_vc.setGeometry(QtCore.QRect(1040, 120, 151, 16))
        self.lbl_PRSC_vc.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PRSC_vc.setObjectName(_fromUtf8("lbl_PRSC_vc"))
        self.lbl_PRSC_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRSC_part.setGeometry(QtCore.QRect(1040, 140, 91, 16))
        self.lbl_PRSC_part.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PRSC_part.setObjectName(_fromUtf8("lbl_PRSC_part"))
        self.lbl_PHD_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PHD_PR.setGeometry(QtCore.QRect(1040, 270, 151, 16))
        self.lbl_PHD_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PHD_PR.setObjectName(_fromUtf8("lbl_PHD_PR"))
        self.lbl_PHD_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PHD_vc.setGeometry(QtCore.QRect(1040, 290, 161, 16))
        self.lbl_PHD_vc.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PHD_vc.setObjectName(_fromUtf8("lbl_PHD_vc"))
        self.lbl_PHD_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PHD_part.setGeometry(QtCore.QRect(1040, 310, 91, 16))
        self.lbl_PHD_part.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PHD_part.setObjectName(_fromUtf8("lbl_PHD_part"))
        self.lbl_PRM_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRM_PR.setGeometry(QtCore.QRect(170, 440, 151, 16))
        self.lbl_PRM_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PRM_PR.setObjectName(_fromUtf8("lbl_PRM_PR"))
        self.lbl_PRM_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRM_vc.setGeometry(QtCore.QRect(170, 460, 161, 16))
        self.lbl_PRM_vc.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PRM_vc.setObjectName(_fromUtf8("lbl_PRM_vc"))
        self.lbl_FRENTE_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_FRENTE_vc.setGeometry(QtCore.QRect(1040, 460, 151, 16))
        self.lbl_FRENTE_vc.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_FRENTE_vc.setObjectName(_fromUtf8("lbl_FRENTE_vc"))
        self.lbl_FRENTE_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_FRENTE_PR.setGeometry(QtCore.QRect(1040, 440, 141, 16))
        self.lbl_FRENTE_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_FRENTE_PR.setObjectName(_fromUtf8("lbl_FRENTE_PR"))
        self.lbl_PRM_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRM_part.setGeometry(QtCore.QRect(170, 480, 121, 16))
        self.lbl_PRM_part.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_PRM_part.setObjectName(_fromUtf8("lbl_PRM_part"))
        self.lbl_FRENTE_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_FRENTE_part.setGeometry(QtCore.QRect(1040, 480, 161, 16))
        self.lbl_FRENTE_part.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 127);"))
        self.lbl_FRENTE_part.setObjectName(_fromUtf8("lbl_FRENTE_part"))
        self.lbl_PRSD_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRSD_PR.setGeometry(QtCore.QRect(1040, 185, 171, 16))
        self.lbl_PRSD_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PRSD_PR.setObjectName(_fromUtf8("lbl_PRSD_PR"))
        self.lbl_PRSD_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRSD_vc.setGeometry(QtCore.QRect(1040, 205, 161, 16))
        self.lbl_PRSD_vc.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PRSD_vc.setObjectName(_fromUtf8("lbl_PRSD_vc"))
        self.lbl_PRSD_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PRSD_part.setGeometry(QtCore.QRect(1040, 225, 91, 16))
        self.lbl_PRSD_part.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PRSD_part.setObjectName(_fromUtf8("lbl_PRSD_part"))
        self.lbl_PQDC_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PQDC_PR.setGeometry(QtCore.QRect(170, 270, 151, 16))
        self.lbl_PQDC_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PQDC_PR.setObjectName(_fromUtf8("lbl_PQDC_PR"))
        self.lbl_PQDC_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PQDC_vc.setGeometry(QtCore.QRect(170, 290, 171, 16))
        self.lbl_PQDC_vc.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PQDC_vc.setObjectName(_fromUtf8("lbl_PQDC_vc"))
        self.lbl_PQDC_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PQDC_part.setGeometry(QtCore.QRect(170, 310, 91, 16))
        self.lbl_PQDC_part.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PQDC_part.setObjectName(_fromUtf8("lbl_PQDC_part"))
        self.lbl_ALIANZA_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_ALIANZA_PR.setGeometry(QtCore.QRect(1040, 525, 171, 16))
        self.lbl_ALIANZA_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_ALIANZA_PR.setObjectName(_fromUtf8("lbl_ALIANZA_PR"))
        self.lbl_ALIANZA_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_ALIANZA_vc.setGeometry(QtCore.QRect(1040, 545, 161, 16))
        self.lbl_ALIANZA_vc.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_ALIANZA_vc.setObjectName(_fromUtf8("lbl_ALIANZA_vc"))
        self.lbl_ALIANZA_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_ALIANZA_part.setGeometry(QtCore.QRect(1040, 565, 91, 16))
        self.lbl_ALIANZA_part.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_ALIANZA_part.setObjectName(_fromUtf8("lbl_ALIANZA_part"))
        self.lbl_APD_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_APD_PR.setGeometry(QtCore.QRect(170, 525, 171, 16))
        self.lbl_APD_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_APD_PR.setObjectName(_fromUtf8("lbl_APD_PR"))
        self.lbl_APD_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_APD_vc.setGeometry(QtCore.QRect(170, 545, 141, 16))
        self.lbl_APD_vc.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_APD_vc.setObjectName(_fromUtf8("lbl_APD_vc"))
        self.lbl_APD_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_APD_part.setGeometry(QtCore.QRect(170, 565, 91, 16))
        self.lbl_APD_part.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_APD_part.setObjectName(_fromUtf8("lbl_APD_part"))
        self.lbl_FNP_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_FNP_PR.setGeometry(QtCore.QRect(170, 355, 171, 16))
        self.lbl_FNP_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_FNP_PR.setObjectName(_fromUtf8("lbl_FNP_PR"))
        self.lbl_PUN_PR = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PUN_PR.setGeometry(QtCore.QRect(605, 440, 151, 16))
        self.lbl_PUN_PR.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PUN_PR.setObjectName(_fromUtf8("lbl_PUN_PR"))
        self.lbl_PUN_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PUN_vc.setGeometry(QtCore.QRect(605, 460, 161, 16))
        self.lbl_PUN_vc.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PUN_vc.setObjectName(_fromUtf8("lbl_PUN_vc"))
        self.lbl_PUN_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_PUN_part.setGeometry(QtCore.QRect(605, 480, 111, 16))
        self.lbl_PUN_part.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_PUN_part.setObjectName(_fromUtf8("lbl_PUN_part"))
        self.lbl_FNP_vc = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_FNP_vc.setGeometry(QtCore.QRect(170, 375, 161, 16))
        self.lbl_FNP_vc.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_FNP_vc.setObjectName(_fromUtf8("lbl_FNP_vc"))
        self.lbl_FNP_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_FNP_part.setGeometry(QtCore.QRect(170, 395, 121, 16))
        self.lbl_FNP_part.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lbl_FNP_part.setObjectName(_fromUtf8("lbl_FNP_part"))
        self.lbl_votar = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_votar.setGeometry(QtCore.QRect(1146, 640, 81, 31))
        self.lbl_votar.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 255);"))
        self.lbl_votar.setObjectName(_fromUtf8("lbl_votar"))


        self.lbl_votar.setVisible(False)


        self.lbl_cancel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_cancel.setGeometry(QtCore.QRect(55, 640, 81, 31))
        self.lbl_cancel.setStyleSheet(_fromUtf8("background-color: rgb(177, 0, 0);"))
        self.lbl_cancel.setObjectName(_fromUtf8("lbl_cancel"))

        

        self.btn_PRM_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PRM_2.setGeometry(QtCore.QRect(350, 440, 25, 25))
        self.btn_PRM_2.setObjectName(_fromUtf8("btn_PRM_2"))
        self.btn_PUN_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PUN_2.setGeometry(QtCore.QRect(785, 440, 25, 25))
        self.btn_PUN_2.setObjectName(_fromUtf8("btn_PUN_2"))
        self.btn_FRENTE_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_FRENTE_2.setGeometry(QtCore.QRect(1220, 440, 25, 25))
        self.btn_FRENTE_2.setObjectName(_fromUtf8("btn_FRENTE_2"))
        self.btn_APD_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_APD_2.setGeometry(QtCore.QRect(350, 525, 25, 25))
        self.btn_APD_2.setObjectName(_fromUtf8("btn_APD_2"))
        self.btn_PR1_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PR1_2.setGeometry(QtCore.QRect(785, 525, 25, 25))
        self.btn_PR1_2.setObjectName(_fromUtf8("btn_PR1_2"))
        self.btn_ALIANZA_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_ALIANZA_2.setGeometry(QtCore.QRect(1220, 525, 25, 25))
        self.btn_ALIANZA_2.setObjectName(_fromUtf8("btn_ALIANZA_2"))
        self.btn_PLD_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PLD_2.setGeometry(QtCore.QRect(785, 100, 25, 25))
        self.btn_PLD_2.setObjectName(_fromUtf8("btn_PLD_2"))
        self.btn_PRSC_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PRSC_2.setGeometry(QtCore.QRect(1220, 100, 25, 25))
        self.btn_PRSC_2.setObjectName(_fromUtf8("btn_PRSC_2"))
        self.btn_MODA_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_MODA_2.setGeometry(QtCore.QRect(350, 185, 25, 25))
        self.btn_MODA_2.setObjectName(_fromUtf8("btn_MODA_2"))
        self.btn_BIS_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_BIS_2.setGeometry(QtCore.QRect(785, 185, 25, 25))
        self.btn_BIS_2.setObjectName(_fromUtf8("btn_BIS_2"))
        self.btn_PRSD_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PRSD_2.setGeometry(QtCore.QRect(1220, 185, 25, 25))
        self.btn_PRSD_2.setObjectName(_fromUtf8("btn_PRSD_2"))
        self.btn_PQDC_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PQDC_2.setGeometry(QtCore.QRect(350, 270, 25, 25))
        self.btn_PQDC_2.setObjectName(_fromUtf8("btn_PQDC_2"))
        self.btn_UDC_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_UDC_2.setGeometry(QtCore.QRect(785, 270, 25, 25))
        self.btn_UDC_2.setObjectName(_fromUtf8("btn_UDC_2"))
        self.btn_FNP_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_FNP_2.setGeometry(QtCore.QRect(350, 355, 25, 25))
        self.btn_FNP_2.setObjectName(_fromUtf8("btn_FNP_2"))
        self.btn_PTD_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PTD_2.setGeometry(QtCore.QRect(785, 355, 25, 25))
        self.btn_PTD_2.setObjectName(_fromUtf8("btn_PTD_2"))
        self.btn_PHD_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PHD_2.setGeometry(QtCore.QRect(1220, 270, 25, 25))
        self.btn_PHD_2.setObjectName(_fromUtf8("btn_PHD_2"))
        self.btn_PAL_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btn_PAL_2.setGeometry(QtCore.QRect(1220, 355, 25, 25))
        self.btn_PAL_2.setObjectName(_fromUtf8("btn_PAL_2"))
        self.lbl_presi = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_presi.setGeometry(QtCore.QRect(70, 10, 46, 13))
        self.lbl_presi.setText(_fromUtf8(""))
        self.lbl_presi.setObjectName(_fromUtf8("lbl_presi"))
        self.lbl_vice = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_vice.setGeometry(QtCore.QRect(130, 10, 46, 13))
        self.lbl_vice.setText(_fromUtf8(""))
        self.lbl_vice.setObjectName(_fromUtf8("lbl_vice"))
        self.lbl_part = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl_part.setGeometry(QtCore.QRect(250, 10, 46, 13))
        self.lbl_part.setText(_fromUtf8(""))
        self.lbl_part.setObjectName(_fromUtf8("lbl_part"))
        self.txt_presi = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.txt_presi.setGeometry(QtCore.QRect(100, 530, 191, 51))
        self.txt_presi.setObjectName(_fromUtf8("txt_presi"))
        self.txt_vice = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.txt_vice.setGeometry(QtCore.QRect(570, 540, 181, 31))
        self.txt_vice.setObjectName(_fromUtf8("txt_vice"))
        self.txt_part = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.txt_part.setGeometry(QtCore.QRect(1020, 540, 181, 31))
        self.txt_part.setObjectName(_fromUtf8("txt_part"))
        self.txtSetPartido = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtSetPartido.setEnabled(False)
        self.txtSetPartido.setGeometry(QtCore.QRect(360, 625, 661, 25))#################################620
        self.txtSetPartido.setObjectName(_fromUtf8("txtSetPartido"))
        
        self.txtSetvice = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtSetvice.setEnabled(False)
        self.txtSetvice.setGeometry(QtCore.QRect(760, 665, 261, 25))#######
        self.txtSetvice.setObjectName(_fromUtf8("txtSetvice"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(255, 625, 61, 25))#########205
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(255, 665, 81, 25))##################33
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(650, 665, 111, 25))######
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        self.txtSetPresi = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtSetPresi.setEnabled(False)
        self.txtSetPresi.setGeometry(QtCore.QRect(360, 665, 261, 25))############
        self.txtSetPresi.setObjectName(_fromUtf8("txtSetPresi"))

        ##########################################################################################
        self.btn_PRD_2.clicked.connect(self.PRD)
        self.btn_PRD_1.clicked.connect(self.PRD)
        self.lbl_PRD_can.mousePressEvent = self.PRD
        self.lbl_PRD_logo.mousePressEvent = self.PRD
        self.lbl_PRD_PR.mousePressEvent = self.PRD
        self.lbl_PRD_vc.mousePressEvent = self.PRD
        self.lbl_PRD_part.mousePressEvent = self.PRD

        self.btn_PLD_2.clicked.connect(self.PLD)
        self.btn_PLD_1.clicked.connect(self.PLD)
        self.lbl_PLD_cand.mousePressEvent = self.PLD
        self.lbl_PLD_logo.mousePressEvent = self.PLD
        self.lbl_PLD_PR.mousePressEvent = self.PLD
        self.lbl_PLD_vc.mousePressEvent = self.PLD
        self.lbl_PLD_part.mousePressEvent = self.PLD

        self.btn_PRSC_2.clicked.connect(self.PRSC)
        self.btn_PRSC_1.clicked.connect(self.PRSC)
        self.lbl_PRSC_cand.mousePressEvent = self.PRSC
        self.lbl_PRSC_logo.mousePressEvent = self.PRSC
        self.lbl_PRSC_PR.mousePressEvent = self.PRSC
        self.lbl_PRSC_vc.mousePressEvent = self.PRSC
        self.lbl_PRSC_part.mousePressEvent = self.PRSC        

        self.btn_MODA_2.clicked.connect(self.MODA)
        self.btn_MODA_1.clicked.connect(self.MODA)
        self.lbl_MODA_cand.mousePressEvent = self.MODA
        self.lbl_MODA_logo.mousePressEvent = self.MODA
        self.lbl_MODA_PR.mousePressEvent = self.MODA
        self.lbl_MODA_vc.mousePressEvent = self.MODA
        self.lbl_MODA_part.mousePressEvent = self.MODA

        self.btn_BIS_2.clicked.connect(self.BIS)
        self.btn_BIS_1.clicked.connect(self.BIS)
        self.lbl_BIS_cand.mousePressEvent = self.BIS
        self.lbl_BIS_logo.mousePressEvent = self.BIS
        self.lbl_BIS_PR.mousePressEvent = self.BIS
        self.lbl_BIS_vc.mousePressEvent = self.BIS
        self.lbl_BIS_part.mousePressEvent = self.BIS

        self.btn_PRSD_2.clicked.connect(self.PRSD)
        self.btn_PRSD_1.clicked.connect(self.PRSD)
        self.lbl_PRSD_cand.mousePressEvent = self.PRSD
        self.lbl_PRSD_logo.mousePressEvent = self.PRSD
        self.lbl_PRSD_PR.mousePressEvent = self.PRSD
        self.lbl_PRSD_vc.mousePressEvent = self.PRSD
        self.lbl_PRSD_part.mousePressEvent = self.PRSD        

        self.btn_PQDC_2.clicked.connect(self.PQDC)
        self.btn_PQDC_1.clicked.connect(self.PQDC)
        self.lbl_PQDC_cand.mousePressEvent = self.PQDC
        self.lbl_PQDC_logo.mousePressEvent = self.PQDC
        self.lbl_PQDC_PR.mousePressEvent = self.PQDC
        self.lbl_PQDC_vc.mousePressEvent = self.PQDC
        self.lbl_PQDC_part.mousePressEvent = self.PQDC

        self.btn_UDC_2.clicked.connect(self.UDC)
        self.btn_UDC_1.clicked.connect(self.UDC)
        self.lbl_UDC_cand.mousePressEvent = self.UDC
        self.lbl_UDC_logo.mousePressEvent = self.UDC
        self.lbl_UDC_PR.mousePressEvent = self.UDC
        self.lbl_UDC_vc.mousePressEvent = self.UDC
        self.lbl_UDC_part.mousePressEvent = self.UDC

        self.btn_PHD_2.clicked.connect(self.PHD)
        self.btn_PHD_1.clicked.connect(self.PHD)
        self.lbl_PHD_cand.mousePressEvent = self.PHD
        self.lbl_PHD_logo.mousePressEvent = self.PHD
        self.lbl_PHD_PR.mousePressEvent = self.PHD
        self.lbl_PHD_vc.mousePressEvent = self.PHD
        self.lbl_PHD_part.mousePressEvent = self.PHD

        self.btn_FNP_2.clicked.connect(self.FNP)
        self.btn_FNP_1.clicked.connect(self.FNP)
        self.lbl_FNP_cand.mousePressEvent = self.FNP
        self.lbl_FNP_logo.mousePressEvent = self.FNP
        self.lbl_FNP_PR.mousePressEvent = self.FNP
        self.lbl_FNP_vc.mousePressEvent = self.FNP
        self.lbl_FNP_part.mousePressEvent = self.FNP

        self.btn_PTD_2.clicked.connect(self.PTD)
        self.btn_PTD_1.clicked.connect(self.PTD)
        self.lbl_PTD_cand.mousePressEvent = self.PTD
        self.lbl_PTD_logo.mousePressEvent = self.PTD
        self.lbl_PTD_PR.mousePressEvent = self.PTD
        self.lbl_PTD_vc.mousePressEvent = self.PTD
        self.lbl_PTD_part.mousePressEvent = self.PTD

        self.btn_PAL_2.clicked.connect(self.PAL)
        self.btn_PAL_1.clicked.connect(self.PAL)
        self.lbl_PAL_cand.mousePressEvent = self.PAL
        self.lbl_PAL_logo.mousePressEvent = self.PAL
        self.lbl_PAL_PR.mousePressEvent = self.PAL
        self.lbl_PAL_vc.mousePressEvent = self.PAL
        self.lbl_PAL_part.mousePressEvent = self.PAL

        self.btn_PRM_2.clicked.connect(self.PRM)
        self.btn_PRM_1.clicked.connect(self.PRM)
        self.lbl_PRM_cand.mousePressEvent = self.PRM
        self.lbl_PRM_logo.mousePressEvent = self.PRM
        self.lbl_PRM_PR.mousePressEvent = self.PRM
        self.lbl_PRM_vc.mousePressEvent = self.PRM
        self.lbl_PRM_part.mousePressEvent = self.PRM

        self.btn_PUN_2.clicked.connect(self.PUN)
        self.btn_PUN_1.clicked.connect(self.PUN)
        self.lbl_PUN_cand.mousePressEvent = self.PUN
        self.lbl_PUN_logo.mousePressEvent = self.PUN
        self.lbl_PUN_PR.mousePressEvent = self.PUN
        self.lbl_PUN_vc.mousePressEvent = self.PUN
        self.lbl_PUN_part.mousePressEvent = self.PUN

        self.btn_FRENTE_2.clicked.connect(self.FRENTE)
        self.btn_FRENTE_1.clicked.connect(self.FRENTE)
        self.lbl_FRENTE_cand.mousePressEvent = self.FRENTE
        self.lbl_FRENTE_logo.mousePressEvent = self.FRENTE
        self.lbl_FRENTE_PR.mousePressEvent = self.FRENTE
        self.lbl_FRENTE_vc.mousePressEvent = self.FRENTE
        self.lbl_FRENTE_part.mousePressEvent = self.FRENTE

        self.btn_APD_2.clicked.connect(self.APD)
        self.btn_APD_1.clicked.connect(self.APD)
        self.lbl_APD_cand.mousePressEvent = self.APD
        self.lbl_APD_logo.mousePressEvent = self.APD
        self.lbl_APD_PR.mousePressEvent = self.APD
        self.lbl_APD_vc.mousePressEvent = self.APD
        self.lbl_APD_part.mousePressEvent = self.APD

        self.btn_PR1_2.clicked.connect(self.PRI)
        self.btn_PR1_1.clicked.connect(self.PRI)
        self.lbl_PRI_cand.mousePressEvent = self.PRI
        self.lbl_PRI_logo.mousePressEvent = self.PRI
        self.lbl_PRI_PR.mousePressEvent = self.PRI
        self.lbl_PRI_vc.mousePressEvent = self.PRI
        self.lbl_PRI_part.mousePressEvent = self.PRI

        self.btn_ALIANZA_2.clicked.connect(self.ALIANZA)
        self.btn_ALIANZA_1.clicked.connect(self.ALIANZA)
        self.lbl_ALIANZA_cand.mousePressEvent = self.ALIANZA
        self.lbl_ALIANZA_logo.mousePressEvent = self.ALIANZA
        self.lbl_ALIANZA_PR.mousePressEvent = self.ALIANZA
        self.lbl_ALIANZA_vc.mousePressEvent = self.ALIANZA
        self.lbl_ALIANZA_part.mousePressEvent = self.ALIANZA


        self.btn_votar.clicked.connect(self.votar)
        self.lbl_votar.mousePressEvent = self.votar

        self.cancel.clicked.connect(self.cancelar)
        self.lbl_cancel.mousePressEvent = self.cancelar

        #self.lbl_Prueba.mousePressEvent = self.funcion



        
        self.txt_part.raise_()
        self.txt_vice.raise_()
        self.txt_presi.raise_()
        self.btn_votar.raise_()
        self.cancel.raise_()
        self.btn_PRD_1.raise_()
        self.lbl_2.raise_()
        self.btn_PLD_1.raise_()
        self.lbl_1.raise_()
        self.lbl_JCE.raise_()
        self.lbl_escudo_1.raise_()
        self.lbl_escudo_2.raise_()
        self.btn_PRSC_1.raise_()
        self.btn_MODA_1.raise_()
        self.btn_PQDC_1.raise_()
        self.btn_FNP_1.raise_()
        self.btn_BIS_1.raise_()
        self.btn_UDC_1.raise_()
        self.btn_PTD_1.raise_()
        self.btn_PRSD_1.raise_()
        self.btn_PHD_1.raise_()
        self.btn_PAL_1.raise_()
        self.btn_PRD_2.raise_()
        self.btn_PRM_1.raise_()
        self.btn_APD_1.raise_()
        self.btn_PUN_1.raise_()
        self.btn_PR1_1.raise_()
        self.btn_FRENTE_1.raise_()
        self.btn_ALIANZA_1.raise_()
        self.lbl_PRD_PR.raise_()
        self.lbl_PRD_vc.raise_()
        self.lbl_PRD_part.raise_()
        self.lbl_APD_cand.raise_()
        self.lbl_ALIANZA_logo.raise_()
        self.lbl_PRD_can.raise_()
        self.lbl_PRD_logo.raise_()
        self.lbl_PLD_cand.raise_()
        self.lbl_MODA_cand.raise_()
        self.lbl_BIS_cand.raise_()
        self.lbl_UDC_cand.raise_()
        self.lbl_PTD_cand.raise_()
        self.lbl_PAL_cand.raise_()
        self.lbl_PRI_cand.raise_()
        self.lbl_PRSC_cand.raise_()
        self.lbl_PRSD_cand.raise_()
        self.lbl_FRENTE_cand.raise_()
        self.lbl_PRM_cand.raise_()
        self.lbl_PQDC_cand.raise_()
        self.lbl_FNP_cand.raise_()
        self.lbl_PUN_cand.raise_()
        self.lbl_PHD_cand.raise_()
        self.lbl_ALIANZA_cand.raise_()
        self.lbl_PRI_logo.raise_()
        self.lbl_PRSC_logo.raise_()
        self.lbl_PLD_logo.raise_()
        self.lbl_PRSD_logo.raise_()
        self.lbl_BIS_logo.raise_()
        self.lbl_MODA_logo.raise_()
        self.lbl_PTD_logo.raise_()
        self.lbl_FNP_logo.raise_()
        self.lbl_PHD_logo.raise_()
        self.lbl_UDC_logo.raise_()
        self.lbl_PQDC_logo.raise_()
        self.lbl_APD_logo.raise_()
        self.lbl_PUN_logo.raise_()
        self.lbl_PRM_logo.raise_()
        self.lbl_PAL_logo.raise_()
        self.lbl_FRENTE_logo.raise_()
        self.lbl_MODA_PR.raise_()
        self.lbl_MODA_vc.raise_()
        self.lbl_MODA_part.raise_()
        self.lbl_PLD_PR.raise_()
        self.lbl_BIS_PR.raise_()
        self.lbl_UDC_PR.raise_()
        self.lbl_PTD_PR.raise_()
        self.lbl_PAL_PR.raise_()
        self.lbl_PRI_PR.raise_()
        self.lbl_PLD_vc.raise_()
        self.lbl_BIS_vc.raise_()
        self.lbl_UDC_vc.raise_()
        self.lbl_PTD_vc.raise_()
        self.lbl_PAL_vc.raise_()
        self.lbl_PRI_vc.raise_()
        self.lbl_PLD_part.raise_()
        self.lbl_BIS_part.raise_()
        self.lbl_UDC_part.raise_()
        self.lbl_PTD_part.raise_()
        self.lbl_PAL_part.raise_()
        self.lbl_PRI_part.raise_()
        self.lbl_PRSC_PR.raise_()
        self.lbl_PRSC_vc.raise_()
        self.lbl_PRSC_part.raise_()
        self.lbl_PHD_PR.raise_()
        self.lbl_PHD_vc.raise_()
        self.lbl_PHD_part.raise_()
        self.lbl_PRM_PR.raise_()
        self.lbl_PRM_vc.raise_()
        self.lbl_FRENTE_vc.raise_()
        self.lbl_FRENTE_PR.raise_()
        self.lbl_PRM_part.raise_()
        self.lbl_FRENTE_part.raise_()
        self.lbl_PRSD_PR.raise_()
        self.lbl_PRSD_vc.raise_()
        self.lbl_PRSD_part.raise_()
        self.lbl_PQDC_PR.raise_()
        self.lbl_PQDC_vc.raise_()
        self.lbl_PQDC_part.raise_()
        self.lbl_ALIANZA_PR.raise_()
        self.lbl_ALIANZA_vc.raise_()
        self.lbl_ALIANZA_part.raise_()
        self.lbl_APD_PR.raise_()
        self.lbl_APD_vc.raise_()
        self.lbl_APD_part.raise_()
        self.lbl_FNP_PR.raise_()
        self.lbl_PUN_PR.raise_()
        self.lbl_PUN_vc.raise_()
        self.lbl_PUN_part.raise_()
        self.lbl_FNP_vc.raise_()
        self.lbl_FNP_part.raise_()
        self.lbl_votar.raise_()
        self.lbl_cancel.raise_()
        self.btn_PRM_2.raise_()
        self.btn_PUN_2.raise_()
        self.btn_FRENTE_2.raise_()
        self.btn_APD_2.raise_()
        self.btn_PR1_2.raise_()
        self.btn_ALIANZA_2.raise_()
        self.btn_PLD_2.raise_()
        self.btn_PRSC_2.raise_()
        self.btn_MODA_2.raise_()
        self.btn_BIS_2.raise_()
        self.btn_PRSD_2.raise_()
        self.btn_PQDC_2.raise_()
        self.btn_UDC_2.raise_()
        self.btn_FNP_2.raise_()
        self.btn_PTD_2.raise_()
        self.btn_PHD_2.raise_()
        self.btn_PAL_2.raise_()
        self.lbl_presi.raise_()
        self.lbl_vice.raise_()
        self.lbl_part.raise_()
        self.txtSetPartido.raise_()
        self.txtSetvice.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.txtSetPresi.raise_()
        ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ScrollArea)
        QtCore.QMetaObject.connectSlotsByName(ScrollArea)


        #########################################################################################
        
    def PRD (self, event):
        self.txt_presi.setText("Danilo Medina")
        self.txt_vice.setText("Margarita Cedeño")
        self.txt_part.setText("PRD")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Danilo Medina")
        self.txtSetvice.setText("Margarita Cedeño")
        self.txtSetPartido.setText("Partido de la Revolución Dominicana(PRD)")
        #self.votar()

    def PLD (self, event):
        self.txt_presi.setText("Danilo Medina")
        self.txt_vice.setText("Margarita Cedeño")
        self.txt_part.setText("PLD")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Danilo Medina")
        self.txtSetvice.setText("Margarita Cedeño")
        self.txtSetPartido.setText("Partido de la Liberación Dominicana(PLD)")
        #self.votar()

    def PRSC (self, event):
        self.txt_presi.setText("Luis Abinader")
        self.txt_vice.setText("Carolina Mejia")
        self.txt_part.setText("PRSC")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Luis Abinader")
        self.txtSetvice.setText("Carolina Mejia")
        self.txtSetPartido.setText("Partido Revolucionario Social Cristiano(PRSC)")
        #self.votar()

    def MODA (self, event):
        self.txt_presi.setText("Danilo Medina")
        self.txt_vice.setText("Margarita Cedeño")
        self.txt_part.setText("MODA")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Danilo Medina")
        self.txtSetvice.setText("Margarita Cedeño")
        self.txtSetPartido.setText("Movimiento Democrático Alternativo(MODA)")

    def BIS (self, event):
        self.txt_presi.setText("Danilo Medina")
        self.txt_vice.setText("Margarita Cedeño")
        self.txt_part.setText("BIS")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Danilo Medina")
        self.txtSetvice.setText("Margarita Cedeño")
        self.txtSetPartido.setText("Bloque Institucional Social Démocrata(BIS)")

    def PRSD (self, event):
        self.txt_presi.setText("Hatuey de Champs")
        self.txt_vice.setText("Rafael Camaño")
        self.txt_part.setText("PRSD")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Hatuey de Champs")
        self.txtSetvice.setText("Rafael Camaño")
        self.txtSetPartido.setText("Partido Radical Socialdemócrata(PRSD)")

    def PQDC (self, event):
        self.txt_presi.setText("Elías Wessin")
        self.txt_vice.setText("Francisco Paulino")
        self.txt_part.setText("PQDC")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Elías Wessin")
        self.txtSetvice.setText("Francisco Paulino")
        self.txtSetPartido.setText("Partido Quisqueyano Demócrata Cristiano(PQDC)")

    def UDC (self, event):
        self.txt_presi.setText("Danilo Medina")
        self.txt_vice.setText("Margarita Cedeño")
        self.txt_part.setText("UDC")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Danilo Medina")
        self.txtSetvice.setText("Margarita Cedeño")
        self.txtSetPartido.setText("Partido Unión Democrata Cristiana(UDC)")

        
    def PHD (self, event):
        self.txt_presi.setText("Luis Abinader")
        self.txt_vice.setText("Carolina Mejia")
        self.txt_part.setText("PHD")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Luis Abinader")
        self.txtSetvice.setText("Carolina Mejia")
        self.txtSetPartido.setText("Partido Humanista Dominicano PHD)")
        
    def FNP (self, event):
        self.txt_presi.setText("Pelegrín Castillo")
        self.txt_vice.setText("Daysi Sepúlveda")
        self.txt_part.setText("FNP")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Pelegrín Castillo")        
        self.txtSetvice.setText("Daysi Sepúlveda")
        self.txtSetPartido.setText("Fuerza Nacional Progresista (FNP)")

    def PTD (self, event):
        self.txt_presi.setText("Danilo Medina")
        self.txt_vice.setText("Margarita Cedeño")
        self.txt_part.setText("PTD")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Danilo Medina")
        self.txtSetvice.setText("Margarita Cedeño")
        self.txtSetPartido.setText("Partido De Los Trabajadores Dominicanos(PTD)")
        
    def PAL (self, event):
        self.txt_presi.setText("Danilo Medina")
        self.txt_vice.setText("Margarita Cedeño")
        self.txt_part.setText("PAL")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Danilo Medina")
        self.txtSetvice.setText("Margarita Cedeño")
        self.txtSetPartido.setText("Patido de Acción Liberal (PAL)")
        #self.votar()

    def PRM (self, event):
        self.txt_presi.setText("Luis Abinader")
        self.txt_vice.setText("Carolina Mejia")
        self.txt_part.setText("PRM")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Luis Abinader")
        self.txtSetvice.setText("Carolina Mejia")
        self.txtSetPartido.setText("Partido Revolucionario Moderno (PRM)")
        #self.votar()


    def PUN (self, event):
        self.txt_presi.setText("Soraya Aquino")
        self.txt_vice.setText("Pedro Corporán")
        self.txt_part.setText("PUN")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Soraya Aquino")
        self.txtSetvice.setText("Pedro Corporán")
        self.txtSetPartido.setText("Partido de Unidad Nacional(PUN)")
        #self.votar()                     


    def FRENTE (self, event):
        self.txt_presi.setText("Luis Abinader")
        self.txt_vice.setText("Carolina Mejia")
        self.txt_part.setText("FRENTE AMPLIO")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Luis Abinader")
        self.txtSetvice.setText("Carolina Mejia")
        self.txtSetPartido.setText("Frente Amplio")
        #self.votar()

    def APD (self, event):
        self.txt_presi.setText("Minou Tavarez")
        self.txt_vice.setText("Mario Berges")
        self.txt_part.setText("APD")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Minou Tavarez")
        self.txtSetvice.setText("Mario Berges")
        self.txtSetPartido.setText("Alianza por la Democracia(APD)")
        #self.votar()

    def PRI (self, event):
        self.txt_presi.setText("Danilo Medina")
        self.txt_vice.setText("Margarita Cedeño")
        self.txt_part.setText("PRI")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Danilo Medina")
        self.txtSetvice.setText("Margarita Cedeño")
        self.txtSetPartido.setText("Partido Revolucionario Institucional (PRI)")
        #self.votar()    
        
    def ALIANZA (self, event):
        self.txt_presi.setText("Guillermo Moreno")
        self.txt_vice.setText("María Cantisano")
        self.txt_part.setText("ALPAIS")
        self.btn_votar.setVisible(True)
        self.lbl_votar.setVisible(True)        
        self.txtSetPresi.setText("Guillermo Moreno")
        self.txtSetvice.setText("María Cantisano")
        self.txtSetPartido.setText("Alianza País (ALPAIS)")

    def cancelar(self, event):
        sys.exit()
        
    def votar(self, event):
        presi = self.txt_presi.toPlainText()
        vice = self.txt_vice.toPlainText()
        part = self.txt_part.toPlainText()
        choice = QtGui.QMessageBox.question(ScrollArea, "Elecciones 2020",
                                            "¿Está Seguro que Desea Votar por: "+part+"?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            letreto = QtGui.QMessageBox.question(ScrollArea, "Elecciones 2020",
                                            "Su voto se ha registrado exitosamente")

            
            datos= "UPDATE Cedula_ciudadano SET voto={} WHERE cedula='{}'".format(1,cedula)##############3
            mariadb_connection = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
            #funciona tanto si el host es 127.0.1.1 como 127.0.0.1
            cursor = mariadb_connection.cursor()

           
            cursor.execute(datos)

            # Fetch a single row using fetchone() method.
            mariadb_connection.commit()
            #ver= "SELECT voto FROM Cedula_ciudadano WHERE cedula='{}'".format(cedula)

            #cursor.execute(ver)
            #data = cursor.fetchone()
            #print("voto en: "+ str(data))
            mariadb_connection.close()

            #hacer eso mismo con la base de datos remota


            ##/////////////////////////////////////////////////////////////////////////////////

            insert= "INSERT INTO Registo_voto (id_mesa_elec, partido, presidente, vicepresidenta) VALUES ('{}', '{}', '{}', '{}')".format(id_col, part, presi, vice)##############3
            mariadb_connectionvoto = mariadb.connect(user='prueba', password='hola', database='voto', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
           
            cursorvoto = mariadb_connectionvoto.cursor()

           
            cursorvoto.execute(insert)

            # Fetch a single row using fetchone() method.
            mariadb_connectionvoto.commit()

##            select= "SELECT MAX(id_voto) * FROM Registro_voto"
##            cursorvoto.execute(select)
##            mensaje = cursorvoto.fetchall()
##            print(mensaje)

            mariadb_connectionvoto.close()



## aqui puedo enviar y el voto en un hilo y revisar conexion antes



            ####enviar el voto aqui### si no hay conexion dura mucho en cerar
            #cmd = "ping -c 1 8.8.8.8"
            #global conexion
            #if (get_return_code_of_simple_cmd(cmd) == 0):
            
        
            datos="SELECT * FROM Registo_voto WHERE recibido=0 order by id_voto DESC LIMIT 1"
            #datos=dat
            mariadb_connection = mariadb.connect(user='prueba', password='hola', database='voto', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
            #funciona tanto si el host es 127.0.1.1 como 127.0.0.1
            cursor = mariadb_connection.cursor()


            cursor.execute(datos)

            # Fetch a single row using fetchone() method.
            data = cursor.fetchall()

            mariadb_connection.close()

            for row in data:
                eid_voto = row[0]
                eid_mesa = row[1]
                epartido = row[2]
                epresidente = row[3]
                evicepresidente = row[4]
                
          ###aqui imprimir el voto
            #os.system("stty -F /dev/ttyUSBPort2 19200")
            impr="echo '       JCE\\nElección Ordinaria\\n17 de Mayo de 2018\\nRecibo de votación\\n\\n"+epresidente+"\\n"+evicepresidente+"\\n"+epartido+"\\n' | lpr -P pp"
            os.system(impr)
            code="lpr -P pp -o fit-to-page /home/pi/Desktop/backup/barcodes/"+epartido+".png"
            if(epartido=='FRENTE AMPLIO'):
                os.system("lpr -P pp -o fit-to-page /home/pi/Desktop/backup/barcodes/FRE.png")
            else:
                os.system(code)



            
            #enviar el voto
            ### hacer un if si hay internet
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.settimeout(1) 
            #host = "192.168.30.10"#softether
            host = "192.168.40.2" #pptp
            port = 5557


            try:
                soc.connect((host, port))
                message = "{},{},{},{},{},{}".format(eid_voto, eid_mesa, epartido, epresidente, evicepresidente, backup) #input(" -> ")
                soc.sendall(message.encode("utf8"))#ver como no se quede esperando
                recibido= soc.recv(5120).decode("utf8")

                #poner un if recibido    
                rec=recibido.split(",")
                
                if (rec[0]=='0'):
                    letreto = QtGui.QMessageBox.question(ScrollArea, "Elecciones 2020",
                                            "Está Cabina Está Fuera de Servicio")
                    os.system('sudo service mysql stop')
                    time.sleep(1)            
                    os.system('sudo reboot')
##                    os.system("")
##                    print(0)#apagar la maquina maybe
##                    #apagar la cabina
                
                #print(rec[0])
                #print(rec[1])
                else:###ver que se está enviando, porque ahora rec[0] parece ser otra cosa
                    datos= "UPDATE Registo_voto SET recibido=1 WHERE id_voto={} and id_mesa_elec='{}'".format(rec[0],rec[1])##############3
                    mariadb_connection = mariadb.connect(user='prueba', password='hola', database='voto', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                    
                    cursor = mariadb_connection.cursor()                   
                    cursor.execute(datos)                    
                    mariadb_connection.commit()            
                    mariadb_connection.close()
               
            except socket.gaierror:
                sys.exit()
                #pass
                #print( "Address-related error connecting to server:") 
                #sys.exit(1)

            except socket.error:
                sys.exit()
                #pass
                #print ("Connection error: ")
                #sys.exit(1)



            try:####marcar a quien ya voto en rds
                
                mariadb_connection = mariadb.connect(user='prueba', password='hola', database='votacion', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
                cursor = mariadb_connection.cursor()

                
                #agrege el timeout
                mariadb_connectionRemota = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com', connection_timeout= 7)
                cursorRemota = mariadb_connectionRemota.cursor()


                votoUpdate="UPDATE Cedula_ciudadano set voto=1, actualizar =1 WHERE cedula= '{}'".format(cedula)    #cedula del que voto
                cursorRemota.execute(votoUpdate)
                mariadb_connectionRemota.commit()
                mariadb_connectionRemota.close()
                
                upda="UPDATE Cedula_ciudadano set actualizar=1 WHERE cedula= '{}'".format(cedula)#cedula
                cursor.execute(upda)
                mariadb_connection.commit()
                        
                        
                mariadb_connection.close()
                

            except:
                pass

            #se puede marcar aqui ha quien vota porque si no hay conexion se cierra en el except

  

            #marcar al voto recibido-------------------------------------------

            #poner un if recibido    
##            rec=recibido.split(",")
##            if (rec[0]==0):
##                print(0)#apagar la maquina maybe
##                #apagar la cabina
##            
##            #print(rec[0])
##            #print(rec[1])
##            else:###ver que se está enviando, porque ahora rec[0] parece ser otra cosa
##                datos= "UPDATE Registo_voto SET recibido=1 WHERE id_voto={} and id_mesa_elec='{}'".format(rec[0],rec[1])##############3
##                mariadb_connection = mariadb.connect(user='prueba', password='hola', database='voto', host='127.0.0.1', unix_socket= '/var/run/mysqld/mysqld.sock')
##                
##                cursor = mariadb_connection.cursor()
##               
##                cursor.execute(datos)
##                
##                mariadb_connection.commit()            
##                mariadb_connection.close()


##                datos="UPDATE Cedula_ciudadano set voto=1 WHERE cedula= '{}'".format(ced)    
##                mariadb_connection = mariadb.connect(user='prueba', password='holahola', database='votacion', host='votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com', connect_timeout=2)
##                cursor = mariadb_connection.cursor()
##                cursor.execute(datos)
##                mariadb_connection.commit()
##                mariadb_connection.close()

        
        
            sys.exit()
        else:
            pass

        
    def retranslateUi(self, ScrollArea):
        ScrollArea.setWindowTitle(_translate("ScrollArea", "Elecciones 2020", None))
        self.lbl_1.setText(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Presidente y Vicepresidente</span></p></body></html>", None))
        self.lbl_2.setText(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_PLD_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_PRSC_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_MODA_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_PQDC_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_FNP_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_BIS_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_UDC_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_PTD_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_PRSD_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_PHD_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_PAL_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_PRD_2.setText(_translate("ScrollArea", "1", None))
        self.btn_PRM_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_APD_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_PUN_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_PR1_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_FRENTE_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_ALIANZA_1.setWhatsThis(_translate("ScrollArea", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.lbl_PRD_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">DANILO MEDINA</span></p></body></html>", None))
        self.lbl_PRD_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MARGARITA CEDEÑO</span></p></body></html>", None))
        self.lbl_PRD_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PRD</span></p></body></html>", None))
        self.lbl_MODA_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">DANILO MEDINA</span></p></body></html>", None))
        self.lbl_MODA_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MARGARITA CEDEÑO</span></p></body></html>", None))
        self.lbl_MODA_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MODA</span></p></body></html>", None))
        self.lbl_PLD_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">DANILO MEDINA</span></p></body></html>", None))
        self.lbl_BIS_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">DANILO MEDINA</span></p></body></html>", None))
        self.lbl_UDC_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">DANILO MEDINA</span></p></body></html>", None))
        self.lbl_PTD_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">DANILO MEDINA</span></p></body></html>", None))
        self.lbl_PAL_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">DANILO MEDINA</span></p></body></html>", None))
        self.lbl_PRI_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">DANILO MEDINA</span></p></body></html>", None))
        self.lbl_PLD_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MARGARITA CEDEÑO</span></p></body></html>", None))
        self.lbl_BIS_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MARGARITA CEDEÑO</span></p></body></html>", None))
        self.lbl_UDC_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MARGARITA CEDEÑO</span></p></body></html>", None))
        self.lbl_PTD_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MARGARITA CEDEÑO</span></p></body></html>", None))
        self.lbl_PAL_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MARGARITA CEDEÑO</span></p></body></html>", None))
        self.lbl_PRI_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MARGARITA CEDEÑO</span></p></body></html>", None))
        self.lbl_PLD_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PLD</span></p></body></html>", None))
        self.lbl_BIS_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">BIS</span></p></body></html>", None))
        self.lbl_UDC_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">UDC</span></p></body></html>", None))
        self.lbl_PTD_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PTD</span></p></body></html>", None))
        self.lbl_PAL_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PAL</span></p></body></html>", None))
        self.lbl_PRI_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PRI</span></p></body></html>", None))
        self.lbl_PRSC_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">LUIS ABINADER</span></p></body></html>", None))
        self.lbl_PRSC_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">CAROLINA MEJIA</span></p></body></html>", None))
        self.lbl_PRSC_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PRSC</span></p></body></html>", None))
        self.lbl_PHD_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">LUIS ABINADER</span></p></body></html>", None))
        self.lbl_PHD_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">CAROLINA MEJIA</span></p></body></html>", None))
        self.lbl_PHD_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PHD</span></p></body></html>", None))
        self.lbl_PRM_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">LUIS ABINADER</span></p></body></html>", None))
        self.lbl_PRM_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">CAROLINA MEJIA</span></p></body></html>", None))
        self.lbl_FRENTE_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">CAROLINA MEJIA</span></p></body></html>", None))
        self.lbl_FRENTE_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">LUIS ABINADER</span></p></body></html>", None))
        self.lbl_PRM_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PRM</span></p></body></html>", None))
        self.lbl_FRENTE_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">FRENTE AMPLIO</span></p></body></html>", None))
        self.lbl_PRSD_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">HATUEY DE CAMPS</span></p></body></html>", None))
        self.lbl_PRSD_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">RAFAEL CAMAÑO</span></p></body></html>", None))
        self.lbl_PRSD_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PRSD</span></p></body></html>", None))
        self.lbl_PQDC_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">ELIAS WESSIN</span></p></body></html>", None))
        self.lbl_PQDC_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">FRANCISCO PAULINO</span></p></body></html>", None))
        self.lbl_PQDC_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PQDC</span></p></body></html>", None))
        self.lbl_ALIANZA_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">GUILLERMO MORENO</span></p></body></html>", None))
        self.lbl_ALIANZA_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MARIA CANTISANO</span></p></body></html>", None))
        self.lbl_ALIANZA_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">ALPAIS</span></p></body></html>", None))
        self.lbl_APD_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MINOU TAVAREZ</span></p></body></html>", None))
        self.lbl_APD_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">MARIO BERGES</span></p></body></html>", None))
        self.lbl_APD_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">APD</span></p></body></html>", None))
        self.lbl_FNP_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PELEGRIN CASTILLO</span></p></body></html>", None))
        self.lbl_PUN_PR.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">SORAYA AQUINO</span></p></body></html>", None))
        self.lbl_PUN_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PEDRO CORPORAN</span></p></body></html>", None))
        self.lbl_PUN_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">PUN</span></p></body></html>", None))
        self.lbl_FNP_vc.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">DAYSI SEPULVEDA</span></p></body></html>", None))
        self.lbl_FNP_part.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">FNP</span></p></body></html>", None))
        self.lbl_votar.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">VOTAR</span></p></body></html>", None))
        self.lbl_cancel.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">CANCELAR</span></p></body></html>", None))
        self.btn_PRM_2.setText(_translate("ScrollArea", "13", None))
        self.btn_PUN_2.setText(_translate("ScrollArea", "14", None))
        self.btn_FRENTE_2.setText(_translate("ScrollArea", "15", None))
        self.btn_APD_2.setText(_translate("ScrollArea", "16", None))
        self.btn_PR1_2.setText(_translate("ScrollArea", "17", None))
        self.btn_ALIANZA_2.setText(_translate("ScrollArea", "18", None))
        self.btn_PLD_2.setText(_translate("ScrollArea", "2", None))
        self.btn_PRSC_2.setText(_translate("ScrollArea", "3", None))
        self.btn_MODA_2.setText(_translate("ScrollArea", "4", None))
        self.btn_BIS_2.setText(_translate("ScrollArea", "5", None))
        self.btn_PRSD_2.setText(_translate("ScrollArea", "6", None))
        self.btn_PQDC_2.setText(_translate("ScrollArea", "7", None))
        self.btn_UDC_2.setText(_translate("ScrollArea", "8", None))
        self.btn_FNP_2.setText(_translate("ScrollArea", "10", None))
        self.btn_PTD_2.setText(_translate("ScrollArea", "11", None))
        self.btn_PHD_2.setText(_translate("ScrollArea", "9", None))
        self.btn_PAL_2.setText(_translate("ScrollArea", "12", None))
        self.label.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Partido:</span></p></body></html>", None))
        self.label_2.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Presidente:</span></p></body></html>", None))
        self.label_3.setText(_translate("ScrollArea", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Vicepresidente:</span></p></body></html>", None))

def get_return_code_of_simple_cmd(cmd, stderr=STDOUT):
    args = shlex.split(cmd)
    return call(args, stdout=PIPE, stderr=stderr)

import JCE

if __name__ == "__main__":

    
    app = QtGui.QApplication(sys.argv)
    
    ced=str(sys.argv[1])
    #print(ced)
    id_col = str(sys.argv[2])
   # print(id_col)
    backup=int(sys.argv[3])
    
    ScrollArea = QtGui.QScrollArea()
    ui = Ui_ScrollArea()
    ui.setupUi(ScrollArea, ced, id_col, backup)
    ScrollArea.show()
    sys.exit(app.exec_())

