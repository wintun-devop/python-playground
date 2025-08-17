import logging
from logging.handlers import RotatingFileHandler

rotating_handler = RotatingFileHandler(
        filename="myapp.log",  # Log file name
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
rotating_handler.setFormatter(formatter)

# Set up the root logger
myapp_logger = logging.getLogger()
myapp_logger.setLevel(logging.DEBUG)
myapp_logger.addHandler(rotating_handler)