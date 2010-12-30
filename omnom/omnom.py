import sys
import os
from PyQt4 import QtGui,QtCore
from omnomgui import *

class MyForm(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.ui = Ui_GUI()
                self.ui.setupUi(self)
		self.setWindowTitle("OmNomNom")
		lvl1 = QtGui.QPixmap("data/images/lvl1.png")
		lvl2 = QtGui.QPixmap("data/images/lvl2.png")
		lvl3 = QtGui.QPixmap("data/images/lvl3.png")
		lvl4 = QtGui.QPixmap("data/images/lvl4.png")
		self.ui.lvl1Pic.setPixmap(lvl1)
		self.ui.lvl2Pic.setPixmap(lvl2)
		self.ui.lvl3Pic.setPixmap(lvl3)
		self.ui.lvl4Pic.setPixmap(lvl4)

		QtCore.QObject.connect(self.ui.lvl1Button, QtCore.SIGNAL('clicked()'), self.doLvl1)
		QtCore.QObject.connect(self.ui.lvl2Button, QtCore.SIGNAL('clicked()'), self.doLvl2)
		QtCore.QObject.connect(self.ui.lvl3Button, QtCore.SIGNAL('clicked()'), self.doLvl3)
		QtCore.QObject.connect(self.ui.lvl4Button, QtCore.SIGNAL('clicked()'), self.doLvl4)

	def doLvl1(self):
		
	def doLvl2(self):
		
	def doLvl3(self):
		
	def doLvl4(self):
		
if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = MyForm()
        myapp.show()
        sys.exit(app.exec_())
