"""
Test Suite for the Class section projects solution
"""
import pytest
from ClassesSection.Project_classes_solution.project_class_solution import Account
from tests.TestLogger import get_logger_instance, log_info, log_error
from tests.DummyLogging import dummy

log = get_logger_instance(__name__)
# pytest.set_trace()

class TestBankingProject:
    """
    Test Class
    """
    def setup_class(self):
        #self.log = get_logger_instance(__name__)
        #pytest.set_trace()
        #self.log.info("Starting TestBankingProject test.")
        log_info("Starting TestBankingProject test.")
        #INFO("Starting TestBankingProject test.")
        
    def setup_method(self):
        """
        setup method to run before the start of each test.
        """
        acc_number = 1
        fname = "Robert"
        lname = "Kenny"
        user_tz = "UTC"
        self.test_account = Account(acc_number=acc_number, fname=fname, lname=lname, user_tz=user_tz)
    
    def test_create_account(self):
        assert self.test_account.account_number == 1
        assert self.test_account.first_name == "Robert"
        assert self.test_account.last_name == "Kenny"
        assert self.test_account.user_tz == "UTC"
        
    def teardown_method(self):
        del self.test_account
        log_error("Teart downnnnnnnnnnnn")
        dummy()
        
    def teardown_class(self):
        log_info("Closing TestBankingProject test.")
        #INFO("Closing TestBankingProject test.")
