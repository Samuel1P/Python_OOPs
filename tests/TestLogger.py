"""
Helper Module for the tests
"""
import logging
from datetime import datetime
import os
import sys
from logging import FileHandler
import traceback
# from tests.FrameworkLogger import INFO, ERROR, configure

def log_info(msg):
  logger = (logging_tests)
  logger.info(msg, extra=__extra())

def log_error(msg):
  logger = (logging_tests)
  logger.error(msg, extra=__extra())
  
def log_warn(msg):
  logger = (logging_tests)
  logger.warn(msg, extra=__extra())
  
def log_critical(msg):
  logger = (logging_tests)
  logger.critical(msg, extra=__extra())
def __extra():
  """Function to pass the callers name and line number.
  Returns:
    A dictionary with 'stage', 'step' and 'file_line' details
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
    global logging_tests
    logging_tests = logging.getLogger(name)
    #logging.tests.handlers = []
    #logging.getLogger().disabled = True
    ROOT_DIR = "/Users/samuel.ip/Documents/Workspace/Learning_Workspace/Python_OOPs/tests"
    path = datetime.now().strftime('%Y-%m-%d-%f.log')
    WO_FUNCTION_FORMAT = '[%(asctime)s,%(msecs)03d] [%(levelname)s] [%(threadName)s] [%(file_line)s] [%(filename)s:%(lineno)s-%(funcName)s()] %(message)s'
    formatter = logging.Formatter(WO_FUNCTION_FORMAT, "%Y-%m-%d %H:%M:%S")
    
    debug_handler = FileHandler(os.path.join(ROOT_DIR, 'test_logs', name +'_' + path), 'a')
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)
    #debug_handler.set_name('primary')

    logging_tests.setLevel(logging.DEBUG)
    logging_tests.addHandler(debug_handler)
    #logging.tests.propagate = 0
    
    


# def help_logger(name, input_args={}):
#     folder = "test_logs/"+str(name)
#     log_name = "{0}_{1}.log".format(
#     name, datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
#     configure(log_dir=folder, log_file=log_name, level="DEBUG")
#     INFO("Script Inputs : {}".format(input_args))
#     INFO("Log file : {0}/{1}".format(folder, log_name))
