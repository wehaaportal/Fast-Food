#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

''' PyQt6 '''
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class DarkFusionPalette(QPalette):
    def __init__(self):
        super().__init__()
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Window, QColor(56, 56, 56))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Base, QColor(56, 56, 56))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.AlternateBase, QColor(63, 63, 63))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Text, Qt.GlobalColor.white)
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Button, QColor(56, 56, 56))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.BrightText, QColor(0, 128, 152))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Link, QColor(42, 130, 218))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Highlight, QColor(0, 128, 152))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white)
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, QColor(51, 51, 51))
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(111, 111, 111))
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(122, 118, 113))
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(122, 118, 113))
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, QColor(32, 32, 32))

class LightFusionPalette(QPalette):
    def __init__(self):
        super().__init__()
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Window, QColor(239, 240, 241))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.WindowText, QColor(49, 54, 59))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Base, QColor(252, 252, 252))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.AlternateBase, QColor(239, 240, 241))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.ToolTipBase, QColor(239, 240, 241))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.ToolTipText, QColor(49, 54, 59))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Text, QColor(49, 54, 59))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Button, QColor(239, 240, 241))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.ButtonText, QColor(49, 54, 59))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.BrightText, QColor(255, 255, 255))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Link, QColor(41, 128, 185))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Highlight, QColor(126, 71, 130))
        self.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white)
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, Qt.GlobalColor.white)
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, QColor(234, 234, 234))
