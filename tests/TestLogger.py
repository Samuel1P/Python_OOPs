"""
Helper Module for the tests
"""
import logging
from datetime import datetime
import os
import sys
from logging import FileHandler, StreamHandler
import traceback
# from tests.FrameworkLogger import INFO, ERROR, configure
# pytest --log-cli-level=10

def log_info(msg):
  logger = (logging.tests)
  logger.info(msg, extra=__extra())

def log_debug(msg):
  logger = (logging.tests)
  logger.debug(msg, extra=__extra())

def log_error(msg):
  logger = (logging.tests)
  logger.error(msg, extra=__extra())
  
def log_warn(msg):
  logger = (logging.tests)
  logger.warning(msg, extra=__extra())
  
def log_critical(msg):
  logger = (logging.tests)
  logger.critical(msg, extra=__extra())
  
def log_exception(msg):
  logger = (logging.tests)
  logger.exception(msg, extra=__extra())
  
def __extra():
  """
  Function to pass the callers name and line number.
  Returns:
    A dictionary with file name and file line
  """
  frame = traceback.extract_stack()[-3]
  file_name = frame[0].split("/")[-1]
  file_line = frame[1]
  return {
    'file_line': "%s:%s" % (file_name, file_line)
  }
  
def get_logger_instance(name):
    """
    Logger for all the tests
    Args:
        name (str): test name
    Returns:
        logger: logger obj
    """
    logging.tests = logging.getLogger(name)
    logging.tests.setLevel(logging.DEBUG)

    
    WO_FUNCTION_FORMAT = '[%(asctime)s,%(msecs)03d] [%(levelname)s] [%(threadName)s] [%(file_line)s] [%(filename)s:%(lineno)s-%(funcName)s()] %(message)s'
    formatter = logging.Formatter(WO_FUNCTION_FORMAT, "%Y-%m-%d %H:%M:%S")
    
    ROOT_DIR = "/Users/samuel.ip/Documents/Workspace/Learning_Workspace/Python_OOPs/"
    file_name_suffix = datetime.now().strftime('%Y-%m-%d-%f.log')
    
    debug_handler = FileHandler(os.path.join(ROOT_DIR, 'tests', 'test_logs', name +'_' + file_name_suffix), 'a')
    debug_handler.set_name('debug_file')
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)
    logging.tests.addHandler(debug_handler)
    
    console_handler = StreamHandler(sys.stdout)
    
    console_handler.set_name('console_stream')
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logging.tests.addHandler(console_handler)
    #logging.tests.propagate = 0




