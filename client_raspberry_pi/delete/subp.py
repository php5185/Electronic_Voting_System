#!/usr/bin/python3

import subprocess
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import subprocess
import sys
import time

#letreto = QtGui.QMessageBox.question(Dialog, "Elecciones 2020", "Usted no tiene permitido emitir el voto en esta mesa electoral")





if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    ScrollArea = QtGui.QScrollArea()
    ScrollArea.setWindowModality(Qt.ApplicationModal)
    let=str(sys.argv[1])

    if let=='1':
        letreto = QtGui.QMessageBox.question(ScrollArea, "Elecciones 2020",
                                            "Usted no Tiene Permitido Votar en Esta Mesa Electoral")
    if let=='2':
        letreto = QtGui.QMessageBox.question(ScrollArea, "Elecciones 2020",
                                            "Usted Ya Emitió Su Voto Exitosamente")
    if let=='3':
        letreto = QtGui.QMessageBox.question(ScrollArea, "Elecciones 2020",
                                            "Verifique el Nombre y Contraseña de la mesa electoral")
    if let=='4':
        letreto = QtGui.QMessageBox.question(ScrollArea, "Elecciones 2020",
                                            "Esta Mesa Electoral ya Tiene La Información Necesaria Cargada")         
    if let=='5':
        letreto = QtGui.QMessageBox.question(ScrollArea, "Elecciones 2020",
                                            "Contraseña Incorrecta")         
    if let=='6':
        letreto = QtGui.QMessageBox.question(ScrollArea, "Elecciones 2020",
                                            "Verifique el Nombre de la mesa electoral")
    if let=='7':
        letreto = QtGui.QMessageBox.question(ScrollArea, "Elecciones 2020",
                                            "Proceso Completado Satisfactoriamente")    
        
    sys.exit()

##
#idc='11111111111'
##
##subprocess.call(["boletae.py"])

##
##cmd= "python --version"
##
##ret= subprocess.call("(python --version)", shell=True)
##print(ret)
##
##rets= os.system(cmd)
##print(rets)

#print(subprocess.check_output(["ping", "-c2", "www.google.com"]))

#print(subprocess.check_output(["python3", "boletae.py", "40626000178"]))
##subprocess.check_output(["python3", "boletae.py", idc])
##print(12)
