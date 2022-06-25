from tests.TestLogger import get_logger_instance, log_info, log_error
import logging
import pytest

# log = get_logger_instance(__name__)
# pytest.set_trace()

def dummy():
    #pytest.set_trace()
    # logging.info("some info log")
    # logging.info("some debug log")
    # logging.info("some critical log")
    log_info("some info log")
    log_info("some debug log")
    log_error("some critical log")