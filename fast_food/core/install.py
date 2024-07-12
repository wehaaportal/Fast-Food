#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import os, logging, string, secrets
from datetime import datetime

''' PyQt6 '''
from PyQt6.QtCore import QSettings, QDate
from PyQt6.QtGui import QPixmap

''' Core '''
import fast_food
from fast_food.define import *
from fast_food.core.utils import restart_program, Usr_id
from fast_food.conexion.database import DBase

class Installer:
	def __init__(self, reset=False):
		self.reset = reset
		self.key = ''

	def install(self) -> bool:
		try:
			if not os.path.exists(HOME_APP_PATH):
				print(f'Installing {fast_food.__title__}')
				self.create_directories()
				self.configure_settings()
				self.create_admin_user()
				self.ok = True
				print(f'Installed {fast_food.__title__}')
				restart_program()
			else:
				self.ok = True
		except Exception as e:
			print(f'Failed to install {fast_food.__title__}: {e}')
			self.ok = False

	def create_directories(self):
		for directory in (HOME_APP_PATH, BACKUP_PATH, LOG_PATH, DATABASE_PATH, KEYPEM_PATH):
			if not os.path.isdir(directory):
				os.mkdir(directory, 0o777)

	def generate_key(self, _long=32) -> str:
		alphanumb = string.ascii_letters + string.digits
		self.key = secrets_key = ''.join(secrets.choice(alphanumb) for _ in range(_long))
		return secrets_key

	def configure_settings(self):
		qsettings = QSettings(SETTINGS_PATH, QSettings.Format.IniFormat)
		data_qsettings = QSettings(DATA_SETTINGS_PATH, QSettings.Format.IniFormat)

		# Configura las opciones de configuración
		data_qsettings.setValue("TITLE", fast_food.__title__)
		data_qsettings.setValue("COMPANY", "Wehaa Portal Soft.")
		data_qsettings.setValue("YEAR", str(QDate.currentDate().year()))
		data_qsettings.setValue("AUTHOR", "Matias W. Pacheco")
		data_qsettings.setValue("EMAIL", "mwpacheco@outlook.es")
		data_qsettings.setValue("URL", "http://www.wehaaportal.com")
		data_qsettings.setValue("DESCRIPTION", u'Fast Food Ordering System for Restaurants.')
		data_qsettings.setValue("VERSION", fast_food.__version__)
		data_qsettings.setValue("FAVICON", FAVICON_FILE)
		data_qsettings.setValue("LANG", "ES")

		# General
		if not self.reset:
			qsettings.setValue("FIRSTRUN", True)

		qsettings.setValue("WELCOME", True)
		qsettings.setValue("SiderBar/ACTIVE", True)

		#Backup
		qsettings.setValue("Backup/BACKUP", True)
		qsettings.setValue("Backup/NOTIFY_BACKUP", True)
		qsettings.setValue("Backup/TIME_BACKUP", datetime.now().strftime("%Y-%m-%d"))
		qsettings.setValue("Backup/DAY_BACKUP", 30)
		# Update
		qsettings.setValue("Update/UPDATES", True)
		qsettings.setValue("Update/NOTIFY_UPDATES", True)
		# Splash
		qsettings.setValue("Splash/SPLASH_IMG", SPLASH_IMG_FILE)
		qsettings.setValue("Splash/SPLASH_FLAG", True)
		# Login
		qsettings.setValue("Login/LOGIN_FLAG", True)
		# Crypt
		if not self.reset:
			#"X7Sab6LFWwjEv1UYlWZAEDZ1M6V04hk8"
			qsettings.setValue("Crypt/SECRET_KEY", self.generate_key(32)) #ToDO: Not change
		# User
		qsettings.setValue("User/USER_NAME", "Z3R0")
		qsettings.setValue("User/USER_ROLES", "UHJlY2VwdG9y")
		# Logs
		qsettings.setValue("Logs/LOG_LEVEL", logging.INFO)
		qsettings.setValue("Logs/LOG_LIMIT", 30)
		qsettings.setValue("Logs/LOG_BACKUP", True)
		# Design			
		qsettings.setValue("Skin/STYLE", "Fusion") #TODO: 'Windows', 'Fusion', 'WindowsVista'			
		qsettings.setValue("Skin/THEME", "light") #TODO: 'dark', 'light'
		qsettings.setValue("Skin/FONT_NAME", 'MS Shell Dlg 2')
		qsettings.setValue("Skin/FONT_SIZE", '8')
		# Windows
		qsettings.setValue("Windows/FULLSCREEN", True)
		qsettings.setValue("Windows/WINPOS", '@Point(282 38)')
		qsettings.setValue("Windows/WINSIZE", '@Size(800 600)')

	def create_admin_user(self):
		try:
			if not self.reset:
				db = DBase(name='ff_user')
				db.create("id INTEGER PRIMARY KEY AUTOINCREMENT, uid TEXT unique, user varchar(40) unique, pass varchar(32), photo blob, name varchar(40), surname varchar(40), dob TEXT, gender varchar(10), roles varchar(32), created DATE","USERS")
				time_created = datetime.now().strftime(TIME_FORMAT)
				from fast_food.core.crypt import Crypt
				person = {'surname': 'Pacheco', 'name': 'Matias', 'dob': '00/00/0000', 'gender': 'X'}
				clave_admin = Crypt(self.key).encode('access') #ToDO: Si funciona mejorar el password de forma alfanumerica y caracteres especiales.
				db.insert("USERS","uid, user, pass, photo, name, surname, dob, gender, roles, created", (Usr_id(person),'admin', clave_admin, 'none.png', person["name"], person["surname"], person["dob"], person["gender"], 'Administrador', time_created))
				db.close()
			else:
				print("Reset Settings, users are not modified")
		except Exception as e:
			print(f'Error: {e}')