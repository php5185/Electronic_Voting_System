import sys
from PyQt4.QtGui import QDialog, QWidget, QLineEdit, QApplication
from PyQt4.QtCore import SIGNAL
import subprocess
import _thread


class extQLineEdit(QLineEdit):
    def __init__(self,parent):
        QLineEdit.__init__(self,parent)
    def mousePressEvent(self,QMouseEvent):
        self.emit(SIGNAL("clicked()"))


class Form(QDialog):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.resize(300,100)

        self.lineEdit=extQLineEdit(self)
        self.lineEdit.move(10,10)
        self.connect(self.lineEdit,SIGNAL("clicked()"), self.printText)

    def printText(self):
        _thread.start_new_thread(self.colegio, ())

    def colegio(self):
        subprocess.check_output(["florence"])

app = QApplication(sys.argv)
form =Form()
form.show()

sys.exit(app.exec_())
    
            
            
