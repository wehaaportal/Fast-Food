#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import logging, base64

from PyQt6.QtCore import QSettings, QDate

''' Core '''
import fast_food
from fast_food.define import SETTINGS_PATH, DATA_SETTINGS_PATH, SPLASH_IMG_FILE, LOG_FILE_PATH, FAVICON_FILE # Define

class BaseSettings:
	def __init__(self):
		self.Sett = QSettings(SETTINGS_PATH, QSettings.Format.IniFormat)
		self.Data = QSettings(DATA_SETTINGS_PATH, QSettings.Format.IniFormat)
        
	def clear(self):
		print("Borrando Configuración")
		self.Sett.clear()

	def export_to_dict(self):
		print("Exportando Configuración")
		keys = self.Sett.allKeys()
		settings = {}
		for k in keys:
			if k != 'User/USER_NAME' and k != 'User/USER_ROLES':
				settings[k] = self.Sett.value(k, '')
		return settings

	def import_from_dict(self, dic):
		print("Importando Configuración")
		for k, v in dic.items():
			self.Sett.setValue(k, v)

class Settings(BaseSettings):
	def __init__(self):
		BaseSettings.__init__(self)			

	# ==================================================
	# GENERAL DATA DO NOT CHANGE!
	# ==================================================
			
	@property
	def TITLE(self) -> str:
		return self.Data.value("TITLE", fast_food.__title__, type=str)

	@property
	def COMPANY(self) -> str:
		return self.Data.value("COMPANY", "Wehaa Portal Soft.", type=str)

	@property
	def YEAR(self) -> str:
		return self.Data.value("YEAR", QDate.currentDate().year(), type=str)

	@property
	def AUTHOR(self):
		return self.Data.value("AUTHOR", "Matias W. Pacheco", type=str)
    
	@property
	def EMAIL(self) -> str:
		return self.Data.value("EMAIL", "mwpacheco@outlook.es", type=str)
    
	@property
	def URL(self) -> str:
		return self.Data.value("URL", "http://www.wehaaportal.com", type=str)

	@property
	def DESCRIPTION(self) -> str:
		return self.Data.value("DESCRIPTION", u'Wehaa Portal Soft.', type=str)

	@property
	def VERSION(self) -> str:
		return self.Data.value("VERSION", fast_food.__version__, type=str)

	@property
	def FAVICON(self) -> str:
		return self.Data.value("FAVICON", FAVICON_FILE, type=str)

	@property
	def LANG(self) -> str:
		return self.Data.value("LANG", "ES", type=str)

	# General
	# ==========
	@property
	def FIRSTRUN(self) -> bool:
		return self.Sett.value("FIRSTRUN", False, type=bool)

	@FIRSTRUN.setter
	def FIRSTRUN(self, value):
		self.Sett.setValue("FIRSTRUN", bool(value)) 

	# Logs
	# ==========
	@property
	def LOG_LEVEL(self) -> str:
		return int(self.Sett.value('Logs/LOG_LEVEL', logging.INFO))

	@LOG_LEVEL.setter
	def LOG_LEVEL(self, value):
		self.Sett.setValue('Logs/LOG_LEVEL', value)

	@property
	def LOG_LIMIT(self) -> int:
		return self.Sett.value("Logs/LOG_LIMIT", 30, type=int)

	@LOG_LIMIT.setter
	def LOG_LIMIT(self, value):
		self.Sett.setValue("Logs/LOG_LIMIT", value) 

	@property
	def LOG_BACKUP(self) -> bool:
		return self.Sett.value("Logs/LOG_BACKUP", True, type=bool)

	@LOG_BACKUP.setter
	def LOG_BACKUP(self, value):
		self.Sett.setValue("Logs/LOG_BACKUP", bool(value)) 

	@property
	def SAVELASTLOGS(self) -> str:
		return self.Sett.value("Logs/SAVELASTLOGS", LOG_FILE_PATH, type=str)

	@SAVELASTLOGS.setter
	def SAVELASTLOGS(self, value):
		self.Sett.setValue("Logs/SAVELASTLOGS", value) 

	# SiderBar
	# ==========
	@property
	def SIDERBAR(self) -> bool:
		return self.Sett.value("SiderBar/ACTIVE", False, type=bool)

	@SIDERBAR.setter
	def SIDERBAR(self, value):
		self.Sett.setValue("SiderBar/ACTIVE", bool(value))

	# ==================================================
	# CHANGE ONLY PREFERENCES GUI
	# ==================================================

	# Backup
	# ==========

	@property
	def BACKUP(self) -> bool:
		return self.Sett.value("Backup/BACKUP", True, type=bool)

	@BACKUP.setter
	def BACKUP(self, value):
		self.Sett.setValue("Backup/BACKUP", bool(value))

	@property
	def TIME_BACKUP(self) -> str:
		return self.Sett.value("Backup/TIME_BACKUP", False, type=str)

	@TIME_BACKUP.setter
	def TIME_BACKUP(self, value):
		self.Sett.setValue("Backup/TIME_BACKUP", value)

	@property
	def DAY_BACKUP(self) -> int:
		return self.Sett.value("Backup/DAY_BACKUP", 30, type=int)

	@DAY_BACKUP.setter
	def DAY_BACKUP(self, value):
		self.Sett.setValue("Backup/DAY_BACKUP", value)

	@property
	def NOTIFY_BACKUP(self) -> bool:
		return self.Sett.value("Backup/NOTIFY_BACKUP", False, type=bool)

	@NOTIFY_BACKUP.setter
	def NOTIFY_BACKUP(self, value):
		self.Sett.setValue("Backup/NOTIFY_BACKUP", bool(value))
		
	# Update
	# ==========
	@property
	def UPDATES(self) -> bool:
		return self.Sett.value("Update/UPDATES", False, type=bool)

	@UPDATES.setter
	def UPDATES(self, value):
		self.Sett.setValue("Update/UPDATES", bool(value))

	@property
	def NOTIFY_UPDATES(self) -> bool:
		return self.Sett.value("Update/NOTIFY_UPDATES", False, type=bool)

	@NOTIFY_UPDATES.setter
	def NOTIFY_UPDATES(self, value):
		self.Sett.setValue("Update/NOTIFY_UPDATES", bool(value))

	@property
	def NEW_UPDATES(self) -> bool:
		return self.Sett.value("Update/NEW_UPDATES", False, type=bool)

	@NEW_UPDATES.setter
	def NEW_UPDATES(self, value):
		self.Sett.setValue("Update/NEW_UPDATES", bool(value))

	# Splash
	# ==========
	@property
	def SPLASH_IMG(self) -> str:
		return self.Sett.value("Splash/SPLASH_IMG", SPLASH_IMG_FILE, type=str)

	@SPLASH_IMG.setter
	def SPLASH_IMG(self, value):
		self.Sett.setValue("Splash/SPLASH_IMG", value)

	@property
	def SPLASH_FLAG(self) -> bool:
		return self.Sett.value("Splash/SPLASH_FLAG", True, type=bool)

	@SPLASH_FLAG.setter
	def SPLASH_FLAG(self, value):
		self.Sett.setValue("Splash/SPLASH_FLAG", bool(value))

	# Login
	# ==========
	@property
	def LOGIN_FLAG(self) -> bool:
		return self.Sett.value("Login/LOGIN_FLAG", True, type=bool)

	@LOGIN_FLAG.setter
	def LOGIN_FLAG(self, value):
		self.Sett.setValue("Login/LOGIN_FLAG", bool(value))

	# Crypt
	# ==========
	@property
	def SECRET_KEY(self) -> str:
		return self.Sett.value("Crypt/SECRET_KEY", True, type=str)

	# User
	# ==========
	@property
	def USER_NAME(self) -> str:
		return self.Sett.value("User/USER_NAME", True, type=str)

	@USER_NAME.setter
	def USER_NAME(self, value):
		self.Sett.setValue("User/USER_NAME", value)

	@property
	def USER_ROLES(self) -> str:
		roles = self.Sett.value("User/USER_ROLES", True, type=str)
		return base64.b64decode(roles.encode("ascii")).decode("utf-8")

	@USER_ROLES.setter
	def USER_ROLES(self, value):
		roles = base64.b64encode(value.encode("utf-8")).decode("ascii")
		self.Sett.setValue("User/USER_ROLES", roles)

	# Design
	@property
	def STYLE(self) -> str:
		return self.Sett.value("Skin/STYLE", "Fusion", type=str)

	@STYLE.setter
	def STYLE(self, value):
		self.Sett.setValue("Skin/STYLE", value)

	@property
	def THEME(self) -> str:
		return self.Sett.value("Skin/THEME", "light", type=str)

	@THEME.setter
	def THEME(self, value):
		self.Sett.setValue("Skin/THEME", value)

	@property
	def FONTNAME(self) -> str:
		return self.Sett.value("Skin/FONT_NAME", "MS Shell Dlg 2", type=str)

	@FONTNAME.setter
	def FONTNAME(self, value):
		self.Sett.setValue("Skin/FONT_NAME", value)

	@property
	def FONTSIZE(self) -> str:
		return self.Sett.value("Skin/FONT_SIZE", "8", type=str)

	@FONTSIZE.setter
	def FONTSIZE(self, value):
		self.Sett.setValue("Skin/FONT_SIZE", value)

	# Windows
	@property
	def FULLSCREEN(self) -> bool:
		return self.Sett.value("Windows/FULLSCREEN", False, type=bool)

	@FULLSCREEN.setter
	def FULLSCREEN(self, value):
		self.Sett.setValue("Windows/FULLSCREEN", bool(value))

	@property
	def WINSIZE(self) -> str:
		return self.Sett.value("Windows/WINSIZE", "@Size(800 600)")

	@WINSIZE.setter
	def WINSIZE(self, value):
		self.Sett.setValue("Windows/WINSIZE", value)

	@property
	def WINPOS(self) -> str:
		return self.Sett.value("Windows/WINPOS", "@Point(77 12)")

	@WINPOS.setter
	def WINPOS(self, value):
		self.Sett.setValue("Windows/WINPOS", value)