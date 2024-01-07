#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Load '''
import logging, glob, os, time, zipfile

''' Core '''
import fast_food
from fast_food.define import LOG_FORMAT, TIME_FORMAT, LOG_PATH, LOG_FILE_PATH
from fast_food.core.settings import Settings

class LogManager:
    def __init__(self):
        self.file_handler = None

    def setup_log(self, strn='0.1', level=logging.INFO):
        if len(self.get_log_files()) > Settings().LOG_LIMIT:
            self.clear_logs()
        self.file_handler = logging.FileHandler(Settings().SAVELASTLOGS)
        handlers = [self.file_handler, logging.StreamHandler()]
        logging.basicConfig(
            level=logging.WARNING, handlers=handlers,
            format=LOG_FORMAT, datefmt=TIME_FORMAT)
        logging.getLogger().setLevel(level)
        mod_logger = logging.getLogger(fast_food.__title__)
        mod_logger.info(strn)

    def clear_logs(self):
        """Elimina archivos de registro antiguos y crea un archivo ZIP para hacer copias de seguridad.
        """
        if self.file_handler:
            self.file_handler.close()
        failures = []

        if Settings().LOG_BACKUP:
            bkp_zip = zipfile.ZipFile('{1}/bkp_{0}.zip'.format(time.strftime("%d-%m-%Y_%H-%M-%S"), LOG_PATH), 'w')

        for filename in self.get_log_files():
            pth = os.path.join(filename)
            try:
                # Comprimir en zip
                if Settings().LOG_BACKUP:
                    bkp_zip.write(os.path.join(LOG_PATH, pth), os.path.relpath(os.path.join(LOG_PATH, pth), LOG_PATH), compress_type=zipfile.ZIP_DEFLATED)
                
                # Eliminar archivos comprimidos
                os.remove(pth)
            except OSError:
                if os.path.exists(pth):
                    logging.getLogger('App').exception(
                        'failed to remove log file %r', pth)
                    failures.append(pth)
        
        if Settings().LOG_BACKUP:
            bkp_zip.close()
        
        return failures

    def get_log_files(self):
        return glob.glob(os.path.join(LOG_PATH, '*.log'))