#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import sys
from PyQt6 import QtWidgets, QtGui, QtCore

from fast_food.core.settings import Settings

class PopupSystem:
    def __init__(self, parent=None):
        self.parent = parent
        self.trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(Settings().FAVICON), self.parent)
        self.trayIcon.activated.connect(self.on_tray_icon_activated)
        self.trayIcon.show()

    def show_toast(self, title=Settings().TITLE, msg=Settings().COMPANY):
        self.trayIcon.showMessage(title, msg)

    def show_popup_info(self, msg=None, title='Information'):
        reply = QtWidgets.QMessageBox.information(self.parent, title, msg, QtWidgets.QMessageBox.StandardButton.Ok)
        return reply == QtWidgets.QMessageBox.StandardButton.Ok

    def show_popup_question(self, msg=None, title='Question'):
        reply = QtWidgets.QMessageBox.question(self.parent, title, msg, QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        return reply == QtWidgets.QMessageBox.StandardButton.Yes

    def show_popup_critical(self, msg=None, title='Critical'):
        reply = QtWidgets.QMessageBox.critical(self.parent, title, msg, QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
        return reply == QtWidgets.QMessageBox.StandardButton.Ok

    def show_popup_information(self, msg=None, title='Information'):
        QtWidgets.QMessageBox.information(self.parent, title, msg, QtWidgets.QMessageBox.StandardButton.Ok)

    def show_popup_warning(self, msg=None, title='WARNING'):
        QtWidgets.QMessageBox.warning(self.parent, title, msg, QtWidgets.QMessageBox.StandardButton.Close)

    def show_popup_error(self, msg=None, title='ERROR'):
        QtWidgets.QMessageBox.critical(self.parent, title, msg, QtWidgets.QMessageBox.StandardButton.Close)

    def show_popup_about(self, msg=None, title='ABOUT'):
        QtWidgets.QMessageBox.about(self.parent, title, msg)

    def on_tray_icon_activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.ActivationReason.Trigger:
            # Manejar el evento de clic en el ícono de la bandeja del sistema aquí
            pass
 