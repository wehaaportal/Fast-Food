#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

''' Load '''
import sys

''' Metadata '''
__title__ = "Fast Food System"
__folder__ = "fast_food"
__version__ = "0.0.0.06"

''' Core '''
from fast_food.core.install import Installer
from fast_food.core.settings import Settings
from fast_food.core.logs import LogManager

''' PyQt6 '''
from PyQt6.QtWidgets import QApplication, QMainWindow

''' Doc '''
"""Fast Food System is cross-platform.
Fast Food Ordering System for Restaurants runs on Linux/X11, Mac OS X and Windows desktop operating systems."""

def setup_and_run():
	apps = QApplication(sys.argv)
	# Setup
	# ==========
	if Installer(reset=False).install():
		return

	# Logs
	# ==========
	LogManager().setup_log(Settings().COMPANY, Settings().LOG_LEVEL)

	"""Load the Core module and trigger the execution."""

	from fast_food import core 
	from multiprocessing import freeze_support

	# Used to support multiprocessing on windows packages
	freeze_support()

	# Run 
	core.start_app(apps, Settings)