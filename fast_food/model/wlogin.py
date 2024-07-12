#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import re
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

''' Load '''
from fast_food.core.settings import *
from fast_food.core.crypt import Crypt
from fast_food.core.translations import *
from fast_food.core.notify import Notify
from fast_food.define import WORKING_FOLDER

''' PyQt6 Gui '''
from fast_food.views.wlogin import Ui_fromLogin

''' Conexion '''
from fast_food.conexion.database import DBase

''' Internal Logs '''
def log():
	return logging.getLogger(__name__) #.info() .debug() .warning() .error()

TR_REG_ALPHANUMBER = r'^[a-zA-Z0-9]+$'
''' Class '''
class WLModel(QtWidgets.QMainWindow, Ui_fromLogin):
	def __init__(self, parent=None):
		try: 
			super(WLModel, self).__init__()
			self.setupUi(self)

			# Flags
			self.setWindowFlag(Qt.WindowType.CustomizeWindowHint, False)
			self.setWindowFlag(Qt.WindowType.WindowTitleHint, True)
			self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)
			self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, True)

			log().info(TR_LOAD_MODEL_X.format("login"))

			# Class
			self.Main = parent
			self.DB = DBase(name='ff_user')

			# Action
			self.btnLogin.setEnabled(False)
			self.txtUser.textChanged.connect(self._validate)
			self.txtPass.textChanged.connect(self._validate)
			self.btnLogin.clicked.connect(self._iniciar)

		except Exception as e:
			log().error(TR_ERROR_MODEL_INTERNO_X.format(__name__,e))

	# Key Press
	def keyPressEvent(self, e):
		if e.key() == 16777220:
			if hasattr(self, '_validate') and self._validate:
				self._iniciar()	

	def _validate(self):
		def set_style(widget, valid):
			color = "7, 126, 246" if valid else "255, 0, 0"
			widget.setStyleSheet(
				f"border: none; border-left: 5px solid; "
				f"border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba({color}, 205)); "
				"padding-left: 5px;"
			)

		def is_valid(text):
			return len(text) > 3 and bool(re.match(TR_REG_ALPHANUMBER, text, re.I))

		user_text = self.txtUser.text()
		pass_text = self.txtPass.text()

		set_style(self.txtUser, bool(user_text) and is_valid(user_text))
		set_style(self.txtPass, bool(pass_text) and is_valid(pass_text))

		flag = bool(user_text) and bool(pass_text) and is_valid(user_text) and is_valid(pass_text)
		self.btnLogin.setEnabled(flag)
		
		return flag

	def _iniciar(self):
		if self._validate():
			_DB_User = self.DB.findOne("USERS",f"user='{self.txtUser.text()}'")
			print(_DB_User)

			if _DB_User[0] is not None:
				_DB_Pass = Crypt().decode(_DB_User[0][3])

				if _DB_Pass == self.txtPass.text():
					self._RUN(_DB_User[0][6], _DB_User[0][5], _DB_User[0][9], _DB_User[0][4])					
					log().info('Iniciando Usuario: {0} ({1})'.format(_DB_User[0][5], _DB_User[0][9]))
				else:
					self.txtPass.setStyleSheet(
						"border: none;border-left: 5px solid; "
						"border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 0, 0, 205));padding-left: 5px;"
					)
					log().error("Contraseña incorrecta")
					Notify().error("Login","Contraseña incorrecta")
			else:
				Notify().error("Login","Usuario no encontrado")
				log().error("Usuario no encontrado")
				self.txtUser.setStyleSheet(
					"border: none;border-left: 5px solid; "
					"border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 0, 0, 205));padding-left: 5px;"
				)
				self.txtPass.setStyleSheet(
					"border: none;border-left: 5px solid; "
					"border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 0, 0, 205));padding-left: 5px;"
				)

	def _RUN(self, surname, name, roles, photo):
		Settings().USER_NAME = name
		Settings().USER_ROLES = roles

		self.Main.txt_name_roles_2.setText( surname +', '+ name +' ( '+roles+' )')
		self.Main.pic_avatar_2.setPixmap(QPixmap(f"{WORKING_FOLDER}/static/avatar/{photo}"))

		self.close()
		Notify().success("Login", f"Bienvenid@ {name}")

		self.Main.show()

	def closeEvent(self, event):		
		log().info(TR_CLOSE_MODEL_X.format("login"))