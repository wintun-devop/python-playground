import logging,sys
from logging.handlers import RotatingFileHandler

class LoggerManager:
    FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    LOG_FILE = "my_app.log"

    @staticmethod
    def get_console_handler():
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(LoggerManager.FORMATTER)
        return console_handler

    @staticmethod
    def get_file_handler():
        # Configure RotatingFileHandler with maxBytes and backupCount(10 MB file size, keeps 3 backups)
        file_handler = RotatingFileHandler(LoggerManager.LOG_FILE, maxBytes=10 * 1024 * 1024, backupCount=3) 
        file_handler.setFormatter(LoggerManager.FORMATTER)
        return file_handler

    @staticmethod
    def get_logger():
        logger = logging.getLogger()
        # logger.setLevel(logging.DEBUG)  # Better to have too much log than not enough
        logger.addHandler(LoggerManager.get_console_handler())
        logger.addHandler(LoggerManager.get_file_handler())
        # With this pattern, it's rarely necessary to propagate the error up to parent
        logger.propagate = False
        return logger

class PutLog:
    @staticmethod
    def debug(message):
        my_logger = LoggerManager.get_logger()
        my_logger.debug(f"{message}")
        return message

    @staticmethod
    def info(message):
        my_logger = LoggerManager.get_logger()
        my_logger.info(f"{message}")
        return my_logger

    @staticmethod
    def warn(message):
        my_logger = LoggerManager.get_logger()
        my_logger.warning(f"{message}")
        return my_logger

    @staticmethod
    def error(message):
        my_logger = LoggerManager.get_logger()
        my_logger.error(f"{message}")
        return my_logger

    @staticmethod
    def critical(message):
        my_logger = LoggerManager.get_logger()
        my_logger.critical(f"{message}")
        return my_logger


