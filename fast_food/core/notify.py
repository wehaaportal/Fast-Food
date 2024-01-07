#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Load '''
from fast_food.core.settings import Settings

''' PyQt6 '''
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

class Notify(QSystemTrayIcon):
	def __init__(self, icon=Settings().FAVICON, parent=None):
		super().__init__(icon, parent)
		self.setToolTip(Settings().TITLE)

		menu = QMenu(parent)

		# Salir
		exitAction = menu.addAction("Exit")
		exitAction.triggered.connect(self.exit_application)

		self.setContextMenu(menu)

	def exit_application(self):
		QApplication.quit()

	def show_message(self, title, msg, icon):
		self.showMessage(title, msg, icon)