#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

''' Load '''
import signal, sys, logging, platform, time

''' Core '''
from fast_food.core.translations import *
from fast_food.core.splash import SplashScreen
from fast_food.core.design import Design
from fast_food.core.updater import Updater
from fast_food.core.backup import CreateBackup, TimeBackup

''' PyQt6 '''
from PyQt6.QtCore import QCoreApplication, QLocale, QTranslator
from PyQt6.QtWidgets import QApplication, QMainWindow

''' Resource '''
import fast_food.assets.resource

''' Model '''

''' Internal Logs '''
def log():
	return logging.getLogger(__name__) #.info() .debug() .warning() .error()

''' Metadata '''
__folder__ = "core"
__version__ = "0.0.0.04"

def start_app(apps, Settings):
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	apps.setApplicationName(Settings().TITLE)
	apps.setApplicationVersion(Settings().VERSION)
	apps.setOrganizationName(Settings().COMPANY)

	# Set design to a 'QtWidgets.QApplication'
	# ==========================================
	Design(apps).set_font_size(fontname=Settings().FONTNAME, fontsize=int(Settings().FONTSIZE)) 
	Design(apps).set_theme(theme=Settings().THEME) 
	Design(apps).set_style(style=Settings().STYLE) 


	# Translations
	# =============
	#translator = QTranslator().load(f"languages/{Settings().LANG}/fast_food.qm") #ToDO: habilitar cuando se cree los archivos de traducción
	#apps.installTranslator(translator)

	apps.processEvents()

	try:
		log().info(TR_INIT_APP_X.format(Settings().VERSION, platform.python_version(), sys.platform))

		if Settings().SPLASH_FLAG:
			log().info(TR_INIT_X.format(TR_SPLASH_SCREEN))
			_Splash = SplashScreen()

			for i in range(0,6):
				_Splash.showMessage(TR_SPLASH_LOADING_X.format(i*20))
				time.sleep(0.5)

			msg = [TR_SETTINGS, TR_PLUGINS, TR_DATABASE, TR_MODERN_DESIGN]
			for i in range(0,4):
				_Splash.showMessage(TR_SPLASH_LOAD_X.format(msg[i]))
				time.sleep(0.5)


			if Settings().UPDATES:
				_Splash.showMessage("Checking for updates")
				Updater()
				time.sleep(0.8)

			if Settings().BACKUP and TimeBackup():
				_Splash.showMessage("Created backup")
				CreatedBackup()
				time.sleep(0.8)	

	except Exception as e:
		log().warning(TR_ERROR_INTERNO_X.format(e))

	sys.exit(apps.exec())