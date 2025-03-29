import logging
from logging.handlers import RotatingFileHandler

rotating_app_log_handler = RotatingFileHandler(
        filename=f"myapp_out.log",  # Log file name
        mode="a",  # Append mode
        maxBytes=1 * 1024 * 1024,  # Maximum size of the log file (e.g., 1 MB)
        backupCount=3,  # Number of backup files to keep
        encoding=None,  # Encoding (None for default)
        delay=False  # Delayed file creation
    )

rotating_error_log_handler = RotatingFileHandler(
        filename=f"myapp_error.log",  # Log file name
        mode="a",  # Append mode
        maxBytes=1 * 1024 * 1024,  # Maximum size of the log file (e.g., 1 MB)
        backupCount=3,  # Number of backup files to keep
        encoding=None,  # Encoding (None for default)
        delay=False  # Delayed file creation
    )

# Set the formatter for the handler
formatter = logging.Formatter(
    fmt="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

rotating_app_log_handler.setFormatter(formatter)
rotating_error_log_handler.setFormatter(formatter)

#logger  instance for outlog
outlog=logging.getLogger("outlog")
outlog.setLevel(logging.DEBUG)
outlog.addHandler(rotating_app_log_handler)

#logger  instance for errorlog
errorlog=logging.getLogger("errorlog")
errorlog.setLevel(logging.ERROR)
errorlog.addHandler(rotating_error_log_handler)

class LogHelper:
    def __init__(self):
        pass
    def debug(message):
        return outlog.debug(message)
    def info(message):
        return outlog.info(message)
    def warning(message):
        return outlog.warning(message)
    def error(message):
        return errorlog.error(message)
