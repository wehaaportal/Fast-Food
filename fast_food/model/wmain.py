#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import time
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QAction, QIcon
from PyQt6.QtWidgets import QMessageBox, QMenu, QMdiSubWindow
from PyQt6.uic import loadUi

''' Load '''
from fast_food.define import GUI_PATH, is_connected_to_internet as Internet
from fast_food.core.settings import *
from fast_food.core.translations import *
from fast_food.core.notify import Notify

''' Model '''
from fast_food.model.wlogin import WLModel

''' PyQt6 Gui '''
from fast_food.views.wmain import Ui_MainWindow

''' Conexion '''
from fast_food.conexion.database import DBase

''' Internal Logs '''
def log():
	return logging.getLogger(__name__) #.info() .debug() .warning() .error()

''' Class '''
class welcomeModel(QMdiSubWindow):
	def __init__(self, mdi_area):
		super().__init__()

		loadUi(f'{GUI_PATH}/winicio.ui', self)
		self.mdi_area = mdi_area

		self.chk_init.setChecked(Settings().WELCOME)

		# Desactivar botones de la barra de título y quitar todos los bordes
		self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
		self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
		self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)

	def setCenter(self):
		mdi_area_size = self.mdi_area.size()
		sub_window_size = self.size()
		self.setGeometry(
			(mdi_area_size.width() - sub_window_size.width()) // 2,
			(mdi_area_size.height() - sub_window_size.height()) // 2,
			sub_window_size.width(),
			sub_window_size.height()
		)

	def closeEvent(self, event):
		Settings().WELCOME = self.chk_init.isChecked()
		self.close()



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

			#Welcome 
			Welcome_window = welcomeModel(self.mdiArea)
			self.mdiArea.addSubWindow(Welcome_window)
			Welcome_window.setCenter()

			if not Settings().SIDERBAR:
				self.siderBar_2.hide()

			self.btn_sidebar.clicked.connect(self.SBcheck)
			self.btn_sidebar.setChecked(Settings().SIDERBAR)

			self.timer = QTimer(self)
			self.timer.timeout.connect(self.check_internet_connection)
			self.timer.start(5000)

			self.btn_security.clicked.connect(self.openLogins)
			self.btn_exit.clicked.connect(self.openLogins)

			if Settings().WELCOME:
				 Welcome_window.show()

		except Exception as e:
			log().error(TR_ERROR_MODEL_INTERNO_X.format(__name__,e))

	def openLogins(self):
		self.bloqueo = 1
		self.security 	= WLModel(self)
		log().info("Bloquear Pantalla")	
		self.mdiArea.closeAllSubWindows()	
		#self.close()
		self.hide()
		self.security.lblWelcome.setText("Locked screen") #"Welcome Back"
		self.security.lblSlogan.setText("Security was activated") #"Nice to see you again"
		self.security.txtUser.setText(Settings().USER_NAME)
		self.security.txtPass.setText("")
		Settings().USER_NAME = TR_FASTFOOD
		Settings().USER_ROLES = TR_FASTFOOD		
		self.security.show()
		self.security.activateWindow()
		self.bloqueo = 0

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

	# UI and Mouse Interaction functions
	def contextMenuEvent(self, event):
		cmenu = QMenu(self)
		quitAct = cmenu.addAction(QIcon(":/Icons/png/icons8-exit-100.png"), "Salir")
		action = cmenu.exec(self.mapToGlobal(event.pos()))
		if action == quitAct:
			self.close()

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

