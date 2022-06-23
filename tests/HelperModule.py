"""
Helper Module for the tests
"""
import logging
from datetime import datetime
import os
import sys
from logging.handlers import TimedRotatingFileHandler

def get_logger_instance(name):
    """
    Logger for all the tests
    Args:
        name (str): test name
    Returns:
        logger: logger obj
    """
    ROOT_DIR = "/Users/samuel.ip/Documents/Workspace/Learning_Workspace/Python_OOPs/tests"
    path = datetime.now().strftime('%Y-%m-%d.log')
    WO_FUNCTION_FORMAT = '[%(asctime)s,%(msecs)03d] [%(levelname)s] [%(threadName)s] [%(filename)s:%(lineno)s-%(funcName)s()] %(message)s'
    formatter = logging.Formatter(WO_FUNCTION_FORMAT, "%Y-%m-%d %H:%M:%S")
    
    debug_handler = TimedRotatingFileHandler(os.path.join(ROOT_DIR, 'test_logs', name +'_' + path), when="D", interval=24, backupCount=5)
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)
    
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setLevel(logging.DEBUG)
    screen_handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(debug_handler)
    logger.addHandler(screen_handler)
    return logger