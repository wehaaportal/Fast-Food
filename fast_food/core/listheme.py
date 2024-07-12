#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, logging

''' PyQt6 '''
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel

from fast_food.core.settings import Settings

''' Internal Logs '''
def log():
	return logging.getLogger(__name__) #.info() .debug() .warning() .error()

class QCustomQWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel = QLabel()
        self.textDownQLabel = QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout = QHBoxLayout()
        self.iconQLabel = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)

        # setStyleSheet
        if Settings().THEME == 'dark' and Settings().STYLE == "Fusion":
            self.textUpQLabel.setStyleSheet(''' color: rgb(207, 216, 220); ''')
            self.textDownQLabel.setStyleSheet(''' color: rgb(102, 187, 106); ''')
        else:
            self.textUpQLabel.setStyleSheet(''' color: rgb(33, 150, 243); ''')
            self.textDownQLabel.setStyleSheet(''' color: rgb(102, 187, 106); ''')

    def setTextUp(self, text:str):
        self.textUpQLabel.setText(text)

    def setTextDown(self, text:str):
        self.textDownQLabel.setText(text)

    def setIcon(self, imagePath):
        self.iconQLabel.setPixmap(QPixmap(imagePath))
        self.iconQLabel.setScaledContents(True)
        self.iconQLabel.setMaximumSize(25, 25)