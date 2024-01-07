#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt

from fast_food.core.settings import Settings

class SplashScreen(QtWidgets.QSplashScreen):
    def __init__(self):
        super().__init__(QtGui.QPixmap(Settings().SPLASH_IMG))
        self.init_ui()
        self.show()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

    def init_ui(self):
        title_font = self.create_font(18, QtGui.QFont.Weight.Bold)
        lbl_title = self.create_label(Settings().TITLE, title_font)

        company_font = self.create_font(12, QtGui.QFont.Weight.Bold)
        lbl_company = self.create_label(Settings().COMPANY, company_font)

        version_year_font = self.create_font(10)
        lbl_version_year = self.create_label(
            f"{Settings().VERSION} ({Settings().YEAR})", version_year_font
        )

        lbl_url = self.create_label(Settings().URL)

        
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(lbl_url)

        # Crear QVBoxLayout principal
        layout = QtWidgets.QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(lbl_title)
        layout.addWidget(lbl_company)
        layout.addWidget(lbl_version_year)
        layout.addStretch(2)

        self.lbl_msg = self.create_label("CEO & Founder: Pacheco, Matias Walter", font_size=10)
        self.lbl_msg.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight) 
       
        h_layout.addWidget(self.lbl_msg)

        layout.addLayout(h_layout)

    def create_font(self, size, weight=QtGui.QFont.Weight.Normal):
        font = QtGui.QFont()
        font.setPixelSize(size)
        font.setWeight(weight)
        return font

    def create_label(self, text, font=None, font_size=None):
        label = QtWidgets.QLabel(text)
        label.setStyleSheet("color: #000;")
        if font:
            label.setFont(font)
        if font_size:
            label.setStyleSheet(f"font-size: {font_size}px;")
        return label

    def showMessage(self, msg):
        self.lbl_msg.setText(msg)
        QtWidgets.QApplication.processEvents()

    def clear_message(self):
        super().clearMessage()
        QtWidgets.QApplication.processEvents()