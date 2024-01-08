#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from PyQt6 import QtWidgets, QtGui, QtCore

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

			# Class
			self.Main = parent
			
		except Exception as e:
			log().error(TR_ERROR_MODEL_INTERNO_X.format(__name__,e))