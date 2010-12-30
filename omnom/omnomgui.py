#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Aug 24 21:39:31 2010
#	  by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

import logging
from PyQt4 import QtCore, QtGui


_moduleLogger = logging.getLogger(__name__)


class Ui_GUI(object):

	def setupUi(self, GUI):
		GUI.setObjectName("GUI")
		GUI.resize(800, 480)
		self.centralwidget = QtGui.QWidget(GUI)
		self.centralwidget.setObjectName("centralwidget")
		self.lvl1Pic = QtGui.QLabel(self.centralwidget)
		self.lvl1Pic.setGeometry(QtCore.QRect(80, 30, 280, 140))
		self.lvl1Pic.setObjectName("lvl1Pic")
		self.lvl2Pic = QtGui.QLabel(self.centralwidget)
		self.lvl2Pic.setGeometry(QtCore.QRect(440, 30, 280, 140))
		self.lvl2Pic.setObjectName("lvl2Pic")
		self.lvl3Pic = QtGui.QLabel(self.centralwidget)
		self.lvl3Pic.setGeometry(QtCore.QRect(80, 210, 280, 140))
		self.lvl3Pic.setObjectName("lvl3Pic")
		self.lvl4Pic = QtGui.QLabel(self.centralwidget)
		self.lvl4Pic.setGeometry(QtCore.QRect(440, 210, 280, 140))
		self.lvl4Pic.setObjectName("lvl4Pic")
		self.lvl1Button = QtGui.QPushButton(self.centralwidget)
		self.lvl1Button.setGeometry(QtCore.QRect(160, 170, 111, 40))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.lvl1Button.setFont(font)
		self.lvl1Button.setObjectName("lvl1Button")
		self.lvl3Button = QtGui.QPushButton(self.centralwidget)
		self.lvl3Button.setGeometry(QtCore.QRect(160, 350, 111, 40))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.lvl3Button.setFont(font)
		self.lvl3Button.setObjectName("lvl3Button")
		self.lvl2Button = QtGui.QPushButton(self.centralwidget)
		self.lvl2Button.setGeometry(QtCore.QRect(530, 170, 111, 40))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.lvl2Button.setFont(font)
		self.lvl2Button.setObjectName("lvl2Button")
		self.lvl4Button = QtGui.QPushButton(self.centralwidget)
		self.lvl4Button.setGeometry(QtCore.QRect(530, 350, 111, 40))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.lvl4Button.setFont(font)
		self.lvl4Button.setObjectName("lvl4Button")
		self.configButton = QtGui.QPushButton(self.centralwidget)
		self.configButton.setGeometry(QtCore.QRect(350, 330, 93, 60))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.configButton.setFont(font)
		self.configButton.setObjectName("configButton")
		GUI.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(GUI)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
		self.menubar.setObjectName("menubar")
		GUI.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(GUI)
		self.statusbar.setObjectName("statusbar")
		GUI.setStatusBar(self.statusbar)

		self.retranslateUi(GUI)
		QtCore.QMetaObject.connectSlotsByName(GUI)

	def retranslateUi(self, GUI):
		GUI.setWindowTitle(QtGui.QApplication.translate("GUI", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
		self.lvl1Pic.setText(QtGui.QApplication.translate("GUI", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
		self.lvl2Pic.setText(QtGui.QApplication.translate("GUI", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
		self.lvl3Pic.setText(QtGui.QApplication.translate("GUI", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
		self.lvl4Pic.setText(QtGui.QApplication.translate("GUI", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
		self.lvl1Button.setText(QtGui.QApplication.translate("GUI", "Level 1", None, QtGui.QApplication.UnicodeUTF8))
		self.lvl3Button.setText(QtGui.QApplication.translate("GUI", "Level 10", None, QtGui.QApplication.UnicodeUTF8))
		self.lvl2Button.setText(QtGui.QApplication.translate("GUI", "Level 6", None, QtGui.QApplication.UnicodeUTF8))
		self.lvl4Button.setText(QtGui.QApplication.translate("GUI", "Level 14", None, QtGui.QApplication.UnicodeUTF8))
		self.configButton.setText(QtGui.QApplication.translate("GUI", "Config", None, QtGui.QApplication.UnicodeUTF8))

