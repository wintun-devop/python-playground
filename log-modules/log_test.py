# from log_helper_file_rotation import myapp_logger
from log_helper_class import LogHelper

def my_function():
    my_data = {"name":"wintun"}
    # myapp_logger.info(f"This is info log.{my_data}")
    # myapp_logger.warning(f"This is wrming log.{my_data}")
    # myapp_logger.error(f"This is error log.{my_data}")
    LogHelper.info(f"This is info class out log.{my_data}")
    LogHelper.warning(f"This is warming class out log.{my_data}")
    LogHelper.error(f"This is error class out log.{my_data}")
    return {}

my_function()