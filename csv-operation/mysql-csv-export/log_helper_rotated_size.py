import logging,sys
from logging.handlers import RotatingFileHandler
FORMATTER =  logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "my_app.log"

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler():
    # Configure RotatingFileHandler with maxBytes and backupCount(10 MB file size, keeps 3 backups)
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=10 * 1024 * 1024, backupCount=3) 
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # Better to have too much logging than not enough
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    # Prevent propagating the error to parent handlers
    logger.propagate = False
    return logger

