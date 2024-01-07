#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Load '''
import os, sys, socket, time

''' PyQt6 '''
from PyQt6.QtCore import QDir

# PATHS
HOME_PATH = QDir.toNativeSeparators(QDir.homePath())
HOME_APP_PATH = os.path.join(HOME_PATH, ".fast_food")
WORKING_FOLDER = os.path.realpath(os.path.dirname(sys.argv[0]))

# INTERNAL PATHS
BACKUP_PATH = os.path.join(HOME_APP_PATH, "backups")
DATABASE_PATH = os.path.join(HOME_APP_PATH, "sqldb")
LOG_PATH = os.path.join(HOME_APP_PATH, 'logs')
KEYPEM_PATH = os.path.join(HOME_APP_PATH, 'keypem')

# Style sheet
STYLE_SHEET = os.path.join(WORKING_FOLDER, 'static', 'style')

# SETTINGS FILES
SETTINGS_PATH = os.path.join(HOME_APP_PATH, 'settings.ini')
DATA_SETTINGS_PATH = os.path.join(HOME_APP_PATH, 'data.ini')

# LOGS
LOG_FILE_PATH = os.path.join(LOG_PATH, f'logs_{os.getpid()}_{time.strftime("%d-%m-%Y_%H-%M-%S")}.log')
# [TIME] LEVELNAME | ID | FILE&NAME | LINE | MSJ
LOG_FORMAT = "[%(asctime)s] %(levelname)s|%(lineno)d::%(process)d %(name)s:%(funcName)-4s :: %(message)s"
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# URLS
BUGS_PAGE = "https://github.com/wehaaportal/Fast-Food/issues"
URL_VERSION = "https://raw.githubusercontent.com/wehaaportal/Fast-Food/main/version"
URL_UPDATE = 'https://github.com/wehaaportal/Fast-Food/releases/latest'
WIKI_URL = 'https://github.com/wehaaportal/Fast-Food/wiki'

# OTHERS
FAVICON_FILE = os.sep.join(['fast_food', 'assets', 'icons.ico'])
SPLASH_IMG_FILE = os.sep.join(['fast_food', 'assets', 'splashscreen.png'])

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def isOnline():
    try:
        socket.gethostbyname("google.com")
        connection = socket.create_connection(("google.com", 80), timeout=1)
        connection.close()
        return True
    except socket.error:
        return False