#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import time
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

''' Load '''
from fast_food.define import is_connected_to_internet as Internet
from fast_food.core.settings import *
from fast_food.core.translations import *
from fast_food.core.notify import Notify

''' PyQt6 Gui '''
from fast_food.views.wmain import Ui_MainWindow

''' Conexion '''
from fast_food.conexion.database import DBase

''' Internal Logs '''
def log():
	return logging.getLogger(__name__) #.info() .debug() .warning() .error()

''' Class '''
class WMModel(QtWidgets.QMainWindow, Ui_MainWindow):
	bloqueo = 0
	def __init__(self, parent=None):
		try: 
			super(WMModel, self).__init__()
			self.setupUi(self)			

			log().info(TR_LOAD_MODEL_X.format("Main"))

			# FullScreen
			if Settings().FULLSCREEN:
				self.showMaximized()
			else:
				self.resize(Settings().WINSIZE)
				self.move(Settings().WINPOS)

			# Class
			self.Main = parent

			# Basic 			
			self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
			self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

			if not Settings().SIDERBAR:
				self.siderBar_2.hide()

			self.btn_sidebar.clicked.connect(self.SBcheck)
			self.btn_sidebar.setChecked(Settings().SIDERBAR)

			self.timer = QTimer(self)
			self.timer.timeout.connect(self.check_internet_connection)
			self.timer.start(5000)


		except Exception as e:
			log().error(TR_ERROR_MODEL_INTERNO_X.format(__name__,e))

	def SBcheck(self):
		if self.btn_sidebar.isChecked() and not Settings().SIDERBAR:
			self.siderBar_2.show()
		else:
			self.siderBar_2.hide()
		Settings().SIDERBAR = True if self.btn_sidebar.isChecked() else False

	def check_internet_connection(self):
		if Internet():
			#print("internet ok")
			self.pic_online.setPixmap(QPixmap(":/Icons/png/icons8-wi-fi-connected-100.png"))
			self.pic_online.setToolTip("On-line")				
		else:
			#print("internet off")
			self.pic_online.setPixmap(QPixmap(":/Icons/png/icons8-wi-fi-disconnected-100.png"))
			self.pic_online.setToolTip("Off-line")

	def closeEvent(self, event):
		if self.bloqueo == 0:
			reply = QMessageBox.question(self,
									'Salir',
									f"Realmente desea salir de {fast_food.__title__}",
									QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
			if reply == QMessageBox.StandardButton.Yes:
				self.mdiArea.closeAllSubWindows()
				Settings().USER_NAME = TR_FASTFOOD
				Settings().USER_ROLES = TR_FASTFOOD

				Settings().FULLSCREEN = True if self.isMaximized() else False		
				if not self.isMaximized():
					Settings().WINSIZE = self.size()
					Settings().WINPOS = self.pos()

				log().info(TR_CLOSED_X.format(TR_FASTFOOD))
				event.accept()
			else:
				event.ignore()

