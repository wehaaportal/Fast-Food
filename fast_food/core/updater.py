#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

''' Load '''
from distutils.version import LooseVersion
from urllib.request import urlopen
import webbrowser
import logging

''' Pyqt6 '''
from PyQt6.QtCore import pyqtSignal, QObject

''' Core '''
from fast_food.define import URL_VERSION, URL_UPDATE
from fast_food.core.settings import *
from fast_food.core.notify import Notify

''' Internal Logs '''
def log():
	return logging.getLogger(__name__) #.info() .debug() .warning() .error()

class Updater(QObject):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.check_updates()

    def callback(self):
        webbrowser.open_new(URL_UPDATE)

    def check_updates(self):
        log().info('Checking for updates...')
        try:
            web_version = urlopen(URL_VERSION).read().decode().strip()
            current_version = Settings().VERSION

            if LooseVersion(current_version) < LooseVersion(web_version):
                log().info(f'New version found: {web_version}')
                if Settings().NOTIFY_UPDATES:
                    Notify().info("Updates", f"New Version: {web_version}. Click here to download", callback=self.callback)
             
                Settings().NEW_UPDATES = True
            else:
                log().info('No new version available')
                if Settings().NOTIFY_UPDATES:
                    Notify().info("Updates", "No new version available") 

                Settings().NEW_UPDATES = False
                pass
        except Exception as e:
            log().error('Error while checking updates', exc_info=True)
        finally:
            self.finished.emit()
        


