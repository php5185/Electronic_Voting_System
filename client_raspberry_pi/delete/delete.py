import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QPushButton(w)
   b.setText("Show message!")

   b.move(50,50)
   b.clicked.connect(showdialog)
   w.setWindowTitle("PyQt Dialog demo")
   w.show()
   sys.exit(app.exec_())

def showdialog():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)

   msg.setText("Elecciones 2020  Elecciones 2020")
  # msg.setInformativeText("This is additional information")
   msg.setWindowTitle("Elecciones 2020")
   #msg.setDetailedText("The details are as follows:")
   msg.setStandardButtons(QMessageBox.Ok)
   #msg.buttonClicked.connect(msgbtn) ##para saber la respuesta si hay mas de 1
	
   retval = msg.exec_()
   #print ("value of pressed message box button:", retval)
	
def msgbtn(i):
   print ("Button pressed is:",i.text())

	
##def showdialog():
##   msg = QMessageBox()
##   msg.setIcon(QMessageBox.Information)
##
##   msg.setText("This is a message box")
##  # msg.setInformativeText("This is additional information")
##   msg.setWindowTitle("MessageBox demo")
##   #msg.setDetailedText("The details are as follows:")
##   msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
##   msg.buttonClicked.connect(msgbtn)
##	
##   retval = msg.exec_()
##   print ("value of pressed message box button:", retval)
##	
##def msgbtn(i):
##   print ("Button pressed is:",i.text())
	
if __name__ == '__main__': 
   window()
