#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

''' Load '''
import logging, glob, os, time, zipfile
from fast_food.define import BACKUP_PATH, DATABASE_PATH
from fast_food.core.settings import Settings
from fast_food.core.notify import Notify
from datetime import datetime

''' Internal Logs '''
def log():
    return logging.getLogger(__name__) #.info() .debug() .warning() .error()

TIME_FORMAT = "%Y-%m-%d"

def TimeBackup():
    first = time.strftime(TIME_FORMAT)
    second = Settings().TIME_BACKUP
    delta = datetime.strptime(first, TIME_FORMAT) - datetime.strptime(second, TIME_FORMAT)
    return delta.days > Settings().DAY_BACKUP

def get_files(path, ext):
    return glob.glob(os.path.join(path, ext))

def CreateBackup():
    try:
        if Settings().BACKUP:
            log().info('Creating Backup...')
            backup_filename = f'bkp_{time.strftime("%d-%m-%Y_%H-%M-%S")}.zip'
            backup_path = os.path.join(BACKUP_PATH, backup_filename)

            with zipfile.ZipFile(backup_path, 'w') as bkp_zip:
                # Compress Database Files
                for filedb in get_files(DATABASE_PATH, '*.db'):
                    pth = os.path.join(filedb)
                    bkp_zip.write(os.path.join(DATABASE_PATH, pth),
                                  os.path.relpath(os.path.join(DATABASE_PATH, pth), BACKUP_PATH),
                                  compress_type=zipfile.ZIP_DEFLATED)

                bkp_zip.setpassword(b"pwd4352gds")

            Settings().TIME_BACKUP = time.strftime(TIME_FORMAT)
            if Settings().NOTIFY_BACKUP:
                Notify.info("Backup", "Backup created successfully.")
    except Exception as e:
        log().error(f'Error creating backup: {e}')
        raise e