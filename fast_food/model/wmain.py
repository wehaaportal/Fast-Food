#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt

''' Load '''
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
			
			
		except Exception as e:
			log().error(TR_ERROR_MODEL_INTERNO_X.format(__name__,e))

	def SBcheck(self):
		if self.btn_sidebar.isChecked() and not Settings().SIDERBAR:
			self.siderBar_2.show()
		else:
			self.siderBar_2.hide()
		Settings().SIDERBAR = True if self.btn_sidebar.isChecked() else False
