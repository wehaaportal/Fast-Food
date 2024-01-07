#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Load '''
from PyQt6.QtCore import Qt, QCoreApplication
from PyQt6.QtWidgets import QApplication

tr = QCoreApplication.translate

# General
TR_FASTFOOD = tr("fast_food", "Fast Food")
TR_SETTINGS = tr("fast_food", "Settings")
TR_PLUGINS = tr("fast_food", "Plugins")
TR_DATABASE = tr("fast_food", "Data Base")
TR_MODERN_DESIGN = tr("fast_food", "Modern Design")
TR_SPLASH_SCREEN = tr("fast_food", "Splash Screen")
TR_SECURITY = tr("fast_food", "Security")
TR_CLOSED_X = tr("fast_food", "Cerrando {0}")

TR_LOAD_MODEL_X = tr("fast_food", "Cargando modulo {0}")
TR_CLOSE_MODEL_X = tr("fast_food", "Cerrando modulo {0}")
TR_ERROR_MODEL_INTERNO_X = tr("fast_food", "Fallo interno en '{0}': {1}")

# LOGS
TR_INIT_X = tr("fast_food", "Initializing {0}")
TR_INIT_APP_X = tr("fast_food", "Iniciando Fast Food v{0} con Python {1} en {2}")

# Splash
TR_SPLASH_LOADING_X = tr("fast_food", "Loading... {0}%")
TR_SPLASH_LOAD_X = tr("fast_food", "Loading {0}...")
TR_SPLASH_INIT = tr("fast_food", "Initializing...")
TR_SPLASH_INIT_X = tr("fast_food", "Initializing {0}...")
TR_INIT_SPLASHNOT = tr("fast_food", "Not Splash Screen")

# Error
TR_ERROR_INTERNO_X = tr("fast_food", "Fallo interno: {0}")

# Install
TR_INIT_USER_MSG = tr(
    "fast_food", 
    "Para poder ingresar usar: \n\n"
       "Administrador:\n"
         "- Usuario: admin\n"
         "- Contraseña: admin\n\n"
    "*Nota: Se puede modificar el 'Administrador' en la Configuración/Login.\n\n")

# Crypt
TR_CRYPT_ENCODE = tr("fast_food", "Contraseña encriptada")
TR_CRYPT_DECODE = tr("fast_food", "Contraseña desencriptada")

# Security
TR_SECURITY_TITLE = tr("fast_food", "Iniciar sesión")
TR_SECURITY_NAME = tr("fast_food", "Nombre")
TR_SECURITY_PASS = tr("fast_food", "Contraseña")
TR_SECURITY_BTN = tr("fast_food", "Iniciar")
TR_SECURITY_TEXT_LOGO = tr("fast_food", "Fast Food")
TR_SECURITY_TEXT_SLOGAN = tr("fast_food", "Sistema de Gestión de Viandas")

# REGX
TR_REG_ALPHA = tr("fast_food", "^[a-zA-Z]+$")
TR_REG_NUMBER = tr("fast_food", "^[0-9]+$")
TR_REG_ALPHANUMBER = tr("fast_food", "^[a-zA-Z0-9]+$")

# Preferences
TR_EXP_TITLE = tr("fast_food", "Export preferences")

# Update
TR_TOOLTIP_VERSION_AVAILABLE = tr("fast_food", "New version available!")
TR_MSG_UPDATES = tr('fast_food', 'Fast Food Updates')
TR_MSG_UPDATES_BODY = tr(
    'fast_food',
    'New version of Fast Food System available: {}\n\nClick on this message or System Tray icon to download!')
